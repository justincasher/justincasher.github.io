---
layout: Writing
indent: true
permalink: /Categorical-Products-and-Coproducts
feedformat: card
title: Categorical Products and Coproducts
---
$$ \newcommand{\cC}{\mathcal{C}} \DeclareMathOperator{\Ob}{Ob} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} $$
<br>
## Table of Contents
1. [Limits and Colimits](#1-limits-and-colimits)
2. [Applications to Sets](#2-applications-to-sets)
3. [K-Theory](#3-k-theory)
4. [References](#4-references)

## 1. Limits and Colimits

&emsp; A category $$ \cC $$ is a class of objects $$ \Ob(\cC) $$ and a class of morphisms $$ \Hom(\cC) $$ equipped with a composition law. Meaning for any $$ A, B, C \in \Ob(\cC) $$, there exists an associative composition operator 

$$
    \circ \colon \Hom(B, C) \times \Hom(A, B) \to \Hom(A, C)
$$ 

and local identities $$ \Id_A \colon A \to A $$ and $$ \Id_B \colon B \to B $$. For any $$ f \colon A \to B $$ these are required to satisfy $$ f \circ \Id_A = f $$ and $$ \Id_B \circ f = f $$.

&emsp; When dealing with categories, we are interested in when a morphism factors through another one. This abstracts the notion of integers dividing on another. This leads to the notion of a limit...


## 2. Applications to Sets

&emsp; One of the most intuitively insightful categories to deal with is that induced by a poset, i.e. partially ordered set.


## 3. K-Theory

&emsp; Addition and coproducts


## 4. References

1. Include Grothendieck's Tohoku
2. MacLane Categories
