"""
Rate limit management for GitHub API.
"""

import time
import logging
from typing import Optional
from datetime import datetime


logger = logging.getLogger(__name__)


class RateLimiter:
    """Manages GitHub API rate limiting with exponential backoff."""
    
    def __init__(self, min_delay: float = 1.0, max_delay: float = 60.0):
        """
        Initialize rate limiter.
        
        Args:
            min_delay: Minimum delay between requests in seconds
            max_delay: Maximum delay for exponential backoff in seconds
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.last_request_time = 0.0
        self.consecutive_failures = 0
    
    def wait_if_needed(self, remaining: Optional[int] = None, reset_time: Optional[datetime] = None):
        """
        Wait if necessary to respect rate limits.
        
        Args:
            remaining: Number of remaining API calls (from GitHub API)
            reset_time: When the rate limit resets (from GitHub API)
        """
        # Calculate base delay
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        
        if elapsed < self.min_delay:
            delay = self.min_delay - elapsed
            logger.debug(f"Rate limiting: waiting {delay:.2f}s")
            time.sleep(delay)
        
        # If we're close to rate limit, add additional delay
        if remaining is not None and remaining < 10:
            if reset_time:
                # Wait until reset if we're out of requests
                wait_until_reset = (reset_time - datetime.now()).total_seconds()
                if wait_until_reset > 0:
                    logger.warning(
                        f"Rate limit nearly exceeded. Waiting {wait_until_reset:.0f}s until reset."
                    )
                    time.sleep(min(wait_until_reset + 5, self.max_delay))
            else:
                # Apply exponential backoff
                delay = min(self.min_delay * (2 ** self.consecutive_failures), self.max_delay)
                logger.warning(f"Low rate limit remaining. Waiting {delay:.2f}s")
                time.sleep(delay)
                self.consecutive_failures += 1
        else:
            # Reset failure counter on successful requests
            self.consecutive_failures = 0
        
        self.last_request_time = time.time()
    
    def handle_rate_limit_error(self, reset_time: Optional[datetime] = None):
        """
        Handle a rate limit error by waiting until reset.
        
        Args:
            reset_time: When the rate limit resets
        """
        if reset_time:
            wait_seconds = (reset_time - datetime.now()).total_seconds()
            if wait_seconds > 0:
                logger.error(
                    f"Rate limit exceeded. Waiting {wait_seconds:.0f}s until reset at {reset_time}"
                )
                time.sleep(wait_seconds + 5)  # Add 5s buffer
        else:
            # Use exponential backoff
            delay = min(self.min_delay * (2 ** self.consecutive_failures), self.max_delay)
            logger.error(f"Rate limit exceeded. Waiting {delay:.2f}s")
            time.sleep(delay)
            self.consecutive_failures += 1
    
    def reset(self):
        """Reset the rate limiter state."""
        self.last_request_time = 0.0
        self.consecutive_failures = 0
        logger.debug("Rate limiter reset")
