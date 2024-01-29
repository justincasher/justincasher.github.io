---
layout: Writing
indent: true
permalink: /infinity-categories-U
feedformat: card
title: Infinity categories and higher algebra seminar notes
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
<br>

**Abstract.** &nbsp; This is a collection of short notes I am creating for a reading group on $ \infty $-categories and higher algebra at Indiana University in the spring of 2024. Some of these notes are from talks given by other participates; I have indicated where.




## Table of Contents
1. [Introduction to $ \infty $-categories](#1-introduction-to-infinity-categories)
2. [Model categories and $ \infty $-categories](#2-model-categories-and-infinity-categories)
3. [References](#3-references)




## 1. Introduction to infinity categories


&emsp; The *simplex category* has objects sets $$ [n] = \{ 0, 1, \dots, n \} $$ equipped with the usual linear ordering, and it has morphisms functions $ f \colon [m] \to [n] $ which respect the ordering, i.e., $ i \leq j $ implies $ f(i) \leq f(j) $. 


&emsp; A presheaf of sets on $ \Delta $, i.e., a contravariant functor $ X \colon \Delta \to \text{Set} $, is called a *simplicial set*; we denote $ X([n]) $ by $ X_n $. A morphism of simplicial sets is a natural transformation of functors. Write $ \text{Set}_{\Delta} $ for the category of simplicial sets. 


&emsp; The simplicial set 

$$ 
\Delta^n([m]) = \text{Hom}_{\Delta}([m], [n]) 
$$

is called the *standard $ n $-simplex*. The Yoneda lemma tells us 

$$
X_n = \text{Hom}_{\text{Set}_{\Delta}}(\Delta^n, X).
$$


&emsp; The simplicial subset of $ \Delta^n $

$$
\Lambda_i^n([m])
= \{f \in \Delta^n([m]) \mid f([m]) \cup \{ i \} \neq [n] \}
$$

is called the *$ i $-th horn*; it is referred to as being *inner* if $ 0 < i < n $ and *outer* if $ i = 0, n $. Lurie visualizes $ \Gamma_0^2 $, $ \Gamma_1^2 $, and $ \Gamma_2^2 $, respectively, as follows:

$$
\xymatrix{ 
    \{1\} \ar@{.>}[dr] \\
    \{0\} \ar[u] \ar[r] & \{2\}
} 
\quad
\xymatrix{ 
    \{1\} \ar[dr] \\
    \{0\} \ar[u] \ar@{.>}[r] & \{2\}
}
\quad
\xymatrix{ 
    \{1\} \ar[dr] \\
    \{0\} \ar@{.>}[u] \ar[r] & \{2\}
}
$$

Here, when performing the operation "$$ \cup \{ i \} $$", we add any arrows touching the vertex $$ \{ i \} $$ to the diagram.


&emsp; Let $ X $ be a simplicial set and $ \iota \colon \Lambda_i^n \hookrightarrow \Delta^n $ the inclusion. We say $ X $ is a *Kan complex* if, for any horn $ \Lambda_i^n $ and morphism $ f_0 \colon \Lambda_i^n \to X $, there exists a morphism $ f \colon \Delta^n \to X $ such that $ f \circ \iota = f_0 $; pictorially, the following diagram must commute:

$$
\xymatrix{ 
    \Lambda_i^n \ar[r]^{f_0} \ar[d]_{\iota} & X \\
    \Delta^n \ar@{.>}[ur]_{f}
} 
$$


**Example 1.** &nbsp; Let $ A $ be a compactly generated topological space. We define a simplicial set $ \text{Sing}(A) $ as follows. Write $ \vert \Delta^n \vert $ for the geometric realization of $ \Delta^n $, i.e., the topological $ n $-simplex in $ \mathbb{R}^n $. We put 

$$
\text{Sing}_n(A) = \text{Hom}_{\text{Top}}(\vert \Delta^n \vert, A) 
$$

to be the set of singular $ n $-simplices. Each $ f \colon [m] \to [n] $ determines a morphism $ \text{Sing}_n(A) \to \text{Sing}_m(A) $ by precomposing with the map 

$$
\vert \Delta^m \vert \to \vert \Delta^n \vert, 
\qquad
(t_0, \dots, t_n) \to 
\left( \sum_{f(i)= 0} t_i, \dots, \sum_{f(i)= n} t_i \right).
$$

$ \text{Sing} $ is a functor from topological spaces to simplicial sets, whose left adjoint is the geometric realization functor $ \vert \cdot \vert $.


**Proposition 2.** &nbsp; *$ \text{Sing}(A) $ is a Kan complex.*


*Proof.* The adjunction $ \vert \cdot \vert \dashv \text{Sing}(\cdot) $ implies the following diagram:

$$
\xymatrix{
    \text{Hom}_{Top}(\vert \Delta^n \vert, A) \ar[r]^{\cong} \ar[d]_{\vert \iota \vert^*}
    & \text{Hom}_{Set_{\Delta}}(\Delta^n, \text{Sing}(A)) \ar[d]^{\iota^*} \\
    \text{Hom}_{Top}(\vert \Gamma_i^n \vert, A) \ar[r]^{\cong} 
    & \text{Hom}_{Set_{\Delta}}(\Lambda_i^n, \text{Sing}(A))
}
$$

This reduces the problem of lifting $ f_0 \colon \Lambda_i^n \to \text{Sing}(A) $ to lifting the associated $ \vert f_0 \vert \colon \vert \Lambda_i^n \vert \to A $. Let $ r \colon \Delta^n \to \Lambda_i^n $ be a continuous retract. We conclude that $ \vert f \vert \colon \vert \Delta^n \vert \to A $ given by $ \vert f \vert = \vert f_0 \vert \circ r $ is our desired map. Q.E.D. 


**Example 3.** &nbsp; Let $ \mathcal{C} $ be a small category. Define a simplicial set $ N(\mathcal{C}) $, the *nerve of $ \mathcal{C} $*, by considering functors

$$
N_n(\mathcal{C}) = \text{Fun}([n], \mathcal{C}).
$$

Here, we are considering $ [n] $ as the category with objects $ \{0, 1, \dots, n\} $ and arrows $ i \to j $ if $ i \leq j $. Explicitly, objects of $ N_n(\mathcal{C}) $ are composable sequences of morphisms 

$$
\xymatrix{
    C_1 \ar[r]^{f_1} & C_2 \ar[r]^{f_2} & \cdots \ar[r]^{f_n} & C_n.
}
$$

The following proposition tells us we can consider the nerve as a *weak Kan complex*, meaning it satisfies the Kan lifting condition for all inner horns.


**Proposition 4.** &nbsp; *Let $ X $ be a simplicial set. The following are equivalent:*

*(1) There exists a small category and an isomorphism $ X \cong N(\mathcal{C}) $.*

*(2) For each inner horn, $ 0 < i < n $, and diagram*

$$
\xymatrix{ 
    \Lambda_i^n \ar[r]^{f_0} \ar[d]_{\iota} & X \\
    \Delta^n, \ar@{.>}[ur]_{f}
}
$$

*there exists a* unique *dotted arrow making it commute*.


*Proof.* This is 1.1.2.2 of [\[1\]](#3-references). We only sketch a couple of main ideas without providing a complete proof.

$ (1) \implies (2) $ &nbsp; Let $ g_k \colon X_{k-1} \to X_k $ denote the restriction $ f_0 \mid \Delta^{\{ k-1, k \}} $. Composing our $ g_k $, 

$$
\xymatrix{
    X_1 \ar[r]^{g_1} & X_2 \ar[r]^{g_2} & \cdots \ar[r]^{g_n} & X_n,
}
$$

determines an $ n $-simplex $ f \colon \Delta^n \to X $. 


$ (2) \implies (1) $ &nbsp; We mention the proof of associativity law of the composition operator. Consider a sequence of morphisms 

$$
\xymatrix{
    w \ar[r]^{f} & x \ar[r]^{g} & y \ar[r]^{h} & z.
}
$$

We have the following 3 faces of the 4-sided 3-simplex:

$$
\xymatrix{ 
    x \ar[dr]^{g} \\
    w \ar[u]^{f} \ar[r]_{g \circ f} & y
} 
\quad
\xymatrix{ 
    y \ar[dr]^{h} \\
    x \ar[u]^{g} \ar[r]_{h \circ g} & z
}
\quad
\xymatrix{ 
    y \ar[dr]^{h} \\
    w \ar[u]^{g \circ f} \ar[r]_{h \circ (g \circ f)} & z
}
$$

By (2), we get a unique fourth face:

$$
\xymatrix{ 
    x \ar[dr]^{h \circ g} \\
    w \ar[u]^{f} \ar[r]_{h \circ (g \circ f)} & z
}
$$

Thus, the associativity law $ h \circ (g \circ f) = (h \circ g) \circ f $. Q.E.D.


&emsp; We define a simplicial set $ X $ to be an *$ \infty $-category* if it is a weak Kan complex; i.e., for each inner horn, $ 0 < i < n $, and diagram 

$$
\xymatrix{ 
    \Lambda_i^n \ar[r]^{f_0} \ar[d]_{\iota} & X \\
    \Delta^n, \ar@{.>}[ur]_{f}
}
$$

there there exists a dotted arrow making it commute. Note that the dotted arrow is not required to be unique, contrasting the case of the nerve of a category, and it is not required to exist on outer horns, unlike $ \text{Sing}(A) $. Thus, $ \infty $-categories can be thought of as a generalized framework for small category theory and algebraic topology.


&emsp; Up to a notion of homotopy equivalence, $ \infty $-categories are equivalent to $ (\infty, 1) $-categories. That is categories with $ n $-morphisms for each $ n \in \mathbb{N} $, where the $ n $-morphisms for $ n > 1 $ are invertible. Lurie proves this in 1.1. of [\[1\]](#3-references).




## 2. Model categories and infinity categories


*From a talk by Vladimir Shein*


&emsp; Let $ \mathcal{M} $ be a category. Then we call $ \mathcal{M} $ a *model category* $ \mathcal{M} $ if it has 3 distinguished classes of morphisms called *weak equivalences* $ W $, *fibrations* $ \text{Fib} $, and *cofibrations* $ \text{Cof} $, which satisfy the following axioms:


(*Composition*) Each class is closed under composition and contains the identity morphism $ \text{Id}_X $ for every $ X $ in $ \mathcal{M} $.

(*Bicomplete*) Finite limits and colimits exist in $ \mathcal{M} $.
(*2-out-of-3*) Let $ f \colon X \to Y $ and $ g \colon Y \to Z $ be morphisms in $ \mathcal{M} $. Then if two of $ f $, $ g $, and $ g \circ f $ are in $ W $, then so is the third.

(*Retractions*) Let $ f \colon X \to X' $ be a retract of $ g \colon Y \to Y' $, i.e., there exists morphisms $ r, i, r', i' $ with $$ r \circ i = \text{Id}_X $$ and $$ r' \circ i' = \text{Id}_{X'} $$, which fit into the following commuting diagram:

$$
\xymatrix{ 
    Y \ar[r]^{g} \ar[d]^{r} & Y' \ar[d]^{r'} \\
    X \ar[r]_f \ar@/^/[u]^{i} & X'. \ar@/_/[u]_{i'}
} 
$$

If $ g $ is in $ W $, $ \text{Fib} $, or $ \text{Cof} $, then so is $ f $.

(*Lifting*) Consider the diagram

$$
\xymatrix{
    A \ar[r]^{f} \ar[d]_i & X \ar[d]^{p} \\
    B \ar[r]_{g} \ar@{.>}[ur]^{h} & Y.
}
$$

(*Factorization*) 





## 3. References

1. J. Lurie, *Higher Topos Theory*, Annals of Mathematics Studies, vol. 170, Princeton University Press, Princeton, NJ, 2009.
2. ————, *Higher Algebra*, 2017.
3. ————, *Kerodon*. [Link](https://kerodon.net/)