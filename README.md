# Path connectedness of multistationarity in a two-layer phosphorylation cascade with a shared phosphatase

Anonymous · 0.1.0-candidate · 20 September 2026

**Unrefereed candidate.** The written theorem states that the full positive 16-dimensional reaction-rate and conserved-total multistationarity region is path connected. The exact overlap certificate and a zero-to-negative ray address Conjecture 4.3 of Kaihnsa and Wang, arXiv:2607.25456v1. No stability, fixed-rate slice, physiological, or historical-first claim is made.

Read [the paper](paper/connectedness.pdf), [source](paper/connectedness.tex), [proof exposition](research/PROOF.md), [assurance](ASSURANCE.md), and [review response](review/RESPONSE.md).

## Replay

Python 3.10+; create an isolated environment, install requirements, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -I verify.py
```

Create the environment outside this sealed directory when verifying the complete manifest. Replay checks both normal and optimized modes and three semantic negative controls. It executes in temporary copies. The algebraic checks do not prove the universal topology theorem; that argument is in the paper and uses an external degree theorem.

## Contents and rights

Original text/data are CC0-1.0; original Python code is MIT. Third-party papers and supplied review code are not redistributed. Their private audit hashes and the response are recorded for provenance, without claiming external review. See PROVENANCE.md and LICENSES.md.

Exact-version DOI: https://doi.org/10.5281/zenodo.22858244
Repository: https://github.com/ipitchford/gk-shared-phosphatase-connectedness
