import pytest
from string_utils import StringUtils

utils = StringUtils()


# --------------------------------------------------------

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("тест", "Тест"),
    ("hello world", "Hello world"),
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("123", "123"),
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected


# --------------------------------------------------------

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
    ("   hello   ", "hello   "),
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected


# --------------------------------------------------------

@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"),
    ("12345", "3"),
])
def test_contains_positive(string, symbol):
    assert utils.contains(string, symbol) is True


@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "Z"),
    ("", "a"),
])
def test_contains_negative(string, symbol):
    assert utils.contains(string, symbol) is False


# --------------------------------------------------------

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello hello", "hello", " "),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),
    ("", "a", ""),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
