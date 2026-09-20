# Devil's Advocate assessment

Recommendation: **Accept**, as an explicitly unrefereed candidate preprint. No Critical or Major defect identified. This is an internal model review, not independent external specialist evidence.

## Frozen scope

Read `paper/connectedness.tex`, `ASSURANCE.md`, and `CLAIMS.json` in the frozen candidate. Did not read other review reports or modify the target. Review target archive SHA-256 supplied by coordinator: `ad360a172bb4287faa493d898df98cdb6b4a31ddadc1b56bc95125e8f9110bcf`; PDF SHA-256: `f5264f711401f870d8a6aecbf312b4371b2c8c5e609470bbc92b73d8b40445dd`. These hashes identify the assigned target; this role did not independently hash the files.

## Strongest attempted counterarguments

1. **Projection trap, potentially Critical but resolved.** Two disconnected auxiliary components do not imply two disconnected physical images. Conversely, overlapping images only connect their union, not automatically all multistationary parameters. Sections 4–6 explicitly address both directions: the exact fibre meets both components; the degree contrapositive supplies a nonpositive-critical lift for every multistationary parameter; and the coordinate ray attaches each relevant zero-critical lift. Physical paths can switch equilibrium lifts at a common parameter. No continuous lift across the two auxiliary components is required.

2. **Degenerate-parameter gap, potentially Critical but resolved.** A vanishing determinant need not imply multistationarity, and mere closure attachment would not by itself prove path connectedness. The proof does neither: its initial zero-critical point projects to a parameter already assumed multistationary, while every positive time along the explicit ray has strictly negative determinant. The affine formula in m3 proves an entire interval lies in the multistationarity region. Locations: lines 217–221 and 294–298.

3. **Fixed-rate substitution error, potentially Major but resolved.** Differentiating after substituting state-dependent effective constants would invalidate the critical polynomial. Lines 174–191 explicitly differentiate with constants held fixed, then substitute. The arbitrary-flux extension follows from the Schur block determinant: each layer contributes minus tau_i(rho_i+tau_i)(sigma_i+tau_i)m_yi m_ui m_vi. Two layers give the positive denominator factor that cancels the reduced-map denominator. Thus the zero-critical ray is valid even though its physical rates change.

4. **Degree-theorem hypothesis/sign mismatch, potentially Critical but resolved on inspection.** The conservation pivots coincide with the replaced rows; rank six gives positive sign convention. The boundary argument successively forces h, x0, x1, x2 positive and then all remaining species positive. I checked the cited Telek–Feliu arXiv v2 Theorem 2.1(A),(B): its positive-everywhere uniqueness and negative-somewhere multiplicity statements match the manuscript. The contrapositive is legitimate even if a fibre contains only degenerate equilibria. Source: https://arxiv.org/html/2209.13936v2#S2.Thmtheorem1 .

5. **Overlap insufficiently robust, potentially Major but resolved.** Both witnesses have nonzero reduced determinants, allowing two locally distinct positive solution branches for all 16 physical parameters. The opposite strict component signs persist on a common neighborhood. The claim is full-dimensional overlap and does not require an invertible 16-dimensional global projection.

## Fresh arithmetic check

Using a new short SymPy calculation typed from the displayed conservation map and rational witness, independently of the bundled checker code, I obtained zero difference of the four total vectors, reduced determinants

- P: `-50294437400138543733503/24284564239106250000`
- Q: `-895903401800934682060509/31400206507812500`

and x2-y2 values `11224290709/10605625` and `-3412151689/2121125`. These agree exactly with the manuscript and establish the proposed overlap witness at the reduced-map level. This is a separate encoding within the same model review and uses the same SymPy dependency; it is not an independent external rerun or reimplementation claim.

## Assurance and residual limits

No actionable Minor finding is required. The private 135-check report is explicitly supporting and unauthenticated, while the public arbitrary-flux proof is algebraically explained without relying on private code. The manuscript distinguishes exact computation from formal proof, internal model review from external review, and multistationarity from stability. I confirmed that the cited Kaihnsa–Wang v1 Conjecture 4.3 states disconnectivity in the rates-and-totals space: https://arxiv.org/html/2607.25456v1 . No historical priority verification was undertaken here.

Confidence: high in the projection/attachment logic and exact witness arithmetic; moderate-to-high in the written proof as a whole. Scope excludes a full independent symbolic coefficient expansion, proof-assistant verification, exhaustive literature search, visual PDF inspection, and authentication of privately supplied audit material. Nothing identified in this role requires a revision to the frozen candidate.
