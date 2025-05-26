from __future__ import annotations

from abc import ABC
from typing import overload

type PyScalar = int | float
"""
A Python scalar value (int, float)
"""

type ParamExpr = _ParamExpr
"""
A parameter expression, i.e.: a composite symbolic expression of order zero, composed
only of parameters and constants, without any decision variables
"""

type Param = _Param
"""
A parameter, i.e.: a symbol which is substituted with an input value before solving
a model
"""

type LinExpr = _LinExpr
"""
A linear expression, i.e.: composite symbolic expression of order one
"""

type Var = _Var
"""
A decision variable, i.e.: a symbol which is optimised over, and whose value is
therefore an output of the model optimisation
"""

type Expr = LinExpr | ParamExpr
"""
A composite symbolic expression of any order
"""


def unbound_param(name: str) -> Param:
    """
    Create a new parameter that is not bound to any model
    """
    raise NotImplementedError()


def unbound_var(name: str) -> Var:
    """
    Create a new decision variable that is not bound to any model
    """
    raise NotImplementedError()


class _ParamExpr(ABC):
    @overload
    def __add__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __add__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __add__(self, other):
        raise NotImplementedError()

    @overload
    def __radd__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __radd__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __radd__(self, other):
        raise NotImplementedError()

    @overload
    def __sub__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __sub__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __sub__(self, other):
        raise NotImplementedError()

    @overload
    def __rsub__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __rsub__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __rsub__(self, other):
        raise NotImplementedError()

    @overload
    def __mul__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __mul__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __mul__(self, other):
        raise NotImplementedError()

    @overload
    def __rmul__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __rmul__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __rmul__(self, other):
        raise NotImplementedError()

    def __truediv__(self, other: ParamExpr | PyScalar) -> ParamExpr:
        raise NotImplementedError()

    @overload
    def __rtruediv__(self, other: ParamExpr | PyScalar) -> ParamExpr: ...
    @overload
    def __rtruediv__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __rtruediv__(self, other):
        raise NotImplementedError()

    def __pos__(self) -> ParamExpr:
        raise NotImplementedError()

    def __neg__(self) -> ParamExpr:
        raise NotImplementedError()


class _Param(_ParamExpr):
    pass


class _LinExpr(ABC):
    @overload
    def __add__(self, other: ParamExpr | PyScalar) -> LinExpr: ...
    @overload
    def __add__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __add__(self, other):
        raise NotImplementedError()

    @overload
    def __radd__(self, other: ParamExpr | PyScalar) -> LinExpr: ...
    @overload
    def __radd__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __radd__(self, other):
        raise NotImplementedError()

    @overload
    def __sub__(self, other: ParamExpr | PyScalar) -> LinExpr: ...
    @overload
    def __sub__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __sub__(self, other):
        raise NotImplementedError()

    @overload
    def __rsub__(self, other: ParamExpr | PyScalar) -> LinExpr: ...
    @overload
    def __rsub__(self, other: LinExpr) -> LinExpr: ...
    # implementation
    def __rsub__(self, other):
        raise NotImplementedError()

    def __mul__(self, other: ParamExpr | PyScalar) -> LinExpr:
        raise NotImplementedError()

    def __rmul__(self, other: ParamExpr | PyScalar) -> LinExpr:
        raise NotImplementedError()

    def __truediv__(self, other: ParamExpr | PyScalar) -> LinExpr:
        raise NotImplementedError()

    # def __rtruediv__(self, other):
    #     ...

    def __pos__(self) -> LinExpr:
        raise NotImplementedError()

    def __neg__(self) -> LinExpr:
        raise NotImplementedError()


class _Var(_LinExpr):
    pass
