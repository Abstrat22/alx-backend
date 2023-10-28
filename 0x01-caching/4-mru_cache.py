#!/usr/bin/env python3

""" BaseCaching module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a Most Recently Used (MRU) caching system.
    """

    def __init__(self):
        """
        Initializes the class by calling the parent's init method and setting up a usage list.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Caches a key-value pair.

        Args:
            key: The key to be cached.
            item: The item to be associated with the key.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value linked to a given key, if it exists, and updates its usage position.

        Args:
            key: The key whose associated value is to be retrieved.

        Returns:
            The value associated with the key if it exists; otherwise, returns None.
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None

