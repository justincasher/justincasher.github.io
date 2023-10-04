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
$$ \newcommand{\CH}{\mathcal{H}} \newcommand{\CL}{\mathcal{L}} \newcommand{\CO}{\mathcal{O}} \newcommand{\FF}{\mathbb{F}} \newcommand{\NN}{\mathbb{N}} \newcommand{\CC}{\mathbb{C}} \newcommand{\QQ}{\mathbb{Q}} \newcommand{\QQ}{\mathbb{Q}} \newcommand{\RR}{\mathbb{R}} \newcommand{\ZZ}{\mathbb{Z}} $$
$$ \DeclareMathOperator{\colim}{colim} \DeclareMathOperator{\Hom}{Hom} \DeclareMathOperator{\Id}{Id} \DeclareMathOperator{\im}{im} \DeclareMathOperator{\Isom}{Isom} \DeclareMathOperator{\Gal}{Gal} \DeclareMathOperator{\GL}{GL} \DeclareMathOperator{\Ob}{Ob} \DeclareMathOperator{\Res}{Res} \DeclareMathOperator{\sh}{sh} \DeclareMathOperator{\SL}{SL} \DeclareMathOperator{\Spec}{Spec} \DeclareMathOperator{\Sym}{Sym} $$
<br>

**Abstract.** &nbsp; We discuss some of the main tools used by Deligne in proving the Ramanujan conjecture. These are notes from a talk, so they skip many proofs.

## Table of Contents
1. [Modular Forms](#1-modular-forms)
2. [Ramanujan's Conjectures](#2-ramanujans-conjectures)
3. [Deligne's Proof](#3-delignes-proof)
4. [References](#4-references)


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

**Theorem 1.** &nbsp; *Let $$ f $$ be an eigenform of weight $$ k $$. Then its Dirichlet series factors as*

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

&emsp; These were conjectured in 1916. The first two relations were proved by Mordell in 1917 using Hecke operators. The third conjecture is what we are interested in and was proved by Deligne in 1971 (modulo the Weil conjectures). We will refer to this as "Ramanujan's conecture" in the sequel.


## 3. Deligne's Proof

#### Overview

&emsp; Let $$ D $$ denote the Dirichlet series associated to $$ \Delta $$. By Theorem 1,

$$
D(s)
= \prod_{p \text{ prime}} H_p(p^{-s})^{-1},
$$

where 

$$
H_p(z)
= 1 - \tau(p) z + p^{11} z^2.
$$

**Lemma 3.1.** &nbsp; *Ramanujan's conjecture is true if the roots of $$ H_p $$ are of absolute value $$ p^{11/2} $$.* 

*Proof.* We see $$ H_p $$ has roots

$$
\alpha_{\pm}
= \frac{\tau(p) \pm \sqrt{\tau(p)^2 - 4 p^{11}}}{2}
$$

Hence, if

$$
2 p^{11/2} = \left| \tau(p) \pm \sqrt{\tau(p)^2 - 4 p^{11}} \right|,
$$

choosing our sign $$ \pm $$ appropriately shows $$ \vert \tau(p) \vert \leq 2 p^{11/2}. $$ $$ \blacksquare $$

&emsp; In order to calculate the absolute value of these roots, we are going to define a Frobenious action on a $$ \QQ_\ell $$ vector space $$ _1^{10} W_{\ell} $$. Deligne proves 

$$ 
H_p(z) = \det(1-FX; \, _1^{10} W_{\ell}),
$$

and hence the roots of $$ H_p $$ are the eigenvalues of this action. Our result will then follow from the Riemann hypothesis of the Weil conjectures. 


#### The Shimura Isomorphism

&emsp; Let $$ S $$ be a complex analytic space. An *elliptic curve* on $$ S $$ is a map $$ f \colon E \to S $$ with a section $$ e \colon S \to E $$, such that the fibres of $$ f $$ are elliptic curves with origin given by $$ e $$. We say an isomorphism $$ R^1 f_* \underline{\ZZ} \to \underline{\ZZ}^2 $$ of sheaves on $$ S $$ is *permitted* if it induces -1 on the map 

$$ 
\bigwedge^2 R^1 f_* \underline{\ZZ} \to \bigwedge^2 \underline{\ZZ}^2.
$$

&emsp; Let $$ \Isom^+(\RR^2, \CC) $$ be the collection of $$ \RR $$-vector space isomorphisms which reverse the orientation, and set $$ X = \CC^* \backslash \Isom^+(\RR^2, \CC) $$. We can identify $$ X $$ with the upper half plane $$ \CH $$ by considering where $$ e_1, e_2 $$ are sent.

**Proposition 3.2.** &nbsp; *$$ X $$ represents the functor which sends an analytic space $$ S $$ to the isomorphism classes of elliptic curves on $$ S $$, equipped with a permitted isomorphism $$ R^1 f_* \underline{\ZZ} \cong \underline{\ZZ}^2 $$.*

&emsp; The set of isomorphism classes of elliptic curves corresponds to complex lattices up to homomthety, i.e. $$ \ZZ[a, b] \sim \ZZ[za, zb] $$ with $$ z \in \CC^{\times} $$, which correspond to elements in $$ X $$. We therefore construct a universal elliptic curve $$ f \colon E_X \to X $$ whose fibers consist of representatives from every isomorphism class of elliptic curves. 

&emsp; Set $$ \omega = f_* \Omega_{X/S} $$. We identify $$ R^1 f_* \underline{\RR} \otimes_{\RR} \CO_X $$ to the sheaf of relative de Rham cohomology of $$ E_X $$ over $$ X $$, and $$ \omega^{-1} $$ to $$ R^1 f_* \CO_X $$ by Poincaré duality. Then the Hodge decomposition

$$
\CH^1(Z) \cong \CH^0(Z, \Omega^1_Z) \oplus \CH^1(Z, \Omega^0_Z)
$$

yields a short exact sequence 

$$
0 \to \omega \to R^1 f_* \underline{\RR} \otimes_{\RR} \CO_X \to \omega^{-1} \to 0.
$$



**Theorem (Shimura Isomorphism).** &nbsp; *There exists an isomorphism $$ \sh $$, called the Shimura isomorphism, making the following diagram commute:* 

$$
\xymatrix{ 
    H^0(\overline{X}, \, \Omega^1 \otimes \omega^k) \oplus \overline{H^0(\overline{X}, \, \Omega^1 \otimes \omega^k)} \ar@{^{(}->}[d] \ar[r]^-\sh & \widetilde{H}^1(X, \, U^k \otimes \CC) \ar@{^{(}->}[d] \\
    H^0(X, \, \Omega^1 \otimes \omega^k) \oplus \overline{H^0(X, \, \Omega^1 \otimes \omega^k)}  \ar[r]^-{\sh_0} & \widetilde{H}^1(X, \, U^k \otimes \CC) 
} 
$$

#### Step 2

So we define 

$$
^{10}_1 W_{\ell}
= \widetilde{H}^1(M_n \otimes \overline{\QQ}, \, \Sym^k(R^1 f_{n *}(\underline{\QQ}_{\ell})))
$$

M_n is defined on page 151. 

and the Frobenious $$ F $$ as on page 161. 

In order to define the Frobenious, we must define $$ W^{(p)} $$.



## 4. References

1. Serge Lang, *Introduction to modular forms*, Springer-Verlag, 1976.
