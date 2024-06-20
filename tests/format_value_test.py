import pytest
from gendiff.formatters.plain import format_value

def test_format_value_dict():
    assert format_value({"a": 1}) == "[complex value]"

def test_format_value_list():
    assert format_value([1, 2, 3]) == "[complex value]"

def test_format_value_none():
    assert format_value(None) == "null"

def test_format_value_bool_true():
    assert format_value(True) == "true"

def test_format_value_bool_false():
    assert format_value(False) == "false"

def test_format_value_string():
    assert format_value("test") == "'test'"

def test_format_value_int():
    assert format_value(42) == "42"

def test_format_value_float():
    assert format_value(3.14) == "3.14"