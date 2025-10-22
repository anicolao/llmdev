"""
Tests for caching infrastructure.
"""

import pytest
import time
import tempfile
from pathlib import Path
from llmdev.cache import DiskCache, RateLimiter


class TestDiskCache:
    """Test cases for DiskCache."""
    
    def test_cache_set_and_get(self):
        """Test basic cache set and get operations."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = DiskCache(tmpdir)
            
            # Set a value
            success = cache.set('test_key', {'data': 'value'})
            assert success is True
            
            # Get the value
            value = cache.get('test_key', ttl=3600)
            assert value == {'data': 'value'}
    
    def test_cache_miss(self):
        """Test cache miss for non-existent key."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = DiskCache(tmpdir)
            
            value = cache.get('nonexistent_key')
            assert value is None
    
    def test_cache_expiration(self):
        """Test cache expiration based on TTL."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = DiskCache(tmpdir)
            
            # Set a value
            cache.set('test_key', {'data': 'value'})
            
            # Should be available immediately
            value = cache.get('test_key', ttl=1)
            assert value == {'data': 'value'}
            
            # Wait for expiration
            time.sleep(1.5)
            
            # Should be expired now
            value = cache.get('test_key', ttl=1)
            assert value is None
    
    def test_cache_clear(self):
        """Test clearing all cache files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = DiskCache(tmpdir)
            
            # Add multiple items
            cache.set('key1', 'value1')
            cache.set('key2', 'value2')
            cache.set('key3', 'value3')
            
            # Clear cache
            count = cache.clear()
            
            assert count == 3
            assert cache.get('key1') is None
            assert cache.get('key2') is None
            assert cache.get('key3') is None
    
    def test_cache_with_complex_data(self):
        """Test caching complex data structures."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = DiskCache(tmpdir)
            
            complex_data = {
                'list': [1, 2, 3],
                'nested': {'a': 1, 'b': 2},
                'string': 'test',
                'number': 42,
            }
            
            cache.set('complex', complex_data)
            value = cache.get('complex')
            
            assert value == complex_data


class TestRateLimiter:
    """Test cases for RateLimiter."""
    
    def test_rate_limiter_basic_delay(self):
        """Test basic delay between requests."""
        limiter = RateLimiter(min_delay=0.1, max_delay=1.0)
        
        start = time.time()
        limiter.wait_if_needed()
        
        # First call should be immediate
        first_duration = time.time() - start
        assert first_duration < 0.05
        
        # Second call should be delayed
        start = time.time()
        limiter.wait_if_needed()
        second_duration = time.time() - start
        
        assert second_duration >= 0.1
    
    def test_rate_limiter_reset(self):
        """Test rate limiter reset."""
        limiter = RateLimiter(min_delay=0.1)
        
        limiter.consecutive_failures = 5
        limiter.last_request_time = time.time()
        
        limiter.reset()
        
        assert limiter.consecutive_failures == 0
        assert limiter.last_request_time == 0.0
    
    def test_rate_limiter_low_remaining(self):
        """Test behavior when rate limit is low."""
        limiter = RateLimiter(min_delay=0.05, max_delay=0.5)
        
        # Simulate low remaining calls (but not zero)
        start = time.time()
        limiter.wait_if_needed(remaining=5)
        duration = time.time() - start
        
        # Should add extra delay when remaining is low
        assert duration >= 0.05
