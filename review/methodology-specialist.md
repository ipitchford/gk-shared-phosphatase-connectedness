# Internal methodology review

Recommendation: **Accept** as an unrefereed candidate, with optional improvements below. No required mathematical revision identified.

## Reviewed object and scope

Reviewed the frozen candidate manuscript `paper/connectedness.tex`, public checker sources, `verify.py`, certificate semantics, assurance/claims metadata, and proof obligations. Did not edit the candidate or consult other internal role reports. Confirmed SHA-256 of archive `ad360a172bb4287faa493d898df98cdb6b4a31ddadc1b56bc95125e8f9110bcf` and PDF `f5264f711401f870d8a6aecbf312b4371b2c8c5e609470bbc92b73d8b40445dd`.

This is a producer-coordinated internal model assessment. It is not unaffiliated specialist review, independent external assurance, or formal verification.

## Findings on load-bearing reasoning

The degree-theorem application has the necessary structure. Conservation provides bounded nonnegative classes and the steady-state balance argument excludes boundary equilibria in positive-total classes. The chosen four conservation pivots agree with the four replaced ODE rows, so the rank-six determinant orientation is consistent. The source theorem's dissipativity, boundary, uniqueness and opposite-sign multiplicity conditions were checked against [Conradi et al., Theorem 1](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005751). The manuscript correctly uses the contrapositive to obtain a nonpositive determinant, rather than claiming a negative determinant over every multistationary parameter.

The Schur-complement argument is valid: the two layer blocks of D each have negative determinant, giving a positive product. The general-flux factor follows directly because the layer contribution k_binding*x_previous*k_catalytic*(k_unbinding+k_catalytic) becomes tau*(rho+tau)*(sigma+tau)*m_y*m_v*m_u. The product over layers cancels exactly the displayed denominator of the reduced determinant. Thus the arbitrary-flux statement does not rely on extrapolating from the public unit-flux test.

The negative-set decomposition is justified by strictly positive A0, A1, A3 and the factored A13. The base parameterizations and successive positive slack coordinates prove path connectedness of each component. The zero-critical ray is particularly important: increasing m3 preserves the coefficient values, gives a strictly negative derivative, and leaves all coordinates positive. The physical projection allows rates and totals to vary and therefore supplies the claimed attachment, including initially degenerate multistationary points. There is no unjustified inference that all zero-critical parameters are multistationary.

The exact witness supplies two positive distinct states at identical rates and totals, both negative-critical, with opposite separating signs. Nonsingular reduced Jacobians support local branches for all sixteen physical parameters by the implicit function theorem; positivity and strict signs persist on a common open neighborhood. Overlap of continuous component images then suffices for the global path argument, without a continuous equilibrium lift through the overlap. I found no gap in this chain.

## Replay and certificate semantics

Ran `PYTHON_ENV/bin/python -I verify.py` from the frozen candidate. It exited 0 with PASS: both implementations in ordinary and optimized modes; identical regenerated certificate bytes; all three semantic mutations rejected in both modes; complete manifest inventory and hashes matched. Execution uses temporary directories and left the target untouched.

The reduced checker recomputes rational witnesses, realizes the rates, verifies common totals, determinant negativity and opposite signs, and establishes the polynomial support, factorization and coefficient positivity. The reaction-level checker independently encodes the reaction changes and asserts conservation, exact ODE residuals, and the complete critical polynomial at unit flux. The two share SymPy, as disclosed. The checks support algebraic inputs rather than machine-certifying the topology. No private 135-check implementation was reviewed here, and no assurance credit depends on it.

## Optional improvements

1. `research/review_independent_checker.py` prints rank, witness totals, reduced/full determinants and separating signs without asserting their expected values. The reduced implementation and written proof cover the required claims, so this is not a blocker, but explicit exact comparisons would make the second implementation's success status more informative. A future reaction-level semantic mutation would further improve regression detection; the current three controls all mutate the reduced checker.
2. `research/OBLIGATIONS.md` cites absent `REVIEW.md` files and labels O2 (the scalar exploratory reduction) load-bearing, whereas the manuscript explicitly and correctly excludes it from the proof. Update the evidence links and dependency metadata for consistency. The complete manuscript supplies the missing mathematical evidence, so these stale metadata entries do not undermine the proof.

## Confidence and limitations

Confidence is high in the audited algebraic structure and the written path-connectedness mechanism, supported by successful exact replay. This assessment does not prove novelty or authenticate source priority, review every external theorem proof, validate physiological interpretation, establish stability, or certify fixed-rate/fixed-total slices. The PDF's identity was verified; this role did not perform a visual typography review. The acceptance recommendation applies to the stated candidate and its disclosed assurance limits, not to a claim of externally certified theorem status.
