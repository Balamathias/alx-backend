#!/usr/bin/python3
"""FIFO Caching implementation
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
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
            dict_list = []
            for (key, value) in self.cache_data.items():
                dict_list.append({'key': key, 'value': value})
            if len(self.cache_data.items()) > self.MAX_ITEMS:
                self.cache_data.pop(dict_list[0]['key'])
                print(f'DISCARD: {dict_list[0]['key']}')
                dict_list.pop()
                print()

    def get(self, key):
        """Get an item from cache by Key

        Args:
            key (any): Key to get but not None

        Returns:
            any: The result or None for the given value of key
        """

        return None if key == None or self.cache_data.get(key) == None \
            else self.cache_data.get(key)
