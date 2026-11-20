"""Tests for string_methods.py. Never edit this file."""

import pytest
from string_methods import (
    censor,
    clean_input,
    count_occurrences,
    find_position,
    format_price,
    frame_title,
    get_lines,
    is_number,
    is_python_file,
    is_secure_url,
    is_word,
    join_with_commas,
    pad_number,
    remove_extension,
    shout,
    split_csv_line,
    strip_hashtag,
    to_title,
    whisper,
)

# --- Case ---------------------------------------------------------------------


def test_shout() -> None:
    assert shout("hello") == "HELLO"
    assert shout("Hello World!") == "HELLO WORLD!"


def test_whisper() -> None:
    assert whisper("HeLLo") == "hello"
    assert whisper("ABC 123") == "abc 123"


def test_to_title() -> None:
    assert to_title("the lord of the rings") == "The Lord Of The Rings"
    assert to_title("PYTHON course") == "Python Course"


# --- Search -------------------------------------------------------------------


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://papernest.com", True),
        ("http://papernest.com", False),
        ("papernest.com/https://", False),
    ],
)
def test_is_secure_url(url: str, expected: bool) -> None:
    assert is_secure_url(url) is expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("main.py", True),
        ("notes.txt", False),
        ("python.txt", False),
    ],
)
def test_is_python_file(filename: str, expected: bool) -> None:
    assert is_python_file(filename) is expected


def test_count_occurrences() -> None:
    assert count_occurrences("the cat and the hat", "the") == 2
    assert count_occurrences("banana", "a") == 3
    assert count_occurrences("banana", "x") == 0


def test_find_position() -> None:
    assert find_position("hello world", "world") == 6
    assert find_position("hello world", "o") == 4
    assert find_position("hello world", "python") == -1


# --- Check --------------------------------------------------------------------


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("2026", True),
        ("20.26", False),
        ("12a", False),
        ("", False),
    ],
)
def test_is_number(text: str, expected: bool) -> None:
    assert is_number(text) is expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("python", True),
        ("Python", True),
        ("python3", False),
        ("two words", False),
        ("", False),
    ],
)
def test_is_word(text: str, expected: bool) -> None:
    assert is_word(text) is expected


# --- Clean --------------------------------------------------------------------


def test_clean_input() -> None:
    assert clean_input("  hello world \n") == "hello world"
    assert clean_input("\tdone") == "done"


@pytest.mark.parametrize(
    ("tag", "expected"),
    [
        ("#python", "python"),
        ("##python", "#python"),
        ("python", "python"),
        ("py#thon", "py#thon"),
    ],
)
def test_strip_hashtag(tag: str, expected: str) -> None:
    assert strip_hashtag(tag) == expected


@pytest.mark.parametrize(
    ("filename", "extension", "expected"),
    [
        ("report.pdf", ".pdf", "report"),
        ("report.pdf", ".txt", "report.pdf"),
        ("archive.tar.gz", ".gz", "archive.tar"),
        ("leaf.pdf", ".pdf", "leaf"),
    ],
)
def test_remove_extension(filename: str, extension: str, expected: str) -> None:
    assert remove_extension(filename, extension) == expected


def test_censor() -> None:
    assert censor("this is bad, very bad", "bad") == "this is ***, very ***"
    assert censor("all good", "bad") == "all good"


# --- Split and join -----------------------------------------------------------


def test_split_csv_line() -> None:
    assert split_csv_line("alice,30,paris") == ["alice", "30", "paris"]
    assert split_csv_line("alone") == ["alone"]


def test_join_with_commas() -> None:
    assert join_with_commas(["red", "green", "blue"]) == "red, green, blue"
    assert join_with_commas(["alone"]) == "alone"
    assert join_with_commas([]) == ""


def test_get_lines() -> None:
    assert get_lines("first\nsecond\nthird") == ["first", "second", "third"]
    assert get_lines("single") == ["single"]


# --- Layout and format --------------------------------------------------------


def test_pad_number() -> None:
    assert pad_number(7, 3) == "007"
    assert pad_number(42, 5) == "00042"
    assert pad_number(1234, 3) == "1234"


def test_frame_title() -> None:
    assert frame_title("menu", 10) == "***menu***"
    assert frame_title("hi", 6) == "**hi**"


def test_format_price() -> None:
    assert format_price(9.5) == "9.50 EUR"
    assert format_price(3.14159) == "3.14 EUR"
    assert format_price(10) == "10.00 EUR"
