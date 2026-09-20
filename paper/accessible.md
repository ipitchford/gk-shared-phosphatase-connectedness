<div class="center">

Unrefereed candidate, version 0.1.0-candidate\
<https://doi.org/10.5281/zenodo.22858244>

</div>

**Keywords:** mass-action kinetics; phosphorylation cascade;
multistationarity; path connectedness; critical determinant; exact
certificate.

# Introduction and main result

A multistationarity region consists of the parameter choices for which a
reaction network admits at least two distinct positive equilibria in the
same stoichiometric compatibility class. Its topology describes whether
such parameter choices can be joined continuously while retaining
multistationarity. Here both reaction rate constants and conserved total
concentrations may vary along the path.

Kaihnsa and Wang  study cascades of Goldbeter–Koshland loops. For the
two-layer cascade with a shared phosphatase, they prove that the full
multistationarity region has at most two connected components and
conjecture that it is disconnected. The negative set of their critical
polynomial in auxiliary coordinates has exactly two components. This
does not decide the physical topology, because the map from auxiliary
coordinates to physical parameters need not preserve their separation.

Earlier work of Feliu and Wiuf  studies the same shared-phosphatase
cascade as motif (k), establishing multistationarity through
steady-state elimination. Multistationarity of the architecture and
scalar elimination are therefore prior results. The contribution here
concerns the topology of the region in the full space of rates and
conserved totals.

We resolve this question by constructing a physical parameter fibre that
meets both negative components. The proof uses the degree criterion of
Conradi, Feliu, Mincheva and Wiuf , in the connectivity framework of
Telek and Feliu , but does not require the negative auxiliary set itself
to be connected.

<div id="thm:main" class="theorem">

**Theorem 1**. *For the mass-action network
<a href="#eq:network" data-reference-type="eqref"
data-reference="eq:network">[eq:network]</a>, let
$`\Omega\subset\mathbb{R}_{>0}^{12}\times\mathbb{R}_{>0}^4`$ be the set
of reaction rates and conserved totals admitting at least two distinct
positive steady states. Then $`\Omega`$ is nonempty and path connected.
In particular, it has exactly one connected component.*

</div>

The theorem includes parameter choices with degenerate steady states. It
contradicts Conjecture 4.3 of ; Theorem 4.2 of that paper, which gives
an upper bound of two, remains valid. We also show that the images of
the two negative components overlap on an open subset of the physical
parameter space.

The exact witness is given in
Section <a href="#sec:witness" data-reference-type="ref"
data-reference="sec:witness">5</a>. The general topological argument
appears in Section <a href="#sec:graph" data-reference-type="ref"
data-reference="sec:graph">4</a>, and the treatment of degenerate
parameters in Section <a href="#sec:global" data-reference-type="ref"
data-reference="sec:global">6</a>. The proof is self-contained apart
from the stated degree criterion. Its determinant identities can be
checked directly from the displayed matrices and are reproduced by the
accompanying exact programs.

# The network, conservation laws, and degree criterion

For $`i=1,2`$, consider
``` math
\begin{equation}
\label{eq:network}
\begin{aligned}
Y_i+X_{i-1}&\underset{\kappa_{6i-4}}{\stackrel{\kappa_{6i-5}}{\rightleftarrows}}V_i
 \xrightarrow{\kappa_{6i-3}}X_i+X_{i-1},\\
X_i+H_1&\underset{\kappa_{6i-1}}{\stackrel{\kappa_{6i-2}}{\rightleftarrows}}U_i
 \xrightarrow{\kappa_{6i}}Y_i+H_1 .
\end{aligned}
\end{equation}
```
This is network (34) of . The species order, used throughout, is
``` math
z=(h,x_0,x_1,x_2,y_1,y_2,u_1,u_2,v_1,v_2).
```
All twelve rate constants are strictly positive. The four conserved
totals are
``` math
\begin{equation}
\label{eq:totals}
\begin{aligned}
H&=h+u_1+u_2,& E&=x_0+v_1,\\
S&=x_1+y_1+u_1+v_1+v_2,& T&=x_2+y_2+u_2+v_2.
\end{aligned}
\end{equation}
```
Write $`Wz=(H,E,S,T)`$ for this linear conservation map. The four rows
of $`W`$ are in reduced row-echelon form, with pivots in the first four
species. The stoichiometric matrix $`N`$ has rank six. For example, the
six columns corresponding to reactions $`1,3,4,7,9,10`$ are linearly
independent: the $`Y_1,U_1,X_0,Y_2,U_2,X_2`$ rows successively force
their coefficients to vanish. Since $`WN=0`$ and $`W`$ has rank four,
the rank is exactly six.

Let $`f_\kappa`$ be the ten-dimensional mass-action vector field and
define
``` math
\begin{equation}
\label{eq:psi}
\psi_\kappa(z)=\bigl(Wz,(f_\kappa)_{y_1},(f_\kappa)_{y_2},
(f_\kappa)_{u_1},(f_\kappa)_{u_2},(f_\kappa)_{v_1},(f_\kappa)_{v_2}\bigr).
\end{equation}
```
The omitted four ODEs are determined by conservation. Because the rank
is six, the critical determinant in the degree criterion is
``` math
q_\kappa(z)=(-1)^6\det D\psi_\kappa(z)=\det D\psi_\kappa(z).
```

We use two consequences of the degree criterion originally established
in  and restated in ; they are Theorem 2.1(A),(B) in arXiv:2209.13936v2.
For a dissipative network without relevant boundary steady states:

1.  if $`q_\kappa(z)>0`$ at every positive steady state with totals
    $`d`$, then $`(\kappa,d)`$ is not multistationary;

2.  if $`q_\kappa(z)<0`$ at some positive steady state with totals
    $`d`$, then $`(\kappa,d)`$ is multistationary.

In particular, contraposing (i), every $`(\kappa,d)\in\Omega`$ has a
positive steady state with $`q_\kappa\leq0`$. This is also the content
used in , numbered Lemma 6.4 in the cited arXiv version. The non-strict
inequality is essential at degenerate parameters.

<div id="lem:boundary" class="lemma">

**Lemma 2**. *Network <a href="#eq:network" data-reference-type="eqref"
data-reference="eq:network">[eq:network]</a> is conservative and has no
boundary steady state in a compatibility class with $`H,E,S,T>0`$. The
degree criterion applies.*

</div>

<div class="proof">

*Proof.* The sum of the four expressions
in <a href="#eq:totals" data-reference-type="eqref"
data-reference="eq:totals">[eq:totals]</a> has a strictly positive
coefficient for every species. Thus each nonnegative compatibility class
is bounded, and the network is conservative, hence dissipative.

At any nonnegative steady state, the complex equations and catalytic
balances give
``` math
\begin{equation}
\label{eq:balances}
\begin{aligned}
\kappa_{6i-5}x_{i-1}y_i&=(\kappa_{6i-4}+\kappa_{6i-3})v_i,\\
\kappa_{6i-2}hx_i&=(\kappa_{6i-1}+\kappa_{6i})u_i,\\
\kappa_{6i-3}v_i&=\kappa_{6i}u_i.
\end{aligned}
\end{equation}
```
The last equality follows by adding the $`Y_i`$ and $`V_i`$ steady-state
equations. If $`h=0`$, then $`u_1=u_2=0`$, contradicting $`H>0`$. If
$`x_0=0`$, then $`v_1=0`$, contradicting $`E>0`$. If $`x_1=0`$, the
balances imply $`u_1=v_1=y_1=v_2=0`$, contradicting $`S>0`$. If
$`x_2=0`$, they imply $`u_2=v_2=y_2=0`$, contradicting $`T>0`$. Thus
$`h,x_0,x_1,x_2`$ are positive;
<a href="#eq:balances" data-reference-type="eqref"
data-reference="eq:balances">[eq:balances]</a> then makes all remaining
species positive. ◻

</div>

# Steady-state coordinates and the critical sign

Define the positive effective constants, as in , by
``` math
\begin{equation}
\label{eq:effective}
\begin{aligned}
a_i&=\frac{\kappa_{6i}\kappa_{6i-2}(\kappa_{6i-4}+\kappa_{6i-3})}
 {\kappa_{6i-3}\kappa_{6i-5}(\kappa_{6i-1}+\kappa_{6i})},\\
b_i&=\frac{\kappa_{6i-2}}{\kappa_{6i-1}+\kappa_{6i}},&
c_i&=\frac{\kappa_{6i}\kappa_{6i-2}}{\kappa_{6i-3}(\kappa_{6i-1}+\kappa_{6i})}.
\end{aligned}
\end{equation}
```
The positive steady states are parametrized by
$`w=(h,x_0,x_1,x_2)\in\mathbb{R}_{>0}^4`$ through
``` math
\begin{equation}
\label{eq:steady}
y_i=a_i\frac{hx_i}{x_{i-1}},\qquad u_i=b_ihx_i,\qquad v_i=c_ihx_i.
\end{equation}
```
Substitution in the balances proves both existence and completeness of
this parametrization. Let $`\varphi_\kappa(w)`$ denote the full state.
Its conservation map is
``` math
\begin{equation}
\label{eq:F}
F_\kappa(w)=W\varphi_\kappa(w)=
\begin{pmatrix}
h+b_1hx_1+b_2hx_2\\
x_0+c_1hx_1\\
x_1+a_1hx_1/x_0+(b_1+c_1)hx_1+c_2hx_2\\
x_2+a_2hx_2/x_1+(b_2+c_2)hx_2
\end{pmatrix}.
\end{equation}
```

<div id="lem:sign" class="lemma">

**Lemma 3**. *At every positive steady state,
``` math
\mathop{\mathrm{sgn}}q_\kappa(\varphi_\kappa(w))=\mathop{\mathrm{sgn}}\det DF_\kappa(w).
```*

</div>

<div class="proof">

*Proof.* Split $`D\psi_\kappa`$ into blocks
$`\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)`$ according
to the free and remaining species. If $`M`$ is the derivative of the six
remaining steady-state coordinates, then differentiating their
steady-state equations gives $`C+DM=0`$, while $`DF_\kappa=A+BM`$. Hence
``` math
\det D\psi_\kappa=\det DF_\kappa\det D.
```
After simultaneously grouping rows and columns by layer, the $`i`$th
block of $`D`$ is
``` math
\begin{pmatrix}
-\kappa_{6i-5}x_{i-1}&\kappa_{6i}&\kappa_{6i-4}\\
0&-(\kappa_{6i-1}+\kappa_{6i})&0\\
\kappa_{6i-5}x_{i-1}&0&-(\kappa_{6i-4}+\kappa_{6i-3})
\end{pmatrix}.
```
Its determinant is
$`-\kappa_{6i-5}x_{i-1}\kappa_{6i-3}(\kappa_{6i-1}+\kappa_{6i})`$. There
are two layers, so $`\det D>0`$. ◻

</div>

## Positive incidence coordinates

Put $`m_j=1/z_j`$. Independently in layer $`i`$, choose positive
reverse-binding fluxes $`\rho_i,\sigma_i`$ and common catalytic flux
$`\tau_i`$. The six reaction fluxes of that layer are
``` math
\begin{equation}
\label{eq:flux}
(\rho_i+\tau_i,\rho_i,\tau_i,\sigma_i+\tau_i,\sigma_i,\tau_i).
\end{equation}
```
For
$`\lambda=(\rho_1,\sigma_1,\tau_1,\rho_2,\sigma_2,\tau_2)\in\mathbb{R}_{>0}^6`$,
divide each flux by its positive reactant monomial at $`z=1/m`$ to
obtain $`\kappa(m,\lambda)`$. These fluxes lie in $`\ker N`$, so this
defines a positive steady-state incidence point. Conversely, every such
point has this form
by <a href="#eq:balances" data-reference-type="eqref"
data-reference="eq:balances">[eq:balances]</a>. Thus the parametrization
covers all positive rates and their positive steady states. The physical
projection is the continuous map
``` math
\begin{equation}
\label{eq:projection}
\Pi(m,\lambda)=\bigl(\kappa(m,\lambda),W(1/m)\bigr)\in\mathbb{R}_{>0}^{16}.
\end{equation}
```
Our ordering of the six flux variables is layerwise; it need not agree
with the order of extreme-ray columns in .

## The critical polynomial

At an incidence point, the effective constants satisfy
``` math
\begin{equation}
\label{eq:inveff}
\begin{aligned}
a_1&=\frac{m_1m_3}{m_5m_2},& a_2&=\frac{m_1m_4}{m_6m_3},\\
b_1&=\frac{m_1m_3}{m_7},& b_2&=\frac{m_1m_4}{m_8},&
c_1&=\frac{m_1m_3}{m_9},& c_2&=\frac{m_1m_4}{m_{10}}.
\end{aligned}
\end{equation}
```
Differentiate <a href="#eq:F" data-reference-type="eqref"
data-reference="eq:F">[eq:F]</a> with the effective constants held
fixed, and only then
substitute <a href="#eq:inveff" data-reference-type="eqref"
data-reference="eq:inveff">[eq:inveff]</a>. The determinant is
``` math
\begin{equation}
\label{eq:g}
\det DF_\kappa=\frac{g(m)}{m_{10}m_5m_6m_7m_8m_9},\qquad
 g=A_{13}m_1m_3+A_1m_1+A_3m_3+A_0.
\end{equation}
```
All four coefficients are independent of $`m_1,m_3`$, and
``` math
\begin{equation}
\label{eq:A13}
A_{13}=(m_6-m_4)\bigl(m_{10}m_2m_7+m_{10}m_5m_7
 +m_{10}m_5m_9+m_{10}m_7m_9-m_5m_8m_9\bigr).
\end{equation}
```
The coefficients $`A_0,A_1,A_3`$ have respectively $`4,5,17`$ monomials,
all with positive coefficients.
Appendix <a href="#app:coeff" data-reference-type="ref"
data-reference="app:coeff">8</a> gives them in full. This recovers the
polynomial in .

For clarity, the full arbitrary-flux identity with the
ordering <a href="#eq:flux" data-reference-type="eqref"
data-reference="eq:flux">[eq:flux]</a> is
``` math
\begin{equation}
\label{eq:fullflux}
q_{\kappa(m,\lambda)}(1/m)
=\prod_{i=1}^2\tau_i(\rho_i+\tau_i)(\sigma_i+\tau_i)\,g(m).
\end{equation}
```
Indeed, the factor $`\det D`$ in
Lemma <a href="#lem:sign" data-reference-type="ref"
data-reference="lem:sign">3</a> becomes the denominator
in <a href="#eq:g" data-reference-type="eqref"
data-reference="eq:g">[eq:g]</a> times the product
in <a href="#eq:fullflux" data-reference-type="eqref"
data-reference="eq:fullflux">[eq:fullflux]</a>. Every factor is
positive. Thus $`g`$ determines the global critical sign, not just the
sign at the particular rates used below.

# Two auxiliary components and an overlap criterion

<div id="lem:components" class="lemma">

**Lemma 4**. *The set $`\{m\in\mathbb{R}_{>0}^{10}:g(m)<0\}`$ has
exactly two path-connected components, distinguished by the sign of
$`m_6-m_4`$. Every positive zero of $`g`$ can be joined immediately to
$`\{g<0\}`$ by increasing $`m_3`$ alone.*

</div>

<div class="proof">

*Proof.* Let
``` math
R=\frac{m_{10}(m_2m_7+m_5m_7+m_5m_9+m_7m_9)}{m_5m_9}>0.
```
Positivity of $`A_0,A_1,A_3`$ implies that $`g<0`$ requires
$`A_{13}<0`$. The latter base consists of
``` math
\begin{align*}
M_-&=\{m_6<m_4,\ m_8<R\},\\
M_+&=\{m_6>m_4,\ m_8>R\},
\end{align*}
```
with base variables $`m_2,m_4,m_5,m_6,m_7,m_8,m_9,m_{10}`$ positive.
Each is path connected. For $`M_-`$ use $`m_4=m_6+s`$, $`m_8=tR`$, with
$`s>0`$ and $`0<t<1`$; for $`M_+`$ use $`m_6=m_4+s`$, $`m_8=R+s_8`$,
with $`s,s_8>0`$. In each case the remaining coordinates vary
independently over positive intervals, giving an explicit homeomorphism
from a product of intervals.

Over either base, solving $`g<0`$ gives precisely
``` math
\begin{equation}
\label{eq:threshold}
m_1>\frac{A_3}{-A_{13}},\qquad
m_3>\frac{A_0+A_1m_1}{-A_{13}m_1-A_3}.
\end{equation}
```
Both successive inequalities can be parametrized by adding an
independent positive slack variable to their lower bounds. Their
denominators are positive on the preceding domains. They therefore give
one path-connected component over each base, denoted $`D_-`$ and
$`D_+`$. These components are nonempty, and a path between them would
cross $`m_6=m_4`$, where $`g>0`$.

If $`g(m)=0`$, the same positivity implies $`A_{13}<0`$ and
``` math
\begin{equation}
\label{eq:ray}
A_{13}m_1+A_3=-\frac{A_0+A_1m_1}{m_3}<0,\qquad
 g(m+te_3)=-\frac{t(A_0+A_1m_1)}{m_3}<0\quad(t>0).
\end{equation}
```
Here all coefficients on the right are evaluated at the starting point
and are unchanged along the ray. This proves the last assertion. ◻

</div>

<div class="remark">

*Remark 5* (The threshold denominator). The final display in the proof
of prints the denominator $`-A_3+A_{13}m_1`$. Direct solution of the
inequality gives $`-A_{13}m_1-A_3`$, as
in <a href="#eq:threshold" data-reference-type="eqref"
data-reference="eq:threshold">[eq:threshold]</a>. This sign correction
is separate from the connectedness result: the substantive additional
step is overlap of the physical images, followed by attachment of
degenerate parameters.

</div>

The following elementary observation organizes that step. It is an
overlap-graph formulation of the image-and-attachment argument, not a
claim of novelty for the abstract topology.

<div id="lem:graph" class="lemma">

**Lemma 6** (Overlap graph and attachment). *Let $`\Pi:X\to Y`$ be
continuous and let $`\Omega\subseteq Y`$. Suppose
$`C_1,\ldots,C_r\subseteq X`$ are nonempty path-connected sets with
$`\Pi(C_i)\subseteq\Omega`$. Form a graph on $`\{1,\ldots,r\}`$, with an
edge $`ij`$ whenever $`\Pi(C_i)\cap\Pi(C_j)\ne\varnothing`$. Assume this
graph is connected and every $`p\in\Omega`$ can be joined within
$`\Omega`$ to a point of $`\bigcup_i\Pi(C_i)`$. Then $`\Omega`$ is path
connected.*

</div>

<div class="proof">

*Proof.* Each image is path connected. Following a finite graph path and
concatenating paths through successive intersections shows that their
union is path connected. For any two points of $`\Omega`$, concatenate
their attaching paths with a path in this union. ◻

</div>

In this application $`X=\mathbb{R}_{>0}^{10}\times\mathbb{R}_{>0}^6`$
and $`C_\pm=D_\pm\times\mathbb{R}_{>0}^6`$. A physical path may be
concatenated at an overlap point without continuously following one
chosen equilibrium lift. The two equilibrium lifts themselves remain in
different auxiliary components.

# An exact physical overlap

Choose
``` math
\begin{equation}
\label{eq:constants}
\begin{aligned}
a_1&=\frac{20827163033}{10847244000},&
a_2&=\frac{401271957}{42422500},\\
b_1&=60,& b_2&=\frac{116}{1025},&
c_1&=26,& c_2&=\frac{28}{5}.
\end{aligned}
\end{equation}
```
For each layer these constants are realized by positive rates
``` math
\begin{equation}
\label{eq:ratechoice}
(\kappa_{6i-5},\ldots,\kappa_{6i})
=\left(\frac{2c_i}{a_i},1,1,2c_i,\frac{c_i}{b_i},\frac{c_i}{b_i}\right).
\end{equation}
```
Substitution into <a href="#eq:effective" data-reference-type="eqref"
data-reference="eq:effective">[eq:effective]</a> verifies the
realization exactly. Take the two free-coordinate points
``` math
\begin{equation}
\label{eq:points}
P=\left(\frac1{150},\frac{5693}{50000},\frac3{10},1340\right),\qquad
Q=\left(\frac6{25},\frac1{2000},\frac{53}{2000},19\right).
\end{equation}
```
The full positive states are obtained
from <a href="#eq:steady" data-reference-type="eqref"
data-reference="eq:steady">[eq:steady]</a>; all their entries and the
twelve rates are listed in
Appendix <a href="#app:witness" data-reference-type="ref"
data-reference="app:witness">9</a>. At the same rates, both give
precisely
``` math
\begin{equation}
\label{eq:commontotals}
(H,E,S,T)=\left(\frac{11661}{10250},\frac{8293}{50000},
\frac{45678099759}{903937000},\frac{727342892891}{434830625}\right).
\end{equation}
```
Direct differentiation of <a href="#eq:F" data-reference-type="eqref"
data-reference="eq:F">[eq:F]</a> gives
``` math
\begin{equation}
\label{eq:detvalues}
\begin{aligned}
\det DF_\kappa(P)&=-\frac{50294437400138543733503}{24284564239106250000}<0,\\
\det DF_\kappa(Q)&=-\frac{895903401800934682060509}{31400206507812500}<0.
\end{aligned}
\end{equation}
```
Finally,
``` math
\begin{equation}
\label{eq:gaps}
\begin{aligned}
(x_2-y_2)(P)&=\frac{11224290709}{10605625}>0,\\
(x_2-y_2)(Q)&=-\frac{3412151689}{2121125}<0.
\end{aligned}
\end{equation}
```
Since $`m_6-m_4=(x_2-y_2)/(x_2y_2)`$, the two states lie in opposite
negative components: $`P`$ lifts to $`C_+`$ and $`Q`$ to $`C_-`$. Their
physical projections agree exactly.

<div id="prop:overlap" class="proposition">

**Proposition 7**. *Writing $`B_\pm=\Pi(C_\pm)`$, one has
$`B_-\cap B_+\ne\varnothing`$. In fact,
``` math
\mathop{\mathrm{int}}_{\mathbb{R}^{16}}(B_-\cap B_+)\ne\varnothing.
```*

</div>

<div class="proof">

*Proof.* Equations <a href="#eq:constants" data-reference-type="eqref"
data-reference="eq:constants">[eq:constants]</a>–<a href="#eq:gaps" data-reference-type="eqref"
data-reference="eq:gaps">[eq:gaps]</a>,
Lemma <a href="#lem:sign" data-reference-type="ref"
data-reference="lem:sign">3</a>, and positivity of the rate realization
prove the first assertion. For the second, apply the implicit function
theorem to $`F_\kappa(w)-d=0`$ at each witness, taking all twelve rates
and all four totals as parameters. Both $`w`$-Jacobians are nonsingular
by <a href="#eq:detvalues" data-reference-type="eqref"
data-reference="eq:detvalues">[eq:detvalues]</a>. In a sufficiently
small common physical neighborhood the two branches remain positive,
distinct, negative-critical, and of opposite signs
in <a href="#eq:gaps" data-reference-type="eqref"
data-reference="eq:gaps">[eq:gaps]</a>. Each nearby parameter therefore
lies in both physical images. ◻

</div>

# Global path connectedness

<div class="proof">

*Proof of Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>.* By
Lemma <a href="#lem:components" data-reference-type="ref"
data-reference="lem:components">4</a>, $`C_-`$ and $`C_+`$ are path
connected. The degree criterion,
Lemma <a href="#lem:boundary" data-reference-type="ref"
data-reference="lem:boundary">2</a>,
and <a href="#eq:fullflux" data-reference-type="eqref"
data-reference="eq:fullflux">[eq:fullflux]</a> show that $`B_-`$ and
$`B_+`$ are subsets of $`\Omega`$.
Proposition <a href="#prop:overlap" data-reference-type="ref"
data-reference="prop:overlap">7</a> supplies the edge of their
two-vertex overlap graph.

Let $`p=(\kappa,d)\in\Omega`$. The contrapositive of the
positive-critical uniqueness criterion supplies a positive steady state
above $`p`$ with $`q_\kappa\leq0`$. Lift it to $`(m,\lambda)`$
using <a href="#eq:flux" data-reference-type="eqref"
data-reference="eq:flux">[eq:flux]</a>. Then $`g(m)\leq0`$. If
$`g(m)<0`$, the point $`p`$ already belongs to $`B_-\cup B_+`$. If
$`g(m)=0`$, consider
``` math
\gamma(t)=\Pi(m+te_3,\lambda),\qquad 0\leq t\leq1.
```
This is a continuous positive physical-parameter path with
$`\gamma(0)=p`$. Equation <a href="#eq:ray" data-reference-type="eqref"
data-reference="eq:ray">[eq:ray]</a> and the negative-critical
implication of the degree criterion give
$`\gamma(t)\in B_-\cup B_+\subseteq\Omega`$ for every $`t>0`$. Its
starting point is in $`\Omega`$ by choice, not merely because its
determinant vanishes. Thus the entire path lies in $`\Omega`$.

Every point of $`\Omega`$ attaches to the negative image.
Lemma <a href="#lem:graph" data-reference-type="ref"
data-reference="lem:graph">6</a> now proves path connectedness, and the
exact witness proves nonemptiness. ◻

</div>

The sign calculation controls every value of $`t`$ on the attaching
path. Paths inside either negative component can likewise be obtained by
linear interpolation in its positive interval and slack coordinates,
then applying the continuous parametrizations. Hence the argument needs
no numerical sampling to certify an entire path interval.

# Scope and reproducibility

The theorem concerns multiple distinct positive equilibria, not multiple
stable equilibria. It does not imply connectedness of every fixed-rate
or fixed-total slice, a result for more than two layers, or
physiological plausibility of the witness concentrations. A connecting
physical path may vary rates and totals simultaneously.

The candidate bundle includes the complete mathematical argument,
machine-readable rational data, and two producer-side algebraic
implementations. The reduced-map checker verifies the exact witness and
the complete polynomial
identity <a href="#eq:g" data-reference-type="eqref"
data-reference="eq:g">[eq:g]</a>. A separately encoded reaction-level
checker verifies the ten ODEs, conservation laws, augmented
determinants, and the critical polynomial at unit fluxes. Both use
SymPy. The supplied review additionally reported an arbitrary-flux
identity check using integer sparse polynomials and rational arithmetic;
its 135 checks were replayed locally in ordinary and optimized Python.
That supplied code is retained privately because redistribution terms
were not supplied. This report is supporting evidence, not authenticated
external specialist review. The public proof
of <a href="#eq:fullflux" data-reference-type="eqref"
data-reference="eq:fullflux">[eq:fullflux]</a> is given by the
Schur-complement calculation in
Section <a href="#sec:critical" data-reference-type="ref"
data-reference="sec:critical">3</a> together with
Appendix <a href="#app:coeff" data-reference-type="ref"
data-reference="app:coeff">8</a>. These checks do not constitute
proof-assistant certification of the topology or the external degree
theorem.

Numerical exploration located a candidate fibre, after which the two
relevant states were reconstructed rationally. Neither numerical search
nor a claim about the exact number of other equilibria in that fibre is
needed for this proof. The manuscript includes all coefficients and
witness entries needed to reconstruct its calculations without relying
on omitted review files.

#### Review status and tool disclosure.

This is an unrefereed candidate preprint. AI tools assisted the
derivation, code generation, checking, and preparation of the text.
Internal model-based assessments and a response to the supplied review
are documented in the bundle and are not represented as external
specialist refereeing. The proof uses an established degree theorem with
its hypotheses checked above. No historical-first claim is made; the
bounded literature search is recorded separately. The scholarly creator
is Anonymous; no affiliation is asserted.

#### Availability.

The accompanying archive contains the LaTeX source, PDF, exact checkers,
pinned dependency requirements, review-response records, and a SHA-256
manifest. Its verification script checks the manifest and runs both
algebraic implementations in temporary copies, in ordinary and optimized
modes, with semantic negative controls. Source references are linked;
third-party source snapshots and supplied audit files are not
redistributed. No experimental or personal data are used.

# Complete critical-polynomial coefficients

Besides $`A_{13}`$ in <a href="#eq:A13" data-reference-type="eqref"
data-reference="eq:A13">[eq:A13]</a>, the coefficients
in <a href="#eq:g" data-reference-type="eqref"
data-reference="eq:g">[eq:g]</a> are
``` math
\begin{align*}
A_0={}&m_5m_7m_9(m_{10}m_4m_6+m_{10}m_4m_8+m_{10}m_6m_8+m_4m_6m_8),\\
A_1={}&m_5m_9(m_{10}m_4m_6+m_{10}m_6m_7+m_{10}m_4m_8
+m_{10}m_6m_8+m_4m_6m_8),\\
A_3={}&m_{10}m_2m_4m_6m_7+m_{10}m_2m_4m_7m_8+m_{10}m_2m_6m_7m_8\\
&+m_{10}m_4m_5m_6m_7+m_{10}m_4m_5m_6m_9+m_{10}m_4m_5m_7m_8\\
&+m_{10}m_4m_5m_8m_9+m_{10}m_4m_6m_7m_9+m_{10}m_4m_7m_8m_9\\
&+m_{10}m_5m_6m_7m_8+m_{10}m_5m_6m_8m_9+m_{10}m_6m_7m_8m_9\\
&+m_2m_4m_6m_7m_8+m_4m_5m_6m_7m_8+m_4m_5m_6m_8m_9\\
&+m_4m_5m_7m_8m_9+m_4m_6m_7m_8m_9.
\end{align*}
```
In particular all three are strictly positive on the positive orthant.
To reconstruct <a href="#eq:g" data-reference-type="eqref"
data-reference="eq:g">[eq:g]</a> directly, let $`s_j=1/m_j`$.
Substitution in the differentiated
map <a href="#eq:F" data-reference-type="eqref"
data-reference="eq:F">[eq:F]</a> gives
``` math
J_m=\begin{pmatrix}
1+m_1(s_7+s_8)&0&m_3s_7&m_4s_8\\
m_1s_9&1&m_3s_9&0\\
m_1(s_5+s_7+s_9+s_{10})&-m_2s_5&1+m_3(s_5+s_7+s_9)&m_4s_{10}\\
m_1(s_6+s_8+s_{10})&0&-m_3s_6&1+m_4(s_6+s_8+s_{10})
\end{pmatrix}.
```
Expanding $`m_{10}m_5m_6m_7m_8m_9\det J_m`$ gives precisely the four
coefficients above and in <a href="#eq:A13" data-reference-type="eqref"
data-reference="eq:A13">[eq:A13]</a>.

# Full rational witness

The rate vector, in reaction order, is
``` math
\kappa=\left(
\frac{564056688000}{20827163033},1,1,52,\frac{13}{30},\frac{13}{30},
\frac{475132000}{401271957},1,1,\frac{56}{5},\frac{1435}{29},\frac{1435}{29}
\right).
```
The complete species vectors are given in
Table <a href="#tab:witness" data-reference-type="ref"
data-reference="tab:witness">[tab:witness]</a>. Their common totals
are <a href="#eq:commontotals" data-reference-type="eqref"
data-reference="eq:commontotals">[eq:commontotals]</a>. Substitution
into the twelve reaction fluxes and the ten mass-action equations gives
zero residuals exactly at both points. The full augmented determinants,
as a separate check on the reduced calculation, are
``` math
\begin{align*}
\det D\psi_\kappa(\varphi_\kappa(P))
&=-\frac{55262991073036297575834372455984}{284019536251510549041796875},\\
\det D\psi_\kappa(\varphi_\kappa(Q))
&=-\frac{54689394267653500504064463302664}{52596210416946397970703125}.
\end{align*}
```

<div class="center">

<div class="minipage">

| Species |  $`\varphi_\kappa(P)`$  |     $`\varphi_\kappa(Q)`$     |
|:-------:|:-----------------------:|:-----------------------------:|
|  $`h`$  |        $`1/150`$        |           $`6/25`$            |
| $`x_0`$ |     $`5693/50000`$      |          $`1/2000`$           |
| $`x_1`$ |        $`3/10`$         |          $`53/2000`$          |
| $`x_2`$ |        $`1340`$         |            $`19`$             |
| $`y_1`$ |  $`3658381/108472440`$  | $`1103839640749/45196850000`$ |
| $`y_2`$ | $`2987246791/10605625`$ |    $`3452453064/2121125`$     |
| $`u_1`$ |        $`3/25`$         |         $`477/1250`$          |
| $`u_2`$ |     $`15544/15375`$     |        $`13224/25625`$        |
| $`v_1`$ |       $`13/250`$        |        $`2067/12500`$         |
| $`v_2`$ |       $`3752/75`$       |         $`3192/125`$          |

<span id="tab:witness" label="tab:witness"></span> Table : Two exact
positive steady states at identical rates and totals.

</div>

</div>

# A scalar reduction for exploring physical fibres

The following reduction was used to locate the overlap and is not
required for the topological proof. Fix the effective constants and
$`H,E,S>0`$. Put $`z=hx_1`$, $`r=c_2/b_2`$, $`D=S-rH`$, and
``` math
f(z)=\frac{a_1z}{E-c_1z}+(b_1+c_1-rb_1)z.
```
For $`0<z<E/c_1`$, the conservation laws give
``` math
rh^2+(D-f(z))h-z=0,
\qquad h(z)=\frac{f(z)-D+\sqrt{(D-f(z))^2+4rz}}{2r}.
```
Reconstruct
``` math
x_0=E-c_1z,\qquad x_1=z/h(z),\qquad
x_2=\frac{H-h(z)-b_1z}{b_2h(z)}.
```
The positivity condition $`H>h(z)+b_1z`$ defines exactly one interval
$`(0,z_{\max})`$. Indeed,
``` math
(h+b_1z)'=
\frac{1/h+a_1E/(E-c_1z)^2+b_1+c_1+b_1z/h^2}{z/h^2+r}>0.
```
At the left endpoint $`h+b_1z`$ tends to $`\max(0,H-S/r)<H`$, while it
tends to infinity as $`z\uparrow E/c_1`$. The positive steady states
with a further fixed total $`T`$ therefore correspond bijectively to
solutions in $`(0,z_{\max})`$ of
``` math
\frac{H-h(z)-b_1z}{b_2h(z)}
\left(1+\frac{a_2h(z)^2}{z}+(b_2+c_2)h(z)\right)=T.
```
Every denominator is positive on this interval. This reduction searches
actual physical fibres while preserving the distinction between multiple
equilibria and stability.

The separating factors have a direct interpretation in these
coordinates. First,
``` math
x_2-y_2=\frac{x_2(x_1-a_2h)}{x_1},
```
so $`m_6-m_4`$ has the sign of $`x_1-a_2h`$. If $`B`$ denotes the second
factor of $`A_{13}`$ in <a href="#eq:A13" data-reference-type="eqref"
data-reference="eq:A13">[eq:A13]</a>, then
``` math
\frac{B}{m_{10}m_5m_7m_9}
 =\frac{y_1v_1}{x_0}+v_1+u_1+y_1-\frac{v_2u_1}{u_2}
 =z f'(z).
```
Thus a negative determinant necessarily satisfies $`(x_1-a_2h)f'(z)<0`$.
This is only a necessary sign condition: the positive terms in $`g`$
must also be overcome. The scalar reduction therefore guides a search
for a physical fibre with negative-critical states of both sign types,
while the exact determinant evaluations certify that the displayed
witness succeeds.

<div class="thebibliography">

9 C. Conradi, E. Feliu, M. Mincheva and C. Wiuf, *Identifying parameter
regions for multistationarity*, PLOS Computational Biology **13**(10)
(2017), e1005751.
[doi:10.1371/journal.pcbi.1005751](https://doi.org/10.1371/journal.pcbi.1005751).

E. Feliu and C. Wiuf, *Enzyme-sharing as a cause of multi-stationarity
in signalling systems*, Journal of the Royal Society Interface **9**
(2012), 1224–1232.
[doi:10.1098/rsif.2011.0662](https://doi.org/10.1098/rsif.2011.0662).

N. Kaihnsa and K. Wang, *Disconnectivity in Multistationarity Regions of
Cascade of Goldbeter–Koshland Loops*, arXiv:2607.25456v1, 28 July 2026.
<https://arxiv.org/abs/2607.25456v1>.
[doi:10.48550/arXiv.2607.25456](https://doi.org/10.48550/arXiv.2607.25456).

M. L. Telek and E. Feliu, *Topological descriptors of the parameter
region of multistationarity: Deciding upon connectivity*, PLOS
Computational Biology **19**(3) (2023), e1010970.
[doi:10.1371/journal.pcbi.1010970](https://doi.org/10.1371/journal.pcbi.1010970).
Preprint version used for theorem-number correspondence:
<https://arxiv.org/abs/2209.13936v2>, 18 March 2023.

</div>
