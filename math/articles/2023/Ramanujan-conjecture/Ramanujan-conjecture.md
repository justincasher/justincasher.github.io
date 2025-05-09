---
layout: Math
indent: true
permalink: /ramanujan-conjecture
feedformat: card
title: The Ramanujan conjecture
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
<br>
**Abstract.** &nbsp; We discuss some of the main tools used by Deligne in proving the Ramanujan conjecture. These are notes from a talk, so I do not include most proofs. For a more comprehensive treatment see [\[1\]](#4-references).




## Table of Contents
1. [Modular forms and Hecke operators](#1-modular-forms-and-hecke-operators)
2. [Ramanujan's conjectures](#2-ramanujans-conjectures)
3. [Deligne's proof](#3-delignes-proof)
4. [References](#4-references)




## 1. Modular forms and Hecke operators


&emsp; See Lang's book, [\[4\]](#4-references), for the details of this section. Let $ k $ be a field, and let $ E $ be a $ k $-variety. The following are equivalent:

1.  $ E $ is an abelian variety of dimension 1 over $ k $;

2.  $ E $ is a smooth, projective curve of genus one with a choice of origin;

we refer to such $ E $ as being *elliptic*.


&emsp; We call a discrete additive subgroup $ L $ of $ k $ a *lattice*. There exists an additive isomorphism of $ L $ with $ \mathbb{Z}^n $; we call $ n $ the *rank* of our lattice. 


&emsp; Assume $ L $ is a complex lattice of rank 2, which we write 

$$
L = \left< w_1, w_2 \right> = \left< a_1 w_1 + a_2 w_2 \mid a_i \in \mathbb{Z} \right>
$$

with $ w_2 / w_1 \in \mathcal{H} $ and $ \mathcal{H} $ the upper-half plane. The quotient $ \mathbb{C}/L $ is an abelian variety of dimension 1 over $ \mathbb{C} $; hence, an elliptic curve. Every complex elliptic curve arises in this manner, and there is a bijection between isomorphism classes of elliptic curves and lattices up to homothety. (This is not true for higher dimensional complex abelian varieties.) In the sequel, we let $ \mathcal{L} $ denote the free abelian group generated by complex lattices of rank 2 (i.e. elliptic curves).


&emsp; Elements of the modular group $ \gamma \in \text{SL}_2(\mathbb{Z}) $ act on $ \mathcal{H} $ by fractional linear transformations; meaning for $ z \in \mathcal{H} $ and

$$
\gamma = \begin{bmatrix} a & b \\ c & d \end{bmatrix}, \text{ we put }
\gamma(z) = \frac{az + b}{cz + d}.
$$


&emsp; A holomorphic function $ f \colon \mathcal{H} \to \mathbb{C} $ is called a *modular form of weight $ k $* if, for any $ \gamma \in \text{SL}_2(\mathbb{Z}) $, 

$$ 
f(\gamma(z)) = (cz+d)^k f(z),
$$

and $ f(z) $ remains bounded as $ \text{im}(z) $ approaches infinity. Equivalently, we define modular forms as homogeneous functions $ F \colon \mathcal{L} \to \mathbb{C} $ of degree $ -k $; meaning, for $ \lambda \in \mathbb{C}^{\times} $,

$$
F(\lambda w_1, \lambda w_2)
= \lambda^{-k} F(w_1, w_2).
$$

Indeed, given a modular form $ f $ of weight $ k $, we put

$$ 
F(a, b) = b^{-k} f(a/b),
$$ 

and given a homogeneous function $ F $ of weight $ -k $, we put

$$ 
f(z) = F(z, 1).
$$ 

This correspondence is bijective, and we denote our spaces of modular forms by $ f \in M_k $ and $ F \in M_k^{\mathcal{L}} $; put $ M_* = \bigoplus M_k $ and $ M_*^{\mathcal{L}} = \bigoplus M_k^{\mathcal{L}} $. We define the Hecke algebra on these spaces as follows.


&emsp; (*$ \mathcal{H} $ point de vue*) Put $ \Gamma = \text{SL}_2(\mathbb{Z}) $. Define $ H_k $ to be the free abelian group with basis elements double cosets $ \Gamma \alpha \Gamma $ where $ \alpha \in M_2^+(\mathbb{Z}) $, the plus meaning positive determinant. Take coset decompositions 

$$ 
x = \Gamma \alpha \Gamma = \coprod_{i=1}^A \Gamma \alpha_i, 
\qquad y = \Gamma \beta \Gamma = \coprod_{j=1}^B \Gamma \beta_j, 
$$

and $ z = \Gamma \xi \Gamma $, then set 

$$
x \cdot y
= \sum_{z \subseteq \Gamma \alpha \Gamma \beta \Gamma} m(x \cdot y, z) z
$$

(summing over all cosets $ z $ contained in $ \Gamma \alpha \Gamma \beta \Gamma $), where 

$$
m(x \cdot y, z)
= \text{Card}\{ (i, j) \mid \Gamma \alpha_i \beta_j = \Gamma \zeta \};
$$

this product is independent of our coset representatives, and it is associative and commutative; we extend it $ \mathbb{Z} $-linearly to define multiplication on $ H $. (Observe multiplication here is a type of convolution.) We call $ H $ the *Hecke algebra*. 


&emsp; $ H $ can be considered a subalgebra of $ \text{End}(M_*) $, and hence $ M $ a left $  H $-module, by the action on $ f \in M_k $

$$
\Gamma \alpha \Gamma \cdot f(z)
= \det(\alpha)^{k-1} \sum_{i=1}^A j(\alpha_i, z)^{-k} f(\alpha_i(z)),
$$

We define the $ n $-th *Hecke operator* as the coset

$$
T_n = 
\Gamma
\begin{bmatrix} 
    n & 0 \\
    0 & 1
\end{bmatrix}
\Gamma
$$

$ H $ is generated by the $ T_n $. (This is the simplest matrix of determinant $ n $.)


&emsp; (*Measure point de vue*) Let 

$$
\varphi \colon \text{SL}_2(\mathbb{Z}) \backslash \text{M}_2^+(\mathbb{Z}) / \text{SL}_2(\mathbb{Z}) \to \mathbb{Z}
$$

be a continuous function with compact support; assuming the left hand side is equipped with the discrete topology, this reduces to saying $ \varphi $ is supported on finitely many cosets. Write $ H^{\mathcal{M}} $ for the set of all such $ \varphi $. Let multiplication on $ H^{\mathcal{M}} $ be the convolution

$$
(\varphi_1 \ast \varphi_2)(x) 
= \int_{\text{SL}_2(\mathbb{Z}) \backslash \text{M}_2^+(\mathbb{Z}) / \text{SL}_2(\mathbb{Z})} \varphi_1(y) \varphi_2(y^{-1} x) dy,
$$

where every $ y $ is a point mass of volume 1. We call $ H^{\mathcal{M}} $ the *Hecke algebra*. 


&emsp; Each $ \varphi \in H^{\mathcal{M}} $ acts on $ f \in M_k $ by

$$
\varphi \cdot f
= \int_{\text{SL}_2(\mathbb{Z}) \backslash M_2^+(\mathbb{Z})} \det(g)^{k-1} j(g, z)^{-k} f(g(z)) \varphi(g) dg
$$

(with the same measure). In particular, the $ n $-th Hecke opeartor $ T_n^{\mathcal{M}} $ is the characteristic function on the coset of $ T_n $ above.


&emsp; (*Lattice point de vue*) We define the $ n $-th *Hecke operator* $ T_n^{\mathcal{L}} \in \text{End}(M_k^{\mathcal{L}}) $ by

$$ 
T_n^{\mathcal{L}} F(L)
= n^{k-1} \sum_{[L : L'] = n} F(L');
$$

note that again the action depends on the weight $ -k $ of $ F $. We call the subalgebra $ H^{\mathcal{L}} $ of $ \text{End} (M^{\mathcal{L}}_{\ast}) $ generated by the $ T_n^{\mathcal{L}} $ the *Hecke algebra*. These satisfy 

$$
T_k(m) T_k(n) = T_k(mn) 
$$

for $ m $ and $ n $  coprime, and

$$
T_k(p^r) T_k(p)
= T_k(p^{r+1}) + p^{k-1} T_k(p^{r-1})
$$

for $ p $ prime.

 
**Theorem 1.** &nbsp; $ T_n f(z) = T_n^{\mathcal{M}} = T_n^{\mathcal{L}} F(z, 1) $. 


&emsp; The first equality follows by definition. Put $ L = \left< z, 1 \right> $. Any index $ n $ sublattice $ L' $ of $ L $ is given by a $ \mathbb{Z} $-linear transformation $ M \colon L \to L' $ with $ \det M = n $. Since $$ \text{SL}_2(\mathbb{Z}) $$ is the kernel of the determinant, we have a bijection between isomorphism classes of index $ n $ sublattices and $$ M_n^+(\mathbb{Z})/\text{SL}_2(\mathbb{Z}) $$. Writing $ \Gamma T_n \Gamma = \coprod_{i=1}^N \Gamma t_i $, it then follows immediately that

$$
T_n f(z) = n^{k-1} \sum_{i=1}^N f(t_i(z)) = n^{k-1} \sum_{[L : L'] = n} F(L) = T_n^{\mathcal{L}} F(L).
$$

Q.E.D.


&emsp; We say a modular form $ f $ of weight $ k $ is an *eigenform* if it is an eigenvector for every $ T_k(n) $. Suppose $ f $ has a $ q $-expansion 

$$
f(q) = \sum_{n=0}^{\infty} a_n q^n
$$

with $ q= e^{2 \pi i z} $. We can then attach a Dirichlet series to $ f $ by 

$$
D_f(s) = \sum_{n=1}^{\infty} a_n n^{-s}.
$$

If $ f $ is an eigenform this series factors.


**Theorem 1.** &nbsp; *Let $ f $ be an eigenform of weight $ k $. Then its Dirichlet series factors as*

$$
D_f(s) =
\prod_{p \text{ prime}} (1-a_p p^{-s} + p^{k-1-2s})^{-1}.
$$




## 2. Ramanujan's conjectures


&emsp; Consider the space $ S_{12} $. It contains the cusp form

$$
\Delta(z)
= \sum_{n>0} \tau(n) q^n
= q \prod_{n > 0} (1-q^n)^{24},
$$

and since $ S_{12} $ is of dimension 1, $ \Delta(z) $ is an eigenform. The coefficient function $ \tau \colon \mathbb{N} \to \mathbb{C} $ is called the *Ramanujan tau function*. 


**Ramanujan Conjectures.** &nbsp; *The following should hold:*
<ol type="1" class="custom" style="list-style-position: outside">
  <li>\( \tau(m) \tau(n) = \tau(mn) \) for \( m \) and \( n \) coprime;</li>
  
  <li>\(\tau(p^r) \tau(p) = \tau(p^{r+1}) + p^{11} \tau(p^{r-1}) \) for \( p \) prime; and</li>
  
  <li>\( |\tau(p)| \leq 2 p^{11/2} \). </li>
</ol>


&emsp; These were conjectured in 1916. The first two relations were proved by Mordell in 1917 using Hecke operators. The third conjecture is what we are interested in and was proved by Deligne in 1971 (modulo the Weil conjectures). We will refer to this as "Ramanujan's conecture" in the sequel.




## 3. Deligne's proof



#### Overview


&emsp; Let $ D $ denote the Dirichlet series associated to $ \Delta $. By [theorem 1](https://www.justinasher.me/ramanujan-conjecture-t1){:target="_blank"},

$$
D(s)
= \prod_{p \text{ prime}} H_p(p^{-s})^{-1},
$$

where 

$$
H_p(z)
= 1 - \tau(p) z + p^{11} z^2.
$$


**Lemma 3.1.** &nbsp; *Ramanujan's conjecture is true if the roots of $ H_p $ are of absolute value $ p^{11/2} $.* 

*Proof.* We see $ H_p $ has roots

$$
\alpha_{\pm}
= \frac{\tau(p) \pm \sqrt{\tau(p)^2 - 4 p^{11}}}{2}
$$

Hence, if

$$
2 p^{11/2} = \left| \tau(p) \pm \sqrt{\tau(p)^2 - 4 p^{11}} \right|,
$$

choosing our sign $ \pm $ appropriately shows $ \vert \tau(p) \vert \leq 2 p^{11/2}. $ Q.E.D.


&emsp; In order to calculate the absolute value of these roots, we are going to define a Frobenious action on a $$ \mathbb{Q}_\ell $$ vector space $$ {_1^{10}} W_{\ell} $$. Deligne proves 

$$
H_p(z) = \det(1-Fz; \, {_1^{10}} W_{\ell}),
$$

and hence the roots of $ H_p $ are the eigenvalues of this action. Our result will then follow from Deligne's second paper on the Weil conjectures. 



#### The Shimura isomorphism


&emsp; Let $ S $ be a complex analytic space. An *elliptic curve* over $ S $ is a map $ f \colon E \to S $ with a section $ e \colon S \to E $, such that the fibers of $ f $ are elliptic curves with origin given by $ e $. 


&emsp; We say an isomorphism $ R^1 f_* \underline{\mathbb{Z}} \to \underline{\mathbb{Z}}^2 $ of sheaves on $ S $ is *permitted* if it induces -1 on the map 

$$
\bigwedge^2 R^1 f_* \underline{\mathbb{Z}} \to \bigwedge^2 \underline{\mathbb{Z}}^2.
$$

Let $ \text{Isom}^+(\mathbb{R}^2, \mathbb{C}) $ be the collection of $ \mathbb{R} $-vector space isomorphisms which reverse the orientation, and set 

$$
X = \mathbb{C}^* \backslash \text{Isom}^+(\mathbb{R}^2, \mathbb{C}). 
$$

We can identify $ X $ with the upper half plane $ \mathcal{H} $ by considering where $ e_1 = (1, 0) $ and $ e_2 = (0, 1) $ are sent, i.e. $ f(e_2)/f(e_1) $.


**Proposition 3.2.** &nbsp; *$ X $ represents the functor which sends an analytic space $ S $ to the isomorphism classes of elliptic curves on $ S $, equipped with a permitted isomorphism $$ R^1 f_* \underline{\mathbb{Z}} \cong \underline{\mathbb{Z}}^2 $$.*


&emsp; The set of isomorphism classes of elliptic curves corresponds to complex lattices up to homothety, i.e. $ \mathbb{Z}[a, b] \sim \mathbb{Z}[za, zb] $ with $ z \in \mathbb{C}^{\times} $, which correspond to elements in $ X $ modulo $ \text{SL}_2(\mathbb{Z}) $ (identify $ X $ with $ \mathcal{H} $ and consider $ b/a $). We therefore construct a "universal elliptic curve" $ f \colon E_X \to X $ whose fibers consist of representatives from each isomorphism class of elliptic curves. 


&emsp; Let $ \Gamma $ be a discrete subgroup of $ \text{SL}_2(\mathbb{Z}) $ without torsion elements such that $ X/\Gamma $ has finite volume (with respect to the Poincaré metric). We can identify $ X/\Gamma $ to a smooth projective curve $ \overline{X/\Gamma} $ minus a finite number of points.


&emsp; One of the main ideas of Deligne's paper is to use a cohomological description of cusp forms. We define a cusp form of weight $ k $ with respect to $ \Gamma $ by 
<ol type="a" class="custom" style="list-style-position: outside">
  <li>for any \( \gamma \in \Gamma \) we have \( f(\gamma(z)) = (cz+d)^k f(z) \); and</li>
  
  <li>for any \( \gamma \in \text{SL}_2(\mathbb{Z}) \) we have \( (cz+d)^{-k} f(\gamma(z)) \to 0 \) as \( \text{im}(z) \to \infty \).</li>
</ol>
We denote the resulting space $ S_k(\Gamma) $. 


&emsp; Alternatively, we see for $ \gamma \in \text{SL}_2(\mathbb{Z}) $, 

$$
\frac{d \gamma(z)}{dz}
= (cz+d)^{-2}.
$$

Hence, the condition 

$$
f(\gamma(z)) = (cz+d)^{2k} f(z) 
$$

is equivalent to 

$$
f(\gamma(z)) d\gamma(z)^k = f(z) dz^k.
$$

In other words, we are interested in the holomorphic differential forms $ f(z) dz^k $ of weight $ k $ invariant under $ \Gamma $. This can be achieved by taking sections of powers of the pushforward $ \omega = f_* \Omega_{E_X/X} $ and prolonging $ \omega $ to $ \overline{X/\Gamma} $. Deligne then identifies $ \Omega_X^1 $ with $ \omega^2 $ and, with additional proof, gets the following:


**Proposition 3.3.** &nbsp; *$ S_{k+2}(\Gamma) $ can be identified with $ H^0(\overline{X/\Gamma}, \Omega_X^1 \otimes \omega^k) $.*


&emsp; Using this theorem, we can then identify cusp forms with the first reduced cohomology group of the symmetric power of a local system on $ \overline{X/\Gamma} $ tensored over $ \mathbb{C} $. We will not explicitely construct this map since we will only be using its existence.


**Theorem (Shimura isomorphism).** &nbsp; *There exists an isomorphism*

$$
S_{k+2}(\Gamma) \oplus \overline{S_{k+2}(\Gamma)} \cong \widetilde{H}^1(\overline{X/\Gamma}, \, \text{Sym}^k(R^1 f_* \underline{\mathbb{Z}})) \otimes_{\mathbb{Z}} \mathbb{C}.
$$



#### Full level $ n $ structures


&emsp; We would like to emulate [proposition 3.2](https://www.justinasher.me/ramanujan-conjecture-p3:2){:target="_blank"} in the case of schemes. An *elliptic curve* over a scheme $ S $ is a proper smooth morphism $ f \colon E \to S $ whose fibers are geometrically connected curves of genus 1, equipped with a section $ e \colon S \to E $. In what follows, we will assume that $ S $ is of characteristic 0, meaning each $ s \in S $ satisfies $ \text{char} k(s) = 0 $. 


&emsp; Let $ \Gamma(n) $ be the elements $ \gamma \in \text{SL}_2(\mathbb{Z}) $ such that $ \gamma \equiv \text{Id} $ modulo $ n $, i.e.

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\equiv
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
\quad \text{modulo } n
$$

or $ a \equiv d \equiv 1 $ and $ b \equiv c \equiv 0 $ modulo $ n $. Define $ M_n $ to be $ X/\Gamma(n) $ considered as a complex algebraic variety; and let $ M_n^{\text{an}} $ be $ X/\Gamma(n) $ considered as a complex analytic space.


**Proposition 3.4.** &nbsp; *For $ n \geq 3 $, $ M_n $ (resp. $ M_n^{\text{an}} $) represents the functor which sends a scheme $ S $ of characteristic 0 (resp. an analytic space) to the isomorphism classes of elliptic curves $ E $ on $ S $, equipped with an isomorphism $ \alpha \colon E_n \to (\mathbb{Z}/n\mathbb{Z})^2 $.*


&emsp; Write $ f_n \colon E \to M_n $ for the universal elliptic curve on $ M_n $ (or $ M_n^{\text{an}} $) for $ n \geq 3 $. Fix an algebraic closure $ \overline{\mathbb{Q}} $ of $ \mathbb{Q} $. We define 

$$
\begin{aligned}
_n^k W & = \widetilde{H}^1(M_n^{\text{an}}, \, \text{Sym}^k(R^1 f_{n*}(\underline{\mathbb{Q}}))) \\
_n^k W_{\ell} & = \widetilde{H}^1(M_n \otimes \overline{\mathbb{Q}}, \, \text{Sym}^k(R^1 f_{n*}(\underline{\mathbb{Q}}_{\ell}))),
\end{aligned}
$$

and 

$$
^kW = \lim_{n \to} {_n^k W}, \qquad 
{^k W_{\ell}} = \lim_{n \to} {_n^k W_{\ell}},
$$

which satisfy $ {^k W_{\ell}} = {^k W} \otimes \mathbb{Q}_{\ell} $.


&emsp; Setting $ ^kW_{\infty} = {^k W} \otimes \mathbb{C} $, the Shimura isomorphism implies

$$
\begin{aligned}
^k W_{\infty} & = \lim_{n \to} S_{k+2}(\overline{M_n^{\text{an}}}) \oplus \overline{S_{k+2}(\overline{M_n^{\text{an}}})}.
\end{aligned}
$$

Defining $ _1^k W = {_n^k W^{\text{GL}_2(\mathbb{Z}/n\mathbb{Z})}} $, Deligne shows

$$
_1^k W_{\infty}
= _1^k W \otimes \mathbb{C}
\cong S_{k+2} \oplus \overline{S_{k+2}}.
$$

Here, the notation means we are considering the elements of $ ^k_n W $ invariant under the $ \text{GL}_2(\mathbb{Z}/n\mathbb{Z}) $.


**Lemma 3.5.** &nbsp; *We have $ _1^k W_{\infty} \cong S_{k+2} \oplus \overline{S_{k+2}} $.*



#### Eichler–Shimura congruence relation


&emsp; We have a Hecke operator acting on $ S_{12}(\Gamma) $. We would like to see what these operators correspond to under the isomorphism given by lemma 3.5. In particular, we can decompose this corresponding operator as a sum of the Frobenious and its adjoint, the Vershiebung. This is because they are the only two $ p $-isogenies in characteristic $ p $, and hence our Hecke operator decomposes as their sum.


&emsp; Fix a pair $ (E, \alpha) $ as in [proposition 3.4](https://www.justinasher.me/ramanujan-conjecture-p3:4){:target="_blank"}, and let $ F \colon E \to E^{(p)} $ denote the (classical) Frobenious. Then we can define a corresponding pair $ (E^{(p)}, \alpha^{(p)}) $ via the diagram over $ M_n \otimes \mathbb{F}_p $

$$
\xymatrix{
& (\mathbb{Z}/n\mathbb{Z})^2 & \\
E_n \ar[ru]^{\alpha} \ar[rr] & & E_n^{(p)} \ar[lu]_{\alpha^{(p)}} \\
E \ar[u] \ar[rr]^{F} & & E^{(p)} \ar[u]
}
$$

For $ \ell \neq p $, this defines an endomorphism of

$$
\widetilde{H}^1(M_n \otimes \overline{\mathbb{F}}_p, \text{Sym}^k(R^1 f_{n*} \underline{\mathbb{Z}}_{\ell}))
$$

by acting on our constant sheaf $ \underline{\mathbb{Z}}_{\ell} $.


&emsp; We likewise have a diagram

$$
\xymatrix{
& (\mathbb{Z}/n\mathbb{Z})^2 & \\
E_n^{(p)} \ar[ru]^{p \alpha^{(p)}} \ar[rr] & & E_n \ar[lu]_{\alpha} \\
E^{(p)} \ar[u] \ar[rr]^{V} & & E \ar[u]
}
$$

which defines the transpose of the Frobenious, the Vershiebung, with respect to an abstracted Peterson inner product.


&emsp; Finally, we define the Hecke operator $ T_p $ acting on $$ {_1^k} W_{\infty} $$ by the coset of 

$$
\begin{bmatrix}
1 & 0 \\
0 & p^{-1}
\end{bmatrix}
$$

in $ \text{GL}_2(\mathbb{Z}_p) \backslash \text{GL}_2(\mathbb{Q}_p)/\text{GL}_2(\mathbb{Z}_p) $. Likewise define $ R_p $ to be the coset of 

$$
\begin{bmatrix}
p^{-1} & 0 \\
0 & p^{-1}
\end{bmatrix}.
$$

Setting $ I_p \colon M_n \to M_n $ to be the functor $ (E, \alpha) \to (E, \alpha/p) $, Deligne proved 


**Proposition 3.6.** &nbsp; *$ F $ is the inverse of the Frobenious from the action of $ \text{Gal}(\overline{\mathbb{F}}_p/\mathbb{F}_p) $ on*

$$
\widetilde{H}^1(M_n \otimes \overline{\mathbb{F}}_p, \text{Sym}^k(R^1 f_{n*} \underline{\mathbb{Z}}_{\ell})).
$$

*Over $ \mathbb{F}_p $, we have $$ T_p = F + I_p^* V $$ and $$ FV = VF = p^{k+1} $$.*


&emsp; From this, we get 


**Theorem 3.7.** &nbsp; *Let $ K_{n, \ell} $ be the largest unramified extension of $ \overline{\mathbb{Q}} $ away from $ n $ and $ \ell $, $ \varphi_p $ a relative Frobenious to $ p $ in $ \text{Gal}(K_{n, \ell}/\mathbb{Q}) $, $ F $ the endomorphism $ \varphi_p^{-1} $ of $ ^k_n W_{\ell} $, and $ V $ the transpose of $ F $. Then*

$$
T_p = F + I_p^* V, \qquad FV = p^{k+1},
$$

$$
1 - T_p + p R_p X^2 = (1-FX)(1+I_p^*VX).
$$



#### Applying Weil II


&emsp; Applying the results of [\[3\]](#4-references), we arrive at

**Theorem 3.8.** &nbsp; *The eigenvalues of the Frobenious $ F $ acting on $ ^k_n W_{\ell} $ are algebraic integers of absolute value $ p^{(k+1)/2} $.*

*Proof.* Recall

$$
{^k_n} W_{\ell}
= \widetilde{H}^1(M_n^{\text{an}} \otimes \overline{\mathbb{Q}}, \, \text{Sym}^k(R^1 f_{n*}(\underline{\mathbb{Q_{\ell}}}))).
$$

We have $$ R^1 f_{n*} (\underline{\mathbb{Q}_{\ell}}) $$ is pointedly pure of weight 1, so $$ \text{Sym}^k(R^1 f_{n*}(\underline{\mathbb{Q_{\ell}}})) $$ is pointedly pure of weight $ k $, and hence the cohomology object is pointedly pure of weight $ k + 1 $. Q.E.D.



&emsp; Since $ I_p^* $ induces the identity on $$ {_1^k} W_{\ell} $$, we have 

$$
1 - T_p X + p^{k+1} X^2 = (1-FX)(1-VX);
$$

and because $ F $ and $ V $ are transposes, 

$$
\det(1-FX; \, {_1^k W_{\ell}}) = \det(1-VX; \, {_1^k W_{\ell}}).
$$

Thus,

$$
\det(1-T_pX+p^{k+1}X^2; \, {_1^k W_{\ell}})
= \det(1-FX; \, {_1^k W_{\ell}})^2.
$$


&emsp; Since $ T_p $ action on $$ {_n^k} W_{\ell} $$ is induced by its action on $$ {_n^k} W_{\infty} $$, we can apply [lemma 3.5](https://www.justinasher.me/ramanujan-conjecture-l3:5){:target="_blank"} to get

$$
\det(1-T_pX +p^{k+1}X^2; \, {_1^k W_{\ell}}) = \det(1-T_pX+p^{k+1}X^2; \, S_{k+2})^2,
$$

and hence 

$$
\det(1-T_pX+p^{k+1}X^2; \, S_{k+2})
= \det(1-FX; \, {_1^k W_{\ell}}).
$$


&emsp; In the case $ k = 10 $, because $ S_{12} $ is of dimension 1, this tells us

$$
H_p(X) = \det(1-FX; \, {_1^{10} W_{\ell}}).
$$

Applying [theorem 3.8](https://www.justinasher.me/ramanujan-conjecture-t3:8){:target="_blank"} completes Deligne's proof of the Ramanujan conjecture. Q.E.D.



## 4. References

1. Pierre Deligne. "Formes modulaires et représentations $ l $-adiques". *Séminaire Bourbaki*, no. 355 (1968–1969).
2. Pierre Deligne. "La conjecture de Weil: I". *Publications Mathématiques de l'IHÉS*, Volume 43 (1974), pp. 273-307. [Link](http://www.numdam.org/item/PMIHES_1974__43__273_0/)
3. Deligne, Pierre. "La conjecture de Weil: II". *Publications Mathématiques de l'IHÉS*, Volume 52 (1980), pp. 137-252. [Link](http://www.numdam.org/item/PMIHES_1980__52__137_0/)
4. Serge Lang, *Introduction to modular forms*, Springer-Verlag, 1976.
5. Jean-Pierre Serre, *A course in arithmetic*, Springer-Verlag, 1973.