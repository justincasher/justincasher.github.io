---
layout: 0_seminar_notes
indent: true
permalink: /infinity-categories-S
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


**Abstract.** &nbsp; This is a collection of short notes I am creating for a reading group on $ \infty $-categories and higher algebra at Indiana University in the spring of 2024. Some of these notes are from talks given by other participants; I have indicated where.






## Table of Contents
1. [Introduction to $ \infty $-categories](#1-introduction-to-infinity-categories)
2. [Model categories and $ \infty $-categories](#2-model-categories-and-infinity-categories)
3. [Fibrations, adjoints, Kan extensions](#3-fibrations-adjoints-kan-extensions)
4. [dg and stable $ \infty $-categories](#4-dg-and-stable-infinity-categories)
5. [References](#5-references)






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

is called the *$ i $-th horn*; it is referred to as being *inner* if $ 0 < i < n $ and *outer* if $ i = 0, n $. Lurie visualizes $ \Lambda_0^2 $, $ \Lambda_1^2 $, and $ \Lambda_2^2 $, respectively, as follows:

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


**Example 1.1.** &nbsp; Let $ A $ be a compactly generated topological space. We define a simplicial set $ \text{Sing}(A) $ as follows. Write $ \vert \Delta^n \vert $ for the geometric realization of $ \Delta^n $, i.e., the topological $ n $-simplex in $ \mathbb{R}^n $. We put 

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


**Proposition 1.2.** &nbsp; *$ \text{Sing}(A) $ is a Kan complex.*


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


**Example 1.3.** &nbsp; Let $ \mathcal{C} $ be a small category. Define a simplicial set $ N(\mathcal{C}) $, the *nerve of $ \mathcal{C} $*, by considering functors

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


**Proposition 1.4.** &nbsp; *Let $ X $ be a simplicial set. The following are equivalent:*

*(1) There exists a small category and an isomorphism $ X \cong N(\mathcal{C}) $.*

*(2) For each inner horn, $ 0 < i < n $, and diagram*

$$
\xymatrix{ 
    \Lambda_i^n \ar[r]^{f_0} \ar[d]_{\iota} & X \\
    \Delta^n, \ar@{.>}[ur]_{f}
}
$$

*there exists a* unique *dotted arrow making it commute*.


*Proof.* This is 1.1.2.2 of [\[3\]](#5-references). We only sketch a couple of main ideas without providing a complete proof.

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


&emsp; Up to a notion of homotopy equivalence, $ \infty $-categories are equivalent to $ (\infty, 1) $-categories. That is categories with $ n $-morphisms for each $ n \in \mathbb{N} $, where the $ n $-morphisms for $ n > 1 $ are invertible. Lurie proves this in 1.1. of [\[3\]](#5-references). 

&emsp; In particular, a *topological category* $ T $ is a category enriched over compactly generated Hausdorff spaces. A *simplicial category* $ C $ is a category enriched over simplicial sets; we denote this category $$ \text{Cat}_{\Delta} $$. The *simplicial nerve* $$ N \colon \text{Cat}_{\Delta} \to \text{Set}_{\Delta} $$ is characterized by 

$$
\text{Hom}_{\text{Set}_{\Delta}}(\Delta, N(C))
\cong \text{Hom}_{\text{Cat}_{\Delta}}(\mathfrak{C}[\Delta^n], C)
$$

for some simplicial category $ \mathfrak{C}[\Delta^n] $ which we will not define here. We set $ N(T) $ to be $ N(\text{Sing}(T)) $. Theorem 1.1.5.13 in [\[3\]](#5-references) asserts that  the conunit

$$
\vert \text{Hom}_{\mathfrak{C}[N(T)]}(x, y) \vert
\to \text{Hom}_T(x, y)
$$

is a weak homotopy equivalence of topological spaces. Since we are interested in objects up to homotopy equivalence, we consider $ \infty $-categories and topological categories to be the same.






## 2. Model categories and infinity categories


*From a talk by Vladimir Shein*


&emsp; Let $ \mathcal{M} $ be a category. Then we call $ \mathcal{M} $ a *model category* $ \mathcal{M} $ if it has 3 distinguished classes of morphisms called *weak equivalences* $ W $, *fibrations* $ \text{Fib} $, and *cofibrations* $ \text{Cof} $, which satisfy the following axioms:


(*Composition*) Each class is closed under composition and contains the identity morphism $ \text{Id}_X $ for every $ X $ in $ \mathcal{M} $.


(*Bicomplete*) Finite limits and colimits exist in $ \mathcal{M} $.
(*2-out-of-3*) Let $ f \colon X \to Y $ and $ g \colon Y \to Z $ be morphisms in $ \mathcal{M} $. Then if two of $ f $, $ g $, and $ g \circ f $ are in $ W $, then so is the third.


(*Retractions*) Let $ f \colon X \to X' $ be a retract of $ g \colon Y \to Y' $, i.e., there exists morphisms $ r, i, r', i' $ with $$ r \circ i = \text{Id}_X $$ and $$ r' \circ i' = \text{Id}_{X'} $$, which fit into the following commuting diagram:

$$
\xymatrix{ 
    Y \ar[r]^{g} \ar[d]^{r} & Y' \ar[d]_{r'} \\
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

Let $ i \in \text{Cof} $ and $ p \in \text{Fib} $. If $ i \in W $ or $ p \in W $, then there exists an $ h \colon B \to X $ making the diagram commute.


(*Factorization*) Any $ f \colon X \to Y $ can be factored in two ways 

$$
\xymatrix{
    X \ar[d]_j \ar[r]^{i} \ar[dr]^f & A \ar[d]^p \\
    B \ar[r]_{q} & Y
}
$$

where $ i, j \in \text{Cof} $, $ p, q \in \text{Fib} $, and $ i, q \in W $.


&emsp; We call the elements in $ \text{Fib} \cap W $ trivial (or acyclic) fibrations, and the elements in $ \text{Cof} \cap W $ trivial (or acyclic) cofibrations. The bicompleteness axiom implies $ \mathcal{M} $ contains initial and terminal objects; letting $ D \colon \varnothing \to \mathcal{C} $ be the empty diagram, we get that $ \text{colim} j $ is the initial object, and $ \lim j $ is the terminal object. It need not be pointed, i.e., have a zero object.


**Example 2.1.** &nbsp; Consider the category of topological spaces $ \text{Top} $; we can endow it with a model structure. $ W $ is the set of homotopy equivalences, i.e., continuous functions $ f \colon X \to Y $ such that $ f $ induces isomorphisms $ f_* \colon \pi_n(X) \to f_*(Y) $. $ \text{Fib} $ are Serre fibrations, i.e., $ f $ for which the right lifting problem

$$
\xymatrix{
    \{0\} \times \vert \Delta^n \vert \ar[r] \ar@{^{(}->}[d] & X \ar[d]^{p} \\
    \vert \Delta^n \vert \ar[r] \ar@{.>}[ur] & Y
}
$$

admits a solution. Finally, $ \text{Cof} $ consists of the retracts of relative cell complexes.


**Example 2.2.** &nbsp; Consider the category of simplicial sets $ \text{Set}_{\Delta} $. $ W $ is the set of maps that induce a weak equivalence on the geometric realizations, $ \text{Fib} $ are Kan fibrations, and $ \text{Cof} $ is the collection of monomorphisms.


**Example 2.3.** &nbsp; Consider the category of chain complexes of $ R $-modules. $ W $ is the set of quasi-isomorphisms, $ \text{Fib} $ are chain maps $ f $ such that each $ f_n \colon X_n \to Y_n $ is surjective, and $ \text{Cof} $ are chain maps $ g $ such that each $ g_n \colon X_n \hookrightarrow Y_n $ is injective with projective cokernel.


&emsp; Let $ \mathcal{M} $ be a model category. We call $ \text{Ho}(\mathcal{M}) = W^{-1} \mathcal{M} $ the *homotopy category of* $ \mathcal{M} $, where inversion means each weak equivalence becomes an isomorphism. We say that $ f, g \colon X \to Y $ are *homotopic* if there exists a commutative diagram

$$
\xymatrix{
    X \ar[d]^{i} \ar[dr]^{f} \\
    C(X) \ar[r]^{h} \ar@/^/[u]^{p}\ar@/_/[d]_{p} & Y \\
    X \ar[ur]_{g} \ar[u]_{j}
}
$$

such that $ p $ is a acyclic fibration with $ p \circ i = p \circ j = \text{Id}_C $, and that 

$$ 
\textstyle i \coprod j \colon X \coprod X \to C(X) 
$$ 

is a cofibration.


&emsp; We say that $ X $ is *fibrant* (resp. cofibrant) if the unique map from the initial (resp. terminal) object, $ \varnothing \to X $ (resp. $ X \to * $), is a fibration (resp. cofibration). If $ X $ is cofibrant and $ Y $ is fibrant, then homotopy equivalence $ \sim $ is an equivalence relation compatible with composition. Hence, the quotient $ C^{cf}/\sim $, fibrant or cofibrant objects modulo homotopy, is well defined.


**Theorem 4.** &nbsp; *The natural functor $ Q \colon (C^{cf}/\sim) \to \text{Ho}(C) $ is an equivalence of categories.*  


*Proof.* See theorem 1 in [\[6\]](#5-references). Q.E.D.


**Example 2.1'.** &nbsp; $ \text{Ho(Top)} $, up to equivalence, has objects CW-complexes and morphisms homotopy classes of continuous maps.


**Example 2.2'.** &nbsp; $ \text{Ho}(\text{Set}_{\Delta}) \cong \text{Ho(Top)} $ via the geometric realization functor. 


**Example 2.3'.** &nbsp; $ \text{Ho}(Ch(R)) \cong D(R) $, where $ D(R) $ is the derived category.


**Theorem 2.4** (CITE) &nbsp; *Let $ C \in \text{Set}_{\Delta} $. Then $ C $ is fibrant if and only if $ C $ is an $ \infty $-category.*

&emsp; Let $$ T \in \text{Cat}_{\Delta} $$ be a simplicial category, i.e., a category enriched over simplicial sets. It has morphisms functors $ F \colon T \to T' $ such that 

$$
F \colon \text{Hom}_T(x, y) \to \text{Hom}_{T'}(F(x), F(y))
$$

a map of simplicial sets. The inclusion $$ \text{Cat} \hookrightarrow \text{Cat}_{\Delta} $$ has a left adjoint $$ [\cdot] \colon \text{Cat}_{\Delta} \to \text{Cat} $$, where $ \text{Ob}([T]) = \text{Ob}(T) $, and  

$$
\text{Hom}_{[T]}(x, y) = \pi_0(\text{Map}(x, y)).
$$

We call $ [T] $ the *homotopy category* of $ T $. A functor $ F $ is called a *Dwyer-Kan* (DK) equivalence if $ [F] $ is essentially surjective, and 

$$ 
F \colon \text{Hom}_T(x, y) \to \text{Hom}_{T'}(F(x), F(y)) 
$$ 

is a weak equivalence of simplicial sets. 


&emsp; $$ \text{Cat}_{\Delta} $$ has a model structure with $ W $ being DK equivalences, and fibrations being functors $ F \colon T \to T' $ such that $ \text{Hom}(x, y) \to \text{Hom}(F(x), F(y)) $ is a Kan fibration which lifts morphisms at a fixed point. We denote $$ \text{Cat}_{\Delta} $$ with this model structure $$ (\text{Cat}_{\Delta})_{DK} $$.


&emsp; $ \text{Set}_{\Delta} $ comes equipped with a *Joyal model structure*, denoted $$ (\text{Set}_{\Delta})_{\text{Joy}} $$. We put $ W $ to be the set of *weak categorical equivalences*, i.e., maps $ A \to B $ such that $ \text{Hom}(A, C) \to \text{Hom}(B, C) $ induces an equivalence of simplicial categories for any $ C $. $ \text{Fib} $ is the collection of *quasi-fibrations*, meaning maps $ F \colon X \to Y $ which have the right lifting property with respect to the inclusion $ \Lambda_i^n \to \Delta^n $. Finally, $ \text{Cof} $ are monomorphisms.


**Theorem 2.5.** &nbsp; *$ C $ and $ N $ determine a Quillen equivalence between $ (\text{Set}_{\Delta})_{\text{Joy}} $ and $ (\text{Cat}_{\Delta})_{DK} $.*


*Proof.* See theorem 2.2.5.1 in [\[3\]](#5-references). Q.E.D.






## 3. Fibrations, adjoints, Kan extensions


&emsp; Let $ X $ and $ X' $ be simplicial sets. The *(convolution) product* of $ X $ and $ X' $ is given by 

$$
(X \star X')([n]) = \coprod_{[n] = I \cup I'},
$$

where the union is taken over all disjoint decompositions $ J = I \cup I' $ such that $ i < i' $ for $ i \in I $, $i' \in I $.


&emsp; Let $ C $ be an $ \infty $-category and $ p \colon I \to C $ be a map of simplicial sets. The *slice category* $ C_{/p} $ is characterized by the universal property, for every $ X \in \text{Set}_{\Delta} $,

$$
\text{Hom}_{\text{Set}_{\Delta}}(X, C_{/p}) 
= \text{Hom}_p(X \star I, C),
$$

where the "$ p $" on the R.H.S. means we only consider $ f \colon Y \star I \to C $ such that $ f \vert_{I} = p $. The dual notion to $ C_{/p} $ is $ C_{p/} $.


&emsp; An explicit way of defining the slice categories is by considering the diagrams in $ \text{Fun}(-, C) $, taking $ C \cong \text{Fun}(*, C) $,

$$
C_{/p} = C \times_{\text{Fun}(I, C)} \text{Fun}([1] \times I, C) \times_{\text{Fun}(I, C)} \{ p \} 
$$

and 

$$
C_{p/} = \{p\} \times_{\text{Fun}(I, C)} \text{Fun}([1] \times I, C) \times_{\text{Fun}(I, C)} C,
$$

where the maps $ \text{Fun}([1] \times I, C) \to \text{Fun}(I, C) $ are given by evaluation at $ 1 $ and $ 0 $ in $ [1] $.


&emsp; The *limit of $ p $*, $ \lim p $, is defined as a final object in $ C_{/p} $. The *colimit of $ p $*, $ \text{colim} \, p $, is an initial object in $ C_{p/} $. By final (resp. initial), we mean up to homotopy equivalence, i.e., $ A $ is initial if $ \text{Hom}(A, X) $ (resp. $ \text{Hom}(X, A) $) is contractible for every $ X $.


&emsp; Let $ D $ be an $ \infty $-category. Write $ \text{Cat}_{/D} $ for the category of morphisms $ F \colon C \to D $. 


&emsp; We say $ F $ has the *right lifting property* with respect to $ \iota \colon \Lambda_i^n \hookrightarrow \Delta^n $ if any diagram 

$$
\xymatrix{ 
    \Lambda_i^n \ar[r] \ar[d]_{\iota} & C \ar[d]^{F} \\
    \Delta^n \ar@{.>}[ur]_{f} \ar[r] & D
} 
$$

has a solution. If for inner horns (resp. any horn), $ 0 < i < n $ (resp. $ 0 \leq i \leq n $), the diagram has a solution, we say $ F $ is an *inner* (resp. *Kan*) *fibration*. If $ F $ has the right lifting property for $ \partial \Delta^n \to \Delta^n $ for every $ n $, then we call $ F $ a *trivial Kan fibration*.


&emsp; Let $ F $ be an inner fibration, and let $ e \colon o_0 \to o_1 $ be an edge in $ O $. If the map

$$
C_{/e} \to C_{/o_1} \times_{D_{/F(o_1)}} C_{/F(e)}
$$

is a trivial fibration, then we call $ e $ an *$ F $-fibration*.


&emsp; We say $ F $ is a *Cartesian fibration* if $ F $ is an inner fibration and, for every edge $ e \colon d_o \to d_1 $ in $ D $ and $ c_1 \in C $ such that $ F(c_1) = d_1 $, there exists an $ F $-cartesian edge $ \widetilde{e} \colon c_0 \to c_1 $ such that $ F(\widetilde{e}) = e $. If $ F^{op} $ is a Cartesian fibration, then we call $ F $ a coCartesian fibration. 


&emsp; We denote the category of (co)cartesian fibrations over $ D $ by $$ \text{(co)Cart}_{/D} $$. The full subcategory of $$ \text{(co)Cart}_{/D} $$ whose morphisms preserve $ F $-(co)Cartesian arrows is denoted $$ (\text{(co)Cart}_{/D})_{\text{strict}} $$. Let $$ (1\text{-(co)Cart}_{/D})_{\text{strict}} $$ denote the corresponding category where we replace $ C $ by the nerve of an ordinary category $ O $. Likewise, let $ 1 $-Cat denote the category of ordinary categories. 


&emsp; The following correspondence is referred to as *straightening and unstraightenin*g; we have stated it as in [\[1\]](#5-references).


**Theorem 3.1.** &nbsp; *There exists a canonical equivalence between $ (1 \text{-coCart}_{/D})_{\text{strict}} $ and $ \text{Fun}(D, 1\text{-Cat}) $.*


*Proof.* See theorem 3.2.0.1 in [\[3\]](#5-references) for a generalization. We will describe the correspondence here without proof.

&emsp; First fix $$ F \in (1\text{-coCart}_{/D})_{\text{strict}} $$. Then we get a functor of categories from $ D $ by taking for each $ d \in D $ the fiber $ F^{-1}(d) $. 

&emsp; Now let $$ \Phi \colon D \to 1\text{-Cat} $$ be a functor. We can construct a coCartsesian fibration $ F \colon O \to D $ by letting $ O $ have objects $ (d, x) $ with $ d \in D $ and $ x \in \Phi(d) $, and by setting $ \text{Hom}_{O}((d_0, x_0), (d_1, x_1)) $ be pairs $$ f \in \text{Hom}_D(d_0, d_1) $$ and $$ g \in \text{Hom}_{\Phi(d_1)}(\Phi_f(x_0), x_1) $$.  Q.E.D.


&emsp; Let $ F \colon C \to D $ and $ G \colon D \to C $ be functors of $ \infty $-categories. Lurie, 5.2.1 of [\[3\]](#5-references), proves that $ G $ is equivalent to a Cartesian fibration $ p \colon M \to \Delta^1 $, where $ M_{\{0\}} $ (the fiber at $ 0 $) is equivalent to $ C $ and $ M_{\{1\}} $ is equivalent to $ D $. Likewise, $ F $ is equivalent to a (different) coCartesian fibration. Hence, we define an *adjunction* between $ C $ and $ D $ to be a map $ p \colon \mathcal{M} \to \Delta^1 $ with $ C \equiv M_{\{0\}} $, $ D \equiv M_{\{1\}} $, $ p $ is a Cartesian fibration, and $ p $ is a coCartesian fibration. If $ F $ and $ G $ are the induced functors, then we write $ F \dashv G $.


&emsp; Alternatively, a *unit transformation* for a pair of functors $ (F, G) $ (as above) is a map $ u \colon \text{id}_C \to G \circ F $ in $ \text{Fun}(C, C) $ such that, for every $ c \in C $ and $ d \in D $, the composition 

$$
\text{Hom}_D(F(c), d) \to \text{Hom}_C(G(F(c), G(d))) \to \text{Hom}_C(c, G(d))
$$

is an isomorphism in the homotopy category.


**Theorem 3.2.** &nbsp; *$ F \dashv G $ if and only if there exists a unit transform.*


*Proof.* See proposition 5.2.2.8 in [\[3\]](#5-references). Q.E.D.


&emsp; Any functor $ F \colon C \to D $ induces $ F^* \colon \text{Fun}(D, E) \to \text{Fun}(C, E) $ by precomposition. The left (resp. right) adjoint of $ F^* $ is called the *left* (resp. *right*) *Kan extension* along $ F $; it is denoted $$ \text{LKE}_F $$ (resp. $$ \text{RKE}_F $$).






## 4. dg and stable infinity categories


&emsp; A *dg-category* $ C $ over $ R $ is a category enriched over $ \text{Ch}(R) $. Set $ R = \mathbb{Z} $. Then, specifically, we require:


(i) For every $ X, Y \in C $ we have $ \text{Hom}_C(X, Y)_* $ is a chain complex of abelian groups:

$$
\cdots \to \text{Hom}_C(X, Y)_1 \to \text{Hom}_C(X, Y)_0 \to \text{Hom}_C(X, Y)_{-1} \to \cdots 
$$


(ii) $ C $ is equipped with an (associative) composition law 

$$
\text{Hom}_C(Y, Z)_* \otimes_{\mathbb{Z}} \text{Hom}_C(X, Y)_* \to \text{Hom}_C(X, Z),
$$

such that that for every $ p, q $, there is a map 

$$
\text{Hom}_C(Y, Z)_p \otimes_{\mathbb{Z}} \text{Hom}_C(X, Y)_q \to \text{Hom}_C(X, Z)_{p+q},
$$

and these satisfy the Leibniz rule $ d(g \circ f) = dg \circ f + (-1)^p q \circ df $.


Note that $ \text{Id}_X $ must be in $ \text{Hom}_C(X, X)_0 $, else composing with it would shift degrees.


&emsp; The *dg-nerve* of $ C $, $ N_{dg}(C) $, is a simplicial set constructed as follows. For each natural number $ n $, we set $$ N_{dg}(C)_n $$ to be the set of ordered pairs $$ (\{X_i\}_{0 \leq i \leq n}, \{f_I\}) $$, where $$ X_i \in \text{Ob}(C) $$ and $ I $ ranged over subsets 

$$
I = \{i_{-}, i_m, i_{m-1}, \dots, i_1, i_+ \} \subseteq [n]
$$

with $ m \geq 0 $. We require $ f_I \in \text{Hom}(X_{i_-}, X_{i_+})_m $, with

$$
d f_I = \sum_{i \leq j \leq m} (-1)^j (f_{I \setminus i_j} - f_{i_j < \cdots < i_1 < i_+} \circ f_{i_-, i_m, < \cdots < i_j}).
$$

If $ \alpha \colon [m] \to [n] $ is nondecreasing, $$ \alpha_* \colon N_{dg}(C)_n \to N_{dg}(C)_m $$ is given by 

$$
( \{ X_i \}_{0 \leq i \leq n}, \{ f_I \}) \to ( \{ X_{f(j)} \}_{0 \leq j \leq m}, \{ g_J \} ),
$$

where 

$$
g_J
= 
\begin{cases}
f_{\alpha(J)} & \text{if } \alpha \vert_J \text{ is injective}, \\
\text{Id}_{X_i} & \text{if } J = \{j, j'\} \text{ with } \alpha(j) = \alpha(j') = i, \\
0 & \text{else}.
\end{cases}
$$


**Example 4.1.** &nbsp; By definition, $$ N_{dg}(C)_1 $$ are objects in $ C $. Likewise, $$ N_{dg}(C)_1 $$ is the set the of morphisms $$ f \in \text{Hom}_C(X, Y)_0 $$ such that $ df = 0 $. Finally, $ N_{dg}(C)_2 $ is the set of triples 

$$ 
f \in \text{Hom}_C(X, Y)_0, 
g \in \text{Hom}_C(Y, Z)_0, 
\text{ and } h \in \text{Hom}_C(X, Z)_0,
$$ 

such that $ df = dg = dh = 0 $ and that there exist $$ z \in \text{Hom}_C(X, Z)_1 $$ with $ dz = (g \circ f) - h $.


**Theorem 4.2.** &nbsp; *Let $ C $ be a dg-category. Then $$ N_{dg}(C) $$ is an $ \infty $-category.*






## 5. References

1. D. Gaitsgory and N. Rozenblyum, *A study in derived algebraic geometry, volume I: Correspondences and duality*, American Mathematical Society, Mathematical Surveys and Monographs, Volume 221, 2017.
2. A. Krause and T. Nikolaus, *Lectures on topological Hochschild homology and cyclotomic spectra*, lecture notes.
3. J. Lurie, *Higher Topos Theory*, Annals of Mathematics Studies, vol. 170, Princeton University Press, Princeton, NJ, 2009.
4. ————, *Higher Algebra*, 2017.
5. ————, *Kerodon*. [Link](https://kerodon.net/)
6. D. Quillen, *Homotopical algbera*, Springer lecture notes in mathematics, 1965.