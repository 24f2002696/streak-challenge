import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test with multiple streaks, ensuring the longest one is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negative numbers correctly break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2

def test_all_positives():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negatives():
    """Test a list containing only negative numbers and zeros."""
    assert longest_positive_streak([-1, -2, 0, -3]) == 0

def test_single_element_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([42]) == 1

def test_single_element_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -2, 3, 4, 5]) == 3

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, -3]) == 0