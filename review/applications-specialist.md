# Internal applications and cross-disciplinary assessment

Decision: **Accept**, within the scope of an unrefereed mathematical candidate preprint. No required revision from this review role.

## Frozen target and scope

Reviewed the manuscript source and accessible rendering, README, and CLAIMS.json in `frozen-extract/candidate`. Verified archive SHA-256 `ad360a172bb4287faa493d898df98cdb6b4a31ddadc1b56bc95125e8f9110bcf` and PDF SHA-256 `f5264f711401f870d8a6aecbf312b4371b2c8c5e609470bbc92b73d8b40445dd` against the supplied frozen identity. No other reviewer reports were read and no target file was edited.

This is an internal model-based applications review, not external specialist refereeing, experimental validation, a full proof audit, or a fresh literature review. Confidence is high that the manuscript states the relevant interpretive limitations consistently; confidence in the universal theorem itself is conditional on the mathematical and source audits undertaken separately.

## Semantic bridge and practical implications

The bridge from auxiliary coordinates to reaction rates and conserved totals is explicit: Section 3.1, source lines 154–162, constructs positive reaction rates from steady-state fluxes and projects to all twelve rates and four totals. This makes “physical parameter” a precise mathematical coordinate distinction. It does not make these parameters experimentally feasible. Sections 4–6 distinguish connected physical images from disconnected equilibrium lifts. In particular, source line 237 explicitly permits path concatenation without following one chosen equilibrium lift. This is a valuable guard against reading the result as continuous tracking of an individual biochemical state.

The introduction and Theorem 1.1 (source lines 34–43) specify distinct positive equilibria in a common compatibility class and the full rates-and-totals space. The abstract, Section 7 (line 306), README, and machine-readable exclusions consistently avoid identifying multistationarity with bistability. The mathematical result therefore supports a statement about connectedness of the model's permissible multistationary parameter choices; it does not establish switching, hysteresis, memory, stable response branches, or a dynamical route between states.

The overlap proof (source lines 280–287) supports qualitative persistence of two distinct negative-critical branches on some open neighborhood. It supplies no quantitative uncertainty radius, experimentally relevant perturbation tolerance, global robustness, or measure of how prevalent overlap is. The manuscript does not claim those stronger conclusions.

The global path can vary kinetic constants and totals together (lines 294–306). Accordingly, it supplies no route available to an intervention that changes only an enzyme total, keeps rate constants fixed, stays in a measured parameter box, or obeys additional physiological relationships. Section 7 expressly excludes fixed-rate/fixed-total slice connectivity, higher-layer extrapolation, and physiological plausibility. These exclusions are appropriate and present early enough through the abstract and introduction as well as in the scope section.

Appendix C's interpretation of the two sign factors (lines 408–423) is algebraically meaningful and described as a necessary condition rather than a sufficient mechanistic test. The scalar search is separated from the topological proof. No clinical, therapeutic, organism-level, or experimental claim needs substantive qualification because none is advanced.

## Required findings

None within this role's scope. The central potential misuses—stability, parameter slices, equilibrium-branch tracking, and physiological realism—are already expressly limited. Acceptance here does not resolve independent mathematical correctness or novelty requirements.

## Optional findings

1. **Explain the time interpretation for applied readers.** Location: Section 7, source line 306, and Section 4, line 237. One optional sentence could say: “The parameter paths are not trajectories of the mass-action ODE and do not constitute an intervention protocol.” Existing definitions and branch-lift warning already establish this distinction, so this is explanatory polish rather than a publication blocker.

2. **State the witness unit convention.** Location: Section 5, equations (5.1)–(5.4), and Appendix B. The rational constants are usable as formal positive model data, but no concentration/time units or scaling convention accompany them. An optional statement that they are numerical values in a fixed arbitrary consistent unit system would make reuse by computational biology readers clearer. This does not undermine the topology or license interpreting the concentrations as physiological measurements.

3. **Keep open-overlap language qualitative in any landing page.** Location: Proposition 5.1 and its proof, lines 280–287. If publication copy uses “robust,” qualify it as local persistence under sufficiently small mathematical parameter perturbations; neither a perturbation bound nor physiological robustness has been established. The current manuscript's wording is already appropriately narrower.

## Limitations

No ODE stability analysis, continuation experiment, physiological calibration, numerical tolerance estimate, or independent reaction-kinetics validation was performed for this assessment. No new external factual claims or bibliographic conclusions are offered. The recommendation applies to the frozen bytes identified above and to the applications framing, not to any later promotional wording or revised artifact.
