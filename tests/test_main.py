import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from main import parse_floors

def test_parse_floors_basic():
    assert parse_floors("1,2,3") == [1, 2, 3]

def test_parse_floors_with_spaces():
    assert parse_floors(" 1, 2, 3") == [1, 2, 3]

def test_parse_floors_negative_numbers():
    assert parse_floors("-2,0,5") == [-2, 0, 5]

def test_parse_floors_rejects_empty_string():
    with pytest.raises(ValueError):
        parse_floors("")

def test_parse_floors_rejects_whitespace_only():
    with pytest.raises(ValueError):
        parse_floors(" ")

def test_parse_floors_rejects_only_commas():
    with pytest.raises(ValueError):
        parse_floors(",,,")

def test_parse_floors_rejects_non_integer():
    with pytest.raises(ValueError):
        parse_floors("1,2,a,4")

def test_parse_floors_rejects_empty_entry():
    with pytest.raises(ValueError):
        parse_floors("1,,2")

def test_parse_floors_rejects_trailing_comma():
    with pytest.raises(ValueError):
        parse_floors("1,2,3,")

def test_parse_floors_rejects_leading_comma():
    with pytest.raises(ValueError):
        parse_floors(",1,2,3")
