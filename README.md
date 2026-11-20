# Python-Learnings

To learn python and become python geek

## How the course works

The notes written during the sessions are in [`lessons/`](lessons/).

The course is split into modules (`01_python_fundamentals/`, ...). Each module holds numbered
exercises, one folder per exercise:

```
01_python_fundamentals/
├── 01_string_methods/
│   ├── string_methods.py        # the instructions are at the top: you write the code here
│   └── test_string_methods.py   # the tests: never edit this file
└── 02_string_manipulation/
```

An exercise is done when all its tests pass. We review it together afterwards.

## Daily workflow

Everything goes through `uv`. Never run `python` or `pip` directly.

| I want to... | Command |
|---|---|
| Install everything after a `git pull` | `uv sync` |
| Run the tests of one exercise | `uv run pytest 01_python_fundamentals/01_string_methods` |
| Stop at the first failing test | `uv run pytest -x <folder>` |
| See every test name and its result | `uv run pytest -v <folder>` |
| Run all the tests | `uv run pytest` |
| Try something quickly in a Python shell | `uv run python` |
| Add a library | `uv add <package>` |
| Add a library used only for development | `uv add --dev <package>` |

## When a test fails

1. Read the **last lines** of the pytest output first: the test name, then the `assert` line
   with the value you returned (left) and the expected value (right).
2. Run only that test: `uv run pytest <folder> -k <test_name>`.
3. Reproduce it in `uv run python`: import your function and call it with the same input.
4. Still stuck after 15 minutes? Write down what you tried and ask.

## Submitting an exercise

1. Create a branch: `git switch -c exercise/string-manipulation`
2. Commit your work, push, open a pull request to `main`.
3. We review the pull request together.
