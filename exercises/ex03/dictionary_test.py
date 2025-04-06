__author__ = "730698517"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len
import pytest


def test_invert_simple():
    """Test inverting a basic dictionary"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single():
    """Test inverting a dictionary with one pair"""
    assert invert({"apple": "fruit"}) == {"fruit": "apple"}


def test_invert_duplicate_value():
    """Test that duplicate values"""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_count_empty():
    """Test count with an empty list."""
    assert count([]) == {}


def test_count_unique():
    """Test count with a list of unique elements."""
    assert count(["apple", "banana", "cherry"]) == {
        "apple": 1,
        "banana": 1,
        "cherry": 1,
    }


def test_count_repeated():
    """Test count with repeated elements."""
    assert count(["apple", "banana", "apple", "cherry", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "cherry": 1,
    }


def test_favorite_color_edge_case_empty():
    """Edge case: Test with an empty dictionary."""
    choices = {}
    result = favorite_color(choices)
    assert result == ""


def test_favorite_color_multiple_people_single_color():
    """Use case: Test with multiple people all having the same favorite color."""
    choices = {"Alice": "blue", "Bob": "blue", "Charlie": "blue"}
    result = favorite_color(choices)
    assert result == "blue"


def test_favorite_color_tied_colors():
    """Use case: Test with a tie between colors, should return the first encountered color."""
    choices = {"Alice": "blue", "Bob": "green", "Charlie": "blue", "David": "green"}
    result = favorite_color(choices)
    assert result == "blue"


def test_bin_len_edge_case_empty():
    """Edge case: Test with an empty list."""
    bin = bin_len([])
    assert bin == {}


def test_bin_len_single_length():
    """Use case: All strings have the same length."""
    bin = bin_len(["the", "fox", "dog"])
    assert bin == {3: {"the", "fox", "dog"}}


def test_bin_len_different_lengths():
    """Use case: Strings of different lengths."""
    bin = bin_len(["the", "quick", "fox"])
    assert bin == {
        3: {"the", "fox"},
        5: {"quick"},
    }
