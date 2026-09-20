# Scalar reduction used to locate the overlap

This reduction is supplementary; the global proof uses the exact two-state certificate rather than numerical continuation.

Use the notation of PROOF.md. Let z=h*x1, r=c2/b2, D=S-r*H, and

    f(z)=a1*z/(E-c1*z)+(b1+c1-r*b1)*z.

For 0<z<E/c1, the unique positive solution of

    r*h^2+(D-f(z))*h-z=0

is

    h(z)=(f(z)-D+sqrt((D-f(z))^2+4*r*z))/(2*r).

For numerical evaluation when D-f(z)>=0, use the algebraically equal expression

    h(z)=2*z/(D-f(z)+sqrt((D-f(z))^2+4*r*z))

to avoid subtraction cancellation. The other free concentrations are

    x0=E-c1*z,
    x1=z/h(z),
    x2=(H-h(z)-b1*z)/(b2*h(z)).

The admissibility condition is H>h(z)+b1*z. It defines exactly one open interval (0,zmax). To see this, implicit differentiation gives

    h'(z)=(1/h+f'(z))/(z/h^2+r),

so

    (h+b1*z)' = [1/h + a1*E/(E-c1*z)^2
                       + b1+c1+b1*z/h^2]/(z/h^2+r) > 0.

At z down to zero, h+b1*z tends to max(0,H-S/r)<H. At z up to E/c1 it tends to infinity. Therefore zmax exists uniquely in (0,E/c1).

Every positive steady state with the fixed rates and totals H,E,S corresponds bijectively to a root in (0,zmax) of

    T(z) = (H-h(z)-b1*z)/(b2*h(z))
               * (1+a2*h(z)^2/z+(b2+c2)*h(z)) = T.

This follows by substituting the reconstructed coordinates into all four conservation laws and the steady-state equations; all denominators are positive on the stated domain. The remaining six species are reconstructed as in PROOF.md. Distinct z give distinct steady states because z=h*x1 is recoverable from the state.

The two sign factors of the auxiliary decomposition have a useful interpretation. Up to strictly positive factors they are

    x2-y2 = x2*(x1-a2*h)/x1,
    f'(z) = a1*E/(E-c1*z)^2+b1+c1-r*b1.

For the second identity, divide the source's second A13 factor by m10*m5*m7*m9. The result is

    y1*v1/x0+v1+u1+y1-v2*u1/u2 = z*f'(z).

Consequently a negative critical point necessarily satisfies

    (x1-a2*h)*f'(z)<0.

This is a necessary condition, not a replacement for the full determinant inequality. It helped find a fibre with both signs, which was subsequently reconstructed and checked exactly.
