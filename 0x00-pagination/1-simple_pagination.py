#!/usr/bin/env python3

"""
Defines a Server class that facilitates the pagination of a
database containing popular baby names.
"""

import csv
from typing import List, Tuple


class Server:
    """A Server class that facilitates the pagination of a
    database containing popular baby names."""

    def __init__(self, data_file: str = "Popular_Baby_Names.csv"):
        """Initializes the Server class with the specified data file."""
        self.data_file = data_file
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the cached dataset, if available.
        """
        if self.__dataset is None:
            with open(self.data_file, 'r') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Computes the start and end indices for a specific page and page size.

        Args:
            page (int): The page number to return (pages are 1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: A tuple containing the start and end indices.
        """
        start = (page - 1) * page_size
        end = start + page_size
        return start, min(end, start + page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the requested page from the dataset.

        Args:
            page (int): The required page number. Must be a positive integer.
            page_size (int): The number of records per page.
            Must be a positive integer.

        Returns:
            List of lists: A list of lists containing the
            required data from the dataset.
        """
        assert isinstance(
            page, int) and page > 0, "Page number must be a positive integer"
        assert isinstance(
            page_size, int) and
        page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        try:
            start, end = self.index_range(page, page_size)
            return dataset[start:end]
        except IndexError:
            return []
