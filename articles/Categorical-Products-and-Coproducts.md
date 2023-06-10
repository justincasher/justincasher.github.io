---
layout: Writing
indent: true
permalink: /Categorical-Products-and-Coproducts
feedformat: card
title: Categorical Products and Coproducts
---
<style>
    ol {
        list-style-position: outside;
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
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\Ob}{Ob} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} $$
<br>
## Table of Contents
1. [Limits and Colimits](#1-limits-and-colimits)
2. [Applications to Sets](#2-applications-to-sets)
3. [K-Theory](#3-k-theory)
4. [References](#4-references)

## 1. Limits and Colimits

&emsp; A *category* $$ \cC $$ is a class of objects $$ \Ob(\cC) $$ and a class of morphisms $$ \Hom(\cC) $$ equipped with a composition law, so that for any $$ A, B, C \in \Ob(\cC), $$ we have the following: 
<ol type="a" style="list-style-position: outside">
  <li>An associative composition operator $$ \circ \colon \Hom(B, C) \times \Hom(A, B) \to \Hom(A, C); $$</li>
  <li>Local identities \( \Id_A \colon A \to A \), such that for any \( f \colon A \to B \), we get \( f \circ \Id_A = f \) and \( \Id_B \circ f = f \).</li>
</ol> 

&emsp; We define maps between categories $$ F \colon \cC \to \CD $$ on the level of pairs 

$$ 
    F \colon (\Ob(\cC), \Hom(\cC)) \to (\Ob(\CD), \Hom(\CD)),
$$

meaning each object (resp. morphism) in $$ \cC $$ is mapped to an object (resp. morphism) in $$ \CD $$. We call $$ F $$ a *functor* if it preserves the composition operator $$ F(f \circ g) = F(f) \circ F(g) $$ and local identities $$ F(\Id_A) = \Id_{F(A)} $$.

**Remark.** When working with categories, we are interested in when a morphism factors through another one. Intuitively, this abstracts the notion of integers dividing each another, and it leads to the notion of categorical limits and colimits. 

&emsp; Let $$ F \colon \CI \to \cC $$ be a functor. Here, we call $$ F $$ a *diagram* and $$ \CI $$ the *indexing category*. We denote an object in the image of $$ F $$ by $$ F(i) = A_i $$. The *limit* of $$ F $$ is then an object $$ \lim A_i $$ in $$ \cC $$ equipped with a morphism

$$ 
f_m \colon \lim A_i \to A_m 
$$ 

for each $$ m \in \CI $$, such that:
<ol type="a">
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
<ol type="a">
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




## 3. Applications to Sets

&emsp; One of the most intuitively insightful categories to deal with is that induced by a poset, i.e. partially ordered set.


## 4. K-Theory

&emsp; Addition and coproducts


## 5. References

1. Include Grothendieck's Tohoku
2. MacLane Categories
