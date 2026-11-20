"""
Environment check

Run it once your project is set up:
    uv run pytest 00_setup

If both tests pass, your environment is ready. Never edit this file.
"""

import sys


def test_python_version_is_at_least_3_13() -> None:
    assert sys.version_info >= (3, 13), (
        f"Python {sys.version_info.major}.{sys.version_info.minor} found, 3.13+ expected. "
        "Fix it with: uv python pin 3.13"
    )


def test_running_inside_a_virtual_environment() -> None:
    assert sys.prefix != sys.base_prefix, (
        "Tests are not running inside a virtual environment. Use: uv run pytest"
    )
