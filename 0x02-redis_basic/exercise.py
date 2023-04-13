#!/usr/bin/env python3
''' import files '''
import redis
import uuid
from typing import Union, Callable
from functools import wraps

''' type annotation '''
difData = Union[int, float, str, bytes]

'''
    function that increments the count for that key every time
    the method is called and returns the value returned by the
    original method.
'''


def count_calls(method: Callable) -> Callable:
    ''' decorator returns a callable wraps from funtools'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' uses the incr method to keep count '''
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
        ''' creates an instance of redis '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: difData) -> str:
        '''
            returns random generated value key
        '''
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
