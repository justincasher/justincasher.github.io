---
layout: Writing
indent: true
permalink: /Weil-Conjectures-Intro
feedformat: card
title: Motivating Schemes with the Weil Conjectures
---
<style>
    ol.custom {
        margin-top: -10px;
        margin-bottom: 20px;
        margin-left: -15px;
    }
    
    li {
        padding-top: 0px; 
        padding-bottom: 0px;
        margin-top: 0px;
        margin-bottom: 5px;
    }
}
</style>
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CD}{\mathcal{D}} \newcommand{\CI}{\mathcal{I}} \newcommand{\CO}{\mathcal{O}} \newcommand{\FF}{\mathbb{F}} \newcommand{\NN}{\mathbb{N}} \newcommand{\PP}{\mathbb{P}} \newcommand{\RR}{\mathbb{R}} \newcommand{\ZZ}{\mathbb{Z}} $$
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\Gr}{Gr} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Ob}{Ob} $$
<br>

**Abstract.** &nbsp; We introduce the Weil Conjectures, then give an overview of how Lefschetz theory and étale cohomology can be used to prove them. I would like to thank Nathan Lowry and Vladimir Shein for useful feedback.

## Table of Contents
1. [Weil's Conjectures](#1-weil-conjectures)
2. [Lefschetz Theory](#2-lefschetz-theory)
3. [Étale Cohomology](#3-etale-cohomology)
4. [References](#4-references)


## 1. Weil's Conjectures

&emsp; Write

$$
\zeta(z) = \sum_{n=1}^{\infty} \frac{1}{n^z}
$$

for the Riemann zeta function. It has the following properties:
<ol type="i" class="custom" style="list-style-position: outside">
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

&emsp; Let $$ V $$ be a nonsingular variety of dimension $$ n $$ over $$ k = \FF_q $$ a finite field with $$ q $$ elements. For instance, we could let $$ f \in \FF_q[X_1, \dots, X_n] $$ and set $$ V $$ to be the zero set of $$ f $$. Write $$ N_d $$ for the number of points (e.g. zeros) of $$ V $$ in a field extension of $$ \FF_q $$ of dimension $$ d $$.

&emsp; In 1948, Weil conjectured in REFERENCE the existence of a *zeta function* $$ Z(U) $$ attached to $$ V $$, which has the following properties. Weil arrived at these conjectures by first observing that they are true for curves, and that they are true for certain higher dimensional varieties, such as the Grassmanian.

**Weil Conjectures.** &nbsp; *With $$ V $$ and $$ Z $$ as above, the following are true*:
<ol type="i" class="custom" style="list-style-position: outside">
    <li><i>The logarithmic derivative of \( Z(U) \) is the generating function for our \( N_d \), meaning \[ \sum_{d=1}^{\infty} N_d U^{d-1} = \frac{d}{du} \ln(Z(U)). \] Furthermore, \( Z(U) \) is a rational polynomial.</i></li>
  
    <li><i>\( Z(U) \) satisfies the functional equation \[ Z((q^n U)^{-1}) = \pm q^{n \chi/2} U^{\chi} Z(U), \] where \( \chi \) is the Euler characteristic of our variety (see Remark 1.1).</i></li>
    
    <li><i>We have \[ Z(U) = \prod_{i=0}^{2n} \frac{P_1(U) P_3(U) \cdots P_{2n-1}(U)}{P_0(U) P_2(U) \cdots P_{2n}(U)}, \] where \( P_0(U) = 1-U \), \(P_{2n}(U) = 1-q^{2n} U\), and \[P_{i}(U) = \prod_{k=1}^{B_i} (1-\alpha_{i, k} U). \] We further guess that the \( \alpha_{i, k} \) are algebraic integers over \( \ZZ \) and satisfy \( \| \alpha_{i, k} \| = q^{i/2} \).</i></li>

    <li><i>The \( B_i \) are called the </i>Betti numbers<i> of our zeta function and satisfy the identity \( \chi = \sum_i (-1)^i B_i \).</i></li>
</ol>

**Remark 1.1.** 

**Example 1.2.** &nbsp; Let $$ \Gr(\FF_q^n, m) $$ be the Grassmanian, i.e. the number of $$ m $$-dimensional subspaces of $$ \FF_q^n $$. Set $$ k = \FF_p $$ and $$ V = \Gr(\FF_p^n, m) $$. Writing $$ q = p^d $$, by a well known formula,

$$
N_d = \frac{(q^n-q)(q^n-q) \cdots (q^n-q^{m-1})}{(q^m-1)(q^m-q) \cdots (q^m-q^{m-1})}.
$$

&emsp; We will verify the Weil Conjectures when $$ n = 2 $$ and $$ m = 1 $$, meaning we are reduced to computing the zeta function for 1-dimensional projectice space $$ \PP_{\FF_p}^1 $$. Solving for $$ Z(U) $$ in (i),

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

&emsp; We observe $$ B_0 = 1 $$, $$ B_1 = 0 $$, and $$ B_2 = 1 $$. This implies $$ \chi = 1 - 0 + 1 = 2 $$, which agrees with the geometric picture of moving a circle slightly off of itself and observing it has two points of intersection, and hence (iii). 

&emsp; Finally, we verify (ii) by computing 

$$
\begin{aligned}
Z((q^n U)^{-1}) & = \frac{1}{(1-(qU)^{-1})(1-q(qU)^{-1})} \\
& = qU^2 \frac{1}{(qU-1)(U-1)}
= qU^2 Z(U).
\end{aligned}
$$ 

We conclude that the Weil Conjectures hold in this case.


## 2. Lefschetz Theory

&emsp; Fix an algebraic closure $$ \overline{\FF}_p $$ of $$ \FF_p $$. In order to check whether an element $$ a \in \overline{\FF}_p $$ belongs to a finite subfield with $$ q = p^n $$ elements, we consider whether it is a fixed point of the Frobenious automorphism $$ F(x) = x^p $$ applied $$ n $$ times. This is an old idea: Fermat's Little Theorem asserts that $$ a^{p-1} \equiv 1 $$ modulo $$ p $$ since $$ \FF_p^{\times} $$ has $$ p - 1 $$ elements. The general case follows by considering $$ \FF_q $$ as the splitting field of $$ x^{p^n} - x $$. 

&emsp; To apply this idea to varieties we 

Thus, we have reduced counting our $$ N_d $$ to counting the number of fixed points of $$ F^{q^d}(x) = x^{q^d} $$.

In manifold theory, algebraic topology had been used to count fixed points.

**Brouwer Fixed Point Theorem.**

Lefschetz theory


## 3. Étale Cohomology




## 4. References

1. Alexander Grothendieck, *Sur quelques points d’algèbre homologique, I*, Tohoku Mathematical Journal **9** (1957), no. 2, 119–221.
2. Saunders Mac Lane, *Categories for the working mathematician*, Springer, 1978.
3. Archana S. Morye, *Note on the Serre-Swan theorem*, Mathematische Nachrichten **286** (2013), no. 2-3, 272–278.
4. Jean-Pierre Serre, *Vector bundles and projective modules*, Annals of Mathematics **61** (1955), no. 2, 197–278.
5. Richard Swan, *Vector bundles and projective modules*, Transactions of the American Mathematical Society **105** (1962), no. 2, 264–277.
