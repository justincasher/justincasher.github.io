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
2. [Main Proof](##Main-Proof)

## 1. Atiyah-Singer Index Theorem

Write $$ M $$ for a closed oriented smooth manifold of dimension $$ n $$. Let $$ E_1, E_2 $$ be complex vector bundles over $$ M $$ of rank $$ r_1, r_2 $$, respectively. A map of sections

$$ 
    D \colon \Gamma(E_0) \to \Gamma(E_1)
$$

which can locally be written as a sum of partial derivatives 

$$
    D \phi(x) = \sum_{|\alpha| \leq M} f^{\alpha}(x) (\partial_{\alpha} \phi)(x),
    \quad \text{where} \quad 
    \partial_{\alpha} = \frac{\partial^{|\alpha|}}{\partial^{\alpha_1} \cdots \partial^{\alpha_n}}
$$

is called a *differential operator*. Here, $$ \alpha = (\alpha_1, \dots, \alpha_n) $$ as a vector in $$ \ZZ^n $$ with $|\alpha| = \sum \alpha_i$, $$ U \subseteq M $$ is an arbitrary open subset where $E_0, E_1$ are trivial, and $$ f^\alpha \in C^{\infty}(U, \Hom(\CC^{r_1}, \CC^{r_2})) $$

For a particular type of differential operator, called *elliptic* The Atiyah-Singer Index Theorem relates the index 

$$
    \text{Ind}(D) = \dim \ker D - \dim \coker D
$$

to characteristic classes, which we can write as differential forms:

$$
    \ind(D)
    = \int_M \text{Ch}(D) \wedge \text{td}(M). 
$$

This generalizes many earlier results 


## 2. Main Proof

