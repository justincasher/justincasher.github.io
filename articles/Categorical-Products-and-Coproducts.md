---
layout: Writing
indent: true
permalink: /Categorical-Products-and-Coproducts
feedformat: card
title: Categorical Products and Coproducts
---
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CD}{\mathcal{D}} \newcommand{\CI}{\mathcal{I}} \newcommand{\CO}{\mathcal{O}} \DeclareMathOperator{\Ob}{Ob} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} $$
<br>
## Table of Contents
1. [Limits and Colimits](#1-limits-and-colimits)
2. [Applications to Sets](#2-applications-to-sets)
3. [K-Theory](#3-k-theory)
4. [References](#4-references)

## 1. Limits and Colimits

&emsp; A *category* $$ \cC $$ is a class of objects $$ \Ob(\cC) $$ and a class of morphisms $$ \Hom(\cC) $$ equipped with a composition law, such that for any $$ A, B, C \in \Ob(\cC), $$ we have the following: 

- An associative composition operator 

$$ 
    \circ \colon \Hom(B, C) \times \Hom(A, B) \to \Hom(A, C).
$$

- Local identities $$ \Id_A \colon A \to A $$, such that for any $$ f \colon A \to B $$, we get $$ f \circ \Id_A = f $$ and $$ \Id_B \circ f = f $$.

&emsp; We define maps between categories $$ F \colon \cC \to \CD $$ on the level of pairs 

$$ 
    F \colon (\Ob(\cC), \Hom(\cC)) \to (\Ob(\CD), \Hom(\CD)),
$$

meaning each object (resp. morphism) in $$ \cC $$ is mapped to an object (resp. morphism) in $$ \CD $$. We call $$ F $$ a *functor* if it preserves the composition operator $$ F(f \circ g) = F(f) \circ F(g) $$ and local identities $$ F(\Id_A) = \Id_{F(A)} $$.

&emsp; When dealing with categories, we are interested in when a morphism factors through another one. Intuitively, this abstracts the notion of integers dividing each another, and it leads to the notion of categorical limits and colimits. 

&emsp; Let $$ F \colon \CI \to \cC $$ be a functor. Here, we call $$ F $$ a *diagram* and $$ \CI $$ the *indexing category*. We denote an object in the image of $$ F $$ by $$ F(i) = A_i $$. The *limit* of $$ F $$ is then an object $$ \displaystyle \lim_{\leftarrow} A_i $$ in $$ \cC $$ and a morphisms $$ \displaystyle f_m \colon \lim_{\leftarrow} A_i \to A_m $$ for each $$ m \in \CI $$. We require  
: (i) for any morphism $$ \phi \colon m \to n $$ in $$ \CI $$, we have $$ F(\phi) \circ f_m = f_n $$;  
: (ii) any other collection of morphisms $$ g_m \colon \CO \to A_m $$ factors through the limit, meaning there exists a unique $$ \displaystyle h \colon \CO \to \lim_{\leftarrow} A_i $$ making this diagram commute:

$$
\xymatrix{ 
    & \CO \ar@{.>}[d]|-{\exists !h} \ar@/_/[ddl]_{g_m} \ar@/^/[ddr]^{g_n} & \\
    & {\displaystyle \lim_{\leftarrow} A_i} \ar[dl]^{f_m} \ar[dr]_{f_n} & \\
    A_m \ar[rr]_{F(\phi)} & & A_n.
}
$$



## 2. Applications to Sets

&emsp; One of the most intuitively insightful categories to deal with is that induced by a poset, i.e. partially ordered set.


## 3. K-Theory

&emsp; Addition and coproducts


## 4. References

1. Include Grothendieck's Tohoku
2. MacLane Categories
