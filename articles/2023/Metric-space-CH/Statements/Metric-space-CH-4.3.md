---
layout: Statement
indent: true
permalink: /Metric-space-CH-4:3
feedformat: card
title: Cartan-Hadamard theorem for metric spaces
---
<br>
		
**Proposition 4.3.** &nbsp; *Let $ \pi \colon \widetilde{X} \to X $ be a local isometry between complete, connected length spaces. Suppose $ X $ is a local unique geodesic space in which minimizing geodesics locally vary continuously with their endpoints. Then $ \pi $ is a covering.*


*Proof.* Note that since arc-length is additive, whether a map preserves arc-length can be determined locally. Thus, $ \pi $ being a local isometry implies that any rectifiable curve $ \widetilde{\gamma} $ in $ \widetilde{X} $ has the same length as its image in $ X $. 
			

&emsp; Fix a point $ x $ in $ X $. Let $ B(x, \varepsilon) $ be a neighborhood of $ x $ that is a geodesic space in which minimizing geodesics locally vary continuously with their endpoints. Let $ \widetilde{x} \in \pi^{-1}(x) $. We claim that $ \pi \colon B(\widetilde{x}, \varepsilon) \to B(x, \varepsilon) $ is bijective. For surjectivity, let $ a \in B(x, \varepsilon) $, and let $ \gamma_a $ be a rectifiable path from $ x $ to $ a $ contained in $ B(x, \varepsilon) $, which exists since $ X $ is a length space. By [lemma 4.2](https://www.justinasher.me/Metric-space-CH-4:2){:target="_blank"} and the property $ \pi $ preserves the length of paths, we get that $ \gamma_a $ lifts uniquely to a path $ \widetilde{\gamma}_a $ starting at $ \widetilde{x} $ contained in $ B(\widetilde{x}, \varepsilon) $. Then the endpoint of $ \widetilde{\gamma}_a $, which we denote $ \widetilde{a} $, is mapped to $ a $ by $ \pi $. For injectivity, suppose $ \widetilde{b} \in B(x, \varepsilon) $ with $ \pi(\widetilde{b}) = a $ as well. Let $ \widetilde{\gamma}_b $ be a rectifiable path from $ \widetilde{x} $ to $ \widetilde{b} $ contained in $ B(\widetilde{x}, \varepsilon) $, and let $ \gamma_b $ be its image in $ B(x, \varepsilon) $. Then $ \gamma_a(t) $ can be connected to $ \gamma_b(t) $ by a unique minimizing geodesic $ [\gamma_a(t), \gamma_b(t)] $, and these geodesics determine a homotopy $ h $ from $ \gamma_a $ to $ \gamma_b $. By [lemma 4.2](https://www.justinasher.me/Metric-space-CH-4:2){:target="_blank"} this homotopy lifts uniquely, which implies $ a = b $. 
			

&emsp; Consequently, $ \pi \colon B(\widetilde{x}, \varepsilon) \to B(x, \varepsilon) $ is an isometry. This is because the rectifiable curves in $ B(x, \varepsilon) $ and $ B(\widetilde{x}, \varepsilon) $ are now seen to be in bijective correspondence. Thus, $ \pi $ being arc-length preserving combined with $ X $ and $ \widetilde{X} $ being length spaces implies $ \pi $ is distance preserving.
			

&emsp; Finally, let $ \widetilde{y} \in \pi^{-1}(x) $ with $ \widetilde{x} \neq \widetilde{y} $. We claim that $ B(\widetilde{x}, \varepsilon/2) $ and $ B(\widetilde{y}, \varepsilon/2) $ are disjoint for every such $ \widetilde{x}, \widetilde{y} $. Suppose not. Then $ B(\widetilde{x}, \varepsilon/2) $ and $ B(\widetilde{y}, \varepsilon/2) $ have nonempty intersection, so $ \widetilde{y} \in B(\widetilde{x}, \varepsilon) $. But $ \pi(\widetilde{x}) = \pi(\widetilde{y}) $ contradicts the injectivity of $ \pi $ on $ B(\widetilde{x}, \varepsilon) $. Thus, our desired neighborhood of $ x $ in $ X $ is given by $ B(x, \varepsilon/2) $. Q.E.D.