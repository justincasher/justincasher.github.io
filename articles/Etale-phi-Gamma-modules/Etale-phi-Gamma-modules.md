---
layout: Writing
indent: true
permalink: /Etale-phi-Gamma-modules
feedformat: card
title: Étale (phi, Gamma)-modules
---
$ \DeclareMathOperator{\ev}{ev} $
<br>

**Abstract.** &nbsp; We define étale $ (\varphi, \Gamma) $-modules in order to formulate a categorical equivalence with certain Galois representations. The only reference is Schneider's book *Galois Representations and $ (\varphi, \Gamma) $-Modules*, and the idea is to compress his definition into a more readable account.

## Table of contents
1. 

## 1. Dependencies

&nbsp; Our goal is to define

> A $ (\varphi_L, \Gamma_L) $-module $ M $ (over $ \mathbb{A}_L $) is a finitely generated $ \mathbb{A}_L $-module $ M $ together with a $ \Gamma_L $-action on $ M $ by semilinear automorphisms which is continuous for the weak topology, and a $ \varphi_L $-linear endomorphism $ φ_M $ of $ M $ which commutes with the $ \Gamma_L $-action.

(Étaleness is straightforward to define.)

Thus, we need to define the following:
- $ \mathbb{A}_L $
    - pg. 94 using $ j $
- $ \Gamma_L $
    - pg . 49
- $ \varphi_L $
    - pg. 78 


## 2. Notations

We define $ \text{Fr} \colon W(o_{\mathbb{C}_p^{\flat}} )_L \to W(o_{\mathbb{C}_p^{\flat}} )_L $ by raising each coordinate to the $ q $ th power.

We define $ \{ \ \} \colon \mathbb{M}_{\mathbb{E}_L} \to \mathbb{M}_{\mathbb{E}_L} $ by $ \{ \alpha \} = \lim_{i \to \infty} ([\pi]_{\phi} \circ \text{Fr}^{-1})^i(\alpha) $. Is this not a form of tilting?

We define $ \omega_{\phi} $ by considering the map $ \iota_{\phi} = \{ \ \} \circ \tau \circ \iota $ and setting $ \omega_{\phi} = \iota_{\phi}(t) $. 

We define $ \mathscr{A}_L = \lim_m o((X))/\pi^m o((X) $.

We define $ j $ by first considering $ o [ [ X ] ] \to W(o_{\mathbb{E}_L})_L $ via $ f(X) \to f(\omega_{\phi}) $. Using that $ \omega_{\phi} $ becomes invertible implies we can extend to a map $ o((X)) \to W(\mathbb{E}_L)_L $. Then $ j $ is given by considering the direct limit. 

We define $ \mathbb{A}_L $ as the image of the injective map $ j \colon \mathscr{A}_L \to W(\mathbb{E}_L) $.


## 1. Formal group laws

&emsp; Write $ L $ for a finite extension of $ \mathbb{Q}_p $. It is a complete nonarchimedian field. Let $ o_L $ be its ring of integers, $ \frak{m} $ the maximal ideal of $ o_L $ with uniformizer $ \pi $, and $ \mathbb{F}_q $ its residue field. Likewise set $ \overline{L} $ to be an algebraic closure of $ L $, and 

$$
\frak{M} = \{ a \in \overline{L} \mid | a | < 1 \} = \bigcup_E \frak{m}_E
$$

where $ L \subseteq E \subseteq \overline{L} $ is a finite extension.

&emsp; An element $ F \in o [ [ X, Y ] ] $ is called a *commutative formal group law* if it is associtive

$$
F(X, F(Y, Z)) = F(F(X, Y), Z),
$$

commutative 

$$
F(X, Y) = F(Y, X),
$$

and addition in degree 1 

$$
F(X, Y) = X + Y \quad \text{mod} \ \left< X, Y \right>^2.
$$

Any such $ F $ admits a formal inverse $ I \in o [ [ X ] ] $ which is $ -X $ in degree 1 and $ F(X, I(X)) = 0 $. This makes $ \frak{m}_L $ into an abelian group with addition given by $ F $ and inverses by $ I $.

&emsp; An element $ h \in o [ [ X ] ] $ is an endomorphism of $ F $ if $ h(0) = 0 $ and $ h(F(X, Y)) = F(h(X), h(Y)) $. The set of endomorphisms $ \text{End}_o(F) $ forms a ring with addition defined by $ F(h_1(X), h_2(X)) $ and multiplication by composition $ h_1(h_2(X)) $.

&emsp; An element $ \phi \in o [ [ X ] ] $ is called a *Frobenious power series* if it is multiplication by $ \pi $ in degree 1 

$$
\phi(X) = \pi X \quad \text{mod} \ \left< X \right>^2
$$

and the Frobenious modulo $ \pi $

$$
\phi(X) = X^q \quad \text{mod} \ \pi o[ [ X ] ].
$$

**Proposition 1.** &nbsp; *For any Frobenious power series there is a unique commutative formal group law $ F_\phi $ such that $ \phi \in \text{End}_o(F_\phi) $.* 

**Proposition 2.** &nbsp; *Let $ \phi $ be a Frobenious power series. There is a unique injective ring homomorphism*

$$ 
[\ \cdot \ ]_{\phi} \colon o \to \text{End}_o(F_{\phi}),
$$

*linear in degree 1*

$$
[a]_{\phi}(X) = aX \quad \text{mod} \ \pi o [ [ X ] ],
$$

*such that $ [\pi]_{\phi} = \phi $.*

&emsp; Denote by $ \frak{M}[\pi^n] $ the $ \pi^n $-torsion points of $ \frak{M} $, i.e. the collection of $ z \in \frak{M} $ such that 

$$
[\pi^n]_{\phi}(z) = \phi^n(z) = 0.
$$

Set $ L_n = L(\frak{M}[\pi^n]) $ and 

$$ 
L_{\infty} = \bigcup_n L_n = \bigcup_n L(\frak{M}[\pi^n])
$$ 

We denote the resulting Galois group 

$$ 
\Gamma_L = \text{Gal}(L_{\infty}/L)
$$

We have (nontrivially) that $ L_n $ is a free $ o / \pi^n o $-module of rank 1. Hence, for any $ \gamma \in \text{Gal}(\overline{L}/L) $ there is a unique $ \chi_{L, n} \in (o/\pi^n o)^{\times} $ such that for $ z \in \frak{M}[\pi^n] $

$$
\gamma(z) = [\chi_{L, n}(\gamma)]_{\phi}(z).
$$

Write $ \chi_L $ for the projective limit of the $ \chi_{L, n} $.

**Theorem 3.** &nbsp; $ \chi_L \colon \text{Gal}(L_{\infty} / L) \to o^{\times} $ *is an isomorphism.*

&emsp; We call

$$
T_{\pi}(\frak{M}) = \lim_{\longleftarrow} \frak{M}[\pi^n]
$$

the *Tate module* of $ \frak{M} $, where the projective limit is taken with respect to multiplication by $ {[ \pi ]}_\phi $. It is a free $ o $-module of rank 1. Fix a generator $ t $ of $ T_\pi (\frak{M}) $. 

&emsp; Define the function (but not necessarily a homomorphism) $ \iota \colon T_{\pi}(\frak{M}) \to o_{\hat{L}^{\flat}_{\infty}} $ by 

$$
\iota((t_n)_{n \in \mathbb{N}}) = (\dots, t_n \ \text{mod} \ \pi, \dots, t_1 \ \text{mod} \ \pi).
$$

We denote the image of our generator by $ \omega = \iota(t) $. It satisfies $ | \omega |_{\flat} < 1 $.

&emsp; Let $ \text{ev}_\omega \colon k [ [ X ] ] \to o_{ \hat{L}_\infty^\flat } $ be the evaluation map 

$$
\text{ev}_{\omega}(f) = f(\omega).
$$

Since $ \omega $ is invertible, it extends to an embedding of fields which we also denote $ \text{ev}_{\omega} \colon k((X)) \to \hat{L}_\infty^{\flat} $. We denote the image of $ \text{ev}_{\omega} $ by $ \mathbb{E}_L $. 

&emsp; We define a map $ \iota_\phi \colon T_{\pi} ( \frak{M} ) \to \mathbb{M}_{ \mathbb{E}_L } $ with $ \omega_{\phi} = \iota_{\phi}(t) $ as follows. Recall the 0th Witt polynomial $ \Phi_0 \colon W(o_{\mathbb{E}_L}) \to o_{\mathbb{E}_L}$ is given by 

$$
\Phi_0((b_n)_n) = b_0,
$$

and our Teichmüller representative $ \tau \colon o_{\mathbb{E}_L} \to W(o_{\mathbb{E}_L}) $ by 

$$
\tau(b) = (b, 0, \dots).
$$

Set $ \mathbb{M}_{\mathbb{E}_L} = \Phi_0^{-1}(\frak{m}_{\mathbb{E}_L}) $, and consider the endomorphism  $ \{ \ \cdot \ \} \colon \mathbb{M}_{\mathbb{E}_L} \to \mathbb{M}_{\mathbb{E}_L} $ 

$$
\{ \alpha \} = \lim_{i \to \infty} ([\pi]_{\phi} \circ \text{Fr}^{-1})^i(\alpha).
$$

We finally define $ \iota_{\phi} = \{ \ \cdot \ \} \circ \tau \circ \iota $.

&emsp; Let $ \displaystyle \text{ev}_{ \omega_\phi } \colon o[ [ X ] ] \to W( o_{ \mathbb{E}_L } )_L $ be the evaluation map 

$$
\text{ev}_{\omega_{\phi}}(f) = f(\omega_{\phi}),
$$

which we extend to a map $ \displaystyle \text{ev}_{\omega_{\phi}} \colon o((X)) \to W(\mathbb{E}_L)_L $. Let 

$$
\mathscr{A}_L = \lim_{\longleftarrow} o((X)) / \pi^m o((X)).
$$

We have that $ \text{ev}_{ \omega_\phi } $ induces a map for each $ m $

$$
o((X))/\pi^m o((X)) \to W(\mathbb{E}_L)_L/\pi^m W(\mathbb{E}_L)_L,
$$

and hence an injective map $ j \colon \mathscr{A}_L \to W(\mathbb{E}_L)_L $. Let $ \textbf{A}_L $ denote the image of this map.