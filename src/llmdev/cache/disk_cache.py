"""
Disk-based cache for GitHub API responses.
"""

import json
import logging
import hashlib
from pathlib import Path
from typing import Any, Optional
from datetime import datetime, timedelta


logger = logging.getLogger(__name__)


class DiskCache:
    """Simple disk-based cache for API responses."""

    def __init__(self, cache_dir: str = ".llmdev_cache"):
        """
        Initialize disk cache.

        Args:
            cache_dir: Directory to store cache files
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Initialized disk cache at {self.cache_dir}")

    def get(self, key: str, ttl: int = 3600) -> Optional[Any]:
        """
        Get a value from cache if it exists and hasn't expired.

        Args:
            key: Cache key
            ttl: Time to live in seconds

        Returns:
            Cached value or None if not found or expired
        """
        cache_file = self._get_cache_file(key)

        if not cache_file.exists():
            logger.debug(f"Cache miss: {key}")
            return None

        try:
            # Check if cache is expired
            file_age = datetime.now() - datetime.fromtimestamp(cache_file.stat().st_mtime)
            if file_age > timedelta(seconds=ttl):
                logger.debug(f"Cache expired: {key}")
                cache_file.unlink()
                return None

            # Read cache
            with cache_file.open("r") as f:
                data = json.load(f)

            logger.debug(f"Cache hit: {key}")
            return data
        except (json.JSONDecodeError, IOError) as e:
            logger.warning(f"Error reading cache for {key}: {e}")
            return None

    def set(self, key: str, value: Any) -> bool:
        """
        Store a value in cache.

        Args:
            key: Cache key
            value: Value to cache (must be JSON-serializable)

        Returns:
            True if successful, False otherwise
        """
        cache_file = self._get_cache_file(key)

        try:
            with cache_file.open("w") as f:
                json.dump(value, f, default=str)

            logger.debug(f"Cached: {key}")
            return True
        except (TypeError, IOError) as e:
            logger.warning(f"Error writing cache for {key}: {e}")
            return False

    def clear(self) -> int:
        """
        Clear all cached files.

        Returns:
            Number of files deleted
        """
        count = 0
        for cache_file in self.cache_dir.glob("*.json"):
            try:
                cache_file.unlink()
                count += 1
            except IOError as e:
                logger.warning(f"Error deleting cache file {cache_file}: {e}")

        logger.info(f"Cleared {count} cache files")
        return count

    def _get_cache_file(self, key: str) -> Path:
        """
        Get the cache file path for a given key.

        Args:
            key: Cache key

        Returns:
            Path to cache file
        """
        # Hash the key to create a safe filename
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return self.cache_dir / f"{key_hash}.json"
