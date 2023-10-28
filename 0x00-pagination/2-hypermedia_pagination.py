#!/usr/bin/env python3

"""
Contains a class and a helper function for creating simple
pagination from CSV data.
"""

import csv
from typing import List, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Computes the start and end indices for pagination.

    Args:
        page (int): The page number to return (pages are 1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, min(end, start + page_size)


class Server:
    """
    Server class for paginating a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retrieves the dataset from the CSV file.

        Returns:
            List[List]: The dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts that the value is a positive integer.

        Args:
            value (int): The value to be asserted.
        """
        assert isinstance(
            value, int) and value > 0, "Value must be a positive integer"

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a page of data from the dataset.

        Args:
            page (int): The page number.
            page_size (int): The page size.

        Returns:
            List[List]: The data corresponding to the requested page.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Retrieves a page of data from the dataset with
        additional pagination information.

        Args:
            page (int): The page number.
            page_size (int): The page size.

        Returns:
            Dict[str, any]: A dictionary containing information
            about the requested page.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
