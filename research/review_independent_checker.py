# SPDX-License-Identifier: MIT
import sympy as s
R = s.Rational
z = s.symbols('h x0 x1 x2 y1 y2 u1 u2 v1 v2')
h, x0, x1, x2, y1, y2, u1, u2, v1, v2 = z
k = s.symbols('k1:13')
react = [x0 * y1, v1, v1, h * x1, u1, u1, x1 * y2, v2, v2, h * x2, u2, u2]
changes = [[-0, -1, 0, 0, -1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0, 0, -1, 0], [0, 1, 1, 0, 0, 0, 0, 0, -1, 0], [-1, 0, -1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, -1, 0, 0, 0], [1, 0, 0, 0, 1, 0, -1, 0, 0, 0], [0, 0, -1, 0, 0, -1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 0, -1], [0, 0, 1, 1, 0, 0, 0, 0, 0, -1], [-1, 0, 0, -1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0, 0, -1, 0, 0], [1, 0, 0, 0, 0, 1, 0, -1, 0, 0]]
N = s.Matrix.hstack(*map(s.Matrix, changes))
ode = N * s.Matrix([a * b for a, b in zip(k, react)])
tot = s.Matrix([h + u1 + u2, x0 + v1, x1 + y1 + u1 + v1 + v2, x2 + y2 + u2 + v2])
if not tot.jacobian(z) * N == s.zeros(4, 12):
    raise RuntimeError('Exact check failed: tot.jacobian(z) * N == s.zeros(4, 12)')
aug = s.Matrix(list(tot) + list(ode[4:]))
J = aug.jacobian(z)
a = [R(20827163033, 10847244000), R(401271957, 42422500)]
b = [R(60), R(116, 1025)]
c = [R(26), R(28, 5)]
rates = sum(([2 * c[i] / a[i], 1, 1, 2 * c[i], c[i] / b[i], c[i] / b[i]] for i in range(2)), [])
F = tot.subs({y1: a[0] * h * x1 / x0, y2: a[1] * h * x2 / x1, u1: b[0] * h * x1, u2: b[1] * h * x2, v1: c[0] * h * x1, v2: c[1] * h * x2}, simultaneous=True)
for free in [(R(1, 150), R(5693, 50000), R(3, 10), R(1340)), (R(6, 25), R(1, 2000), R(53, 2000), R(19))]:
    H, X0, X1, X2 = free
    full = free + (a[0] * H * X1 / X0, a[1] * H * X2 / X1, b[0] * H * X1, b[1] * H * X2, c[0] * H * X1, c[1] * H * X2)
    sub = dict(zip(z, full)) | dict(zip(k, rates))
    if not ode.subs(sub) == s.zeros(10, 1):
        raise RuntimeError('Exact check failed: ode.subs(sub) == s.zeros(10, 1)')
    print('totals', list(tot.subs(sub)))
    print('DF', F.jacobian(z[:4]).subs(sub).det())
    print('aug determinant', J.subs(sub).det())
    print('x2-y2', full[3] - full[5])
print('rank', N.rank())
m = s.symbols('m1:11')
M1, M2, M3, M4, M5, M6, M7, M8, M9, M10 = m
A13 = (M6 - M4) * (M10 * M2 * M7 + M10 * M5 * M7 + M10 * M5 * M9 + M10 * M7 * M9 - M5 * M8 * M9)
A1 = M5 * M9 * (M10 * M4 * M6 + M10 * M6 * M7 + M10 * M4 * M8 + M10 * M6 * M8 + M4 * M6 * M8)
A3 = M10 * M2 * M4 * M6 * M7 + M10 * M4 * M5 * M6 * M7 + M10 * M2 * M4 * M7 * M8 + M10 * M4 * M5 * M7 * M8 + M10 * M2 * M6 * M7 * M8 + M2 * M4 * M6 * M7 * M8 + M10 * M5 * M6 * M7 * M8 + M4 * M5 * M6 * M7 * M8 + M10 * M4 * M5 * M6 * M9 + M10 * M4 * M6 * M7 * M9 + M10 * M4 * M5 * M8 * M9 + M10 * M5 * M6 * M8 * M9 + M4 * M5 * M6 * M8 * M9 + M10 * M4 * M7 * M8 * M9 + M4 * M5 * M7 * M8 * M9 + M10 * M6 * M7 * M8 * M9 + M4 * M6 * M7 * M8 * M9
A0 = M5 * M7 * M9 * (M10 * M4 * M6 + M10 * M4 * M8 + M10 * M6 * M8 + M4 * M6 * M8)
g = A13 * M1 * M3 + A1 * M1 + A3 * M3 + A0
B = s.Matrix([[s.degree(r, Z) for r in react] for Z in z])
flux = s.diag(*[2, 1, 1] * 4)
Jflux = N * flux * B.T * s.diag(*m)
Jcrit = tot.jacobian(z).col_join(Jflux[4:, :])
from itertools import combinations
out = 0
for chosen in combinations(range(10), 4):
    wdet = tot.jacobian(z)[:, chosen].det()
    if wdet:
        remaining = [i for i in range(10) if i not in chosen]
        out += (-1) ** (sum(chosen) + 6) * wdet * (N * flux * B.T)[4:, remaining].det() * s.prod((m[i] for i in remaining))
if not s.expand(out - 16 * g) == 0:
    raise RuntimeError('Exact check failed: s.expand(out - 16 * g) == 0')
print('Independent complete m-polynomial equality at all ell=1: PASS')
