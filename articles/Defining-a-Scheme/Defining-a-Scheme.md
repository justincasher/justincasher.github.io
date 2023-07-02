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

**Abstract.** We use sheaves of sections to define schemes. 

**Prerequisites.** Familiarity with category theory and manifolds is assumed. My article [Categorical Coproducts and K-Theory](https://www.justinasher.me/Categorical-Coproducts) gives a brief overview of some of these ideas.

## Table of Contents
1. [Sheaves](#1-sheaves)
4. [References](#4-references)

## 1. Sheaves

&emsp; Let $$ X $$ be a topological space. Then associated to $$ X $$ is a category $$ \Op(X) $$, whose objects are the open subsets of $$ X $$ and morphisms are the inclusion maps $$ \iota \colon U \hookrightarrow V $$ when $$ U \subseteq V $$. A *presheaf of $$ \cC $$* is a contravariant functor $$ F \colon \Op(X) \to \cC $$. Elements in $$ F(U) $$ are called *sections* (see Example 1.1). Inclusions are mapped to restrictions, which we denote $$ F(\iota) = \res_{V, U} $$ or $$ F(\iota)(s) = s \mid_{U} $$. 

We further call $$ F $$ a *sheaf* if a gluing condition is satisfied for every open set $$ U $$: For every open cover $$ \{ U_i \}_{i \in I} $$ of $$ U $$ and elements $$ s_i \in F(U_i) $$ such that $$ s_i \mid_{U_i \cap U_j} = s_j \mid_{U_i \cap U_j} $$, there exists a unique $$ s \in F(U) $$ such that $$ s \mid_{U_i} = s_i $$.

**Example 1.1.** Let $$ \varphi \colon Y \to X $$ be a continuous function. Associated to $$ f $$ is a *sheaf of sections* $$ \Gamma_f $$, which maps each open subset of $$ X $$ to the set of sections on $$ X $$:

$$
\Gamma_{\varphi}(U) = \{ s \colon U \to Y \mid f \circ s = \Id_U \},
$$

and whose restriction maps are given by restricting the individual sections, i.e. $$ \res_{U, V}(s) = s \mid_{V} $$. It is clear that this is indeed a sheaf. This is the canonical example from which sheaves are derived.

**Example 1.2.** Write $$ M $$ for a smooth (real manifold) of dimension $$ n $$, and consider the sheaf of smooth sections of the trivial bundle $$ M \times \RR \to M $$. It associates to each open subset $$ U $$ the local ring of smooth functions $$ s \colon U \to \RR $$. In the sequel, we denote it $$ \cC^{\infty}_M $$.

A morphism between sheaves $$ f \colon X \to Y $$ on a fixed space $$ X $$ is a morphism of functors, and hence a natural transformation. This means to each open subset $$ U $$ we have a morphism $$ f_U \colon F(U) \to G(U) $$ such that the following diagram commutes:

$$ 
\xymatrix{ 
F(V) \ar[d]_{\res_{V, U}} \ar[r]^{f_V} & G(V) \ar[d]^{\res_{V, U}} \\
F(U) \ar[r]^{f_U} & G(U) 
} 
$$

In order to define morphisms between sheaves on different topological spaces, we can use pushforward and inverse image functors.

**Proposition 1.3.** Let $$ M $$ and $$ N $$ be smooth manifolds. Then if there exists a homeomorphism $$ f \colon M \to N $$ such that $$ \cC^{\infty}_N \to \cC^{\infty}_M $$ is a local isomorphism, then $$ M $$ and $$ N $$ are diffeomorphic.

*Proof.* Prove this!



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

1. Categorical Coproducts and K-theory
