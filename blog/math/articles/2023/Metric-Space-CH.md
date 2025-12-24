---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /metric-space-ch
title: Cartan-Hadamard theorem for metric spaces
date: "December 2022"
abstract: "We fill in some details in S. Alexander and R. Bishop's proof of the metric space Cartan-Hadamard theorem. Our goal is to make the proof more motivated and accessible to non-experts."
toc:
  - title: "Introduction"
    anchor: "1-introduction"
  - title: "Covering spaces"
    anchor: "2-covering-spaces"
  - title: "Metric space analogues"
    anchor: "3-metric-space-analogues"
  - title: "Main proof"
    anchor: "4-main-proof"
  - title: "References"
    anchor: "5-references"
---

## 1. Introduction


&emsp; Contrary to its name, the Cartan-Hadamard theorem originates in the work of Hans von Mangoldt. He proved in 1881 that two arbitrarily close geodesics on a real analytic surface of nonpositive curvature can intersect at most once. Jacques Hadamard then developed this theory in 1898 by showing that each homotopy class of paths connecting two points contains a unique geodesic. Both of these results can be found on page 50 of [\[6\]](#5-references). Élie Cartan later generalized Hadamard’s theory to a wider class of manifolds in [\[3\]](#5-references), giving us the name Cartan-Hadamard.


&emsp; In its more modern form, the Catan-Hadamard theorem is a statement about universal coverings. This is because, for a certain class of topological spaces, a universal cover can be constructed via homotopy classes of paths starting at a point. Hence, in the case of a complete, connected Riemannian manifold of nonpositive curvature, our homotopy classes of paths are given by geodesics starting at a point; in particular, our covering map is simply the exponential map, cf. [\[2\]](#5-references). This theory was later generalized by M. Gromov, [\[5\]](#5-references), then S. Alexander and R. Bishop to complete, connected metric spaces with a locally convex metric (locally m-convex), [\[1\]](#5-references).




## 2. Covering spaces


&emsp; Let $ A, E $ be topological space, and let $ \pi \colon E \to A $ be a surjective continuous map. Suppose for each $ a \in A $ there exists an open neighborhood $ U $ so that $ \pi^{-1}(U) = \prod_{i \in E_a} V_i $, with each $ V_i $ disjoint and homeomorphic to $ U $, where $ E_a = \pi^{-1}(a) $ is the fiber at $ a $. Then $ \pi \colon E \to A $ is said to be a *covering*. If $ E $ is simply connected, then our covering is called *universal*. This name is derived from the following universal property: for any other covering $ \varphi \colon F \to A $, there exists a unique continuous map $ h \colon F \to E $ such that $ \varphi = \pi \circ h $. Universal covers are of particular interest when our space is simply connected, as then our cover is a homeomorphism, and hence we can study it instead when considering topologically invariant properties.
		

&emsp; We now construct the universal cover for a suitably nice class of topological spaces.

**Theorem 2.1** *Any connected, locally path connected, and locally simply connected topological space admits a universal cover.*

*Proof.* Indeed, let $ A $ be such a space. Choose a basepoint $ a \in A $, and set $ E $ to be the homotopy classes of paths starting at $ a $. For each path connected open subset $ U \subseteq A $ and $ [\gamma] \in E $ with $$ [\gamma](1) \in U $$, denote $ U_{[\gamma]} $ to be the collection of curves $ [\omega \circ \gamma] $ with $ \omega \colon [0, 1] \to U $. Then the sets $ U_{[\gamma]} $ form a basis for a topology on $ E $, and the endpoint map $$ \pi([\gamma]) = [\gamma](1) $$ is a universal cover. See [\[8\]](#5-references), chapter 3, §8 for the remainder of the proof. Q.E.D.




## 3. Metric space analogues


&emsp; Let us recall the Riemannian

**Cartan-Hadamard theorem.** &nbsp; *Let $ M $ be a complete, connected Riemannian manifold of nonpositive curvature. Fix a point $ p $. Then the exponential $ \text{exp}_p \colon T_p M \to M $ is a universal cover.*


&emsp; We would like to understand what it means for a metric space to have nonpositive curvature. For Riemannian manifolds, nonpositive curvature is equivalent to both local m-convexity and locally being a $ \text{CAT}(0) $ space. For complete metric spaces, the later condition implies the former, and therefore we will develop our theory in the more general locally m-convex case.

&emsp; A real function $ f \colon \mathbb{R} \to \mathbb{R} $ is called *convex* if for every $ a, b \in \mathbb{R} $ and $ t \in [0, 1] $, 

$$
f(ta + (1-t)b) \leq t f(a) + (1-t) f(b). 
$$

In particular, if $ f $ is second-differentiable, then convexity equates to $ f''(x) $ being nonnegative. Let $ \gamma \colon [0, 1] \to X $ be a curve parameterized proportional to arc length. If $ \gamma $ is locally length minimizing between its endpoints, then it is called a *geodesic*. If the length of $ \gamma $ equals the distance between its endpoints, then it is called a *minimizing geodesic*. A metric space in which every two points can be connected by a (unique) minimizing geodesic is called a *(unique) geodesic space*. If any point has a neighborhood which is a (unique) geodesic space, then it is called a *local (unique) geodesic space*.
		
&emsp; Let $ (X, d) $ be a geodesic space and $ f \colon X \to \mathbb{R} $. If for any minimizing geodesic $ \gamma $, the composition $ f \circ \gamma $ is a real convex function, then we call $ f $ a *convex function*. Let $ X $ be a (local) geodesic space. Equip $ X \times X $ with the metric 

$$
d'((x_1, y_1), (x_2, y_2)) = d(x_1, x_2) + d(y_1, y_2).
$$

If the our metric $ d $ is (locally) a convex function in $ (X, d') $, then we call $ X $ *(locally) m-convex*. 


&emsp; We also need a metric space analogue of the tangent space at a point. Fix a point $ x $ in a metric space $ X $. We denote by $ G_x $ the set of geodesics starting $ x $, and equip it with the uniform metric $ \rho $. We define the *evaluation map* $ \text{ev}_x \colon G_x \to X $ by $ \text{ev}_x(\gamma) = \gamma(1) $. 

		


## 4. Main proof


&emsp; Our first step is to further assume that our space is complete, as this allows us to show that the evaluation map is a local isometry. In what follows, $ \frak{g}(a, b) $ denotes a geodesic from $ a $ to $ b $, not necessarily minimizing.


**Proposition 4.1.** &nbsp; *Let $ X $ be a complete, locally m-convex space. Fix a point $ x $ in $ X $. Then $ \text{ev}_x \colon G_x \to X $ is a local isometry.* 


*Proof.* Fix a geodesic $ \gamma $ in $ G_x $. For each $ t \in [0, 1] $, let $ r_t $ be the largest radius so that $ B_d(\gamma(t), r_t) $ is a m-convex space. Set $ r = \inf r_t $, which is strictly positive since each $ r_t $ is and they vary continuously with $ t $. Consider the following statement:


> $ \textbf{P(L):} $ Let $ \gamma' \in G_x $ be subsegment of $ \gamma $ with length at most $ L $ and endpoint $$ x' = \text{ev}_x(\gamma') $$ Then for any $ y \in B_d(x', r/2) $, there exists an $ \omega \in G_x $ contained in $ B_{\rho}(\gamma', r/2) $ such that $ \text{ev}_x(\omega) = y $.


We claim that $ P(L) $ holding for some $ L $ implies it does for every. Therefore, $ P(r) $ being true implies we can apply the statement to $ \gamma' = \gamma $. Thus, by covering $ B_{\rho}(\gamma, r/2) $ in increasingly small balls, we get that $$ \text{ev}_x \colon B_{\rho}(\gamma, r/2) \to B_d(\text{ev}_x(\gamma), r/2) $$ is indeed an isometry
			

&emsp; We proceed by induction. Suppose $ P(L) $ holds, and let $ \gamma' $ be of length at most $ 3L/2 $. Set $ a_0 = \gamma'(1/3) $ and $ b_0 = \gamma'(2/3) $. Then $ \frak{g}(x, b_0) \in G_x $ and $ \frak{g}(a_0, x') \in G_{x'} $ have length at most $ L $, so we can apply $ P(L) $ to see that the midpoint $ a_1 = \text{Mid}(\frak{g}(x, b_0)) $ and $ b_1 = \text{Mid}(\frak{g}(a_0, y)) $ are contained in $ B_d(a_0, r/2) $ and $ B_d(b_0, r/2) $, respectively. Now define inductively $ a_n = \text{Mid}(\frak{g}(x, b_{n-1})) $ and $ b_n = \text{Mid}(\frak{g}(a_{n-1}, y)) $, where $ \frak{g}(x, b_{n-1}) $ and $ \frak{g}(a_{n-1}, y) $ exist by $ P(L) $. Then m-convexity implies 

$$
d(a_n, a_{n+1})
\leq \frac{d(x, x) + d(b_{n-1}, b_n)}{2}
= \frac{d(b_{n-1}, b_n)}{2}
$$

and likewise $ d(b_n, b_{n+1}) \leq d(a_{n-1}, a_n)/2 $. Thus, $ d(a_{n-1}, a_n) < r/2^n $, so $ (a_n) $ is Cauchy with limit $ a_* $ and $ d(a_*, a_0) < r/2 $. Then m-convexity implies 

$$
\rho(\frak{g}(a_n, y), \frak{g}(a_*, y)) \leq d(a_n, a_*),
$$

and hence $ \frak{g}(a_n, y) $ converges uniformly to $$ \frak{g}(a_*, y) $$. Accordingly $$ \frak{g}(x, b_n) $$ converges uniformly to $$ \frak{g}(x, b_*) $$. Since both $$ \frak{g}(x, b_*) $$ and $$ \frak{g}(a_*, y) $$ contain $$ \frak{g}(a_*, b_*) $$, we conclude that gluing them gives us our desired geodesic $ \omega $. Q.E.D.
	

&emsp; One nice property of local isometries between complete metric spaces is that they satisfy the unique path lifting property. In our desired case, this will allow us to strengthen the evaluation map from being a local isometry to a covering by applying proposition 4.3.


**Lemma 4.2.** &nbsp; *Let $ f \colon Y \to X $ be a local isometry between complete metric spaces. Let $ x \in X $ and $ y \in f^{-1}(x) $. Then for any rectifiable curve $ \gamma $ starting at $ x $, there exists a unique curve $ \omega $ starting at $ y $ so that $ f \circ \omega = \gamma $.*


*Proof.* Choose a neighborhood $ V $ of $ y $ so that $ f \mid_V \colon V \to U $ is an isometry. Then we can lift $ \gamma \mid_U $ to a unique curve $ \omega \mid_V $. Suppose that the endpoint of $ \gamma $ is not contained within $ U $. Then as $ \omega \mid_V $ approaches the boundary $ V $, we use $ Y $ being complete to get a unique point $ y' $ on the boundary of $ V $ which continuously extends $ \omega \mid_V $.  Now we can choose a neighborhood of $ y' $ which is a local isometry to continue uniquely lifting $ \gamma $. Since $ \gamma $ is rectifiable, after finitely many steps this process terminates, yielding our unique lift $ \omega $. Q.E.D.

		
**Proposition 4.3.** &nbsp; *Let $ \pi \colon \widetilde{X} \to X $ be a local isometry between complete, connected length spaces. Suppose $ X $ is a local unique geodesic space in which minimizing geodesics locally vary continuously with their endpoints. Then $ \pi $ is a covering.*


*Proof.* Note that since arc-length is additive, whether a map preserves arc-length can be determined locally. Thus, $ \pi $ being a local isometry implies that any rectifiable curve $ \widetilde{\gamma} $ in $ \widetilde{X} $ has the same length as its image in $ X $. 
			

&emsp; Fix a point $ x $ in $ X $. Let $ B(x, \varepsilon) $ be a neighborhood of $ x $ that is a geodesic space in which minimizing geodesics locally vary continuously with their endpoints. Let $ \widetilde{x} \in \pi^{-1}(x) $. We claim that $ \pi \colon B(\widetilde{x}, \varepsilon) \to B(x, \varepsilon) $ is bijective. For surjectivity, let $ a \in B(x, \varepsilon) $, and let $ \gamma_a $ be a rectifiable path from $ x $ to $ a $ contained in $ B(x, \varepsilon) $, which exists since $ X $ is a length space. By lemma 4.2 and the property $ \pi $ preserves the length of paths, we get that $ \gamma_a $ lifts uniquely to a path $ \widetilde{\gamma}_a $ starting at $ \widetilde{x} $ contained in $ B(\widetilde{x}, \varepsilon) $. Then the endpoint of $ \widetilde{\gamma}_a $, which we denote $ \widetilde{a} $, is mapped to $ a $ by $ \pi $. For injectivity, suppose $ \widetilde{b} \in B(x, \varepsilon) $ with $ \pi(\widetilde{b}) = a $ as well. Let $ \widetilde{\gamma}_b $ be a rectifiable path from $ \widetilde{x} $ to $ \widetilde{b} $ contained in $ B(\widetilde{x}, \varepsilon) $, and let $ \gamma_b $ be its image in $ B(x, \varepsilon) $. Then $ \gamma_a(t) $ can be connected to $ \gamma_b(t) $ by a unique minimizing geodesic $ [\gamma_a(t), \gamma_b(t)] $, and these geodesics determine a homotopy $ h $ from $ \gamma_a $ to $ \gamma_b $. By lemma 4.2 this homotopy lifts uniquely, which implies $ a = b $. 
			

&emsp; Consequently, $ \pi \colon B(\widetilde{x}, \varepsilon) \to B(x, \varepsilon) $ is an isometry. This is because the rectifiable curves in $ B(x, \varepsilon) $ and $ B(\widetilde{x}, \varepsilon) $ are now seen to be in bijective correspondence. Thus, $ \pi $ being arc-length preserving combined with $ X $ and $ \widetilde{X} $ being length spaces implies $ \pi $ is distance preserving.
			

&emsp; Finally, let $ \widetilde{y} \in \pi^{-1}(x) $ with $ \widetilde{x} \neq \widetilde{y} $. We claim that $ B(\widetilde{x}, \varepsilon/2) $ and $ B(\widetilde{y}, \varepsilon/2) $ are disjoint for every such $ \widetilde{x}, \widetilde{y} $. Suppose not. Then $ B(\widetilde{x}, \varepsilon/2) $ and $ B(\widetilde{y}, \varepsilon/2) $ have nonempty intersection, so $ \widetilde{y} \in B(\widetilde{x}, \varepsilon) $. But $ \pi(\widetilde{x}) = \pi(\widetilde{y}) $ contradicts the injectivity of $ \pi $ on $ B(\widetilde{x}, \varepsilon) $. Thus, our desired neighborhood of $ x $ in $ X $ is given by $ B(x, \varepsilon/2) $. Q.E.D.
	

&emsp; We are now are ready to prove our main result following [\[1\]](#5-references).


**Theorem 4.4.** (Cartan-Hadamard)	&nbsp; Let $ X $ be a complete, connected locally m-convex space. Fix a point $ x $ in $ X $. Then the evaluation map $ \text{ev}_x \colon G_x \to X $ is a universal cover. In particular, every homotopy class of curves between two points in $ X $ contains a geodesic.


*Proof.* Let us verify the hypotheses of proposition 4.3, so that $ \text{ev}_x $ is a covering. We know that $ \text{ev}_x $ is a local isometry by proposition 4.1. Since $ X $ is locally m-convex, for any point $ y \in X $, there exists an m-convex neighborhood $ U $. By definition, $ U $ is a geodesic space. Suppose $ \gamma_1, \gamma_2 $ are minimizing geodesics in $ U $ with the same endpoints. Then by m-convexity, $ d(\gamma_1(t), \gamma_2(t)) $ is at its largest at $ t = 0 $  or $ t=1 $, so that $ \gamma_1 = \gamma_2 $, and thus $ U $ is unique geodesic space. Likewise, m-convexity implies our minimizing geodesics vary continuously with their endpoints. 
			

&emsp; We are left to show that $ G_x $ and $ X $ are length spaces, and that $ G_x $ is complete. Since we only care about the topology of our spaces when considering covers, we equip them with their respective intrinsic metrics $ \hat{\rho} $ and $ \hat{d} $. Because $ X $ is locally a geodesic space and $ \text{ev}_x $ is a local isometry, this implies that the topologies induced by our intrinsic metrics agree locally with the original topologies, and thus globally. For $ (G_x, \hat{\rho}) $ being complete, we observe that the distance between two elements in the intrinsic metric is always greater than the original. Therefore, a sequence being Cauchy with respect to $ \hat{\rho} $ implies it is for $ \rho $. Since $ X $ is locally m-convex, in small neighborhoods on $ G_x $ we get that $ \rho(\gamma_1, \gamma_2) = d(\text{ev}_x(\gamma_1), \text{ev}_x(\gamma_2)) $, and thus $ X $ being complete implies $ G_x $ is complete, both with $ \rho $ and $ \hat{\rho} $.
		
        	
&emsp; We conclude our proof by observing that $ G_x $ is contractible, and thus simply connected, meaning our cover is universal. Comparing this to the proof of theorem 2.1, we see that our construction gives us a unique geodesic in each homotopy class of curves between two points in $ X $. Q.E.D.




## 5. References

1. Stephanie Alexander and Richard Bishop, *The Hadamard-Cartan theorem in locally con- vex metric spaces*, L'Enseignement Mathématique **36** (1990), 309–320.
2. Werner Ballman, Mikhael Gromov, and Viktor Schroeder, *Manifolds of nonpositive curvature*, Birkhäuser Boston, Inc., 1985.
3. Élie Cartan, *Lecçons sur la géométrie des surfaces de Riemann*, Gauthier-Villars, 1928.
4. Manfredo do Carmo, *Riemannian geometry*, Birkhäuser, 1992.
5. Mikhael Gromov, *Hyperbolic manifolds, groups and actions, Riemann surfaces and related topics*, 1978, pp. 183–213.
6. Hadamard Jacques, *Les surfaces à courbures opposées et leurs lignes géodésiques*, Journal de mathématiques pures et appliquées 5e série **4** (1898), 27–74.
7. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of differential geometry*, Inter- science Publishers, 1969.
8. J.P. May, *A concise course in algebraic topology*, Chicago Lectures in Mathematics, 1999.