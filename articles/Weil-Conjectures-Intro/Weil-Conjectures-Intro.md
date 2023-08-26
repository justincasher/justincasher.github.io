---
layout: Writing
indent: true
permalink: /Weil-Conjectures-Intro
feedformat: card
title: Motivating Schemes with the Weil Conjectures
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
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CD}{\mathcal{D}} \newcommand{\CI}{\mathcal{I}} \newcommand{\CO}{\mathcal{O}} \newcommand{\NN}{\mathbb{N}} \newcommand{\RR}{\mathbb{R}} \newcommand{\ZZ}{\mathbb{Z}} $$
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\Ob}{Ob} $$
<br>

**Abstract.** &nbsp; We define products and coproducts for arbitrary categories, then use them to define $$ K $$-theories. In particular, we discuss how the integers result from this construction, and we mention the Serre-Swan Theorem.

## Table of Contents
1. [Weil's Conjectures](#1-weil-conjectures)
2. [Lefschetz Theory](#2-lefschetz-theory)
3. [Étale Cohomology](#3-etale-cohomology)
4. [References](#4-references)


## 1. Weil's Conjectures

Write

$$
\zeta(z) = \sum_{n=1}^{\infty} \frac{1}{n^z}
$$

for the Riemann zeta function. It has the following properties:
<ol type="i" class="custom" style="list-style-position: outside">
    <li>The logarithmic derivative is \( \frac{d}{dz} \ln(\zeta(z)) = \sum_{n=1}^{\infty} \Lambda(n) n^{-z} \), where \( \Lambda(n) \) is the Von Mangoldt function which equals \( \ln p \) when \( n = p^q \) for some \( p \) and \( 0 \) elsewise.</li>
  
    <li>It satisfies the functional equation 
    
    \( 
    \zeta(z) = 2^{z} \pi^{z-1} \sin(\pi z/2) \Gamma(1-z) \zeta(1-z).
    \)

    </li>
  
    <li></li>
</ol>


## 2. Lefschetz Theory




## 3. Étale Cohomology




## 4. References

1. Alexander Grothendieck, *Sur quelques points d’algèbre homologique, I*, Tohoku Mathematical Journal **9** (1957), no. 2, 119–221.
2. Saunders Mac Lane, *Categories for the working mathematician*, Springer, 1978.
3. Archana S. Morye, *Note on the Serre-Swan theorem*, Mathematische Nachrichten **286** (2013), no. 2-3, 272–278.
4. Jean-Pierre Serre, *Vector bundles and projective modules*, Annals of Mathematics **61** (1955), no. 2, 197–278.
5. Richard Swan, *Vector bundles and projective modules*, Transactions of the American Mathematical Society **105** (1962), no. 2, 264–277.
