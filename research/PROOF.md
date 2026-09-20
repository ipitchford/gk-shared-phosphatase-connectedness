# Connectedness of the two-layer shared-phosphatase multistationarity region

Status: full mathematical argument with exact computational checks and one fresh-context adversarial model review; unrefereed and not formally verified. Date: 2026-09-20.

## Claim
For network (34) of Kaihnsa and Wang, arXiv:2607.25456v1, with all twelve reaction rate constants and all four conserved totals positive, the set Omega of parameters admitting at least two distinct positive steady states is path connected. Thus it has exactly one connected component. This contradicts Conjecture 4.3 of that version. No assertion about stability is made.

## 1. Exact overlap witness
Write a_i=alpha_i, b_i=beta_i, c_i=gamma_i, in the notation of equation (4) of the source. Use

    a1 = 20827163033/10847244000
    a2 = 401271957/42422500
    b1 = 60
    b2 = 116/1025
    c1 = 26
    c2 = 28/5.

These are realized by strictly positive rates, independently for each layer i, via

    (k_(6i-5), k_(6i-4), k_(6i-3), k_(6i-2), k_(6i-1), k_(6i))
      = (2*c_i/a_i, 1, 1, 2*c_i, c_i/b_i, c_i/b_i).

The two free-coordinate vectors (h,x0,x1,x2) are

    P = (1/150, 5693/50000, 3/10, 1340)
    Q = (6/25, 1/2000, 53/2000, 19).

Reconstruct the remaining coordinates by

    y1=a1*h*x1/x0; y2=a2*h*x2/x1;
    u1=b1*h*x1; u2=b2*h*x2;
    v1=c1*h*x1; v2=c2*h*x2.

Every coordinate is positive. Both yield the same totals, ordered (H,E,S,T):

    (11661/10250, 8293/50000,
     45678099759/903937000, 727342892891/434830625).

The conservation map on free steady-state coordinates is

    F(h,x0,x1,x2) = (
      h+b1*h*x1+b2*h*x2,
      x0+c1*h*x1,
      x1+a1*h*x1/x0+(b1+c1)*h*x1+c2*h*x2,
      x2+a2*h*x2/x1+(b2+c2)*h*x2).

Its Jacobian determinants, with columns ordered (h,x0,x1,x2), are exactly

    det DF(P) = -50294437400138543733503/24284564239106250000
    det DF(Q) = -895903401800934682060509/31400206507812500.

Both are strictly negative. Proposition 2.2 of Kaihnsa–Wang identifies this sign with the critical determinant sign.

For inverse concentration coordinates m, ordered (H1,X0,X1,X2,Y1,Y2,U1,U2,V1,V2), the first auxiliary separating factor is m6-m4. Its sign equals sign(x2-y2). At P and Q respectively,

    x2-y2 = 11224290709/10605625 > 0,
    x2-y2 = -3412151689/2121125 < 0.

Consequently these two negative-critical incidence points belong to opposite auxiliary components and project to precisely the same physical parameter point.

## 2. The two auxiliary components and their closure
Use the positive convex-coordinate parametrization f(m,l) of equation (35). It is surjective onto positive steady-state incidence points: l consists of the four positive reverse-reaction fluxes and the two positive common catalytic fluxes; the steady-state complex and substrate equations give the remaining fluxes. Rates are recovered by dividing each reaction flux by its reactant monomial. Thus every positive-rate positive steady state has a positive lift.

The critical function is a strictly positive l-dependent factor times

    g = A13*m1*m3 + A1*m1 + A3*m3 + A0,

where A0,A1,A3 are strictly positive on the positive orthant, and

    A13 = (m6-m4)*(m10*m2*m7 + m10*m5*m7
                       + m10*m5*m9 + m10*m7*m9 - m5*m8*m9).

These are equation (37) and its coefficients in Kaihnsa–Wang. Define

    R = m10*(m2*m7+m5*m7+m5*m9+m7*m9)/(m5*m9).

The base A13<0 has exactly two path-connected components:

    Mminus: m6<m4 and m8<R;
    Mplus:  m6>m4 and m8>R.

For Mminus, write m4=m6+s and m8=t*R with s>0, 0<t<1; for Mplus write m6=m4+s and m8=R+s8 with s,s8>0. The remaining coordinates are independently positive. These are homeomorphic parametrizations by products of positive intervals.

For either base, g<0 is equivalent to

    m1 > A3/(-A13),
    m3 > (A0+A1*m1)/(-A13*m1-A3).

Each successive strict lower bound can be parametrized by adding an arbitrary positive number. Therefore each base lifts to one path-connected component Dminus or Dplus of g<0, and they are the only components. Multiplication by the positive l orthant preserves this conclusion. The displayed m3 bound corrects a sign typo in the source PDF's final display in the proof of Theorem 4.2.

At any positive point with g=0, positivity of A0,A1,A3 implies A13<0, and

    partial g / partial m3 = A13*m1+A3
                          = -(A0+A1*m1)/m3 < 0.

Increasing m3 by any epsilon>0 (holding the other coordinates fixed) gives g<0. This proves the relative closure property and supplies an explicit curve into the negative set from every zero point.

## 3. Why the overlap proves the global conclusion
Let pi map a steady-state incidence point to its reaction rates and conserved totals. In convex coordinates this is explicitly (m,l) -> (kappa(m,l), W*(1/m)), where W is the four-row conservation matrix. Paths in this proof may vary both rates and totals. Let Bminus and Bplus be the physical images of Dminus x R^6_>0 and Dplus x R^6_>0. Each is path connected by continuity. Every point in either image is multistationary by the negative-critical determinant criterion. Section 1 gives a point of Bminus intersect Bplus. Therefore B=Bminus union Bplus is nonempty and path connected inside Omega.

For an arbitrary p in Omega, there exists a positive steady state over p with critical determinant <=0. This is the contrapositive of the uniqueness part of the degree criterion; equivalently it is Lemma 6.4 of Telek–Feliu, arXiv:2209.13936v2 (18 March 2023). Its hypotheses hold here: the network is conservative, hence dissipative, and has no relevant boundary steady states.

For completeness, the latter fact follows directly. At any nonnegative steady state the binding and catalytic flux equalities hold. If h=0, then u1=u2=0, contradicting H>0. If x0=0, then v1=0, contradicting E>0. If x1=0, then u1=v1=0; x0>0 forces y1=0; also v2=0, contradicting S>0. If x2=0, then u2=v2=0 and x1>0 forces y2=0, contradicting T>0. Positivity of all remaining coordinates follows from the binding/flux equations. Conservation supplies a strictly positive linear conserved quantity and bounded compatibility classes.

Lift the selected steady state to (m,l). If g<0, p is already in B. If g=0, increase m3 as in Section 2 and project the resulting curve. At its starting point the projection is p in Omega; at every later point its critical determinant is negative, so its projection belongs to B and hence Omega. This joins p to B through a continuous path entirely inside Omega, including at degenerate p.

Every point of Omega is thus path-connected to the same nonempty path-connected set B. Omega is path connected. This argument controls the entire path interval by strict algebraic inequalities, not by sampled numerical continuation.

## 4. The overlap contains an open physical neighborhood

The two nonzero DF determinants imply by the implicit function theorem that both steady states continue for all physical parameters in some common open neighborhood of the witness. Shrink that neighborhood to preserve positivity, negative determinant, distinctness, and the opposite signs of x2-y2. This neighborhood belongs to both Bminus and Bplus. Thus their intersection has nonempty interior in the full sixteen-dimensional physical parameter space. The connection is not confined to a singular coincidence.

## Source and assurance boundary
The degree criterion is used as an external theorem. The polynomial and sign reduction are also reproduced below and in the exact checkers, so the proof does not depend on an unverified arbitrary-flux factorization. The overlap arithmetic is local exact computation, not a literature claim. No formal proof assistant has checked this argument; no stability or historical priority claim follows. Source numbering differs between arXiv and published versions of Telek–Feliu, so both theorem statement and version must be recorded rather than citing an unverified number.


## Appendix: direct verification of the global critical sign

At an arbitrary positive incidence point put m_j=1/(species j). The effective constants are necessarily

    a1=m1*m3/(m5*m2), a2=m1*m4/(m6*m3),
    b1=m1*m3/m7, b2=m1*m4/m8,
    c1=m1*m3/m9, c2=m1*m4/m10.

Differentiate F at fixed effective constants first, then substitute these identities. This gives the matrix

    [1+m1/m7+m1/m8,                  0, m3/m7,                   m4/m8]
    [m1/m9,                          1, m3/m9,                   0]
    [m1*(1/m5+1/m7+1/m9+1/m10), -m2/m5, 1+m3*(1/m5+1/m7+1/m9), m4/m10]
    [m1*(1/m6+1/m8+1/m10),           0, -m3/m6, 1+m4*(1/m6+1/m8+1/m10)].

Expanding its determinant gives exactly

    det DF = g/(m10*m5*m6*m7*m8*m9).

The complete coefficients are in certificate.json. check_certificate.py computes this symbolic identity, the factorization of A13, and strict positivity of all coefficients of A0,A1,A3. The independent review checker obtains the same g directly from the reaction stoichiometry at unit elementary fluxes.

To connect DF to the degree criterion for every positive rate choice, form the augmented steady-state map psi with the four conservation laws followed by the six ODEs for y1,y2,u1,u2,v1,v2. Its Jacobian has blocks A,B,C,D corresponding to free variables (h,x0,x1,x2) and remaining species (y1,y2,u1,u2,v1,v2). Differentiating the steady-state parametrization gives C+D*M=0 and DF=A+B*M. Hence det Jpsi = det DF * det D.

After simultaneously grouping D's rows and columns by layer, its ith block is

    [-k_(6i-5)*x_(i-1), k_(6i),              k_(6i-4)]
    [0,                   -(k_(6i-1)+k_(6i)), 0]
    [k_(6i-5)*x_(i-1),  0,                  -(k_(6i-4)+k_(6i-3))].

Its determinant is -k_(6i-5)*x_(i-1)*k_(6i-3)*(k_(6i-1)+k_(6i)). There are two layers, so det D is strictly positive. The conservation rows are row-reduced with pivots in the first four species, and the stoichiometric rank is six. Therefore Jpsi is exactly the augmented matrix in the degree theorem and the degree sign (-1)^6 is positive. This proves the global critical sign correspondence for arbitrary fluxes and rates.

## Reproduction and references

Run `python3 check_certificate.py` and `python3 review_independent_checker.py` from this directory with SymPy 1.14.0. Both use exact rational arithmetic; numerical search is not a dependency of the proof. See REVIEW.md for the independent review's scope and PRIOR_ART.md for the bounded search.

- Kaihnsa and Wang, [arXiv:2607.25456v1](https://arxiv.org/abs/2607.25456v1), especially equations (4), (5), (34)–(37), Theorem 4.2, Conjecture 4.3.
- Telek and Feliu, [arXiv:2209.13936v2](https://arxiv.org/abs/2209.13936v2), Theorem 2.1 and Lemma 6.4; published in PLOS Computational Biology 19(3), e1010970 (2023), [DOI](https://doi.org/10.1371/journal.pcbi.1010970).
