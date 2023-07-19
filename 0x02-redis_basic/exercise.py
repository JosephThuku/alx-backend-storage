#!/usr/bin/env python3

"""
writing strings to Redis
"""
import uuid
import redis
from typing import Union


class Cache:
    """exercise.py"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """exercise.py"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
