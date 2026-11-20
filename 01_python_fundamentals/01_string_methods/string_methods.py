"""
String methods

Instructions:
    A string comes with dozens of built-in methods. This exercise is a tour of them.
    Implement every function below so that all the tests pass.
    Each function fits in ONE line: if yours is longer, there is a method you have
    not found yet.

How to find the right method:
    uv run python
    >>> dir(str)              # every method a string has
    >>> help(str.startswith)  # what one method does
    >>> "hello".upper()       # try it

Methods to explore (some are not needed, all are worth reading):
    case       upper, lower, title, capitalize, swapcase, casefold
    search     startswith, endswith, find, index, rfind, count
    check      isdigit, isalpha, isalnum, isspace, isupper, islower
    clean      strip, lstrip, rstrip, removeprefix, removesuffix, replace
    split      split, rsplit, splitlines, partition, join
    layout     center, ljust, rjust, zfill
    format     f-strings: f"{value:.2f}", f"{text:>10}"

Run the tests:
    uv run pytest 01_python_fundamentals/01_string_methods

Rules:
    - No imports.
    - Do not change the function names or their parameters.
    - Do not edit test_string_methods.py.

Documentation:
    https://docs.python.org/3/library/stdtypes.html#string-methods
"""

# --- Case ---------------------------------------------------------------------


def shout(text: str) -> str:
    """Return `text` in upper case.

    >>> shout("hello")
    'HELLO'
    """
    raise NotImplementedError


def whisper(text: str) -> str:
    """Return `text` in lower case.

    >>> whisper("HeLLo")
    'hello'
    """
    raise NotImplementedError


def to_title(text: str) -> str:
    """Return `text` with the first letter of every word in upper case.

    >>> to_title("the lord of the rings")
    'The Lord Of The Rings'
    """
    raise NotImplementedError


# --- Search -------------------------------------------------------------------


def is_secure_url(url: str) -> bool:
    """Return True if `url` begins with "https://".

    >>> is_secure_url("https://papernest.com")
    True
    >>> is_secure_url("http://papernest.com")
    False
    """
    raise NotImplementedError


def is_python_file(filename: str) -> bool:
    """Return True if `filename` ends with ".py".

    >>> is_python_file("main.py")
    True
    >>> is_python_file("notes.txt")
    False
    """
    raise NotImplementedError


def count_occurrences(text: str, word: str) -> int:
    """Return how many times `word` appears in `text`.

    >>> count_occurrences("the cat and the hat", "the")
    2
    """
    raise NotImplementedError


def find_position(text: str, sub: str) -> int:
    """Return the index where `sub` first appears in `text`, or -1 if it is absent.

    >>> find_position("hello world", "world")
    6
    >>> find_position("hello world", "python")
    -1
    """
    raise NotImplementedError


# --- Check --------------------------------------------------------------------


def is_number(text: str) -> bool:
    """Return True if `text` is made only of digits (and is not empty).

    >>> is_number("2026")
    True
    >>> is_number("20.26")
    False
    """
    raise NotImplementedError


def is_word(text: str) -> bool:
    """Return True if `text` is made only of letters (and is not empty).

    >>> is_word("python")
    True
    >>> is_word("python3")
    False
    """
    raise NotImplementedError


# --- Clean --------------------------------------------------------------------


def clean_input(text: str) -> str:
    """Remove the spaces, tabs and newlines at both ends of `text`.

    >>> clean_input("  hello world \\n")
    'hello world'
    """
    raise NotImplementedError


def strip_hashtag(tag: str) -> str:
    """Remove ONE leading "#" from `tag`, if there is one.

    >>> strip_hashtag("#python")
    'python'
    >>> strip_hashtag("##python")
    '#python'
    >>> strip_hashtag("python")
    'python'
    """
    raise NotImplementedError


def remove_extension(filename: str, extension: str) -> str:
    """Remove `extension` from the end of `filename`, if it is there.

    >>> remove_extension("report.pdf", ".pdf")
    'report'
    >>> remove_extension("report.pdf", ".txt")
    'report.pdf'
    """
    raise NotImplementedError


def censor(text: str, word: str) -> str:
    """Replace every occurrence of `word` in `text` with as many "*" as it has letters.

    >>> censor("this is bad, very bad", "bad")
    'this is ***, very ***'
    """
    raise NotImplementedError


# --- Split and join -----------------------------------------------------------


def split_csv_line(line: str) -> list[str]:
    """Split a line of comma-separated values.

    >>> split_csv_line("alice,30,paris")
    ['alice', '30', 'paris']
    """
    raise NotImplementedError


def join_with_commas(words: list[str]) -> str:
    """Join `words` with ", " between them.

    >>> join_with_commas(["red", "green", "blue"])
    'red, green, blue'
    """
    raise NotImplementedError


def get_lines(text: str) -> list[str]:
    """Return the lines of `text`, without the newline characters.

    >>> get_lines("first\\nsecond\\nthird")
    ['first', 'second', 'third']
    """
    raise NotImplementedError


# --- Layout and format --------------------------------------------------------


def pad_number(number: int, width: int) -> str:
    """Return `number` as a string, with zeros on the left to reach `width` characters.

    >>> pad_number(7, 3)
    '007'
    >>> pad_number(1234, 3)
    '1234'
    """
    raise NotImplementedError


def frame_title(title: str, width: int) -> str:
    """Center `title` in a string of `width` characters, filled with "*".

    >>> frame_title("menu", 10)
    '***menu***'
    """
    raise NotImplementedError


def format_price(amount: float) -> str:
    """Return `amount` with exactly 2 decimals, followed by " EUR".

    >>> format_price(9.5)
    '9.50 EUR'
    >>> format_price(3.14159)
    '3.14 EUR'
    """
    raise NotImplementedError
