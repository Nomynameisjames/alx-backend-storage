#!/usr/bin/env python3
''' import files '''
import redis
import uuid
from typing import Union, Callable
from functools import wraps

difData = Union[int, float, str, bytes]


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        myRedisDB = self._redis
        myRedisDB.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''
        class creates an instance of the Redis saves in a private class
        attribute and generates a random key using the uuid4 method
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: difData) -> str:
        _key: str = str(uuid.uuid4())
        self._redis.set(_key, data)
        return _key

    def get(self, key: str, fn=None):
        '''
            get method uses a callable function to decode data from str
            or uses the decode method to convert to a desired str
        '''
        data = self._redis.get(key)
        if fn:
            data = fn(data)
            return data
        else:
            return data

    def get_str(self, key: str):
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str):
        return self.get(key, fn=lambda x: int(x))
