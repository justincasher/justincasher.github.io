---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /Defining-a-Scheme
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
$$ \newcommand{\fa}{\mathfrak{a}} \newcommand{\fm}{\mathfrak{m}} \newcommand{\fp}{\mathfrak{p}} $$
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CO}{\mathcal{O}} \newcommand{\CV}{\mathcal{V}} $$ 
$$ \newcommand{\RR}{\mathbb{R}} $$
$$ \DeclareMathOperator{\CHom}{\mathcal{H}om} \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\et}{Ét} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Op}{Op} \DeclareMathOperator{\res}{res} \DeclareMathOperator{\Spec}{Spec}  $$
<br>

**Abstract.** We use sheaves of sections to define schemes. 

**Prerequisites.** Familiarity with category theory and manifolds is assumed. My article [Categorical Coproducts and K-Theory](https://www.justinasher.me/Categorical-Coproducts) gives a brief overview of some of these ideas.

## Table of Contents
1. [Sheaves](#1-sheaves)
2. [Zariski Topology](#2-zariski-topology)
3. [Schemes](#3-schemes)
4. [References](#4-references)

## 1. Sheaves

#### Sheaves and stalks

&emsp; Let $$ X $$ be a topological space. Then associated to $$ X $$ is a category $$ \Op(X) $$, whose objects are the open subsets of $$ X $$ and morphisms are the inclusion maps $$ \iota \colon U \hookrightarrow V $$ when $$ U \subseteq V $$. A *presheaf of $$ \cC $$* is a contravariant functor $$ F \colon \Op(X) \to \cC $$. Elements in $$ F(U) $$ are called *sections* (see Example 1.1). Inclusions are mapped to restrictions, which we denote $$ F(\iota) = \res_{V, U} $$ or $$ F(\iota)(s) = s \mid_{U} $$. 

&emsp; We call a presheaf $$ F $$ a *sheaf* if a gluing condition is satisfied for every open set $$ U $$: For every open cover $$ \{ U_i \}_{i \in I} $$ of $$ U $$ and elements $$ s_i \in F(U_i) $$ such that $$ s_i \mid_{U_i \cap U_j} = s_j \mid_{U_i \cap U_j} $$, there exists a unique $$ s \in F(U) $$ such that $$ s \mid_{U_i} = s_i $$.

**Example 1.1a.** &nbsp; Let $$ \varphi \colon Y \to X $$ be a continuous function. Associated to $$ \varphi $$ is a *sheaf of sections* $$ \Gamma_\varphi $$, which maps each open subset of $$ X $$ to the set of sections on $$ X $$:

$$
\Gamma_{\varphi}(U) = \{ s \colon U \to Y \mid \varphi \circ s = \Id_U \},
$$

and whose restriction maps are given by restricting the individual sections, i.e. $$ \res_{U, V}(s) = s \mid_{V} $$. It is clear that this is indeed a sheaf. This is the canonical example from which sheaves are derived.

&emsp; The *stalk* of a sheaf $$ F $$ at a point $$ x \in X $$ allows us to observe its local behavor at $$ x $$. It is defined as 

$$
F_x = \underset{x \in U}{\colim} F(U), 
$$

where the colimit is taken over open sets containing $$ x $$. This is equivalent to 

$$
F_x = \{ (U, s) \mid x \in U, s \in F(U) \} / \sim,
$$

where $$ (U_1, s_1) \sim (U_2, s_2) $$ if there exists a $$ U_3 \subseteq U_1 \cap U_2 $$ such that $$ s_1 \mid_{U_3} = s_2 \mid_{U_3} $$. Elements of the stalk $$ (U, s) $$ are referred to as *germs*.

**Example 1.1b.** &nbsp; With $$ \varphi $$ as above, we see that $$ (\Gamma_\varphi)_x $$ is the set of sections $$ s \colon U \to Y $$ with $$ x \in U $$ modulo if two sections agree on any neighborhood of $$ x $$.

&emsp; Bundling the stalks gives us the *étale space* over $$ X $$

$$
p \colon \et(X) = \coprod_{x \in X} F_x \to X,
$$

where $$ F_x $$ is mapped to $$ x $$. Recall that a local homeomorphism is also called an étale map. If we equip each stalk with the discrete topology, then $$ p $$ is étale: for any germ $$ (U, s) $$, we have $$ \coprod_{x \in U} \{s\} $$ is homeomorphic to $$ U $$. Importantly, $$ \Gamma_p(U) = F(U) $$, which (with further proof) yields an equivalence between sheaves of sets on $$ X $$ étale maps with codomain $$ X $$. 

**Theorem 1.2.** &nbsp; There is an equivalence between the categories of sheaves on $$ X $$ and étale spaces over $$ X $$, which is given by sending a sheaf to its étale space and an étale space to its sheaf of sections.

*Proof.* See MAC LANE REFERENCE page 88 cor 3

&emsp; One application of the étale space is sheafification. Given a presheaf $$ F $$ on $$ X $$, we would like to find the smallest sheaf $$ F^{sh} $$ which $$ F $$ factors through. This means for any sheaf $$ G $$ on $$ X $$ and morphism (i.e. natural transformation) of presheaves $$ f \colon F \to G $$, there exists a morphism $$ f^{sh} \colon F^{sh} \to G $$ making the following diagram commute:

$$ 
\xymatrix{ 
F \ar[d] \ar[r]^{f} & G  \\
F^{sh} \ar[ur]_{f^{sh}} & 
} 
$$

We can construct $$ F^{sh} $$ by taking the sheaf of sections of the étale space of $$ F $$, and call it the *sheafification* of $$ F $$.

**Proposition 1.3.** PROVE THIS IS MINIMAL


#### Morphisms of sheaves

&emsp; A morphism between sheaves $$ f^{\#} \colon F \to G $$ on a fixed space $$ X $$ is a morphism of functors, and hence a natural transformation. Explicitly, $$ f^{\#} $$ associates to each open subset $$ U $$ a morphism $$ f^{\#}_U \colon F(U) \to G(U) $$ such that the following diagram commutes:

$$ 
\xymatrix{ 
F(V) \ar[d]_{\res_{V, U}} \ar[r]^{f^{\#}_V} & G(V) \ar[d]^{\res_{V, U}} \\
F(U) \ar[r]_{f^{\#}_U} & G(U) 
} 
$$

We denote the set of morphisms $$ \CHom(F, G) $$.

&emsp; The direct image and inverse image functors allow us to define morphisms between sheaves on different spaces (among other things). Fix a continuous map $$ \varphi \colon X \to Y $$, and let $$ F $$ and $$ G $$ be sheaves on $$ X $$ and $$ Y $$, respectively. We call the sheaf on $$ Y $$ 

$$
\varphi_* F(U) = F(\varphi^{-1}(U))
$$

the *direct image* of $$ F $$ by $$ \varphi $$. Accordingly, we call the sheaf on $$ X $$ 

$$
\varphi^{-1} G(U) = \underset{\varphi(U) \subseteq V}{\colim} G(V)
$$

the *inverse image* of $$ F $$ by $$ \varphi $$. Here, we are taking the colimit over open sets containing $$ \varphi(U) $$, because $$ \varphi(U) $$ is not necessarily open.

&emsp; These are adjoint functors between the categories of sheaves on $$ X $$ and sheaves on $$ Y $$

$$
\CHom(\varphi^{-1} G, F) = \CHom(G, \varphi_* F).
$$

Since every right (resp. left) adjoint is left (resp. right) exact, we see $$ \varphi_* F $$ is left exact and $$ \varphi^{-1} $$ is right exact. 

**Lemma 1.4.** &nbsp; Let $$ \varphi \colon X \to Y $$ be continuous and $$ G $$ a sheaf on $$ Y $$. Then $$ (\varphi^{-1} G)_x \cong G_{\varphi(x)} $$. 

*Proof.* Indeed,

$$
\begin{aligned}
(\varphi^{-1} G)_x 
& = \underset{x \in U}{\colim} \underset{\varphi(U) \subseteq V}{\colim} G(V) \\
& = \underset{f(x) \in V}{\colim} G(V),
\end{aligned}
$$

where the second equality follows from continuity. $$ \blacksquare $$


&emsp; Hence, a morphism of sheaves $$ (f, f^{\#}) \colon (X, F) \to (Y, G) $$ is given by a continuous $$ f \colon X \to Y $$ and a map $$ f^{\#} \in \CHom(G, f_* F) $$. Using the adjoint relation, we can also consider $$ f^{\#} $$ as an element in $$ \CHom( f^{-1} G, F) $$. We will often use the supressed notation $$ f \colon F \to G $$ to denote a morphism. 

&emsp; Recall for a fixed morphism $$ f \colon F \to G $$ in an arbitrary category, we have the following notions:
<ol type="a" class="custom" style="list-style-position: outside">
  <li>We call \( f \) a *monomorphism* if for any \( g_1, g_2 \colon E \to F \) we have \( f \circ g_1 = f \circ g_2 \) implies \( g_1 = g_2 \);</li>
  
  <li>We call \( f \) an *epimorphism* if for any \( h_1, h_2 \colon G \to H \) we have \( h_1 \circ f = h_2 \circ f \) implies \( h_1 = h_2 \); </li>
  
  <li>We call \( f \) an *isomorphism* if there exists a \( f^{-1} \colon G \to F \) such that \( f^{-1} \circ f = \Id_F \) and \( f \circ f^{-1} = \Id_G \);</li>
</ol>

**Proposition 1.5.** &nbsp; *Let $$ f \colon F \to G $$ be a morphism of sheaves. Then $$ f $$ is a monomorphism (resp. epimorphism, isomorphism) if and only if it the induced map on each stalk is.*

*Proof.* It is clear that if $$ f $$ is a monomorphism then the map induced on stalks is. So assume $$ f $$ induces a monomorphism on stalks . The cases of epimorphisms and isomorphisms follow similarily. 

**Corollary 1.6.** The inverse image functor is exact.


#### Locally ringed spaces

&emsp; We conclude this section by discussing locally ringed spaces, which arise naturally in geometry. Let $$ X $$ be a topological space and $$ \CO_X $$ a sheaf of rings such that each stalk $$ \CO_{X, x} $$ is a local ring. Then we call the pair $$ (X, \CO_x) $$ a *locally ringed space*. We denote the maximal ideal in $$ F_x $$ by $$ \fm_x $$. A morphism of locally ringed spaces $$ (f, f^{\#}) \colon (X, \CO_X) \to (Y, \CO_Y) $$ is a map of sheaves of rings, such at each stalk, the map $$ f_x \colon \CO_{Y, f(x)} \to \CO_{X, x} $$ is a local ring homomorphism, i.e. $$ f_x(\fm_{f(x)}) \subseteq \fm_x $$. FIX INVERSE IMAGE FUNCTOR 

 **Example 1.4.** &nbsp; Write $$ M $$ for a smooth (real manifold) of dimension $$ n $$, and consider the sheaf of smooth sections of the trivial bundle $$ M \times \RR \to M $$, which we denote $$ \cC^{\infty}_M $$. It associates to each open subset $$ U $$ the ring of smooth functions $$ s \colon U \to \RR $$. Notably, $$ (M, \cC^{\infty}_M) $$ is a localy ringed space. Indeed, at any point $$ x \in M $$, a germ $$ (U, f) $$ is equivalent to a smooth function $$ f \colon U \to \RR $$. The maximal ideal $$ \fm_x $$ in $$ F_x $$ is then the set of functions which vanish at $$ x $$, i.e. $$ f(x) = 0 $$. 
 
&emsp; Write $$ A $$ for a subset of $$ \RR^n $$ and $$ \cC^{\infty}_A $$ its sheaf of smooth functions. The following proposition shows that we could equivalently define a smooth manifold as a locally ringed spaced which is locally isomorphic to an affine space $$ (A, C^{\infty}_A) $$.

**Proposition 1.7.** &nbsp; *Let $$ M $$ and $$ N $$ be smooth manifolds. If there exists a homeomorphism $$ f \colon M \to N $$ such that $$ \cC^{\infty}_N \to \cC^{\infty}_M $$ is a local isomorphism of locally ringed spaces, then $$ M $$ and $$ N $$ are diffeomorphic.*

*Proof.* Prove this!

**Corollary 1.8.** &nbsp; *The category of smooth manifolds is equivalent to the category of locally ringed spaces locally isomorphic to affine space.* 



## 2. Zariski Topology

&emsp; Write $$ R $$ for a commutative ring with unit. An ideal $$ \fp $$ is called *prime* if it satisfies the following equivalent conditions: 
<ol type="a" class="custom" style="list-style-position: outside">
  <li>\( R / \fp \) is a domain;</li>
  
  <li>\( ab \in \fp \) implies \( a \in \fp \) or \( b \in \fp \).</li>
</ol>
We denote the set of prime ideals $$ \Spec R $$ and call it the *prime spectrum*. For instance, every maximal ideal is prime, and the zero ideal $$ (0) $$ is prime.

&emsp; For any ideal $$ \fa $$ we let $$ \CV(\fa) $$ be the set of prime ideals containing $$ \fa $$:

$$
\CV(\fa) = \{\fp \in \Spec R \mid \fa \subseteq \fp \}
$$

The following proposition shows that these form the closed sets for what we call the *Zariski topology* on $$ \Spec R $$. 

**Proposition 2.1.** &nbsp; *The sets $$ V(\fa) $$ form the closed sets for a topology on $$ \Spec R $$.*

*Proof.* To show arbitrary intersections, let $$ \fa_i $$ be a (possibility infinite) family of ideals, and observe

$$
\textstyle \bigcap_i \CV(\fa_i) = \CV(\sum_i \fa_i).
$$

Here, $$ \sum_i \fa_i $$ is the ideal generated by finite sums of elements from the $$ \fa_i $$. Likewise for finite unions we consider a finite family $$ \fa_1, \dots, \fa_n $$, and observe

$$
\textstyle \bigcup_{i=1}^{n} \CV(\fa_i) = \CV(\fa_1 \cdots \fa_n).
$$

Finally, we see that $$ \CV(\varnothing) = \Spec R$$ and $$ \CV(R) = \varnothing $$, so the empty set and entire space are both closed. $$ \blacksquare $$
 
**Remark 2.2.** &nbsp; Any ring homomorphism $$ f \colon R \to S $$ induces a continuous map $$ f^{\#} \colon \Spec S \to \Spec R $$ given by $$ f^{\#}(\fp) = f^{-1}(\fp). $$ This is one reason to consider prime ideals instead of, for instance, maximal ideals, as the inverse image of a prime ideal is again prime.

&emsp; The Zariski topology has a basis of the form 

$$ 
D(r) = \Spec R \setminus  V(r) = \{ \fp \in \Spec R \mid f \not \in \fp \}
$$

for $$ r \in R $$. Indeed, if $$ U = \Spec R \setminus V(\fa) $$ is open, then 

$$ 
U = \Spec R \setminus \bigcap_{r \in \fa} V(r) = \bigcup_{r \in \fa} D(r).
$$

We call the $$ D(r) $$ *distinguished open sets*.

&emsp; The Zariski topology can also be described using localization. Let $$ S $$ be a multiplicatively closed subset of $$ R $$, i.e. $$ a, b \in S $$ implies $$ ab \in S $$. Then we define the *localization* of $$ R $$ by $$ S $$ as the set of formal quotients

$$
S^{-1} R = \{ r/s \mid r \in R, s \in S \}
$$

equipped with the operator 

$$
\frac{r_1}{s_1} + \frac{r_2}{s_2} = \frac{r_1 s_2 + r_2 s_1}{s_1 s_2}.
$$

&emsp; One important instance of a multiplicatively closed subset is that associated to a prime ideal $$ S_{\fp} = R \setminus \fp $$. We denote $$ R_{\fp} = S_{\fp}^{-1} R $$. Another is given by taking any $$ f \in R $$ and considering the multiplicative system $$ S_f = \{f, f^2, f^3, \dots, \} $$. We denote $$ R_f = S_f^{-1} R $$. We have 

$$
V(\fp) = \Spec R_{\fp}
$$

and 

$$
D(f) = \Spec R_f.
$$

INCLUDE HOW THIS RELATES TO COLIMITS

&emsp; We conclude this section by listing some properties and examples of the Zariski topology. 

**Proposition 2.3.** &nbsp; *The Zariski topology makes $$ \Spec R $$ quasi-compact.*

*Proof.* Suppose $$ D(f_i) $$ cover $$ \Spec R $$. Then $$ \bigcap V(f_i) = \varnothing, $$ which implies $$ \sum (f_i) = R $$. (If not, $$ \sum (f_i) $$ would be contained in a maximal, and hence prime, ideal). Therefore there exists a finite collection of $$ a_i \in f_i $$ such that $$ a_1 + \cdots + a_n = 1 $$. Consequently, 

$$ 
(f_1) \cup \cdots \cup (f_i) = R 
$$ 

and thus 

$$
D(f_1) \cup \cdots \cup D(f_i) = \Spec R,
$$

yielding a finite subcover. $$ \blacksquare $$
 
**Proposition 2.4.** &nbsp; *A point is closed in $$ \Spec R $$ if and only if it is a maximal ideal.*

*Proof.* Suppose $$ \fp \in \Spec R $$ is closed. Then $$ \CV(\fp) = \{ \fp \} $$, meaning no other prime ideals contain $$ \fp $$, and in particular no maximal ideals properly contain $$ \fp $$. We conclude that $$ \fp $$ is maximal. $$ \blacksquare $$

**Proposition 2.5.** &nbsp; *A subspace of $$ \Spec R $$ is irreducible if and only if it is of the form $$ \CV(\fp) $$ for $$ \fp $$ prime. INCLUDE  $$ \overline{\{\fp\}} $$.*

*Proof.* Let $$ \CV(\fa) $$ be a closed subspace. If $$ \CV(\fa) $$ contains multiple primes of height 1 above $$ \fa $$, then we can write $$ \CV(\fa) = \bigcup \CV(\fp_i) $$. Hence $$ \CV(\fa) $$ is irreducible if and only if $$ \CV(\fa) = \CV(\fp) $$ for some $$ \fp $$. FIX

**Theorem 2.6.** SPECTRAL SPACES

**Example 2.7.** Let $$ k $$ be a field. Then $$ \Spec k = \{0\} $$ with the trivial topology. Hence, any continuous map $$ f \colon \Spec k \to \Spec R $$ is determined by the image of $$ \{0\} $$. 

**Example 2.8.** By definition

**Example 2.9.** Affine space



## 3. Schemes

&emsp; Any two fields have the same prime spectrum ($$ \Spec k = \{0\} $$) while being not necessarily isomorphic. Therefore, we need to equip $$ \Spec R $$ with a sheaf to differentiate between nonisomorphic commutative rings as follows.

&emsp; Fix a commutative ring $$ R $$ with prime spectrum $$ \Spec R $$. Equip each $$ R_{\fp} $$ with the discrete topology. Consider the bundle

$$
\coprod_{\fp \in \Spec R} R_{\fp} \to \Spec R,
$$

which sends elements in $$ R_{\fp} $$ to $$ \fp $$. We denote its sheaf of continuous sections by $$ \CO_{\Spec R} $$ and call the pair ($$ \Spec R $$, $$ \CO_{\Spec R}) $$ an *affine scheme*. 

**Remark 3.1.** &nbsp; Any continuous function $$ \varphi \colon X \to Y $$ into a discrete space $$ Y $$ is locally constant. Indeed, choose an $$ x \in X $$ and write $$ \varphi(x) = y $$. By assumption $$ \{y\} $$ is open, so $$ \varphi^{-1}(y) $$ is an open neighborhood of $$ x $$ on which $$ \varphi $$ is constant. Thus, we could replace “continuous sections” by “locally constant sections” in our definition, which is  the given definition in, for instance, Hartshorne's book CITE.

&emsp; We call a locally ringed space $$ (X, \CO_X) $$ which is locally isomorphic to an affine scheme a *scheme*. PROPERTIES OF THE CATEGORIES OF SCHEMES. The following theorem shows that the category of rings is equivalent to a subcategory of the category of schemes.

**Theorem 3.2.** &nbsp; *Let $$ R $$ and $$ S $$ be commutative rings. The following are equivalent:*
<ol type="a" class="custom" style="list-style-position: outside">
  <li>\( f \colon R \to S \) <i>is an isomorphism of rings;</i></li>
  
  <li>\( f^\# \colon (\Spec S, \CO_S) \to (\Spec R, \CO_R) \) <i>is an isomorphism of locally ringed spaces.</i></li>
</ol>

*Proof.* Prove this!



## 4. References

1. Categorical Coproducts and K-theory
