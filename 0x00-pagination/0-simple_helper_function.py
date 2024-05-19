#!/usr/bin/env python3
"""Module to write a function that takes integer args"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Function to calculate the start and end index for the
    given pagination parameters.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
