---
layout: Statement
indent: true
permalink: /metric-space-ch-4:1
feedformat: card
title: Cartan-Hadamard theorem for metric spaces
---
<br>
		
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
