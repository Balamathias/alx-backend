#!/usr/bin/python3
"""Basic Caching Implementation

Returns:
    Any: any
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """...

    Args:
        BaseCaching (any): ...
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add item to cache dict

        Args:
            key (any): The key to insert
            item (any): the value of Key
        """

        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache by Key

        Args:
            key (any): Key to get but not None

        Returns:
            any: The result or None for the given value of key
        """

        return None if key == None or self.cache_data.get(key) == None \
            else self.cache_data.get(key)
