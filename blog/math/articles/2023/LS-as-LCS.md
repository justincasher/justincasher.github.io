---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /ls-as-lcs
title: Local systems as locally constant sheaves
date: "May 2023"
abstract: "Let X be a locally simply connected space. We prove that the categories of locally constant sheaves and local systems on X are equivalent."
toc:
  - title: "Overview"
    anchor: "1-overview"
  - title: "Proof"
    anchor: "2-proof"
  - title: "References"
    anchor: "3-references"
---
<div style="display: none;">
$$
\DeclareMathOperator{\LC}{LC}
\DeclareMathOperator{\LS}{LS}
\newcommand{\CA}{\mathcal{A}}
\newcommand{\CB}{\mathcal{B}}
\DeclareMathOperator{\Aut}{Aut}
$$
</div>

## 1. Overview
    
&emsp; Let $$ X $$ be a topological space. Associated to any $$ R $$-module $$ M $$ is a presheaf on $$ X $$, which is given by mapping every open subset to $$ M $$ and setting restrictions to be the identity map. The sheafification of this presheaf is called a *constant sheaf* on $$ X $$ and is denoted $$ \underline{M} $$. Consequently, a sheaf $$ F $$ on $$ X $$ of $$ R $$-modules is said to be *locally constant* if for every point $$ x \in X $$, there exists a neighborhood $$ U $$ such that $$ F \mid_{U} $$ is a constant sheaf. This is equivalent to giving an open cover $$ \{U_{\alpha}\} $$ and $$ R $$-modules $$ \{M_{\alpha}\} $$ which satisfy $$ F \mid_{U_{\alpha}} = \underline{M_{\alpha}} $$. We denote the category of locally constant sheaves of $$R $$-modules on $$ X $$ by $$ \LC(X, R) $$; it is an abelian category.

&emsp; Now let $$ \Pi(X) $$ be the fundamental groupoid of $$ X $$ with the operator $$ \star $$ of path composition. We call a functor $$ L \colon \Pi(X) \to R\text{-Mod} $$ an *$$ R $$-local system on $$ X $$*. Morphisms between local systems are given by natural transformations of functors. Write $$ \LS(X, R) $$ for the category of $$ R $$-local systems on $$ X $$; it is again an abelian category. The purpose of this note is to provide a proof of the following theorem.


**Theorem.** &nbsp; *Let $$ X $$ be a locally simply-connected space. Then the categories $$ \LC(X, R) $$ and $$ \LS(X, R) $$ are equivalent.*
    
    
## 2. Proof
        
&emsp; Again assume $$ X $$ to be locally simply-connected. We are going to construct a pair of functors 

$$
\begin{aligned}
    \CA & = \LC(X, R) \to \LS(X, R) \\
    \CB & = \LS(X, R) \to \LC(X, R)
\end{aligned}
$$

which induce a categorical equivalence. Our proof can be generalized semi-locally simply connected spaces, cf. [\[1\]](#3-references). In the sequel, by an $$ R $$-module we mean a left $$ R $$-module equipped with the discrete topology, unless specified elsewise. We are not assuming coverings to be path-connected. In particular, a cover is universal if every other path-connected cover factors through it. 

&emsp; A continuous map $$ f \colon Y \to X $$ is called *étale* if it is a local homeomorphism. For any sheaf $$ F $$ we define *étale space* of $$ F $$ as the bundle

$$
    p \colon \coprod_{x \in X} F_x \to X,
$$

where elements of $$ F_x $$ are mapped to $$ x $$. This map is indeed étale: for any germ $$ (U, m) $$ the set $$ \coprod_{x \in U} \{m\} $$ is homeomorphic to $$ U $$. The utility of this construction is that the sheaf of sections of $$ p $$ is isomorphic to $$ F $$. Hence, it is not hard to show that the categories of étale maps with codomain $$ X $$ and of sheaves of sets on $$ X $$ are equivalent, cf. [\[5, ch.2, §6\]](#3-references).

&emsp; In the case that $$ F $$ is locally constant, its étale space is a covering. Indeed, let $$ U $$ be a neighborhood of $$ x $$ such that $$ S \mid_U = \underline{M} $$. Then the étale space restricted to $$ U $$ takes the form $$ p \colon U \times M \to U $$, which is a cover by the assumption that the topology on $$ M $$ is discrete. If we assume that $$ X $$ is locally connected, then this condition is also sufficient.


**Lemma 1.** &nbsp; *Let $$ X $$ be a locally connected space. A sheaf $$ F $$ of $$ R $$-modules on $$ X $$ is locally constant if and only if its étale space is a covering.*

*Proof.* Suppose the étale space of $$ F $$ is a covering. Then every point $$ x \in X $$ has a neighborhood $$ U $$ such that the restriction is $$ p \colon U \times M \to U $$. Assuming $$ U $$ to be connected implies that the sections of this map are constant since the topology on $$ M $$ is discrete, and thus our sheaf is constant on $$ U $$. $$ \blacksquare $$


**Lemma 2.** &nbsp; *A locally constant sheaf on a simply connected space is constant.*

*Proof.* Let $$ X $$ be a simply connected space with $$ F $$ locally constant. Then by lemma 1 the étale space of $$ F $$ covers $$ X $$. The only covers of a simply connected space are a discretely indexed copies of itself, and hence we can write our étale space in the form $$ p \colon X \times M \to X $$. Since $$ X $$ is connected, the sections of this map are constant, meaning our sheaf is constant. $$ \blacksquare $$


&emsp; Now we are ready to construct are functors and start with constructing $$ \CA $$. Fix an element $$ F \in \LC(X, R) $$ and define $$ \CA(F) = L $$ as follows. For each $$ x \in X $$ set $$ L(x) = F_x $$. Next take a homotopy class of paths $$ [\gamma] $$ from $$ x $$ to $$ y $$ and choose a representative $$ \gamma $$. Since $$ \gamma $$ has compact image, there exists a finite open cover $$ U_1, \dots, U_n $$ and a partition $$ t_0, \dots, t_n $$ of $$ [0, 1] $$ such that

- $$ \gamma([t_{j-1}, t_j]) $$ is contained in $$ U_j $$, and
- $$ F \mid_{U_j} $$ is the constant sheaf $$ \underline{M} $$ on each $$ U_j $$ for some fixed $$ M $$.

Observe that $$ F \mid_{U_j} $$ being constant implies that for any $$ a, b \in U_j $$, there exists a canonical isomorphism $$ F_a \cong F(U_j) \cong F_b $$. Applying this to the sequence $$ \gamma(t_j) $$ yields a chain of isomorphisms, which compose to a map $$ L([\gamma]) \colon F_x \to F_y $$. 

&emsp; It is not hard to see that this isomorphism does not depend on the choice of partition. We do need to show any other representative $$ \omega \in [\gamma] $$ induces the same map. Indeed, let $$ h \colon [0, 1]^2 \to X $$ be a homotopy with $$ h(0, t) = \gamma(t) $$ and $$ h(1, t) = \omega(t) $$. Since the image of $$ h $$ is compact, we can choose a partition $$ s_0, \dots, s_n $$ of $$ [0, 1] $$ such that $$ F $$ is constant on $$ [s_j, s_{j+1}] \times [s_k, s_{k+1}] $$ for $$ 0 \leq j, k \leq n-1 $$. Set $$ \gamma_j = h(s_j, t) $$ so that $$ \gamma_0 = \gamma $$ and $$ \gamma_n = \omega $$. Then $$ \gamma_j $$ and $$ \gamma_{j+1} $$ induce the same isomorphism, because they are contained in the same sequence of locally constant neighborhoods. We conclude that our isomorphism is homotopy invariant.

&emsp; Now let $$ f \colon F \to G $$ be a map of locally constant sheaves on $$ X $$. We define $$ \CA(f) $$ to be the induced map on stalks $$ f_x \colon F_x \to G_x $$. To show this is a natural transformation, we can restrict ourselves to open subsets $$ U $$ where $$ F $$ and $$ G $$ are both constant sheaves $$ \underline{M} $$ and $$ \underline{N} $$, respectively. Our morphism $$ f $$ is induced by an $$ R $$-module homomorphism $$ f_0 \colon M \to N $$. Then our result follows from the following diagram commuting:

$$
\begin{CD}
    F_x     @>\sim>>    F(U)    @>\sim>>    F_y \\
    @VVf_0V             @VVf_0V             @VVf_0V \\
    G_x @>\sim>> F(U) @>\sim>> G_y
\end{CD}
$$

&emsp; Next fix an element $$ L \in \LS(X, R) $$ and define $$ \CA(L) = F $$ as follows. Since $$ X $$ is locally simply connected it has a universal cover $$ \varphi \colon \widetilde{X} \to X $$, cf. [4, ch. 3, §8](#3-references). The functor $$ L $$ pulls back to $$ \widetilde{X} $$ by $$ L^{\ast} = L \circ \varphi $$, giving us the bundle

$$
    \nu \colon \coprod_{x \in \widetilde{X}} L^{\ast}(x) \to \widetilde{X}.
$$

The fundamental groupoid $$ \Pi(X) $$ acts on $$ \widetilde{X} $$ by considering the orbits of $$ \pi_1(X, x) $$ for differing $$ x $$. In particular, $$ \widetilde{X}/\Pi(X) = X $$. Likewise, $$ \Pi(X) $$ acts on each $$ L^{\ast}(x) $$ via the induced map $$ L \colon \pi_1(X, x) \to \Aut(L^{\ast}(x)) $$. This allows us to form the quotient bundle

$$
    \overline{\nu} \colon [\coprod_{x \in \widetilde{X}} L^{\ast}(x)] /\Pi(X) \to X. 
$$

We set $$ F $$ to be its sheaf of sections. Explicitly, elements of $$ F(U) $$ are sections $$ s \colon U \to \coprod_{x \in U} L(x) $$, such that for any class of paths $$ [\gamma] $$ from $$ x $$ to $$ y $$, we get that $$ s(y) = L([\gamma])(s(x)) $$. Our sheaf being locally constant follows from $$ X $$ being locally simply connected (lemma 2).

&emsp; Finally suppose we are given a natural transformation $$ \eta \colon L \to L' $$ between local systems. Then $$ \eta $$ induces a morphism $$ \CB(\eta) \colon \CB(L) \to \CB(L') $$ by pulling back sections, i.e. for each open subset $$ U $$, we map $$ s \in \CB(L)(U) $$ to $$ \eta \circ s $$. This is indeed a morphism of sheaves since $$ \eta $$ is functorial.

*Proof (Theorem).* Tracing through our definitions, it is not hard to see that $$ (\CA \circ \CB)(L) = L $$ and $$ (\CB \circ \CA)(F) = F $$. $$ \blacksquare $$


## 3. References

1. Pramod Achar, *Perverse sheaves and applications to representation theory*, American Mathematics Society, 2021.
2. bavajee, *Why are local systems and representations of the fundamental group equivalent*. [Link](https://mathoverflow.net/q/17786){:target="_blank"}. (version: 2016-02-07).
3. Alexandru Dimca, *Sheaves in topology*, Springer, 2004.
4. J.P. May, *A concise course in algebraic topology*, Chicago Lectures in Mathematics, 1999.
5. Saunders Mac Lane and Ieke Moerdijk, *Sheaves in geometry and logic: A first introduction to topos theory*, Springer-Verlag, 1992.
