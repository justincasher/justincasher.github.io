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
$$ \newcommand{\CB}{\mathcal{B}} \newcommand{\cC}{\mathcal{C}} \newcommand{\CO}{\mathcal{O}} \newcommand{\CV}{\mathcal{V}} $$ 
$$ \newcommand{\RR}{\mathbb{R}} $$
$$ \DeclareMathOperator{\CHom}{\mathcal{H}om}  $$
<br>

**Abstract.** These are solutions to some of the Indiana University analysis qualifying problems. They are indexed by "\[Year\] \[Semester\] \[Number\]". I also include in each section some theorems which might be useful.

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

*Proof.* Suppose not. Then there exists a sequence $$ \{x_n\} $$ such that the ball of radius $$ 1/n $$ at $$ x_n $$, i.e. $$ B(x_n, 1/n) $$ is not contained in any $$ U_{\alpha} $$. By Theorem 1.2, there exists a convergent subsequence $$ \{x_{n_i}\} $$. Consequently, for $$ N \gg 0 $$ large, we have $$ i > N $$ implies $$ x_{n_i} $$ is contained in some $$ U_{\alpha} $$. We conclude that for $$ i $$ large, we have  $$ B(x_i, 1/n_i) $$ is contained in $$ U_{\alpha} $$ as well, a contradiction. $$ \blacksquare $$

**2017 F P1.** &nbsp; *Let $$ X $$ be the set of sequences $$ \{ a_n \} $$ with $$ a_n \in \{0, 1\} $$. Equip $$ X $$ with the metric*

$$
d(\{a_n\}, \{b_n\}) = 
\begin{cases} 
    0 & \text{if } \{a_n\} = \{b_n\} \\
    2^{-m} & \text{if } m = \min\{n \mid a_n \neq b_n \}.
\end{cases}
$$

*(a) Prove $$ (X, d) $$ is compact, and (b) that there exists no isolated points.*

*Proof.* (a) Suppose not. By Theorem 1.2, there exists a sequence $$ \{s_{\ell}\} = \{ \{a_n\}_{\ell} \} $$ in $$ X $$ with no convergent subsequence. Further suppose $$ S $$ has no repeating values. Hence, for each term $$ s_{\ell} $$, there exists a $$ N_{\ell} > 0 $$ such that $$ B(s_{\ell}, 2^{-N_{\ell}) $$ contains no other elements from our sequence. But 

$$ 
s_1, \dots, s_{2^{N_{\ell}}+1} 
$$ 

cannot have pairwise distinct first $$ N_{\ell} $$ terms by the pigeon-hole principle, a contradiction.

(b) Suppose $$ \{an\} $$ is an isolated point. Then there exists an $$ N \gg 0 $$ with $$ B(\{a_n\}, 2^{-N}) $$ only containing $$ \{a_n\} $$. But

$$
b_n = 
\begin{cases}
    a_n & \text{if } n \leq N \\
    1-a_n & \text{if } n > N
\end{cases}
$$

is an element of $$ X $$ distinct from $$ \{a_n\} $$ contained in $$ B(\{a_n\}, 2^{-N}) $$. $$ \blacksquare $$

**2014 F P2.** &nbsp; *Let $$ K $$ be a compact subset of $$ \RR^n $$, and let $$ f \colon K \to \RR $$ be continuous. Prove that there exists an $$ M \geq 0 $$ such that for all $$ x, y \in K $$,*

$$
\|f(x)-f(y)\| \leq M \|x-y\| + \varepsilon.
$$

*Show this is not necessarily true for $$ \varepsilon = 0 $$.*

*Proof.* By continuity, there exists a $$ \delta > 0 $$ such that $$ \|x-y\| < \delta $$ implies $$ \|f(x) - f(y)\| \leq \varepsilon $$; consequently, we can assume $$ \|x-y\| \geq \delta $$. Then the Heinel-Borel Theorem and 2019 F P5 show that $$ K $$ and $$ f(K) $$ are bounded, i.e. $$ \|f(x) - f(y)\| < C $$ for a fixed $$ C $$. Consequently, 

$$
\|f(x) - f(y) \| \leq C/\delta \|x-y\| + \varepsilon,
$$

and we set $$ M = C/\delta $$.

For a counterexample, consider $$ f \colon [0, 1] \to [0, 1] $$ with $$ f(x) = \sqrt{x} $$. We see $$ \lim_{x \to 0^+} f'(x) = \infty $$ implies no such $$ M $$ exists. $$ \blacksquare $$.



## 2. Sequences and Series

**Monotone Convergence Theorem.** &nbsp; *Let $$ \{a_n\} $$ be a monotonically increasing sequence in $$ \RR $$. Then $$ \{a_n\} $$ has a limit if and only if it is bounded.*

**Theorem 2.1.** &nbsp; *In $$ \RR^n $$ every Cauchy sequence convergences, i.e. it is a complete metric space.*

**Ratio Test.** &nbsp; *Let $$ \sum a_n $$ be a series in $$ \RR $$. Write $$ L = \lim_n \|a_{n+1}/a_n\| $$. Then $$ L < 1 $$ implies absolute convergence; $$ L > 1 $$ implies divergence; and $$ L = 1 $$ is inconclusive.*


## 3. Uniform Continuity


## 4. Uniform Convergence


## 5. Derivatives


## 6. Optimization


## 7. Integration


## 8. Convergence of Integrals


## 9. Polynomials and Stone-Weierstrass



## 10. Stoke's Theorem




## 11. Implicit Functin Theorem


