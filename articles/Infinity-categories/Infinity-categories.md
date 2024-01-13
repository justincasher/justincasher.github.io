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
**Abstract.** &nbsp; This is a collection of notes I am creating for a reading group on infinity categories and higher algebra at Indiana University in the spring of 2024.




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

The simplicial subset 

$$
\Lambda_i^n([m])
= \{f \in \Delta^n([m]) \mid f([m]) \cup \{ i \} \neq [n] \}
$$

is called the *$ i $-th horn*; it is referring to as being *inner* if $ 0 < i < n $ and *outer* if $ i = 0, n $.

$$
\xymatrix{ 
    & \{1\} \ar@{.>}[dr] \\
    \{0\} \ar[ur] \ar[rr] & \{2\}
} 
$$


## 2. References

1. 