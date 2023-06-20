---
layout: Writing
indent: true
permalink: /Defining-a-Scheme
feedformat: card
title: Defining a Scheme
---
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\RR}{\mathbb{RR}} $$
$$ \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Op}{Op} \DeclareMathOperator{\res}{res}  $$
<br>

**Abstract.** 

## Table of Contents
1. [Sheaves](#1-sheaves)
4. [References](#4-references)

## 1. Sheaves

&emsp; Let $$ X $$ be a topological space. Then associated to $$ X $$ is a category $$ \Op(X) $$, whose objects are the open subsets of $$ X $$ and morphisms are the inclusion maps $$ \iota \colon U \hookrightarrow V $$ when $$ U \subseteq V $$. A *presheaf of $$ \cC $$* is a contravariant functor $$ F \colon \Op(X) \to \cC $$. We furthermore call $$ F $$ a *sheaf* if for every open set $$ U $$ the following gluing condition is satisfied: For every open cover $$ \{ U_i \}_{i \in I} $$ of $$ U $$ and elements $$ s_i \in F(U_i) $$ such that $$ s_i \mid_{U_i \cap U_j} = s_j \mid_{U_i \cap U_j} $$, there exists a unique $$ s \in F(U) $$ such that $$ s \mid_{U_i} = s_i $$.

**Example 1.1.** Let $$ f \colon Y \to X $$ be a continuous function. Associated to $$ f $$ is a *sheaf of sections* $$ \Gamma_f $$, which maps each open subset of $$ X $$ to the set of sections on $$ X $$:

$$
\Gamma_f(U) = \{ s \colon U \to Y \mid f \circ s = \Id_U \},
$$

and whose restriction maps are given by restricting the individual sections, i.e. $$ \res_{U, V}(s) = s \mid_{V} $$. It is clear that this is indeed a sheaf. This is the canonical example from which sheaves are derived, and the reason why for any sheaf $$ F $$, we refer to elements of $$ F(U) $$ as *sections*.

**Example 1.2.** Write $$ M $$ for a smooth real manifold of dimension $$ n $$. The sheaf of smooth sections of the trivial bundle $$ \pi \colon M \times \RR \to M $$ is the algebra of smooth functions $$ f \colon U \to \RR $$ for each $$ U $$ open. This sheaf determines our manifold up to diffeomorphism. In order to describe this correspondence, we need a notion of an (iso)morphism of sheaves.



# 2. Schemes




## 4. References

1. 
