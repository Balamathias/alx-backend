#!/usr/bin/python3
'''
Basic caching algorithmic implementation in PYTHON.
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class Implementation of Basic Caching in PYTHON."""

    def put(self, key, item):
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        return None if key == None or self.cache_data.get(key) == None \
            else self.cache_data.get(key)
