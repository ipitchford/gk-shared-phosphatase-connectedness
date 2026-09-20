# Internal Editor-in-Chief assessment

Recommendation: **Minor Revision** for release as an **unrefereed candidate preprint**. No substantive editorial blocker was identified in the manuscript's stated contribution or assurance framing. One small provenance correction is required below. This is an internal model assessment, not external peer review or a declaration of mathematical correctness.

## Frozen scope and limits

Reviewed the complete LaTeX manuscript, CLAIMS.json, README.md, STATUS.md, ASSURANCE.md, research/PRIOR_ART.md, and CITATION_AUDIT.md in the frozen candidate. No other editorial role reports were read. The target was not modified. Verified archive SHA-256 `ad360a172bb4287faa493d898df98cdb6b4a31ddadc1b56bc95125e8f9110bcf` and PDF SHA-256 `f5264f711401f870d8a6aecbf312b4371b2c8c5e609470bbc92b73d8b40445dd` against the supplied identities.

Confidence is high concerning manuscript scope, internal editorial consistency, and assurance wording; moderate concerning significance conditional on the mathematics and cited conjecture being correct. I did not independently browse the cited literature, replay checkers, visually inspect the PDF, or perform a line-by-line specialist proof audit. Citation-audit and replay statements are evaluated as disclosed producer evidence, not independently confirmed by this role.

## Significance and fit

The narrowly specified full sixteen-dimensional rates-and-totals connectivity result is a suitable mathematical candidate contribution. Sections 4–6 distinguish separation of auxiliary equilibrium components from separation of their physical images, exhibit an exact shared fibre, and address degenerate parameters explicitly. This is materially more than numerical multistationarity or a correction of a displayed denominator. The open-overlap consequence adds robustness to the witness. The paper credits the earlier auxiliary decomposition and does not claim novelty for the elementary overlap-graph lemma.

The abstract and Introduction correctly distinguish contradiction of Conjecture 4.3 of a named version from invalidation of the upper-bound theorem. Section 7 and CLAIMS.json explicitly exclude stability, fixed-rate/fixed-total slice connectivity, physiological realism, higher-layer generalization, priority, and formal verification. These boundaries make the candidate suitable for Evidence Press's transparent research-artifact format, subject to the separate technical and release gates.

The ordinary mathematical phrase “We prove” is acceptable in a candidate manuscript containing a written proof; the conspicuous unrefereed status and explicit dependence on the external degree theorem prevent it from implying authenticated external acceptance. Neither the abstract nor release metadata should be promoted to a historically first or externally validated resolution.

## Required finding

**EIC-1 — Minor provenance correction.** `research/PRIOR_ART.md:9` says “The normalization is recorded in target.yaml,” but the frozen candidate inventory contains no target.yaml. Replace this with a reference to the included network definition and target scope (for example, manuscript Section 2 and CLAIMS.json), or explicitly identify target.yaml as a private development artifact that is not included. The public provenance record should not direct readers to a nonexistent bundled file. This does not affect the displayed mathematical argument.

## Optional improvements

1. `paper/connectedness.tex:313` says internal model assessments are documented “in the bundle.” The currently frozen inventory contains a response record but no separate internal role reports. At final packaging, ensure the statement is literally true or qualify the location of the assessments. This is a release-assembly check rather than a demand to alter this frozen mathematical source now.
2. `research/PRIOR_ART.md:62` recommends deeper full-text/supplement review for a publication-oriented priority audit. Keeping bounded uncertainty and avoiding first-proof language is adequate for this candidate release. A later journal submission or novelty-centered announcement would benefit from completing that deeper audit, particularly the Giaroli–Bihan–Dickenstein paper and Feliu–Wiuf supplement.

## Release recommendation

After the small provenance correction, editorial acceptance as an unrefereed candidate is appropriate, conditional on the separately assessed mathematical, reproducibility, licensing, and public-readback requirements. This recommendation does not certify those requirements or authorize presenting internal model review as unaffiliated specialist refereeing.
