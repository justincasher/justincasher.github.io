---
layout: Writing
indent: true
permalink: /IU-Analysis-Qualifying-Solutions
feedformat: card
title: IU Analysis Qualifying Solutions
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
$$ \newcommand{\fa}{\mathfrak{a}} \newcommand{\fm}{\mathfrak{m}} \newcommand{\fp}{\mathfrak{p}} $$
$$ \newcommand{\cC}{\mathcal{C}} \newcommand{\CO}{\mathcal{O}} \newcommand{\CV}{\mathcal{V}} $$ 
$$ \newcommand{\RR}{\mathbb{R}} $$
$$ \DeclareMathOperator{\CHom}{\mathcal{H}om}  $$
<br>

**Abstract.** These are solutions to some of the Indiana University analysis qualifying problems. They are indexed by "\[Year\] \[Semester\] \[Number\]".

## Table of Contents
1. [Compact Spaces](#1-compact-spaces)
2. [Zariski Topology](#2-zariski-topology)
3. [Schemes](#3-schemes)
4. [References](#4-references)

## 1. Compact Spaces 

Fix a topological space $$ X $$. We say $$ X $$ is compact if every open cover $$ \{U_{\alpha}\} $$ of $$ X $$ admits a finite subcover $$ U_1, \dots, U_n $$. 

**Heine-Borel Theorem.** &nbsp; *Let $$ X $$ be a subset of $$ \RR^n $$. Then $$ X $$ is compact with respect to the Euclidean metric if and only if $$ X $$ is closed and bounded.*

**Proposition 1.1.** &nbsp; *Let $$ X $$ be a topological space. Then $$ X $$ is compact if and only if there exists a subbase $$ \CB $$ of $$ X $$ such that every open cover by elements of $$ \CB $$ admits a finite subcover.*

**Theorem 1.2.** &nbsp; *Let $$ X $$ be a metric space. Then $$ X $$ is compact if and only if every sequence in $$ X $$ has a convergent subsequence.*

**2019 F P5.** &nbsp; *Let $$ f \colon \RR^n \to \RR^m $$ be continuous ($$ n, m < \infty $$), and let $$ K \subseteq \RR^n $$ be compact. Show $$ f(K) $$ is compact.*

*Proof.* We show this holds for any $$ f \colon X \to Y $$ continuous. Let $$ \{U_{\alpha}\} $$ cover $$ f(K) $$. Then $$ \{f^{-1}(U_{\alpha})\} $$ forms an open cover of $$ K $$ by (the topological definition of) continuity, and hence admits a finite subcover $$ f^{-1}(U_1), \dots, f^{-1}(U_n) $$. We conclude that $$ U_1, \dots, U_n $$ cover $$ f(K) $$. $$ \blacksquare $$ 

*Alternative proof.* Let $$ \{ y_n \} $$ be a sequence in $$ f(K) $$. Then it lifts to a (not necessarily unique) sequence $$ \{x_n\} $$ in $$ K $$, i.e. $$ f(x_n) = y_n $$. By Theorem 1.2, this sequence has a convergence subsequence $$ \{x_{n_i}\} $$, whose image $$ \{ y_{n_i} \} $$ is a convergent subsequence of $$ \{ y_n \} $$ by continuity, i.e. $$ \lim_i f(x_{n_i}) = f(\lim_i x_{n_i}) $$. $$ \blacksquare $$.

**2019 W P2.** &nbsp; *Let $$ X $$ be a compact metric space with open cover $$ \{U_{\alpha}\} $$. Show that for some $$ \varepsilon > 0 $$ every ball of radius $$ \varepsilon $$ is contained in some $$ U_{\alpha} $$.*

*Proof.* 




## 2. Sequences and Series


## 3. Uniform Continuity


## 4. Uniform Convergence


## 5. Derivatives


## 6. Optimization


## 7. Integration


## 8. Convergence of Integrals


## 9. Polynomials and Stone-Weierstrass



## 10. Stoke's Theorem




## 11. Implicit Functin Theorem


