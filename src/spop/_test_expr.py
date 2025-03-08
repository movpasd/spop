import pytest

from spop import _testutils

from .expr import *


def test_symbol_add_runtime_types():
    """
    Tests publicly-facing runtime types of addition of two symbols of all degree
    combination
    """
    p = p_symbol("p")
    q = p_symbol("q")
    x = l_symbol("x")
    y = l_symbol("y")

    assert isinstance(p + q, PExpr), "P+P"
    assert isinstance(p + y, LExpr), "P+L"
    assert isinstance(x + q, LExpr), "L+P"
    assert isinstance(x + y, LExpr), "L+L"


@pytest.mark.xfail(reason="nyi", raises=NotImplementedError)
def test_symbol_mul_runtime_types():
    """
    Tests publicly-facing runtime types of multiplication of two symbols of all degree
    combinations
    """
    p = p_symbol("p")
    q = p_symbol("q")
    x = l_symbol("x")
    y = l_symbol("y")

    assert isinstance(p * q, PExpr), "P*P"
    assert isinstance(p * y, LExpr), "P*L"
    assert isinstance(x * q, LExpr), "L*P"

    with pytest.raises(TypeError):
        _ = x * y  # type: ignore


@pytest.mark.xfail(reason="nyi", raises=NotImplementedError)
def test_symbol_sub_runtime_types():
    """
    Tests publicly-facing runtime types of subtraction of two symbols of all degree
    combinations
    """
    p = p_symbol("p")
    q = p_symbol("q")
    x = l_symbol("x")
    y = l_symbol("y")

    assert isinstance(p - q, PExpr), "P-P"
    assert isinstance(p - y, LExpr), "P-L"
    assert isinstance(x - q, LExpr), "L-P"
    assert isinstance(x - y, LExpr), "L-L"


@pytest.mark.xfail(reason="nyi", raises=NotImplementedError)
def test_symbol_neg_runtime_types():
    """
    Tests publicly-facing runtime types of unary negation of symbols of all degrees
    """
    p = p_symbol("p")
    x = l_symbol("x")

    assert isinstance(-p, PExpr), "-P"
    assert isinstance(-x, LExpr), "-L"


def test_symbol_add_static_types():
    """
    Tests static type-checking of addition of two symbols of all degree combinations
    """
    file = "./testdata/mypy_scripts/expr/symbol_add.py"
    hits, status_code, stderr = _testutils.run_mypy(file)

    assert status_code == 0, "expected status code 0"
    assert stderr.strip() == "", "expected emtpy stderr"

    assert len(hits) == 0, "expected no mypy hits"


def test_symbol_mul_static_types():
    """
    Tests static type-checking of addition of two symbols of all degree combinations
    """
    file = "./testdata/mypy_scripts/expr/symbol_mul.py"
    hits, status_code, stderr = _testutils.run_mypy(file)

    assert status_code == 1, "expected status code 1"
    assert stderr.strip() == "", "expected empty stderr"

    expected_hit_line_nos = {11}
    actual_hit_line_nos = set(hit["line"] for hit in hits)
    assert actual_hit_line_nos == expected_hit_line_nos, "wrong mypy hits"


def test_symbol_sub_static_types():
    """
    Tests static type-checking of addition of two symbols of all degree combinations
    """
    file = "./testdata/mypy_scripts/expr/symbol_sub.py"
    hits, status_code, stderr = _testutils.run_mypy(file)

    assert status_code == 0, "expected status code 0"
    assert stderr.strip() == "", "expected empty stderr"

    assert len(hits) == 0, "expected no mypy hits"


def test_symbol_neg_static_types():
    """
    Tests static type-checking of unary negation of symbols of all degrees
    """
    file = "./testdata/mypy_scripts/expr/symbol_neg.py"
    hits, status_code, stderr = _testutils.run_mypy(file)

    assert status_code == 0, "expected status code 0"
    assert stderr.strip() == "", "expected empty stderr"

    assert len(hits) == 0, "expected no mypy hits"
