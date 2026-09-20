# Prior-art and citation verification

Search date: 2026-09-20. Outcome: **BOUNDED UNCERTAINTY about priority**. The mathematical conclusion is supported by the attached proof; no historical-first claim is made. No author enquiry or publication occurred.

## Frozen claim and fingerprints

The target is path connectivity of the full sixteen-dimensional positive rates-and-totals multistationarity set for the specific ten-species twelve-reaction two-layer cascade with shared phosphatase. A fixed-rate projection, a different shared-kinase network, Michaelis–Menten approximation, or a stability result is not identical.

The normalization is recorded in target.yaml. Formula fingerprints are the bilinear-in-(m1,m3) critical polynomial and its factor (m6-m4), the rational four-by-four conservation Jacobian, the scalar reduction z=h*x1, and overlapping images of two negative-critical components. Exact witnesses and determinant values are in certificate.json. There is no natural enumerative sequence, generating function, or finite matrix family whose OEIS fingerprint would identify this continuous parameter-region theorem; none was invented. The finite witness matrix is a verification device, not the target object.

Aliases searched include Goldbeter–Koshland loops, enzyme-sharing, shared phosphatase, cascaded phosphorylation, five steady states, critical determinant, multistationarity, overlapping physical images, and connected parameter regions. The general mathematical mechanism is a continuous image of an incidence set with overlapping components plus boundary attachment. Stochastic, representation-theoretic, and orthogonal-polynomial analogues are not identities for this target.

## Search log and inspected sources

The following query families were run through web search in this session:

- `Kaihnsa Wang cascades Goldbeter Koshland connected components multistationarity region`
- `"2607.25456" "conjecture"` and `"2607.25456" connectedness resolution`
- `"Enzyme-sharing as a cause" multistationarity cascade phosphatase`
- `Telek Feliu topological descriptors parameter region multistationarity theorem 4 closure 2023`
- `"Goldbeter" "five" "steady states" cascade`
- `"Goldbeter" "phosphatase" "five steady"`
- `"Goldbeter" "connected" "shared phosphatase"`
- `"multistationarity" "overlap" "components" cascade`
- `"multistationarity" "images" "intersect" connectivity`
- `"m6" "m4" "A13" "multistationarity"`
- `"enzyme sharing" "connected" "parameter" region`

Primary documents examined:

1. **Kaihnsa and Wang, arXiv:2607.25456v1 (28 July 2026).** The live arXiv record lists only v1. PDF pages 14–16 contain the exact target network, inverse-concentration parametrization, two-component auxiliary calculation, upper bound, and Conjecture 4.3. The conjecture is disconnection in the full physical space, not a fixed-rate slice. This is the exact originating statement, and the attached conclusion contradicts it. The original paper is credited for the auxiliary decomposition; it does not support our connectedness conclusion.
2. **Telek and Feliu, arXiv:2209.13936v2 (18 March 2023), published PLOS Computational Biology 19(3), e1010970, DOI 10.1371/journal.pcbi.1010970.** Theorem 2.1(A),(B) gives the degree criteria; Lemma 6.4 selects a nonpositive-critical steady state over every multistationary physical parameter. The proof's degenerate attachment follows the same general strategy as Lemma 6.5, with an explicit curve available here. These are existing methods, not claimed new. Its Section 3.3 studies a twelve-species fifteen-reaction cascade with shared kinase, and a two-layer MAPK cascade with a dual-phosphorylation layer. Neither is the present ten-species twelve-reaction shared-phosphatase network. Thus its cascade-connectivity statements are not an immediate object-identity collision.
3. **Giaroli, Bihan and Dickenstein, Regions of multistationarity in cascades of Goldbeter–Koshland loops**, J. Math. Biol. 78, 1115–1145 (2019), DOI 10.1007/s00285-018-1304-0, arXiv:1807.08400. Abstract and metadata establish explicit multistationarity regions for the same family, and Kaihnsa–Wang credits its parametrization. This session did not audit the entire paper for implicit connectivity consequences.
4. **Feliu and Wiuf, Enzyme-sharing as a cause of multi-stationarity in signalling systems**, J. R. Soc. Interface 9, 1224–1232 (2012), DOI 10.1098/rsif.2011.0662, arXiv:1101.5799. The primary text describes a cascade with non-layer-specific phosphatase (motif k) and scalar steady-state response functions. It is a relevant antecedent for scalar reductions. Its supplement was not exhaustively audited for an implicit version of the overlap argument.

Searches also surfaced double-modification cascades with five equilibria, but these use a different reaction network and sometimes Michaelis–Menten kinetics. Numerical multiplicity in those models cannot be substituted for the present topological theorem.

## Citation verification matrix

| Source claim used | Existence/metadata | Direct support | Scope/context |
|---|---|---|---|
| KW poses disconnection for the exact full physical space | Live arXiv v1 verified | Conjecture 4.3, PDF p.16 | Fair; not cited as proof of connectedness |
| KW auxiliary negative set has two components | PDF pp.14–15 inspected | Eq.37 and Theorem 4.2 | Locally re-derived; correct m3-bound sign typo |
| Degree theorem selects <=0 in a multiple-equilibrium fibre | TF v2 verified | Theorem 2.1 and Lemma 6.4, pp.6,23–24 | Exact hypotheses checked in PROOF.md |
| TF already proves other cascade connectivity results | TF Section 3.3 inspected | Yes, different networks | Not conflated with the target |
| Exact opposite-sign fibre overlap exists | Local computation | certificate.json plus independent ODE checker | Not attributed to any cited paper |

The KW PDF's displayed bound on m3 has a sign error: the correct denominator is -A13*m1-A3, as obtained directly from g<0. This repair is documented, not silently used as a verbatim source claim. Theorem numbering differs between TF arXiv and published versions; PROOF.md cites the inspected arXiv v2 numbers.

## Outcome and limits

No earlier statement of this exact connectedness result was found in the bounded search described above. This is negative search evidence, not proof of novelty. Citation indexes may lag the July 2026 preprint; supplements, non-English literature, private correspondence, and all possible algebraic reparametrizations were not exhaustively searched. The originating paper's open-problem language alone is not evidence that the target remains unresolved elsewhere.

| Contribution unit | Outcome | Permitted wording |
|---|---|---|
| Connectedness statement and complete proof | Bounded uncertainty on priority | A complete locally checked proof contradicting Conjecture 4.3 of v1 |
| General topology method | Existing method | Builds on the degree/closure framework of Telek–Feliu |
| Two auxiliary components | Existing result, locally checked | Kaihnsa–Wang decomposition with corrected epigraph display |
| Exact physical overlap certificate | Locally established | Exact witness reproduced by two encodings |
| Verification artifacts | Locally produced | Reproducible rational and symbolic checks, not formal verification |

No 'first proof', 'proved novel', or externally accepted resolution language is justified. A publication-oriented priority audit would require deeper full-text/supplement review and a new search after any further simplification.

## Source integrity

Downloaded source PDF SHA-256 values:

- Kaihnsa–Wang v1: `2137aa8679618467d13936282fa5f0ff208454ee0da0b9b3ca90d6a6def3e5f1`.
- Telek–Feliu v2: `8b434aacf9c5f5ab2b5f87880480abd12dd2db45a7f676011797152f01fea033`.

Sources: [KW v1](https://arxiv.org/abs/2607.25456v1), [TF v2](https://arxiv.org/abs/2209.13936v2), [Giaroli et al.](https://arxiv.org/abs/1807.08400), [Feliu–Wiuf](https://arxiv.org/abs/1101.5799).
