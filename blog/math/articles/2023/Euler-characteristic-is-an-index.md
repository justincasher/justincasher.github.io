---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /euler-characteristic-is-an-index
title: Euler characteristic is the index of an operator
date: "May 2023"
abstract: "Let M be a closed oriented Riemannian manifold. We show that the (analytic) index of a specific Dirac operator equals the Euler characteristic of M. This is the first step in the proof that the Atiyah-Singer index theorem implies the Chern-Gauss-Bonnet theorem."
toc:
  - title: "Atiyah-Singer index theorem"
    anchor: "1-atiyah-singer-index-theorem"
  - title: "The de Rham complex"
    anchor: "2-the-de-rham-complex"
  - title: "Main proof"
    anchor: "3-main-proof"
  - title: "References"
    anchor: "4-references"
---

## 1. Atiyah-Singer index theorem

&emsp; Write $ M $ for a closed oriented Riemannian manifold of dimension $ n $. Let $ E_1, E_2 $ be complex vector bundles over $ M $ of rank $ r_1, r_2 $, respectively. A map of sections

$$
    F \colon \Gamma(E_1) \to \Gamma(E_2)
$$

which can locally be written as a sum of partial derivatives 

$$
    F \phi(x) = \sum_{\|\alpha\| \leq M} f^{\alpha}(x) (\partial_\alpha \phi)(x),
$$

where 

$$
    \partial_\alpha = \frac{\partial^{\|\alpha\|}}{\partial^{\alpha_1} \cdots \partial^{\alpha_n}}
$$

is called a *differential operator*. Here, $ \alpha = (\alpha_1, ..., \alpha_n) $ is a vector in $ \mathbb{Z}^n $ with $ \|\alpha\| = \sum \alpha_i $, we let $ U \subseteq M $ be any open subset where $ E_1, E_2 $ are trivial, and $ f^\alpha \in C^{\infty}(U, \text{Hom}(\mathbb{C}^{r_1}, \mathbb{C}^{r_2})) $

&emsp; For a particular type of differential operator, called *elliptic*, the Atiyah-Singer index theorem relates the index 

$$
    \text{Ind}(F) = \dim \ker F - \dim \text{coker} F
$$

to characteristic classes:

$$
    \text{Ind}(F)
    = \int_M \text{Ch}(F) \wedge \text{td}(M). 
$$

&emsp; The following Theorems are corollaries of the Atiyah-Singer index theorem:

- Chern-Gauss-Bonnet theorem;
- Hirzebruch–Riemann–Roch theorem;
- Hirzebruch signature theorem.

We focus on the first, which states that the Euler characteristic of $ M $ equals the Euler class of the tangent bundle $ e(TM) $ integrated over $ M $:

$$
    \chi(M) = \int_M e(TM)
$$

In particular, we will show that that the Euler characteristic is the index of a Dirac operator. Note that in what follows our vector bundles are not complex, nor do we show that this operator is indeed elliptic. In order to do so we would need to complexify the de Rham complex then compute our operator's symbol.


## 2. The de Rham complex

&emsp; Write $ \Omega^k(M) = \Gamma(\bigwedge^k T^{\ast}M) $ for the (real) vector space of differential $ k $-forms of $ M $. In what follows, we omit $ M $ simply writing $ \Omega^k $. We further set $ \Omega^{\ast} = \bigoplus_k \Omega^k $ to be the associated graded vector space. It has a decomposition into components with $ k $ even or odd:

$$
    \Omega^{\ast} = \Omega^{\text{ev}} \oplus \Omega^{\text{od}}.
$$

&emsp; Recall that there is a natural map $ d \colon \Omega^k \to \Omega^{k+1} $ such that $ d \circ d = 0 $ called the *differential*. We see that the image of $ d $ is a subobject of its kernel, and we define 

$$
    H_{\text{dR}}^k(M) = \frac{\ker d \colon \Omega^k \to \Omega^{k+1}}{\text{im} d \colon \Omega^{k-1} \to \Omega^k}
$$

to be the *$ k $th de Rham cohomology group of $ M $*.

&emsp; We can dually define the *codifferential* $ \delta \colon \Omega^{k} \to \Omega^{k-1} $ using the *Hodge star operator* $ \star \colon \Omega^{k} \to \Omega^{n-k} $. We will not explicitly define the later, but the idea is that there is a natural isomorphism $ \bigwedge^k T^{\ast}M \to \bigwedge^{n-k} T^{\ast}M $ since the vector spaces are of the same dimension. This map pulls back to the Hodge star operator, which is used to define the codifferential on $ \Omega^k $ by $ \delta = (-1)^k \star^{-1} d \star $. 

&emsp; The Hodge star operator yields a natural inner product structure on $ \Omega^{\ast} $. For $ \omega, \eta \in \Omega^k $, we set 

$$
    \left< \omega, \eta \right> = \int_M \omega \wedge \star \eta,
$$

and then we define differential forms of unequal degrees to be orthogonal. In particular, given a bounded linear operator $ T \colon \Omega^{\ast} \to \Omega^{\ast} $ its *adjoint* is a map $ T^{\ast} \colon \Omega^{\ast} \to \Omega^{\ast} $ such that $ \left< T \omega, \eta \right> = \left< \omega, T^{\ast} \eta \right> $.

&emsp; Finally, we define the Euler characteristic of $ M $ as the alternating sum 

$$
    \chi(M) = \sum_{k=0}^n (-1)^k \dim H_{\text{dR}}^k(M).
$$

It is a topological invariant of our manifold.


## 3. Main Proof

&emsp; We call $ \Delta = (d + \delta)^2 $ the *Laplace operator*. It abstracts the traditional definition of the divergence of the gradient. We set 

$$
    \mathcal{H}^k(M) = \ker \{\Delta \colon \Omega^k \to \Omega^k\}
$$

and call elements of $ \mathcal{H}^k(M) $ *harmonic $ k $-forms*. They allow us to compute the de Rham cohomology groups. 

**Hodge isomorphism.** &nbsp; *Let $ M $ be a closed oriented Riemannian manifold. Then there exists a canonical isomorphism $ \mathcal{H}^k(M) \cong H_{\text{dR}}^k(M) $.*

&emsp; Associated to Laplace operator is the *Dirac operator* $ D = d + \delta $. It is a self-adjoint operator, whose name is due to the property $ D^2 = \Delta $.

**Lemma.** &nbsp; *The kernel of $ D $ contained in $ \Omega^k $ equals $ \mathcal{H}^k(M) $.*

*Proof.* Indeed, we see that $ (d + \delta) \omega = 0 $ if and only if 

$$
    \left< (d + \delta) \omega, (d + \delta) \omega \right>
    = \left< \Delta \omega, \omega \right>
    = 0,
$$

giving us our result. $ \blacksquare $

&emsp; Using decomposition of $ \Omega^{\ast} $ into even and odd components, we can restrict $ D $ to get adjoint operators 

$$
\begin{aligned}
    D^{\text{ev}} & \colon \Omega^{\text{ev}} \to \Omega^{\text{od}} \\
    D^{\text{od}} & \colon \Omega^{\text{od}} \to \Omega^{\text{ev}}.
\end{aligned}
$$

In general, we can calculate the dimension of the kernel of an elliptic operator using its adjoint

$$
    \dim \text{coker} F = \dim \ker F^{\ast}.
$$

Combining this with the Hodge isomorphism we get 

$$
\begin{aligned}
    \text{Ind}(D^{\text{ev}})
    & = \dim \ker D^{\text{ev}} - \dim \ker D^{\text{od}} \\
    & = \sum_{k \text{ even}} \dim \mathcal{H}^k(M) - \sum_{k \text{ odd}} \dim \mathcal{H}^k(M) \\
    & = \sum_{k=0}^{n} (-1)^k \dim H_{\text{dR}}^k(M) \\
    & = \chi(M).
\end{aligned}
$$

**Theorem.** &nbsp; *We have the equality $ \chi(M) = \text{Ind}(D^{\text{ev}}) $.*


## 4. References

1. Michael Atiyah and Isadore Singer, *The index of elliptic operators on compact manifolds*, Bulletin of The American Mathematical Society **69** (1963), no. 3, 422–433.
2. Daniel Freed, *The Atiyah-Singer index theorem*, Bulletin of The American Mathematical Society **58** (2021), no. 4, 517–566.
3. Frank Warner, *Foundations of differentiable manifolds and Lie groups*, Springer, 1983.
