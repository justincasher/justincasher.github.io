---
layout: Post
indent: true
permalink: /Euler-Characteristic-is-an-Index
feedformat: card
title: The Euler Characteristic is the Index of an Elliptic Operator
---

<br>
## Table of Contents
1. [Atiyah-Singer Index Theorem](##Atiyah-Singer-Index-Theorem)
2. [The de Rham Complex](##The-de-Rham-Complex)
3. [Main Proof](##Main-Proof)

## 1. Atiyah-Singer Index Theorem

&emsp; Write $$ M $$ for a closed oriented Riemannian manifold of dimension $$ n $$. Let $$ E_1, E_2 $$ be complex vector bundles over $$ M $$ of rank $$ r_1, r_2 $$, respectively. A map of sections

$$ 
    D \colon \Gamma(E_1) \to \Gamma(E_2)
$$

which can locally be written as a sum of partial derivatives 

$$
    D \phi(x) = \sum_{\|\alpha\| \leq M} f^{\alpha}(x) (\partial_\alpha \phi)(x),
    \quad \text{where} \quad 
    \partial_\alpha = \frac{\partial^{\|\alpha\|}}{\partial^{\alpha_1} \cdots \partial^{\alpha_n}}
$$

is called a *differential operator*. Here, $$ \alpha = (\alpha_1, ..., \alpha_n) $$ is a vector in $$ \mathbb{Z}^n $$ with $$ \|\alpha\| = \sum \alpha_i $$, $$ U \subseteq M $$ is an open subset where $$ E_0, E_1 $$ are trivial, and $$ f^\alpha \in C^{\infty}(U, \text{Hom}(\mathbb{C}^{r_1}, \mathbb{C}^{r_2})) $$

&emsp; For a particular type of differential operator, called *elliptic*, the Atiyah-Singer Index Theorem relates the index 

$$
    \text{Ind}(D) = \dim \ker D - \dim \text{coker} D
$$

to characteristic classes:

$$
    \text{Ind}(D)
    = \int_M \text{Ch}(D) \wedge \text{td}(M). 
$$

&emsp; The following Theorems are corollaries of the Atiyah-Singer Index Theorem:

- Chern-Gauss-Bonnet Theorem;
- Hirzebruch–Riemann–Roch Theorem;
- Hirzebruch Signature Theorem.

We focus on the first, which states that the Euler characteristic of $$ M $$ equals the Euler class of the tangent bundle $$ e(TM) $$ integrated over $$ M $$:

$$
    \chi(M) = \int_M e(TM)
$$

In particular, we will show that we can express the Euler characteristic as the index of a certain Dirac operator.


## 2. The de Rham Complex

&emsp; Write $$ \Omega^k(M) = \Gamma(\bigwedge^k T^{\ast}M) $$ for the (real) vector space of differential $$ k $$-forms of $$ M $$. In what follows, we omit $$ M $$ simply writing $$ \Omega^k $$. We further set $$ \Omega^{\ast} = \bigoplus_k \Omega^k $$ to be the associated graded vector space. It has a decomposition into components with $$ k $$ even or odd:

$$
    \Omega^{\ast} = \Omega^{\text{ev}} \oplus \Omega^{\text{od}}.
$$

&emsp; Recall that there is a natural map $$ d \colon \Omega^k \to \Omega^{k+1} $$ such that $$ d \circ d = 0 $$ called the *differentail*. We see that the image of $$ d $$ is a subobject of its kernel, and we define 

$$
    H_{\text{dR}}^k(M) = \frac{\ker d \colon \Omega^k \to \Omega^{k+1}}{\text{im} d \colon \Omega^{k-1} \to \Omega^k}
$$

to be the *$$ i $$th de Rham cohomology group of $$ M $$*.

&emsp; We can dually define the *codifferential* $$ \delta \colon \Omega^{k} \to \Omega^{k-1} $$ using the *Hodge star operator* $$ \star \colon \Omega^{k} \to \Omega^{n-k} $$. We will not explicitely define the later, but the idea is that there is a natural isomorphism $$ \bigwedge^k T^{\ast}M \to \bigwedge^{n-k} T^{\ast}M $$ since the vector spaces are of the same dimension. This map pulls back to the Hodge star operator, which is used to define the codifferential on $$ \Omega^k $$ by $$ \delta = (-1)^k \star^{-1} d \star $$. 

&emsp; Finally, we define the Euler characteristic of $$ M $$ as the alternating sum 

$$
    \chi(M) = \sum_{k=0}^n (-1)^k \dim H_{\text{dR}}^k(M).
$$

It is a topological invariant of our manifold.


## 3. Main Proof

We call 

**Hodge Isomorphism** Let $$ M $$ be a closed oriented Riemannian manifold. Then there exists an isomorphism $$ \mathcal{H}^k(M) \cong H_{\text{dR}}^k(M) $$.