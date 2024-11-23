from abc import ABC, abstractmethod
from typing import final, override

import string

from . import _base


# -- Interface --


class Expr(_base.SymbolicObject):
    """An expression"""

    __slots__ = ()

    @abstractmethod
    def degree(self) -> int: ...


class LinExpr(Expr):
    """A linear expression, that is, having degree 1"""

    __slots__ = ()


class ParamExpr(LinExpr):
    """A parameter expression, that is, having degree 0"""

    __slots__ = ()


class LitExpr(ParamExpr):
    """A literal expression, that is, containing just a literal numeric"""

    __slots__ = ()


class Symbol(Expr):
    """
    A symbol
    """

    valid_name_chars = string.ascii_letters + string.digits + "_"

    __slots__ = ()

    @abstractmethod
    def name(self) -> str: ...


class LinSymbol(Symbol, LinExpr):
    """
    A linear symbol, that is, of degree 1
    """

    __slots__ = ()


class ParamSymbol(Symbol, ParamExpr):
    """
    A pure-parameter symbol, that is, of degree 0
    """

    __slots__ = ()


class InvalidNameError(Exception):
    """
    Raised if an invalid name is passed when constructing a symbol
    """


def unbound_lin_symbol(name: str) -> LinSymbol:
    return _ImplLinSymbol(name)


def unbound_param_symbol(name: str) -> ParamSymbol:
    return _ImplParamSymbol(name)


# -- Implementation --


@final
class _ImplLinSymbol(LinSymbol):

    __slots__ = ("_name",)

    def __init__(self, name: str):
        valid_name_chars = Symbol.valid_name_chars
        if not set(name).issubset(valid_name_chars):
            raise InvalidNameError(
                f"Invalid name for symbol:\n{name=}\n{valid_name_chars=}"
            )
        self._name = name

    # SymbolicObject overrides

    @override
    def identical_to(self, other: _base.SymbolicObject | _base.ScalarLit) -> bool:
        return isinstance(other, _ImplLinSymbol) and other.name() == self._name

    @override
    def __repr__(self) -> str:
        return f"LinSymbol({self._name})"

    @override
    def __str__(self) -> str:
        return self._name

    # Expr overrides

    @override
    def degree(self) -> int:
        return 1

    # Symbol overrides

    @override
    def name(self) -> str:
        return self._name


@final
class _ImplParamSymbol(ParamSymbol):

    __slots__ = ("_name",)

    def __init__(self, name: str):
        valid_name_chars = Symbol.valid_name_chars
        if not set(name).issubset(valid_name_chars):
            raise InvalidNameError(
                f"Invalid name for symbol:\n{name=}\n{valid_name_chars=}"
            )
        self._name = name

    # SymbolicObject overrides

    @override
    def identical_to(self, other: _base.SymbolicObject | _base.ScalarLit) -> bool:
        return isinstance(other, _ImplParamSymbol) and other.name() == self._name

    @override
    def __repr__(self) -> str:
        return f"ParamSymbol({self._name})"

    @override
    def __str__(self) -> str:
        return self._name

    # Expr overrides

    @override
    def degree(self) -> int:
        return 0

    # Symbol overrides

    @override
    def name(self) -> str:
        return self._name
