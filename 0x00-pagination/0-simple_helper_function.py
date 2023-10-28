#!/usr/bin/env python3

"""
This script contains the definition of the 'index_range' helper function.

The 'index_range' function takes two integer arguments,
'page' and 'page_size', and returns a tuple of size two.
This tuple contains the start and end index that correspond to the
range of indexes to be returned in a list,
considering the provided pagination parameters.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a specific
    page and page size in a list.

    Args:
        page (int): The page number to return (pages are 1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices of
        the specified page and page size.
    """
    # Calculate the start index based on the provided page and page size
    start_index = (page - 1) * page_size

    # Calculate the end index based on the start index and the page size
    end_index = start_index + page_size

    # Return a tuple containing the start and end indices
    return (start_index, end_index)
