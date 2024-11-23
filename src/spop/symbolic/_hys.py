"""
Hypothesis strategies for the `symbolic` module
"""

import hypothesis.strategies as hys

from . import _expr


valid_symbol_name = hys.text(_expr.Symbol.valid_name_chars)


@hys.composite
def lin_symbol(draw: hys.DrawFn) -> _expr.LinSymbol:
    name = draw(valid_symbol_name)
    return _expr.unbound_lin_symbol(name)


@hys.composite
def param_symbol(draw: hys.DrawFn) -> _expr.ParamSymbol:
    name = draw(valid_symbol_name)
    return _expr.unbound_param_symbol(name)
