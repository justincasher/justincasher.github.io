---
layout: Writing
indent: true
permalink: /Categorical-Products-and-Coproducts
feedformat: card
title: Categorical Products and Coproducts
---
$$ \usepackage[all, cmtip]{xy} \newcommand{\cC}{\mathcal{C}} \newcommand{\CD}{\mathcal{D}} \DeclareMathOperator{\Ob}{Ob} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} $$
<br>
## Table of Contents
1. [Limits and Colimits](#1-limits-and-colimits)
2. [Applications to Sets](#2-applications-to-sets)
3. [K-Theory](#3-k-theory)
4. [References](#4-references)

## 1. Limits and Colimits

&emsp; A *category* $$ \cC $$ is a class of objects $$ \Ob(\cC) $$ and a class of morphisms $$ \Hom(\cC) $$ equipped with a composition law. In particular, for any $$ A, B, C \in \Ob(\cC), $$ we have the following: 

- An associative composition operator 

$$ 
    \circ \colon \Hom(B, C) \times \Hom(A, B) \to \Hom(A, C).
$$

- Local identities $$ \Id_A \colon A \to A $$, such that for any $$ f \colon A \to B $$, we have $$ f \circ \Id_A = f $$ and $$ \Id_B \circ f = f $$.

&emsp; We define maps between categories $$ F \colon \cC \to \CD $$ on the level of pairs 

$$ 
    F \colon (\Ob(\cC), \Hom(\cC)) \to (\Ob(\CD), \Hom(\CD)).
$$

We call $$ F $$ a *fucntor* if it preserves the composition operator $$ F(f \circ g) = F(f) \circ F(g) $$ and local identities $$ F(\Id_A) = \Id_{F(A)} $$.

&emsp; When dealing with categories, we are interested in when a morphism factors through another one. Intuitively, this abstracts the notion of integers dividing each another, and it leads to the notion of categorical limits and colimits.

&emsp; DEFINE LIMIT AND COLIMIT 

$$
\xymatrix @R=5em{
\Gamma(U, f^{-1}(\mathcal{O}_Y)) \ar[d]_\cong\ar[r]^\cong &
\Gamma(U, \mathcal{O}_X) \\
\Gamma(U, f'^{-1}(\mathcal{O}_V)) \ar@/^/[ru]^{f'^\sharp}
\ar@/_/[ru]_{f''^\sharp} &
}
$$


## 2. Applications to Sets

&emsp; One of the most intuitively insightful categories to deal with is that induced by a poset, i.e. partially ordered set.


## 3. K-Theory

&emsp; Addition and coproducts


## 4. References

1. Include Grothendieck's Tohoku
2. MacLane Categories