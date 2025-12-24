---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /weil-conjectures-intro
title: Motivating schemes with the Weil conjectures
date: "August 2023"
abstract: "We introduce the Weil Conjectures, then give an overview of how Lefschetz theory and étale cohomology can be used to prove them. I would like to thank Nathan Lowry and Vladimir Shein for useful feedback."
toc:
  - title: "Weil's conjectures"
    anchor: "1-weil-conjectures"
  - title: "Lefschetz theory"
    anchor: "2-lefschetz-theory"
  - title: "Étale cohomology"
    anchor: "3-étale-cohomology"
  - title: "References"
    anchor: "4-references"
---

<div style="display: none;">
$$
\newcommand{\cC}{\mathcal{C}}
\newcommand{\CD}{\mathcal{D}}
\newcommand{\CI}{\mathcal{I}}
\newcommand{\CO}{\mathcal{O}}
\newcommand{\FF}{\mathbb{F}}
\newcommand{\NN}{\mathbb{N}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\QQ}{\mathbb{Q}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\DeclareMathOperator{\colim}{colim}
\DeclareMathOperator{\Gr}{Gr}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Id}{Id}
\DeclareMathOperator{\Ob}{Ob}
$$
</div>

## 1. Weil's conjectures

&emsp; Write

$$
\zeta(z) = \sum_{n=1}^{\infty} \frac{1}{n^z}
$$

for the Riemann zeta function. It has the following properties:
<ol type="i" style="list-style-position: outside">
    <li>The logarithmic derivative is \( \frac{d}{dz} \ln(\zeta(z)) = \sum_{n=1}^{\infty} \Lambda(n) n^{-z} \), where \( \Lambda(n) \) is the Von Mangoldt function which equals \( \ln p \) when \( n = p^q \) for some \( p \) and \( 0 \) elsewise.</li>
  
    <li>It satisfies the functional equation 
    
    \[ 
    \zeta(z) = 2^{z} \pi^{z-1} \sin(\pi z/2) \Gamma(1-z) \zeta(1-z).
    \]

    </li>
  
    <li>It has an Euler product expansion 
    
    \[
    \zeta(z) = \prod_{p \text{ prime}} \frac{1}{1-p^{-z}}.
    \]
    
    </li>
</ol>

&emsp; Let $$ V $$ be a nonsingular projective variety of dimension $$ n $$ over $$ k = \FF_q $$ a finite field with $$ q $$ elements. For instance, we could let $$ f \in \FF_q[X_1, \dots, X_n] $$ and set $$ V $$ to be the zero set of $$ f $$. Write $$ N_d $$ for the number of points (e.g. zeros) of $$ V $$ in a field extension of $$ \FF_q $$ of degree $$ d $$.

&emsp; In 1948, Weil conjectured in [\[5\]](#4-references) the existence of a *zeta function* $$ Z(U) $$ attached to $$ V $$, which has the following properties. Weil arrived at these conjectures by first observing that they are true for curves, and that they are true for certain higher dimensional varieties, such as the Grassmanian. These are now known to be true.

**Weil Conjectures.** &nbsp; *With $$ V $$ and $$ Z $$ as above, the following are true*:
<ol type="i" style="list-style-position: outside">
    <li><i>The logarithmic derivative of \( Z(U) \) is the generating function for our \( N_d \), meaning \[ \sum_{d=1}^{\infty} N_d U^{d-1} = \frac{d}{du} \ln(Z(U)). \] Furthermore, \( Z(U) \) is a rational polynomial.</i></li>
  
    <li><i>\( Z(U) \) satisfies the functional equation \[ Z((q^n U)^{-1}) = \pm q^{n \chi/2} U^{\chi} Z(U), \] where \( \chi \) is the Euler characteristic of our variety (see Remark 1.1).</i></li>
    
    <li><i>We have \[ Z(U) = \prod_{i=0}^{2n} \frac{P_1(U) P_3(U) \cdots P_{2n-1}(U)}{P_0(U) P_2(U) \cdots P_{2n}(U)}, \] where \( P_0(U) = 1-U \), \(P_{2n}(U) = 1-q^{2n} U\), and \[P_{i}(U) = \prod_{k=1}^{B_i} (1-\alpha_{i, k} U). \] We further guess that the \( \alpha_{i, k} \) are algebraic integers over \( \ZZ \) and satisfy \( \| \alpha_{i, k} \| = q^{i/2} \).</i></li>

    <li><i>The \( B_i \) are called the </i>Betti numbers<i> of our zeta function and satisfy the identity \( \chi = \sum_i (-1)^i B_i \).</i></li>
</ol>

**Remark 1.1.** &nbsp; We are defining the Euler characteristic $$ \chi $$ as the *self-intersection number* of the diagonal $$ I(\Delta, \Delta) $$ in $$ V \times V $$. The idea is that the number of fixed points of a function can be defined as $$ I(\Delta, \text{graph}(f)) $$, because $$ (x, x) = (x, f(x)) $$ implies $$ f(x) = x $$. The Euler characteristic is the number of fixed points of the identity map; but this quantity is infinite, so we move our variety slightly off of itself when computing the self-intersection number. 

**Remark 1.2.** &nbsp; Write $$ M $$ for a smooth compact manifold. Then we can again define $$ \chi(M) = I(\Delta, \Delta) $$. This quantity is related to the *Betti numbers* $$ b_i = \dim_{\QQ} H_i(M, \QQ) $$  by Corollary 2.1.

**Example 1.3.** &nbsp; Let $$ \Gr(\FF_q^n, m) $$ be the Grassmanian, i.e. the number of $$ m $$-dimensional subspaces of $$ \FF_q^n $$. Set $$ k = \FF_p $$ and $$ V = \Gr(\FF_p^n, m) $$. Writing $$ q = p^d $$, by a well known formula,

$$
N_d = \frac{(q^n-q)(q^n-q) \cdots (q^n-q^{m-1})}{(q^m-1)(q^m-q) \cdots (q^m-q^{m-1})}.
$$

&emsp; We will verify the Weil Conjectures when $$ n = 2 $$ and $$ m = 1 $$, meaning we are reduced to computing the zeta function for 1-dimensional projective space $$ \PP_{\FF_p}^1 $$. Solving for $$ Z(U) $$ in (i),

$$
\begin{aligned}
Z(U) & = \exp \left( \sum_{d=1}^{\infty} (p^d+1) \frac{U^d}{d} \right) \\
& = \exp \left( \sum_{d=1}^{\infty} \frac{(pU)^d}{d} + \sum_{d=1}^{\infty} \frac{U^d}{d} \right) \\
& = \exp ( -\ln(1-qU) - \ln(1-U) ) \\
& = \frac{1}{(1-U)(1-qU)},
\end{aligned} 
$$

since

$$
\sum_{n=1}^{\infty} \frac{x^n}{n} = -\ln(1-x)
$$

for $$ x $$ near $$ 0 $$. 

&emsp; (iii) We observe $$ B_0 = 1 $$, $$ B_1 = 0 $$, and $$ B_2 = 1 $$. This implies $$ \chi = 1 - 0 + 1 = 2 $$. This agrees with the Euler characteristic of the Riemann sphere in the complex case.

&emsp; Finally, we verify (ii) by computing 

$$
\begin{aligned}
Z((q^n U)^{-1}) & = \frac{1}{(1-(qU)^{-1})(1-q(qU)^{-1})} \\
& = qU^2 \frac{1}{(qU-1)(U-1)}
= qU^2 Z(U).
\end{aligned}
$$ 

We conclude that the Weil Conjectures hold for $$ \PP_{\FF_p}^1 $$.


## 2. Lefschetz theory

&emsp; Fix an algebraic closure $$ \overline{\FF}_p $$ of $$ \FF_p $$. In order to check whether an element $$ a \in \overline{\FF}_p $$ belongs to a finite subfield with $$ q = p^n $$ elements, we consider whether it is a fixed point of the Frobenious automorphism $$ F(x) = x^p $$ applied $$ n $$ times. This is an old idea: Fermat's little theorem asserts that $$ a^{p-1} \equiv 1 $$ modulo $$ p $$ since $$ \FF_p^{\times} $$ has $$ p - 1 $$ elements. The general case follows by considering $$ \FF_q $$ as the splitting field of $$ x^q - x $$. 

&emsp; Hence, with our previous setup, we can compute $$ N_d $$ by counting the number of fixed points of $$ F^{q^d}(x) = x^{q^d} $$, where the Frobenious acts on an algebraic closure of our variety in a suitable manner. In particular, we have reduced the Weil Conjectures to a fixed point problem. 

&emsp; It was well known when Weil published his conjectures that algebraic topology can be used to prove the existence of and count fixed points. The following is a simple example:

**Brouwer fixed point theorem.** &nbsp; *Let $$ f \colon D^2 \to D^2 $$ be a continuous map from the disk to itself. Then $$ f $$ has a fixed point.*

*Proof.* Suppose $$ f $$ has no fixed points. Let $$ h \colon D^2 \to S^1 $$ be the map which sends $$ x $$ to the point on $$ S^1 $$ which intersects the ray starting at $$ f(x) $$ and passing through $$ x $$. Since $$ f $$ has no fixed points this map is well-defined and continuous. Writing $$ \iota \colon S^1 \to D^2 $$ for the inclusion, we see $$ h \circ \iota = \text{Id}_{S_1} $$. But $$ \pi_1(S^1) = \ZZ $$ and $$ \pi_1(D^1) = 0 $$ implies $$ \pi_1(h \circ \iota) $$ factors through zero, contradicting that its image is $$ \ZZ $$. $$ \blacksquare $$

&emsp; Our main use of algebraic topology will be abstracting Lefschetz Theory, as it will allow us to write our Zeta function using trace formulas. Let $$ M $$ be a compact oriented manifold and $$ F \colon M \to M $$ smooth. We call the oriented intersection 

$$ 
L(f) = I(\Delta, \text{graph}(f)) 
$$ 

the *global Lefschetz number* of $$ f $$. Recall that the oriented intersection is the sum over each intersection $$ x $$ as $$ +1 $$ if $$ f $$ preserves the orientation at $$ x $$ and $$ - 1 $$ elsewise. The global Lefschetz number is related to the singular homology groups by the Lefschetz-Hopf theorem.

**Lefschetz-Hopf theorem.** &nbsp; *We have the equality*

$$
L(f) = \sum_{i=0}^{\infty} (-1)^i \text{Tr}(f_* \mid H_i(M, \QQ)).
$$

**Corollary 2.1.** &nbsp; *Let $$ b_i = \dim_{\QQ} H_i(M, \QQ) $$ be the $$ i $$th Betti number of our manifold. Then $$\chi(M) = \sum_{i} (-1) b_i $$.*

*Proof.* As in Remark 1.2 let $$ f $$ be the identity. Then $$ f_* $$ is the identity, and hence 

$$ 
\text{Tr}(f_* \mid H_i(M, \QQ)) = \dim_{\QQ} H_i(M, \QQ).
$$

Our result follows. $$ \blacksquare $$

&emsp; Now let $$ x $$ be a fixed point of $$ f $$. We define the local Lefschetz number $$ L_x(f) $$ as $$ +1 $$ if $$ f $$ preserves the orientation at $$ x $$ and $$ - 1 $$ elsewise. Clearly 

$$
\sum_{f(x) = x} L_x(f) = L(f),
$$ 

and combining this with the Lefschetz-Hopf Theorem we arrive at the following.

**Corollary 2.2.** &nbsp; *We have the equality*

$$
\sum_{f(x)=x} L_x(f) = \sum_{i=0}^{\infty} (-1)^i \text{Tr}(f_* \mid H_i(M, \QQ)).
$$



## 3. Étale cohomology

&emsp; In order to develop a Lefschetz theory for algebraic varieties we need a suitable notion of cohomology. This was one of the main purposes for writing the EGA and SGA. In the 1950s there was a developing theory of sheaf cohomology, which can be shown to be equal to singular cohomology in the case of manifolds. Thus, like how a manifold is an object which locally looks like $$ \RR^n $$, Grothendieck defined a scheme as an object which locally looks like a commutative ring using sheaves. 

&emsp; Although simply using the derived global section functor of the structure sheaf did not include the needed information. Hence, a functor called *étale cohomology* based on covering spaces of schemes was developed. It is a rule which assigns to each étale map $$ f \colon Y \to X $$ an object in a category and satisfies gluing. The following results can be found in the SGA 4 1/2.

&emsp; Let $$ X_0 $$ be a scheme of finite type over $$ \FF_q $$ (i.e. locally $$ X_0 $$ looks like a finite $$ \FF_q $$ algebra), and $$ X = X \times_{\FF_q} \text{Spec} \overline{\FF}_q $$ its extension to the algebraic closure. Write $$ A_0 $$ for a constructible $$ \QQ_{\ell} $$-sheaf on $$ X_0 $$ (a type of formal sheaf on the étale site), and $$ A $$ for its extension to $$ X $$. Finally let $$ F $$ be the Frobenious on $$ X $$, which locally acts by sending $$ x \to x^q $$ as an endomorphism of an $$ \FF_q$$-algebra. This Frobenious action (locally) permutes the prime ideals of our $$ \FF_q $$-algebras, and hence we can consider its fixed points.

&emsp; An analogue of Corollary 2.2 is the following:

**Theorem 3.1.** &nbsp; *For every $$ n $$,*

$$
\sum_{F^n(x) = x} \text{Tr}(F^{n*}, A_x) = \sum_{i=0}^{\infty} \text{Tr}(F^{n*}, H_c^i(X, A))
$$

&emsp; Likewise we can prove the following product expansion of our zeta function using trace formulas. Set 

$$
\zeta_X(z) = \prod_{x \in C_X} (1-\text{Card}(k(x))^{-s})^{-1}, 
$$

where $$ C_X $$ is the set of closed points of $$ X $$ (i.e. points which are locally maximal ideals). If we set $$ q_x = \text{Card}(k(x)) $$, $$ \text{deg}(x) = [k(x), \FF_q] $$, and $$ U = q^{-z} $$, we can write

$$
\zeta_X(z) = Z_X(q^{-z}),
$$

where 

$$
Z_X(U) = \prod_{x \in C_X} (1-U^{\text{deg}(x)})^{-1}.
$$

Again $$ Z_X(U) $$ converges for $$ U $$ small.

**Theorem 3.2.** &nbsp; *We have* 

$$
Z_X(U) = \prod_{i=0}^{\infty} \det(1-F^* U, H_c^i(X, \QQ_{\ell}))^{(-1)^{i+1}}.
$$

*Since our cohomology groups vanish for $$ i > 2n $$, our zeta function is indeed a rational polynomial.*


## 4. References

1. Pierre Deligne. "La conjecture de Weil: I". *Publications Mathématiques de l'IHÉS*, Volume 43 (1974), pp. 273-307. [Link](http://www.numdam.org/item/PMIHES_1974__43__273_0/)
2. Pierre Deligne, *Sga 4 1/2: Cohomologie étale*, Springer, 1977.
3. Victor Guillemin and Alan Pollack, *Differential topology*, Prentice-Hall, 1974.
4. Robin Hartshorne, *Algebraic geometry*, Springer, 1977.
5. André Weil. "Numbers of solutions of equations in finite fields". *Bulletin of the American Mathematical Society*, 55(5) pp. 497-508, May 1949.
