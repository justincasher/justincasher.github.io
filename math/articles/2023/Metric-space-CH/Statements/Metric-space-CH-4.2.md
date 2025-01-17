---
layout: Statement
indent: true
permalink: /metric-space-ch-4:2
feedformat: card
title: Cartan-Hadamard theorem for metric spaces
---
<br>
		
**Lemma 4.2.** &nbsp; *Let $ f \colon Y \to X $ be a local isometry between complete metric spaces. Let $ x \in X $ and $ y \in f^{-1}(x) $. Then for any rectifiable curve $ \gamma $ starting at $ x $, there exists a unique curve $ \omega $ starting at $ y $ so that $ f \circ \omega = \gamma $.*


*Proof.* Choose a neighborhood $ V $ of $ y $ so that $ f \mid_V \colon V \to U $ is an isometry. Then we can lift $ \gamma \mid_U $ to a unique curve $ \omega \mid_V $. Suppose that the endpoint of $ \gamma $ is not contained within $ U $. Then as $ \omega \mid_V $ approaches the boundary $ V $, we use $ Y $ being complete to get a unique point $ y' $ on the boundary of $ V $ which continuously extends $ \omega \mid_V $.  Now we can choose a neighborhood of $ y' $ which is a local isometry to continue uniquely lifting $ \gamma $. Since $ \gamma $ is rectifiable, after finitely many steps this process terminates, yielding our unique lift $ \omega $. Q.E.D.