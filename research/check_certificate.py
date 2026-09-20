# SPDX-License-Identifier: MIT
"""Exact witness and symbolic critical-polynomial check. Requires SymPy."""
import sympy as s
import json
from pathlib import Path
R = s.Rational
a, A, b, B, c, C = map(R, ['20827163033/10847244000', '401271957/42422500', '60', '116/1025', '26', '28/5'])
p = [R(1, 150), R(5693, 50000), R(3, 10), R(1340)]
q = [R(6, 25), R(1, 2000), R(53, 2000), R(19)]
h, e, x, t = s.symbols('h e x t', positive=True)
aa, AA, bb, BB, cc, CC = s.symbols('a A b B c C', positive=True)
F = s.Matrix([h + bb * h * x + BB * h * t, e + cc * h * x, x + aa * h * x / e + (bb + cc) * h * x + CC * h * t, t + AA * h * t / x + (BB + CC) * h * t])
J = F.jacobian([h, e, x, t])
eff = dict(zip([aa, AA, bb, BB, cc, CC], [a, A, b, B, c, C]))
expected = [R('11661/10250'), R('8293/50000'), R('45678099759/903937000'), R('727342892891/434830625')]
rates = []
for ai, bi, ci in [(a, b, c), (A, B, C)]:
    k = [2 * ci / ai, R(1), R(1), 2 * ci, ci / bi, ci / bi]
    if not k[3] / (k[4] + k[5]) == bi:
        raise RuntimeError('Exact check failed: k[3] / (k[4] + k[5]) == bi')
    if not k[5] * k[3] / (k[2] * (k[4] + k[5])) == ci:
        raise RuntimeError('Exact check failed: k[5] * k[3] / (k[2] * (k[4] + k[5])) == ci')
    if not k[5] * k[3] * (k[1] + k[2]) / (k[2] * k[0] * (k[4] + k[5])) == ai:
        raise RuntimeError('Exact check failed: k[5] * k[3] * (k[1] + k[2]) / (k[2] * k[0] * (k[4] + k[5])) == ai')
    rates += k
states = []
dets = []
sides = []
for free in [p, q]:
    sub = eff | dict(zip([h, e, x, t], free))
    if not list(F.subs(sub)) == expected:
        raise RuntimeError('Exact check failed: list(F.subs(sub)) == expected')
    det = s.factor(J.subs(sub).det())
    if not det < 0:
        raise RuntimeError('Exact check failed: det < 0')
    hh, ee, xx, tt = free
    state = free + [a * hh * xx / ee, A * hh * tt / xx, b * hh * xx, B * hh * tt, c * hh * xx, C * hh * tt]
    if not all((z > 0 for z in state)):
        raise RuntimeError('Exact check failed: all((z > 0 for z in state))')
    side = state[3] - state[5]
    states.append(state)
    dets.append(det)
    sides.append(side)
if not (sides[0] > 0 and sides[1] < 0):
    raise RuntimeError('Exact check failed: sides[0] > 0 and sides[1] < 0')
m = s.symbols('m1:11', positive=True)
m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = m
msub = {h: 1 / m1, e: 1 / m2, x: 1 / m3, t: 1 / m4, aa: m1 * m3 / (m5 * m2), AA: m1 * m4 / (m6 * m3), bb: m1 * m3 / m7, BB: m1 * m4 / m8, cc: m1 * m3 / m9, CC: m1 * m4 / m10}
JM = J.subs(msub, simultaneous=True).applyfunc(s.cancel)
D = s.factor(JM.det(method='domain-ge'))
num, den = s.fraction(D)
if not (all((v >= 0 for v in s.Poly(den, m).coeffs())) and den != 0):
    raise RuntimeError('Exact check failed: all((v >= 0 for v in s.Poly(den, m).coeffs())) and den != 0')
poly = s.Poly(num, m1, m3)
if not set(poly.monoms()) == {(1, 1), (1, 0), (0, 1), (0, 0)}:
    raise RuntimeError('Exact check failed: set(poly.monoms()) == {(1, 1), (1, 0), (0, 1), (0, 0)}')
A13 = poly.coeff_monomial(m1 * m3)
if not s.factor(A13 - (m6 - m4) * (m10 * m2 * m7 + m10 * m5 * m7 + m10 * m5 * m9 + m10 * m7 * m9 - m5 * m8 * m9)) == 0:
    raise RuntimeError('Exact check failed: s.factor(A13 - (m6 - m4) * (m10 * m2 * m7 + m10 * m5 * m7 + m10 * m5 * m9 + m10 * m7 * m9 - m5 * m8 * m9)) == 0')
coefficients = {}
for name, mon in [('A1', m1), ('A3', m3), ('A0', 1)]:
    expr = poly.coeff_monomial(mon)
    if not all((v > 0 for v in s.Poly(expr, m2, m4, m5, m6, m7, m8, m9, m10).coeffs())):
        raise RuntimeError('Exact check failed: all((v > 0 for v in s.Poly(expr, m2, m4, m5, m6, m7, m8, m9, m10).coeffs()))')
    coefficients[name] = str(expr)
report = {'rates': list(map(str, rates)), 'totals': list(map(str, expected)), 'states': [list(map(str, st)) for st in states], 'determinants': list(map(str, dets)), 'x2_minus_y2': list(map(str, sides)), 'symbolic_det_denominator': str(den), 'A13': str(s.factor(A13)), **coefficients, 'sympy_version': s.__version__, 'result': 'PASS: exact overlap and symbolic sign structure'}
Path(__file__).with_name('certificate.json').write_text(json.dumps(report, indent=2) + '\n')
print(report['result'])
print('Symbolic denominator:', den)
print('Determinants:', dets)
