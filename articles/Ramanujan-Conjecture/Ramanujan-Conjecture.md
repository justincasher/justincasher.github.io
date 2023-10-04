---
layout: Writing
indent: true
permalink: /Ramanujan-Conjecture
feedformat: card
title: The Ramanujan Conjecture
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
$$ \newcommand{\CH}{\mathcal{H}} \newcommand{\CL}{\mathcal{L}} \newcommand{\FF}{\mathbb{F}} \newcommand{\NN}{\mathbb{N}} \newcommand{\CC}{\mathbb{C}} \newcommand{\QQ}{\mathbb{Q}} \newcommand{\QQ}{\mathbb{Q}} \newcommand{\RR}{\mathbb{R}} \newcommand{\ZZ}{\mathbb{Z}} $$
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\im}{im} \DeclareMathOperator{\Ob}{Ob} \DeclareMathOperator{\Res}{Res} \DeclareMathOperator{\SL}{SL}  \DeclareMathOperator{\Spec}{Spec} $$
<br>

**Abstract.** &nbsp; We discuss some of the main tools used by Deligne in proving the Ramanujan conjecture.

## Table of Contents
1. [Modular Forms](#1-Modular Forms)
2. [Ramanujan's Conjectures](#2-ramanujans-conjectures)
3. [Deligne's Proof](#3-delignes-proof)
4. [References](#references)


## 1. Modular Forms

&emsp; See Lang's book [\[1\]](#4-references) for the details of this section. Let 

$$ 
\CH 
= \{ z \in \CC \mid \text{im} \, z > 0 \}
$$

denote the upper half complex plane. The group $$ \SL_2(\ZZ) $$ acts on $$ \CH $$ via Möbius transformations

$$
\gamma
=
\begin{bmatrix}
a & b \\
c & d 
\end{bmatrix}
\to 
\frac{az + b}{cz + d}.
$$

We denote this action by $$ \gamma(z) $$.

&emsp; A holomorphic function $$ f \colon \CH \to \CC $$ is called a *modular form of weight $$ k $$* if for any $$ \gamma \in \SL_2(\ZZ) $$,
<ol type="a" class="custom" style="list-style-position: outside">
  <li>\( f(\gamma(z) = (cz+d)^k f(z) \); and</li>
  
  <li>\( (cz+d)^{-k}f(\gamma(z)) \) remains bounded as \( \im(z) \) approaches infinity.</li>
</ol>
Condition (b) is equivalent to $$ f $$ having a $$ q $$-expansion at infinity. Additionally, we call $$ f $$ a *cusp form* if 

$$ 
\lim_{\im(z) \to \infty} (cz+d)^{-k} f(\gamma(z)) = 0.
$$

This is equivalent to $$ f $$ having constant term 0 in its $$ q $$ expansion. We denote the space of modular forms of weight $$ k $$ by $$ M_k $$, and of cusp forms by $$ S_k $$.

&emsp; We can consider modular forms as homogenious functions $$ F \colon \CL \to \CC $$ on complex lattices of degree $$ -k $$. Here, $$ \CL $$ is the space of complex lattices $$ \ZZ[a, b] $$ with $$ a, b \in \CC $$; and homogeneity means for $$ \lambda \in \CC^{\times} $$

$$
F(\lambda a, \lambda b)
= \lambda^{-k} F(a, b).
$$

The correspondence is given as follows. For $$ f $$ a modular form of weight $$ k $$, we set

$$ 
F(a, b) = b^{-k} F(a/b).
$$ 

Conversely, given such an $$ F $$, we set

$$ 
f(z) = F(z, 1).
$$ 

It is not hard to see these satisfy our desired properties.

&emsp; We define the $$ k $$th *Hecke operator* $$ T_k(N) \colon \CL \to \CL $$ by 

$$ 
T_k(n) F(L)
= n^{k-1} \sum_{[L : L'] = n} F(L'). 
$$

Using our correspondence, this is yields an operator $$ T_k(n) \colon M_k \to M_k $$. These satisfy $$ T_k(m) T_k(n) = T_k(mn) $$ for $$ m $$ and $$ n $$  coprime, and

$$
T_k(p^r) T_k(p)
= T_k(p^{r+1}) + p^{k-1} T_k(p^{r-1})
$$

for $$ p $$ prime.

&emsp; We say a modular form $$ f $$ of weight $$ k $$ is an *eigenform* if it is an eigenvector for every $$ T_k(n) $$. Suppose $$ f $$ has a $$ q $$-expansion 

$$ 
f(q) = \sum_{n=0}^{\infty} a_n q^n
$$ 

with $$ q= e^{2 \pi i z} $$. We can then attach a Dirichlet series to $$ f $$ by 

$$
D_f(s) = \sum_{n=1}^{\infty} a_n n^{-s}.
$$

If $$ f $$ is an eigenform this series factors.

**Theorem 1.** &nbsp; *Let $$ f $$ is an eigenform of weight $$ k $$. Then its Dirichlet series factors as*

$$
D_f(s) =
\prod_{p \text{ prime}} (1-a_p p^{-s} + p^{k-1-2s})^{-1}.
$$


## 2. Ramanujan's Conjectures

&emsp; Consider the space $$ M_{12} $$. It contains the cusp form

$$
\Delta(z)
= \sum_{n>0} \tau(n) q^n
= q \prod_{n > 0} (1-q^n)^{24},
$$ 

and since $$ M_{12} $$ is of dimension 1, $$ \Delta(z) $$ is an eigenform. The coefficient function $$ \tau \colon \NN \to \CC $$ is called the *Ramanujan tau function*. 

**Ramanujan Conjectures.** &nbsp; *The following should hold:*
<ol type="1" class="custom" style="list-style-position: outside">
  <li>\( \tau(m) \tau(n) = \tau(mn) \) for \( m \) and \( n \) coprime;</li>
  
  <li>\(\tau(p^r) \tau(p) = \tau(p^{r+1}) + p^{11} \tau(p^{r-1}) \) for \( p \) prime; and</li>
  
  <li>\( |\tau(p)| \leq 2 p^{11/2} \). </li>
</ol>

&emsp; The first two relations were proved by Mordell in 1917 using Hecke operators. The third conjecture is what we are interested in. Let $$ D $$ denote the Dirichlet series associated to $$ \Delta $$. Theorem 1 tells us

$$
D(s)
= \prod_{p \text{ prime}} H_p(p^{-s})^{-1},
$$

where 

$$
H_p(z)
= 1 - \tau(p) z + p^{11} z^2.
$$

We see $$ H_p $$ has roots

$$
\alpha_{\pm}
= \frac{\tau(p) \pm \sqrt{\tau(p)^2 - 4 p^{11}}}{2}
$$

&emsp; Ramanujan's third conjecture is follows from showing the roots of $$ H_p $$ being of absolute value $$ p^{11/2} $$. Indeed, use

$$
2 p^{11/2} = \left| \tau(p) \pm \sqrt{\tau(p)^2 - 4 p^{11}} \right|
$$

to bound $$ \mid \tau(p) \mid $$. We therefore would like to apply the Riemann hypothesis of the Weil conjectures to prove our hypothesis on the roots of $$ H_p $$.


## 3. Deligne's Proof

&emsp; 


## 4. References

1. Serge Lang, *Introduction to modular forms*, Springer-Verlag, 1976.
