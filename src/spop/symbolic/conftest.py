import hypothesis.strategies as hys

from . import _expr
from . import _hys as symbolic_hys


hys.register_type_strategy(_expr.LinSymbol, symbolic_hys.lin_symbol())
hys.register_type_strategy(_expr.ParamSymbol, symbolic_hys.param_symbol())
