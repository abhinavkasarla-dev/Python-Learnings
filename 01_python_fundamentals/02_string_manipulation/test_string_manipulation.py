"""Tests for string_manipulation.py. Never edit this file."""

import pytest
from string_manipulation import (
    count_vowels,
    greet,
    is_palindrome,
    mask_email,
    reverse_words,
    to_snake_case,
    truncate,
)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("alice", "Hello, Alice!"),
        ("  BOB ", "Hello, Bob!"),
        ("charlie", "Hello, Charlie!"),
    ],
)
def test_greet(name: str, expected: str) -> None:
    assert greet(name) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", 3),
        ("AEIOU aeiou", 10),
        ("rhythm", 0),
        ("", 0),
    ],
)
def test_count_vowels(text: str, expected: int) -> None:
    assert count_vowels(text) == expected


@pytest.mark.parametrize(
    ("sentence", "expected"),
    [
        ("hello big world", "world big hello"),
        ("  too   many   spaces ", "spaces many too"),
        ("alone", "alone"),
        ("", ""),
    ],
)
def test_reverse_words(sentence: str, expected: str) -> None:
    assert reverse_words(sentence) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("kayak", True),
        ("Kayak", True),
        ("A man, a plan, a canal: Panama", True),
        ("12321", True),
        ("python", False),
        ("ab", False),
    ],
)
def test_is_palindrome(text: str, expected: bool) -> None:
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello_world"),
        ("  Python-Course   Exercise ", "python_course_exercise"),
        ("already_snake", "already_snake"),
        ("ONE", "one"),
    ],
)
def test_to_snake_case(text: str, expected: str) -> None:
    assert to_snake_case(text) == expected


@pytest.mark.parametrize(
    ("text", "max_length", "expected"),
    [
        ("Hello World", 8, "Hello..."),
        ("Hello World", 11, "Hello World"),
        ("Hi", 8, "Hi"),
        ("abcdef", 5, "ab..."),
    ],
)
def test_truncate(text: str, max_length: int, expected: str) -> None:
    assert truncate(text, max_length) == expected


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("john.doe@example.com", "j*******@example.com"),
        ("ab@test.fr", "a*@test.fr"),
        ("a@b.io", "a@b.io"),
    ],
)
def test_mask_email(email: str, expected: str) -> None:
    assert mask_email(email) == expected
