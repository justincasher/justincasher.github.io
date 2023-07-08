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
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CO}{\mathcal{O}} \newcommand{\CV}{\mathcal{V}} $$ 
$$ \newcommand{\RR}{\mathbb{R}} $$
$$ \DeclareMathOperator{\CHom}{\mathcal{H}om} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Op}{Op} \DeclareMathOperator{\res}{res} \DeclareMathOperator{\Spec}{Spec}  $$
<br>

**Abstract.** We use sheaves of sections to define schemes. 

**Prerequisites.** Familiarity with category theory and manifolds is assumed. My article [Categorical Coproducts and K-Theory](https://www.justinasher.me/Categorical-Coproducts) gives a brief overview of some of these ideas.

## Table of Contents
1. [Sheaves](#1-sheaves)
2. [Zariski Topology](#2-zariski-topology)
3. [Schemes](#3-schemes)
4. [References](#4-references)

## 1. Sheaves

&emsp; Let $$ X $$ be a topological space. Then associated to $$ X $$ is a category $$ \Op(X) $$, whose objects are the open subsets of $$ X $$ and morphisms are the inclusion maps $$ \iota \colon U \hookrightarrow V $$ when $$ U \subseteq V $$. A *presheaf of $$ \cC $$* is a contravariant functor $$ F \colon \Op(X) \to \cC $$. Elements in $$ F(U) $$ are called *sections* (see Example 1.1). Inclusions are mapped to restrictions, which we denote $$ F(\iota) = \res_{V, U} $$ or $$ F(\iota)(s) = s \mid_{U} $$. 

&emsp; We call a presheaf $$ F $$ a *sheaf* if a gluing condition is satisfied for every open set $$ U $$: For every open cover $$ \{ U_i \}_{i \in I} $$ of $$ U $$ and elements $$ s_i \in F(U_i) $$ such that $$ s_i \mid_{U_i \cap U_j} = s_j \mid_{U_i \cap U_j} $$, there exists a unique $$ s \in F(U) $$ such that $$ s \mid_{U_i} = s_i $$.

**Example 1.1.** &nbsp; Let $$ \varphi \colon Y \to X $$ be a continuous function. Associated to $$ \varphi $$ is a *sheaf of sections* $$ \Gamma_\varphi $$, which maps each open subset of $$ X $$ to the set of sections on $$ X $$:

$$
\Gamma_{\varphi}(U) = \{ s \colon U \to Y \mid f \circ s = \Id_U \},
$$

and whose restriction maps are given by restricting the individual sections, i.e. $$ \res_{U, V}(s) = s \mid_{V} $$. It is clear that this is indeed a sheaf. This is the canonical example from which sheaves are derived.

**Example 1.2.** &nbsp; Write $$ M $$ for a smooth (real manifold) of dimension $$ n $$, and consider the sheaf of smooth sections of the trivial bundle $$ M \times \RR \to M $$. It associates to each open subset $$ U $$ the local ring of smooth functions $$ s \colon U \to \RR $$. In the sequel we denote it $$ \cC^{\infty}_M $$.

&emsp; A morphism between sheaves $$ f \colon X \to Y $$ on a fixed space $$ X $$ is a morphism of functors, and hence a natural transformation. Explicitly, $$ f $$ associates to each open subset $$ U $$ a morphism $$ f_U \colon F(U) \to G(U) $$ such that the following diagram commutes:

$$ 
\xymatrix{ 
F(V) \ar[d]_{\res_{V, U}} \ar[r]^{f_V} & G(V) \ar[d]^{\res_{V, U}} \\
F(U) \ar[r]_{f_U} & G(U) 
} 
$$

We denote the set of morphisms $$ \CHom(F, G) $$.

&emsp; The direct image and inverse image functors allow us to define morphisms between sheaves on different spaces (among other things). Fix a continuous map $$ \varphia \colon X \to Y $$, and let $$ F $$ and $$ G $$ be sheaves on $$ X $$ and $$ Y $$, respectively. We call the sheaf

$$
\varphi_* F(U) = F(\varphi^{-1}(U))
$$

on $$ Y $$ the direct image of $$ F $$ by $$ \varphi $$. Accordingly, we call the sheaf

$$
\varphi^{-1} G(U) = \colim_{\varphi(U) \subseteq V) G(V)
$$

on $$ X $$ the inverse image of $$ F $$ by $$ \varphi $$.

These are adjoint functors between the categories of sheaves on $$ X $$ and sheaves on $$ Y $$

$$
\CHom(f^{-1} F, G) = \CHom(F, f_* G).
$$

**Proposition 1.3.** &nbsp; Let $$ M $$ and $$ N $$ be smooth manifolds. Then if there exists a homeomorphism $$ f \colon M \to N $$ such that $$ \cC^{\infty}_N \to \cC^{\infty}_M $$ is a local isomorphism, then $$ M $$ and $$ N $$ are diffeomorphic.

*Proof.* Prove this!



# 2. Zariski topology

&emsp; Write $$ R $$ for a commutative ring with unit. An ideal $$ \fp $$ is called *prime* if it satisfies the following equivalent conditions: 
<ol type="a" class="custom" style="list-style-position: outside">
  <li>\( R / \fp \) is a domain;</li>
  
  <li>\( ab \in \fp \) implies \( a \in \fp \) or \( b \in \fp \).</li>
</ol>
We denote the set of prime ideals $$ \Spec R $$ and call it the *prime spectrum*.

&emsp; For any ideal $$ \fa $$ we let $$ \CV(\fa) $$ be the set of prime ideals containing $$ \fa $$:

$$
\CV(\fa) = \{\fp \in \Spec R \mid \fa \subseteq \fp \}
$$

The following proposition shows that these form the closed sets for the *Zariski topology* on $$ \Spec R $$. 

**Proposition 2.1.** &nbsp; The sets $$ V(\fa) $$ are the closed sets of a topology on $$ \Spec R $$.

*Proof.* To show arbitrary intersections, let $$ \fa_i $$ be a (possibility infinite) family of ideals, and observe

$$
\bigcap_i \CV(\fa_i) = \CV(\sum_i \fa_i),
$$

Likewise for finite unions we consider a finite family $$ \fa_1, \dots, \fa_n $$, and observe

$$
\bigcup_{i=1}^{n} \CV(\fa_i) = \CV(\prod_{i=1}^{n} \fa_i).
$$

Finally, we see that $$ \CV(\varnothing) = \Spec R$$ and $$ \CV(R) = \varnothing $$, so the empty set and entire space are both closed. $$ \blacksquare $$
 
&emsp; Any ring homomorphism $$ f \colon R \to S $$ induces a map $$ f^{\#} \colon \Spec S \to \Spec R $$ given by $$ f^{\#}(\fp) = f^{-1}(\fp). $$ This is one reason to consider prime ideals instead of, for instance, maximal ideals, as the inverse image of a prime ideal is again prime.



# 3. Schemes

&emsp; Any two fields have the same prime spectrum ($$ \Spec k = \{0\} $$) while being not necessarily isomorphic. Therefore, we need to equip $$ \Spec R $$ with a sheaf to differentiate between nonisomorphic commutative rings as follows.

&emsp; Fix a commutative ring $$ R $$ with prime spectrum $$ \Spec R $$. Equip each $$ R_{\fp} $$ with the discrete topology. Consider the bundle

$$
\coprod_{\fp \in \Spec R} R_{\fp} \to X,
$$

which sends elements of $$ R_{\fp} $$ to $$ \fp $$. We denote its sheaf of continuous sections by $$ \CO_X $$ and call the pair ($$ X $$, $$ \CO_X $$) an *affine scheme*. 

**Remark 3.1.** &nbsp; Any continuous function $$ \varphi \colon X \to Y $$ into a discrete space $$ Y $$ is locally constant. Indeed, choose an $$ x \ in X $$ and write $$ \varphi(x) = y $$. By assumption $$ \{y\} $$ is open, so $$ \varphi^{-1}(y) $$ is an open neighborhood of $$ x $$ on which $$ \varphi $$ is constant. Thus, we could replace “continuous sections” by “locally constant sections” in our definition, which is often the given definition.

**Theorem 3.2.** &nbsp; *Let $$ R $$ and $$ S $$ be commutative rings. The following are equivalent:*
<ol type="a" class="custom" style="list-style-position: outside">
  <li>\( f \colon R \to S \) <i>is an isomorphism of rings;</i></li>
  
  <li>\( f^* \colon \Spec S \to \Spec R \) <i>is an isomorphism of locally ringed spaces.</i></li>
</ol>

*Proof.* Prove this!



## 4. References

1. Categorical Coproducts and K-theory
