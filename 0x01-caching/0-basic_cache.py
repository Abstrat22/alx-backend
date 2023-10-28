#!/usr/bin/env python3

""" BaseCaching module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs.

    Methods:
        put(key, item) - Store a key-value pair.
        get(key) - Retrieve the value associated with a key.
    """

    def __init__(self):
        """
        Initializes the BasicCache class by calling the parent class's __init__ method.
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Stores a key-value pair.

        Args:
            key: The key to be stored.
            item: The item to be associated with the key.
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value linked to the provided key.

        If the key is None or does not exist, returns None.

        Args:
            key: The key whose associated value is to be retrieved.

        Returns:
            The value associated with the key if it exists; otherwise, returns None.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None

