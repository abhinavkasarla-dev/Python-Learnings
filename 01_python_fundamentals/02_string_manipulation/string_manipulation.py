"""
String manipulation

Instructions:
    Implement every function below so that all the tests pass.
    Each docstring explains what the function must do and shows examples.
    Replace `raise NotImplementedError` with your code.

Run the tests:
    uv run pytest 01_python_fundamentals/02_string_manipulation

Rules:
    - No imports: everything can be done with built-in string methods.
    - Do not change the function names or their parameters.
    - Do not edit test_string_manipulation.py.

Useful documentation:
    https://docs.python.org/3/library/stdtypes.html#string-methods
"""


def greet(name: str) -> str:
    """Return a greeting for `name`.

    Remove the spaces around the name and capitalize it.

    >>> greet("alice")
    'Hello, Alice!'
    >>> greet("  BOB ")
    'Hello, Bob!'
    """
    raise NotImplementedError


def count_vowels(text: str) -> int:
    """Return how many vowels (a, e, i, o, u) `text` contains, upper or lower case.

    >>> count_vowels("Hello World")
    3
    >>> count_vowels("rhythm")
    0
    """
    raise NotImplementedError


def reverse_words(sentence: str) -> str:
    """Return the words of `sentence` in reverse order, separated by a single space.

    >>> reverse_words("hello big world")
    'world big hello'
    >>> reverse_words("  too   many   spaces ")
    'spaces many too'
    """
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """Return True if `text` reads the same backwards.

    Ignore case, spaces and punctuation: only letters and digits count.

    >>> is_palindrome("kayak")
    True
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("python")
    False
    """
    raise NotImplementedError


def to_snake_case(text: str) -> str:
    """Convert `text` to snake_case.

    Words are separated by spaces or dashes. The result is lower case,
    words joined by a single underscore.

    >>> to_snake_case("Hello World")
    'hello_world'
    >>> to_snake_case("  Python-Course   Exercise ")
    'python_course_exercise'
    """
    raise NotImplementedError


def truncate(text: str, max_length: int) -> str:
    """Shorten `text` to at most `max_length` characters.

    If `text` is too long, cut it and end it with "..." so that the result
    is exactly `max_length` characters long (the "..." counts).
    If `text` already fits, return it unchanged.

    >>> truncate("Hello World", 8)
    'Hello...'
    >>> truncate("Hi", 8)
    'Hi'
    """
    raise NotImplementedError


def mask_email(email: str) -> str:
    """Hide the part of `email` before the "@", except its first character.

    Each hidden character becomes a "*". The domain stays visible.

    >>> mask_email("john.doe@example.com")
    'j*******@example.com'
    >>> mask_email("a@b.io")
    'a@b.io'
    """
    raise NotImplementedError
