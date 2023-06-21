---
layout: Writing
indent: true
permalink: /Defining-a-Scheme
feedformat: card
title: Defining a Scheme
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
$$ \newcommand{\fa}{\mathfrak{a}} \newcommand{\fp}{\mathfrak{p}} $$
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CV}{\mathcal{V}} $$ 
$$ \newcommand{\RR}{\mathbb{R}} $$
$$ \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Op}{Op} \DeclareMathOperator{\res}{res} \DeclareMathOperator{\Spec}{Spec}  $$
<br>

**Abstract.** We use sheaves of sections to define schemes. Familiarity with category theory is assumed.

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

DEFINE NATURAL TRANSFORMATION/MORPHISM



# 2. Zariski topology

&emsp; Write $$ R $$ for a commutative ring with unit. An ideal $$ \fp $$ is called *prime* if it satisfies the following equivalent conditions: 
<ol type="a" class="custom" style="list-style-position: outside">
  <li>\( R / \fp \) is a domain;</li>
  
  <li>if \( ab \in \fp \) then \( a \in \fp \) or \( b \in \fp \).</li>
</ol>
We denote the set of prime ideals $$ \Spec R $$ and call it the *prime spectrum*.

&emsp; For any ideal $$ \fa $$ we let $$ \CV(\fa) $$ be the set of prime ideals containing $$ \ca $$:

$$
\CV(\fa) = \{\fp \in \Spec R \mid \fa \subseteq \fp \}
$$

It is not hard to show that 
<ol type="1" class="custom" style="list-style-position: outside">
  <li>INTERSECTIONS</li>
  
  <li>UNIONS</li>
</ol>
Thus, the $$ \CV(\fa) $$ form the closed subsets for a topology on $$ \Spec R $$ called the *Zariski topology*.

Describe how the inverse image of a prime ideal is prime, but not necessarily maximal. 


# 3. Schemes




## 4. References

1. 
