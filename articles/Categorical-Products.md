---
layout: Writing
indent: true
permalink: /Categorical-Products
feedformat: card
title: Categorical Products and Coproducts
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
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CD}{\mathcal{D}} \newcommand{\CI}{\mathcal{I}} \newcommand{\CO}{\mathcal{O}} $$
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Ob}{Ob} $$
<br>

**Abstract.** We first define products and coproducts for arbitrary categories. We then argue that addition is an example of a specific coproduct, which motivates K-theory.

## Table of Contents
1. [Limits and Colimits](#1-limits-and-colimits)
2. [Products and Coproducts](#2-products-and-coproducts)
3. [Partially Ordered Sets](#3-partially-ordered-sets)
4. [K-Theory](#4-k-theory)
5. [References](#5-references)


## 1. Limits and Colimits

&emsp; A *category* $$ \cC $$ is a class of objects $$ \Ob(\cC) $$ and a class of morphisms $$ \Hom(A, B) $$ between any two objects equipped with a composition law, so that for any $$ A, B, C \in \Ob(\cC), $$ we have the following: 
<ol type="a" class="custom" style="list-style-position: outside">
  <li>An associative composition operator $$ \circ \colon \Hom(B, C) \times \Hom(A, B) \to \Hom(A, C); $$</li>
  
  <li>Local identities \( \Id_A \colon A \to A \), such that for any \( f \colon A \to B \), we get \( f \circ \Id_A = f \) and \( \Id_B \circ f = f \).</li>
</ol>
We denote the class of all morphisms in $$ \cC $$ by $$ \Hom(\cC) $$.

&emsp; We define maps between categories $$ F \colon \cC \to \CD $$ on the level of pairs 

$$ 
    F \colon (\Ob(\cC), \Hom(\cC)) \to (\Ob(\CD), \Hom(\CD)),
$$

meaning each object (resp. morphism) in $$ \cC $$ is mapped to an object (resp. morphism) in $$ \CD $$. We call $$ F $$ a *functor* if it preserves the composition operator 

$$ 
F(f \circ g) = F(f) \circ F(g) 
$$ 

and local identities $$ F(\Id_A) = \Id_{F(A)} $$.

**Remark.** When working with categories, we are interested in when a morphism factors through another one. Intuitively, this abstracts the notion of integers dividing each another, and it leads to the notion of categorical limits and colimits. 

&emsp; Let $$ F \colon \CI \to \cC $$ be a functor. Here, we call $$ F $$ a *diagram* and $$ \CI $$ the *indexing category*. We denote an object in the image of $$ F $$ by $$ F(i) = A_i $$. The *limit* of $$ F $$ is then an object $$ \lim A_i $$ in $$ \cC $$ equipped with a morphism

$$ 
f_m \colon \lim A_i \to A_m 
$$ 

for each $$ m \in \CI $$, such that:
<ol type="a" class="custom" style="list-style-position: outside">
    <li>For any morphism \( \phi \colon m \to n \) in \( \CI \), we have \( F(\phi) \circ f_m = f_n \);</li>
    
    <li>Any other collection of morphisms \( g_m \colon \CO \to A_m \) factors through the limit, meaning there exists a unique \( h \colon \CO \to \lim A_i \) making this diagram commute: 
        $$ 
        \xymatrix{ 
            & \CO \ar@{.>}[d]|-{\exists !h} \ar@/_/[ddl]_{g_m} \ar@/^/[ddr]^{g_n} & \\
            & \lim A_i \ar[dl]^{f_m} \ar[dr]_{f_n} & \\
            A_m \ar[rr]_{F(\phi)} & & A_n.
        } 
        $$</li>
</ol>

&emsp; There is likewise the dual notion of the *colimit* of $$ F $$, which is given by reversing the arrows in the definition of a limit. Explicitely, the colimit is an object $$ \displaystyle \colim A_i $$ in $$ \cC $$ equipped with a morphism

$$ 
\displaystyle f_m \colon A_m \to \colim A_i
$$ 


for each $$ m \in \CI $$, such that:
<ol type="a" class="custom" style="list-style-position: outside">
    <li>For any morphism \( \phi \colon m \to n \) in \( \CI \), we have \( f_m =  f_n \circ F(\phi); \)</li>
    
    <li>Any other collection of morphisms \( g_m \colon A_m \to \CO \) factors through the limit, meaning there exists a unique \( \displaystyle h \colon \colim A_i \to \CO \) making this diagram commute: 
        $$ 
        \xymatrix{ 
            A_m \ar[rr]^{F(\phi)} \ar@/_/[ddr]_{g_m} \ar[dr]^{f_m} & & A_n \ar@/^/[ddl]^{g_n} \ar[dl]_{f_n} \\
            & \colim A_i \ar@{.>}[d]|-{\exists !h} & \\
            & \CO &
        } 
        $$</li>
</ol> 

## 2. Products and coproducts

&emsp; We call the limit over a diagram $$ F \colon \CI \to \cC $$ such that $$ \CI $$ has only identity morphisms 

$$
    \Hom_{\CI}(m, n) = 
    \begin{cases}
        \Id_A & \text{ if } m = n \\
        \varnothing & \text{ if } m \neq n
    \end{cases}
$$

a *product*, which is denoted

$$
    \prod A_i = \lim A_i.
$$

This is the same as choosing an indexed subset of objects $$ \{ A_i \} $$ in $$ \cC $$, such that the following diagram commutes:

$$ 
\xymatrix{ 
    & \CO \ar@{.>}[d]|-{\exists !h} \ar[dl]_{g_m} \ar[dr]^{g_n} & \\
    A_m & \prod A_i \ar[l]^{\pi_m} \ar[r]_{\pi_n} & A_n.
} 
$$

Here, we have replaced $$ f_m $$ with $$ \pi_m $$, which we call the *projection onto $$ A_m $$*.

&emsp; We likewise define define the coproduct as the colimit over diagrams with no morphisms, which we denote 

$$
    \coprod A_i = \colim A_i,
$$

This is equivalent to choosing an indexed subset of objects $$ \{ A_i \} $$ in $$ \cC $$, such that the following diagram commutes:

$$ 
\xymatrix{ 
    A_m \ar[dr]_{g_m} \ar[r]^{\iota_m} & \colim A_i \ar@{.>}[d]|-{\exists !h} & A_n \ar[dl]^{g_n} \ar[l]_{\iota_n} \\
    & \CO &
} 
$$

We call the maps $$ \iota_m $$ the *inclusion into $$ A_m $$*.

&emsp; The following table gives common names of products and coproducts in different categories. Note that for schemes only finite products and coproducts necessarily exist.

| Category | Product | Coproduct |
| :--------: | :-------: | :---------: |
| Sets | Cartesian product | Disjoint union |
| Groups | Direct product | Free product |
| Abelian groups | Direct product | direct sum |
| Rings | Direct product | Free product |
| Commutative rings | Direct product | Tensor product (over $$ \ZZ $$) |
| $$ R $$-modules | Direct product | Direct sum |
| $$ k $$-vector spaces | Direct product | Direct sum |
| Topological spaces | Box topology | Product topology |
| Pointed topological spaces | Box topology modulo basepoint | Wedge sum |
| Schemes | Fiber product (over $$ \ZZ $$) | Disjoint union | 


## 3. Partially Ordered Sets

&emsp; One of the most intuitively insightful categories to deal with is that induced by a poset, i.e. a partially ordered set, as in this case products and coproducts are simple the infimum and supremum. Recall that a set $$ P $$ equipped with a relation $$ \leq $$ is called *partially ordered* if it satisfies
<ol type="a" class="custom" style="list-style-position: outside">
    <li>\( x \leq x \),</li>
    
    <li>\( x \leq y \) and \(y \leq x \) implies \( x = y \), and</li> 
    
    <li>\( x \leq y \) and \( y \leq z \) implies \( x \leq z \).</li>
</ol> 

## 4. K-Theory

&emsp; Addition and coproducts


## 5. References

**FIX THESE**
1. Grothendieck, A. (1957), “Sur quelques points d’algèbre homologique”, *Tôhoku Mathematical Journal*. doi:10.2748/tmj/1178244839
2. Mac Lane, Saunders (September 1998). *Categories for the Working Mathematician. Graduate Texts in Mathematics*. Vol. 5 (Second ed.). Springer.