"""
Test script for static type-checking of expression construction
"""

from typing import Any
import spop as sp


def discard(_: Any):
    pass


def is_param_expr(_: sp.ParamExpr):
    pass


def is_lin_expr(_: sp.LinExpr):
    pass


def _(
    scalar: sp.PyScalar,
    param_expr: sp.ParamExpr,
    other_param_expr: sp.ParamExpr,
    lin_expr: sp.LinExpr,
    other_lin_expr: sp.LinExpr,
):
    # All binary combinations:
    # * scalar . param_expr
    # * scalar . lin_expr
    # * param_expr . scalar
    # * param_expr . other_param_expr
    # * param_expr . lin_expr
    # * lin_expr . scalar
    # * lin_expr . param_expr
    # * lin_expr . other_lin_expr

    # -- Addition --
    # test: ok
    is_param_expr(scalar + param_expr)
    # test: ok
    is_lin_expr(scalar + lin_expr)
    # test: ok
    is_param_expr(param_expr + scalar)
    # test: ok
    is_param_expr(param_expr + other_param_expr)
    # test: ok
    is_lin_expr(param_expr + lin_expr)
    # test: ok
    is_lin_expr(lin_expr + scalar)
    # test: ok
    is_lin_expr(lin_expr + param_expr)
    # test: ok
    is_lin_expr(lin_expr + other_lin_expr)

    # -- Subtraction --
    # test: ok
    is_param_expr(scalar - param_expr)
    # test: ok
    is_lin_expr(scalar - lin_expr)
    # test: ok
    is_param_expr(param_expr - scalar)
    # test: ok
    is_param_expr(param_expr - other_param_expr)
    # test: ok
    is_lin_expr(param_expr - lin_expr)
    # test: ok
    is_lin_expr(lin_expr - scalar)
    # test: ok
    is_lin_expr(lin_expr - param_expr)
    # test: ok
    is_lin_expr(lin_expr - other_lin_expr)

    # -- Multiplication --
    # test: ok
    is_param_expr(scalar * param_expr)
    # test: ok
    is_lin_expr(scalar * lin_expr)
    # test: ok
    is_param_expr(param_expr * scalar)
    # test: ok
    is_param_expr(param_expr * other_param_expr)
    # test: ok
    is_lin_expr(param_expr * lin_expr)
    # test: ok
    is_lin_expr(lin_expr * scalar)
    # test: ok
    is_lin_expr(lin_expr * param_expr)
    # test: fail
    discard(lin_expr * other_lin_expr)

    # -- Division --
    # test: ok
    is_param_expr(scalar / param_expr)
    # test: fail
    discard(scalar / lin_expr)
    # test: ok
    is_param_expr(param_expr / scalar)
    # test: ok
    is_param_expr(param_expr / other_param_expr)
    # test: fail
    discard(param_expr / lin_expr)
    # test: ok
    is_lin_expr(lin_expr / scalar)
    # test: ok
    is_lin_expr(lin_expr / param_expr)
    # test: fail
    discard(lin_expr / other_lin_expr)

    # -- Unary plus --
    # test: ok
    is_param_expr(+param_expr)
    # test: ok
    is_lin_expr(+lin_expr)

    # -- Unary minus --
    # test: ok
    is_param_expr(-param_expr)
    # test: ok
    is_lin_expr(-lin_expr)
