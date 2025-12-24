---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /casas-alvero
title: The Casas-Alvero conjecture
date: "September 2023"
abstract: "The Casas-Alvero Conjecture asserts that if F(X) ∈ k[X], k is of characteristic 0, and F shares a root with each derivative F⁽ⁱ⁾, then F(X) = (x - α)ⁿ for some α ∈ k. We show that it is true for polynomials of degree n = pᵏ for p prime following [3]."
toc:
  - title: "Overview"
    anchor: "1-overview"
  - title: "Proof"
    anchor: "2-proof"
  - title: "References"
    anchor: "3-references"
---
</style>
<div style="display: none;">
$$
\newcommand{\cC}{\mathcal{C}}
\newcommand{\CD}{\mathcal{D}}
\newcommand{\CI}{\mathcal{I}}
\newcommand{\CO}{\mathcal{O}}
\newcommand{\FF}{\mathbb{F}}
\newcommand{\NN}{\mathbb{N}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\QQ}{\mathbb{Q}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\DeclareMathOperator{\colim}{colim}
\DeclareMathOperator{\gcd}{gcd}
\DeclareMathOperator{\Gr}{Gr}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Id}{Id}
\DeclareMathOperator{\Ob}{Ob}
\DeclareMathOperator{\Res}{Res}
\DeclareMathOperator{\Spec}{Spec}
$$
</div>

## 1. Overview

&emsp; Our goal is to prove the following conjecture when $ F $ is of degree $ n = p^k $ for $ p $ prime.

**Casas-Alvero Conjecture.** &nbsp; *Let $ F(X) \in k[X] $ for $ k $ of characteristic 0. If $ F $ shares a root with each derivative $ F^{(i)} $, then $ F(X) = (x - \alpha)^n $ for some $ \alpha \in k $.*

**Example 1.1.** &nbsp; This is from [\[2\]](#3-references). Consider $ F(X) = x^4 + X^2 + 2x $ in $ \FF_7[X] $. Then $ F'(X) = 4x^3 + 2x + 2 $ shares root $ 4 $ with $ F $, $ F''(X) = 5X^2 + 2 $ shares root $ 6 $, and $ F'''(X) = 3x $ shares root $ 0 $. But $ F(X) $ is not of the desired form.

&emsp; We can assume the following: (1) Dividing by the leading coefficient, we can assume $ F $ is monomial. Hence, 

$$
F(X) = \sum a_i X^i = X^n + a_{n-1} X^{n-1} + \cdots + a_1 X + a_0.
$$

(2) The $ i \text{th} $ *Hasse derivative* is given by $ H^i F(X) = F^{(i)}(X)/i! $. Since our field is of characteristic 0, we are going to assume that $ F $ shares a root with each $ H^i F $ for each $ 1 \leq i \leq n $. We can expand this as 

$$
H^i F(X) = {n \choose i} X^{n-i} + \cdots + {i+1 \choose i} a_{i+1} X + a_i.
$$

(3) Because $ H^{n-1} F $ is linear, we observe $ F $ has a zero $ \alpha $ in $ k $. Translating $ \alpha $ to 0 we can further assume $ a_0 = 0 $. Thus, we need to show that $ a_1 = \cdots = a_{n-1} = 0 $, allowing us to state our target theorem as follows:

**Theorem 1.2.** &nbsp; *Let $ F \in k[X] $ be a monic polynomial of degree $ n = p^k $ satisfying (1), (2), and (3) with $ k $ of characteristic zero. Then $ a_1 \cdots = a_{n-1} = 0 $.*


## 2. Proof

&emsp; In the sequel, we will write $ k $ for a field of characteristic zero. Let $ F, G \in k[X] $, $ F(X) = \sum a_i X^i $ and $ G(X) = \sum b_i X^i $, and $ \deg F = m $ and $ \deg G = n $. Recall that their resultant is defined as the determinant 

$$
\Res(F, G) =
{\begin{vmatrix}a_{m}&0&\cdots &0&b_{n}&0&\cdots &0\\a_{m-1}&a_{m}&\cdots &0&b_{n-1}&b_{n}&\cdots &0\\a_{m-2}&a_{m-1}&\ddots &0&b_{n-2}&b_{n-1}&\ddots &0\\\vdots &\vdots &\ddots &a_{m}&\vdots &\vdots &\ddots &b_{n}\\a_{0}&a_{1}&\cdots &\vdots &b_{0}&b_{1}&\cdots &\vdots \\0&a_{0}&\ddots &\vdots &0&b_{0}&\ddots &\vdots \\\vdots &\vdots &\ddots &a_{1}&\vdots &\vdots &\ddots &b_{1}\\0&0&\cdots &a_{0}&0&0&\cdots &b_{0}\end{vmatrix}}.
$$

Suppose $ F $ (resp. $ G $) has roots $ \alpha_i $ (resp. $ \beta_i $). Then we can rewrite the resultant as the product

$$
\Res(F, G)
= a_n^m b_m^n \prod_{i, j} (\alpha_i - \beta_j).
$$

In particular, $ F $ sharing a root with $ H^i F $ is equivalent to $ \Res(F, H^i F) = 0 $. 

&emsp; Setting 

$$ 
F = X^n + Y_{n-1} X^{n-1} + \cdots + Y_1 X,
$$

we can consider $ \Res(F, H^iF) $ as a polynomial map from $ \ZZ[X_1, \dots, X_{n-1}] $ to itself. Our problem then reduces to finding the zeroes of $ \Res(F, H^iF) $ in our field $$ k $$. We can rephrase this using a weighted projective scheme.

&emsp; Let $ (w_1, \dots, w_n) $ be an $ n $-tuple of positive integers and $ R $ be a commutative ring. Grade $ k[x_1, \dots, x_n] $ by setting $ x_i $ to be of weight (or degree) $ w_i $. We define *weighted projective space* as 

$$ 
\PP_R(w_1, \dots, w_n) = \text{Proj}(k[x_1, \dots, x_n])
$$

In classical terms, we are setting

$$
(x_0, \dots, x_n) \sim (\lambda^{w_1} x_1, \dots, \lambda^{w_n} x_n)
$$

with $ \lambda \in R $. For example, $ x_1^2 x_3 + x_2 $ is homogeneous of degree $ 4 $ in $ \PP_{\ZZ}(1, 4, 2) $.

&emsp; Consider the resultant $ \Res(F, H^i F) $ as a polynomial in the weighted projective space $ \PP_{\ZZ}(1, 2, \dots, n-1) $. Then it is homogeneous of degree $ n(n-i) $. Hence, the ideal 

$$
I_n = \left< \Res(F, H^iF) \mid 1 \leq i \leq n-1 \right>
$$

is homogeneous in $ \PP_{\ZZ}(1, 2, \dots, n-1) $. We define $ X_n $ to be the closed subscheme of $ \PP_{\ZZ}(1, 2, \dots, n-1) $ given by the sheaf of ideals $ I_n $.

&emsp; The $ k $-valued points $ X_n(k) $ correspond to monomials over $ k $ of degree $ n $ which share a root with each Hasse derivative. Since we want $ a_1 = \cdots = a_{n-1} = 0 $ and $ 0 $ is not a point in projective space, we have

**Lemma 2.1.** &nbsp; *The Casas-Alvero Conjecture is true for polynomials of degree $ n $ over $ k $ if and only if $ X_n(k) $ is empty.*

&emsp; The following lemma tells us it is enough to prove Theorem 1.2 for polynomials over $ \FF_p $ of degree $ n $.

**Lemma 2.2.** &nbsp; *If $ X_n(\FF_p) $ is empty for some $ p $, then $ X_n(k) $ is empty.*

*Proof.* Since $ k $ is of characteristic zero, $ \QQ $ is a subfield of $ k $. Hence if

$$
X_n(\QQ) = \Hom_{\ZZ}(\Spec \QQ, X_n) 
$$

is empty, then 

$$
X_n(k) = \Hom_{\ZZ}(\Spec k, X_n) 
$$

is empty as well. Thus, we have reduced ourselves to showing $ X_n(\QQ) $ is empty. 

&emsp; Consider the structure morphism $ \phi_n \colon X_n \to \ZZ $. Since 

$$
X_n(\FF_p) 
= \Hom_{\ZZ}(\Spec \FF_p, X_n) 
= \Hom_{\FF_p}(\Spec \FF_p, X_n \times \FF_p),
$$

we see $ X_n(\FF_p) $ being empty is equivalent to $ X_n \times \FF_p $ being empty. In particular, the fiber $ X_n \times \FF_p $ of $ \phi_n $ at $ p $ is empty, and therefore the subset 

$$ 
U = \ZZ \setminus \phi_n(X_n)
$$

is nonempty. Furthermore, $ X_n $ being projective implies it is proper, and so $ \phi_n $ has closed image. We conclude that $ U $ is a nonempty open subset of $ \ZZ $, meaning it contains $ (0) $. Thus, the fiber $ X_n \times \QQ $ is empty, meaning

$$
X_n(\QQ) 
= \Hom_{\QQ}(\Spec \QQ, X_n \times \QQ)
$$

is empty. $ \blacksquare $

**Lemma 2.3.** &nbsp; *Let $ n = p^k $ for $ p $ prime. Then for $ 1 \leq i \leq n-1 $ we have $ {n \choose i } \equiv 0 $ modulo $ p $.*

*Proof.* This is equivalent to showing $ v_p({n \choose i }) > 0 $. Indeed,

$$
\begin{aligned}
v_p \left({n \choose i} \right) & = v_p \left( \frac{n!}{i!(n-i)!} \right) \\
& = \sum_{h=1}^n v_p(h) - \sum_{h=1}^i v_p(h) - \sum_{h=1}^{n-i} v_p(h) \\
& = \sum_{h=n-i+1}^n v_p(h) - \sum_{h=1}^{n-i} v_p(h) \\
& = \sum_{h=1}^{n-i} v_p(h+i) - \sum_{h=1}^{n-i} v_p(h) \\
& = S_1 - S_2.
\end{aligned}
$$

Since $ S_1 $ contains $ v_p(n) = k $ and $ S_2 $ does not, it is not hard to see $ S_1 > S_2 $. $ \blacksquare $

&emsp; We now have the tools needed to prove Theorem 1.2.

*Proof (Theorem 1.2).* By Lemmas 2.1 and 2.2, we are reduced to proving the theorem for $ F(X) \in \FF_p[X] $ of degree $ n = p^k $. Recall 

$$
H^i F(X)
= {n \choose i} X^{n-i} + \cdots + {i+1 \choose i} a_{i+1} X + a_i.
$$

In particular, $ F $ shares a root with

$$
H^{n-1} F(X) 
= {n \choose n-1} X + a_{n-1}
= n X + a_{n-1}
= a_{n-1},
$$

but this is only possible if $ a_{n-1} = 0 $. Next, we observe $ F $ shares a root with

$$
H^{n-1} F(X) 
= {n \choose n-2} X^2 + {n-1 \choose n-2} a_{n-1} X + a_{n-2}.
$$

By Lemma 2.3 and since $ a_{n-1} = 0 $,

$$
H^{n-1} F(X) 
= a_{n-2},
$$

which implies $ a_{n-2} = 0 $. Proceeding by induction, we conclude $ a_1 = \cdots = a_{n-1} = 0 $. $ \blacksquare $

## 3. References

1. Eduardo Casas-Alvero, "Higher order polar germs", *Journal of Algebra* **240** (2001), no. 1, 326–337.
2. Jan Draisma and J. W. De Jong, "On the casas-alvero conjecture", 2011.
3. H.C. Graf von Bothmer, O. Labs, J. Schicho, and C. van de Woestijne, "The casas-alvero conjecture for infinitely many degrees", *Journal of Algebra* **316** (2007), no. 1, 224–230.
