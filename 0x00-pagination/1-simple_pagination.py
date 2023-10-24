#!/usr/bin/env python3
"""
Defines a Server class for paginating a database of popular baby names
"""
import csv
from typing import List, Tuple


class Server:
    """Server class for paginating a database of popular baby names
    """

    def __init__(self, data_file: str = "Popular_Baby_Names.csv"):
        self.data_file = data_file
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.data_file, 'r') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Returns the start and end indices for a specific page and page size
        Args:
            page (int): page number to return (pages are 1-indexed)
            page_size (int): number of items per page
        Return:
            tuple(start_index, end_index)
        """
        start = (page - 1) * page_size
        end = start + page_size
        return start, min(end, start + page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the requested page from the dataset
        Args:
            page (int): required page number. Must be a positive integer
            page_size (int): number of records per page. Must be a positive integer
        Return:
            List of lists containing the required data from the dataset
        """
        assert isinstance(
            page, int) and page > 0, "Page number must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        try:
            start, end = self.index_range(page, page_size)
            return dataset[start:end]
        except IndexError:
            return []
