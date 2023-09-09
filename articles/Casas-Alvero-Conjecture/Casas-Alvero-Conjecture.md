---
layout: Writing
indent: true
permalink: /Casas-Alvero
feedformat: card
title: The Casas-Alvero Conjecture
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
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CD}{\mathcal{D}} \newcommand{\CI}{\mathcal{I}} \newcommand{\CO}{\mathcal{O}} \newcommand{\FF}{\mathbb{F}} \newcommand{\NN}{\mathbb{N}} \newcommand{\PP}{\mathbb{P}} \newcommand{\QQ}{\mathbb{Q}} \newcommand{\RR}{\mathbb{R}} \newcommand{\ZZ}{\mathbb{Z}} $$
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\gcd}{gcd} \DeclareMathOperator{\Gr}{Gr} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Ob}{Ob} $$
<br>

**Abstract.** &nbsp; The Casas-Alvero Conjecture asserts that if $$ F(X) \in k[X] $$, $$ k $$ is of characteristic 0, and $$ F $$ shares a root with each derivative $$ F^{(i)} $$, then $$ F(X) = (x - \alpha)^n $$ for some $$ \alpha \in k $$. We show that it is true for polynomials of degree $$ n = p^k $$ for $$ p $$ prime following [\[3\]](#3-references). 

## Table of Contents
1. [Overview](#1-overview)
2. [Proof](#2-main-proof)
3. [References](#3-references)


## 1. Overview

&emsp; Our goal is to prove the following conjecture when $$ F $$ is of degree $$ n = p^k $$ for $$ p $$ prime.

**Casas-Alvero Conjecture.** &nbsp; *Let $$ F(X) \in k[X] $$ for $$ k $$ of characteristic 0. If $$ F $$ shares a root with each derivative $$ F^{(i)} $$, then $$ F(X) = (x - \alpha)^n $$ for some $$ \alpha \in k $$.*

**Example.** &nbsp; This is from [\[2\]](#3-references). Consider (INSERT mod p case)

&emsp; We start by making some assumptions. (i) Dividing by the leading coefficient, we can assume $$ F $$ is monomial. Hence, 

$$
F(X) = \sum a_i X^i = X^n + a_{n-1} X^{n-1} + \cdots + a_1 X + a_0.
$$

(ii) The $$ i $$th *Hasse derivative* is given by $$ H^i F(X) = F^{(i)}(X)/i! $$. Since our field is of characteristic 0, we are going to assume that $$ F $$ shares a root with each $$ H^i F $$ for each $$ 1 \leq i \leq n $$. We can expand this as 

$$
H^i F(X) = {n \choose i} X^{n-i} + \cdots + {i+1 \choose i} a_{i+1} X + a_i.
$$

(iii) Because $$ H^{n-1} F $$ is linear, we observe $$ F $$ has a zero $$ \alpha $$ in $$ k $$. Translating $$ \alpha $$ to 0 we can further assume $$ a_0 = 0 $$. Thus, we need to show that $$ a_1 = \cdots = a_{n-1} = 0 $$. 

**Theorem.** &nbsp; *Let $$ F \in k[X] $$ be a monic polynomial satisfying (i), (ii), and (iii) with $$ k $$ of characteristic zero. Then $$ a_1 \cdots = a_{n-1} = 0 $$.*


## 2. Proof

&emsp; 


## 3. References

1. Eduardo Casas-Alvero, "Higher order polar germs", *Journal of Algebra* **240** (2001), no. 1, 326–337.
2. Jan Draisma and J. W. De Jong, "On the casas-alvero conjecture", 2011.
3. H.C. Graf von Bothmer, O. Labs, J. Schicho, and C. van de Woestijne, "The casas-alvero conjecture for infinitely many degrees", *Journal of Algebra* **316** (2007), no. 1, 224–230.
