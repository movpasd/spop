import pytest

from mypy.api import run as run_mypy

from spop import _testutils

from .expr import *


@pytest.mark.xfail(reason="nyi")
def test_symbol_add_runtime_types():
    """
    Tests publicly-facing runtime types of addition of two symbols of all type
    combination
    """
    p = p_symbol("p")
    q = p_symbol("q")
    x = l_symbol("x")
    y = l_symbol("y")

    assert isinstance(p + q, PExpr)
    assert isinstance(p + y, LExpr)
    assert isinstance(x + q, LExpr)
    assert isinstance(x + y, LExpr)


@pytest.mark.xfail(reason="nyi")
def test_symbol_mul_runtime_types():
    """
    Tests publicly-facing runtime types of multiplication of two symbols of all type
    combination
    """
    p = p_symbol("p")
    q = p_symbol("q")
    x = l_symbol("x")
    y = l_symbol("y")

    assert isinstance(p * q, PExpr)
    assert isinstance(p * y, LExpr)
    assert isinstance(x * q, LExpr)

    with pytest.raises(TypeError):
        _ = x * y  # type: ignore


def test_symbol_add_static_types():
    """
    Tests static type-checking of addition of two symbols of all type combination
    """
    stdout, stderr, status_code = run_mypy(
        [
            "-O",
            "json",
            "--",
            "./testdata/mypy_scripts/expr/symbol_add.py",
        ]
    )
    assert status_code == 0
    assert stderr.strip() == ""

    hits = _testutils.parse_mypy_output(stdout)
    assert len(hits) == 0


def test_symbol_mul_static_types():
    """
    Tests static type-checking of addition of two symbols of all type combination
    """
    stdout, stderr, status_code = run_mypy(
        [
            "-O",
            "json",
            "--",
            "./testdata/mypy_scripts/expr/symbol_mul.py",
        ]
    )
    assert status_code == 1
    assert stderr.strip() == ""

    hits = _testutils.parse_mypy_output(stdout)
    expected_hit_lines = {11}
    assert set(hit["line"] for hit in hits) == expected_hit_lines
