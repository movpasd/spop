from spop.expr import *

p = p_symbol("p")
q = p_symbol("q")
x = l_symbol("x")
y = l_symbol("y")

s1: PExpr = p - q
s2: LExpr = p - y
s3: LExpr = x - q
s4: LExpr = x - y
