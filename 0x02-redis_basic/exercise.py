#!/usr/bin/env python3
import redis
import uuid
from typing import Union
'''
    import the redis module to establish a connection to the redis server
    import uuid to generate random numbers
    import Union from typing to annotate various datatypes
'''


difData = Union[int, float, str, bytes]


class Cache:
    '''
        class creates an instance of the Redis saves in a private class
        attribute and generates a random key using the uuid4 method
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: difData) -> str:
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
