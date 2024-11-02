"""
Pytest global test configuration
"""

import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--pre-commit",
        action="store_true",
        dest="pre_commit",
        help="used by git pre-commit hook",
    )
