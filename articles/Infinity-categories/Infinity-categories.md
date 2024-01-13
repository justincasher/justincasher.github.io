---
layout: Writing
indent: true
permalink: /Infinity-categories
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
**Abstract.** &nbsp; This is a collection of notes I am creating for a reading group on $ \infty $-categories and higher algebra at Indiana University in the spring of 2024.




## Table of Contents
1. [Introduction to $ \infty $-categories](#1-introduction-to-infinity-categories)
2. [References](#2-references)




## 1. Introduction to infinity-categories


&emsp; The *simplex category* has objects sets $ [n] = \{0, 1, \dots, n \} $ equipped with the usual linear ordering, and it has morphisms functions $ f \colon [m] \to [n] $ which respect the ordering, i.e. $ i \leq j $ implies $ f(i) \leq f(j) $. 


&emsp; A presheaf of sets, i.e. a contravariant functor $ X \colon \Delta \to \text{Set} $, is called a *simplicial set*; we denote $ X([n]) $ by $ X_n $. A morphisms of simplicial sets is a natural transformation of functors. Write $ \text{Set}_{\Delta} $ for the category of simplicial sets. 


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

is called the *$ i $-th horn*; it is referred to as being *inner* if $ 0 < i < n $ and *outer* if $ i = 0, n $.

$$
\xymatrix{ 
    \{1\} \ar@{.>}[dr] \\
    \{0\} \ar[u] \ar[r] & \{2\}
} 
\xymatrix{ 
    \{1\} \ar[dr] \\
    \{0\} \ar[u] \ar@{.>}[r] & \{2\}
}
\xymatrix{ 
    \{1\} \ar[dr] \\
    \{0\} \ar@{.>}[u] \ar[r] & \{2\}
}
$$


&emsp; Let $ X $ be a simplicial set and $ \iota \colon \Lambda_i^n \hookrightarrow \Delta^n $ the inclusion. We say $ X $ is a *Kan complex* if, for any horn $ \Lambda_i^n $ and morphism $ f_0 \colon \Lambda_i^n \to X $, there exists a morphism $ f \colon \Delta^n \to X $ such that $ f \circ \iota = f_0 $: 

$$
\xymatrix{ 
    \Lambda_i^n & X \\
    \Delta^n
} 
$$


**Example 1.** &nbsp; Let $ A $ be a topological space. We define a simplicial set $ \text{Sing}(A) $ as follows. Write $ | \Delta^n | $ for the geometric realization of $ \Delta^n $, i.e. the topological $ n $-simplex in $ \mathbb{R}^n $. We put 

$$
\text{Sing}_n(A) = \text{Hom}_{\text{Top}}(|\Delta^n|, A) 
$$

to be the set of singular $ n $-simplices. Each $ f \colon [m] \to [n] $ determines a morphism $ \text{Sing}_n(A) \to \text{Sing}_m(A) $ by precomposing with the map 

$$
|\Delta^m| \to |\Delta^n|, 
\qquad
(t_0, \dots, t_n) \to 
\left( \sum_{f(i)= 0} t_i, \dots, \sum_{f(i)= n} t_i \right).
$$

We will not show this here, but $ \text{Sing} $ is a functor from topological spaces to simplicial sets, whose left adjoint is the geometric realization functor $ | \cdot | $.


**Proposition 2.** &nbsp; *$ \text{Sing}(A) $ is a Kan complex.*




## 2. References

1. 