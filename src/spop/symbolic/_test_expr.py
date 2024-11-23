import pytest
import hypothesis as hy
import hypothesis.strategies as hys

import string

from ._expr import *
from . import _base
from . import _hys as symbolic_hys


# Tests for `unbound_lin_symbol`


@hy.given(symbolic_hys.valid_symbol_name)
def test_unbound_lin_symbol_name_consistent(name: str):
    symbol = unbound_lin_symbol(name)
    assert symbol.name() == name


@hy.given(hys.text())
def test_unbound_lin_symbol_invalid_names_raises(name: str):
    if not set(name).issubset(Symbol.valid_name_chars):
        with pytest.raises(InvalidNameError):
            _ = unbound_lin_symbol(name)


# Tests for `unbound_param_symbol`


@hy.given(symbolic_hys.valid_symbol_name)
def test_unbound_param_symbol_name_consistent(name: str):
    symbol = unbound_param_symbol(name)
    assert symbol.name() == name


@hy.given(hys.text())
def test_unbound_param_symbol_invalid_names_raises(name: str):
    if not set(name).issubset(Symbol.valid_name_chars):
        with pytest.raises(InvalidNameError):
            _ = unbound_param_symbol(name)


# Tests for `LinSymbol`


@hy.given(hys.from_type(LinSymbol), hys.from_type(_base.SymbolicObject))
def test_lin_symbol_identical_to(it: LinSymbol, other: _base.SymbolicObject):
    if not isinstance(other, LinSymbol):
        assert not it.identical_to(other)
    else:
        if it.name() == other.name():
            assert it.identical_to(other)
        else:
            assert not it.identical_to(other)


@hy.given(hys.from_type(LinSymbol))
def test_lin_symbol_repr(it: LinSymbol):
    name = it.name()
    assert repr(it) == f"LinSymbol({name})"


@hy.given(hys.from_type(LinSymbol))
def test_lin_symbol_str(it: LinSymbol):
    name = it.name()
    assert str(it) == name


@hy.given(hys.from_type(LinSymbol))
def test_lin_symbol_degree(it: LinSymbol):
    assert it.degree() == 1


# Tests for `ParamSymbol`


@hy.given(hys.from_type(ParamSymbol), hys.from_type(_base.SymbolicObject))
def test_param_symbol_identical_to(it: ParamSymbol, other: _base.SymbolicObject):
    if not isinstance(other, ParamSymbol):
        assert not it.identical_to(other)
    else:
        if it.name() == other.name():
            assert it.identical_to(other)
        else:
            assert not it.identical_to(other)


@hy.given(hys.from_type(ParamSymbol))
def test_param_symbol_repr(it: ParamSymbol):
    name = it.name()
    assert repr(it) == f"ParamSymbol({name})"


@hy.given(hys.from_type(ParamSymbol))
def test_param_symbol_str(it: ParamSymbol):
    name = it.name()
    assert str(it) == name


@hy.given(hys.from_type(ParamSymbol))
def test_param_symbol_degree(it: ParamSymbol):
    assert it.degree() == 0
