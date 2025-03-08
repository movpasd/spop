"""
Type-safe expression-building DSL
"""

# Docstring draft
# ---------------

# The base unit of the expression is the symbol. Symbols are atomic and can't be broken
# down any further. These are then composed into value-expressions using mathematical
# operations `+`, `-` (subtraction), `-` (unary minus), and `*`, into. Two
# value-expressions can then be compared using `==`, `<=`, and `>=` into
# comparison-expressions.

# As this module is meant to represent expressions for optimisation problems, it keeps
# track of the polynomial degree of expressions. However, this is not just the number of
# symbol terms in a factor, because we want symbol terms to be substitutable with
# higher-degree expressions, or even zero-degree expressions. (The polynomial order we
# want to keep track of will be the order in decision variables, but parameter variables
# should be allowed.)

# For the initial release of `spop`, we will track two degrees, and therefore be able to
# represent only purely-linear (or MILP) problems. We use the symbols:

# * P (for "parameter"): degree 0
# * L (for "linear"): degree 1

# Trying to construct of higher-order expressions should result in a statically resolvable
# type error.

# Strictly speaking, expressions of a degree may contain high-degree terms that cancel
# out, producing an expression of a mathematically lower degree. For example, `ax^2 - ax^2
# + 3x` is mathematically equal to the linear expression `3x`. It's not possible to avoid
# this statically, so we will consider such expressions to be quadratic. Similarly, it is
# possible for an expression to considered a higher degree even though mathematically it
# is of a lower one because of `0` coefficients.

# To minimise sub-typing and the complexities associated with it, the degrees above are
# disjunctive.

from __future__ import annotations

from typing import Any, Type, overload

from abc import ABC, abstractmethod
import inspect


def p_symbol(name: str) -> PExpr:
    return _PSymbol(name)


def l_symbol(name: str) -> LExpr:
    return _LSymbol(name)


@overload
def add(self: PExpr, other: PExpr) -> PExpr: ...
@overload
def add(self: LExpr, other: PExpr) -> LExpr: ...
@overload
def add(self: PExpr, other: LExpr) -> LExpr: ...
@overload
def add(self: LExpr, other: LExpr) -> LExpr: ...
# implementation
def add(self: Any, other: Any) -> Expr:
    if not isinstance(self, Expr) or not isinstance(other, Expr):
        raise TypeError(f"expected (Expr, Expr), got ({type(self)}, {type(other)})")

    match (self, other):
        case (PExpr(), PExpr()):
            return _PAdd(self, other)
        case (PExpr(), LExpr()):
            return _LAdd(self, other)
        case (LExpr(), PExpr()):
            return _LAdd(self, other)
        case (LExpr(), LExpr()):
            return _LAdd(self, other)
        case _:
            raise TypeError(
                f"can't handle ({type(self)}, {type(other)}) -- "
                f"did you subclass `Expr`?"
            )


@overload
def mul(self: PExpr, other: PExpr) -> PExpr: ...
@overload
def mul(self: LExpr, other: PExpr) -> LExpr: ...
@overload
def mul(self: PExpr, other: LExpr) -> LExpr: ...
# implementation
def mul(self: Expr, other: Any) -> Expr:
    raise NotImplementedError()


@overload
def sub(self: PExpr, other: PExpr) -> PExpr: ...
@overload
def sub(self: LExpr, other: PExpr) -> LExpr: ...
@overload
def sub(self: PExpr, other: LExpr) -> LExpr: ...
@overload
def sub(self: LExpr, other: LExpr) -> LExpr: ...
# implementation
def sub(self: Expr, other: Any) -> Expr:
    raise NotImplementedError()


@overload
def neg(self: PExpr) -> PExpr: ...
@overload
def neg(self: LExpr) -> LExpr: ...
# implementation
def neg(self: Expr) -> Expr:
    raise NotImplementedError()


# TODO: pos() -- unary plus


class Expr(ABC):
    """
    Base class for expressions

    Sealed: do not subclass.
    """

    # Mathematical operations are implemented in module-level functions (`add`, `mul`,
    # ...) rather than as methods because it's easier to do double dispatch that way
    __add__ = add
    __mul__ = mul
    __sub__ = sub
    __neg__ = neg

    @abstractmethod
    def ast_dict(self) -> dict:
        """[Unstable] The abstract syntax tree as a dictionary"""
        ...


class PExpr(Expr):
    """
    Base class for parameter-level (i.e.: degree-zero) expressions

    Sealed: do not subclass.
    """


class LExpr(Expr):
    """
    Base class for linear (i.e.: degree-one) expressions

    Sealed: do not subclass.
    """


# ---


class _PSymbol(PExpr):
    def __init__(self, name: str):
        self.name = name

    def ast_dict(self):
        return {"type": "PSymbol", "name": self.name}


class _LSymbol(LExpr):
    def __init__(self, name: str):
        self.name = name

    def ast_dict(self):
        return {"type": "LSymbol", "name": self.name}


class _PAdd[L: PExpr, R: PExpr](PExpr):
    def __init__(self, left: L, right: R):
        self.left: L = left
        self.right: R = right

    def ast_dict(self):
        return {
            "type": "PAdd",
            "left": self.left.ast_dict(),
            "right": self.right.ast_dict(),
        }


class _LAdd[L: PExpr | LExpr, R: PExpr | LExpr](LExpr):
    def __init__(self, left: L, right: R):
        self.left: L = left
        self.right: R = right

    def ast_dict(self):
        return {
            "type": "LAdd",
            "left": self.left.ast_dict(),
            "right": self.right.ast_dict(),
        }


