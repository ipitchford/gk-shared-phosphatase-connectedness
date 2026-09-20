# Proof obligations

Established means justified by the linked proof and checks, not formal or external certification.

```json
[
  {
    "id": "O1",
    "statement": "Verify the exact source network and the degree-criterion hypotheses; establish the auxiliary decomposition directly.",
    "status": "established",
    "load_bearing": true,
    "depends_on": [],
    "evidence": [
      "PROOF.md Sections 2-3 and Appendix",
      "PRIOR_ART.md",
      "../review/RESPONSE.md"
    ],
    "next_action": "None required for this proof; reopen if a concrete mathematical objection is identified."
  },
  {
    "id": "O2",
    "statement": "Derive an exact scalar steady-state reduction with positivity domain and reconstruct all equilibria.",
    "status": "established",
    "load_bearing": false,
    "depends_on": [],
    "evidence": [
      "REDUCTION.md"
    ],
    "next_action": "None required for this proof; reopen if a concrete mathematical objection is identified."
  },
  {
    "id": "O3",
    "statement": "Determine whether the two negative-critical auxiliary components can have intersecting physical images or connecting degenerate fibres.",
    "status": "established",
    "load_bearing": true,
    "depends_on": [],
    "evidence": [
      "PROOF.md Sections 1 and 4",
      "certificate.json",
      "check_certificate.py",
      "review_independent_checker.py",
      "../review/RESPONSE.md"
    ],
    "next_action": "None required for this proof; reopen if a concrete mathematical objection is identified."
  },
  {
    "id": "O4",
    "statement": "Prove the final connected-component count for the entire original multistationarity region.",
    "status": "established",
    "load_bearing": true,
    "depends_on": [
      "O1",
      "O3"
    ],
    "evidence": [
      "PROOF.md Sections 2-3 and Appendix",
      "../review/RESPONSE.md"
    ],
    "next_action": "None required for this proof; reopen if a concrete mathematical objection is identified."
  }
]
```
