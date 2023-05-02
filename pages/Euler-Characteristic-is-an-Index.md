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

&emsp; Write $$ M $$ for a closed oriented smooth manifold of dimension $$ n $$. Let $$ E_1, E_2 $$ be complex vector bundles over $$ M $$ of rank $$ r_1, r_2 $$, respectively. A map of sections

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

to characteristic classes, which we can write as differential forms:

$$
    \text{Ind}(D)
    = \int_M \text{Ch}(D) \wedge \text{td}(M). 
$$

&emsp; The following Theorems are corollaries of the Atiyah-Singer Index Theorem:

- Chern-Gauss-Bonnet theorem;
- Hirzebruch–Riemann–Roch theorem;
- Hirzebruch signature theorem.

We focus on the first, which states that the Euler characteristic of $$ M $$ equals the Euler class of the tangent bundle $$ e(TM) $$ integrated over $$ M $$:

$$
    \chi(M) = \int_M e(TM)
$$

In particular, we will show that we can express the Euler characteristic as the index of a certain Dirac operator.


## 2. The de Rham Complex



## 3. Main Proof

