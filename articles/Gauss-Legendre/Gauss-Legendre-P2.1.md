---
layout: Statement
indent: true
permalink: /Gauss-Legendre-P2:1
feedformat: card
title: The Gauss-Legendre Algorithm
---
<br>

**Proposition 2.1.** &nbsp; *Let $$ k^2 = 1 - b^2/a^2 $$. Then the identities*

$$
\begin{aligned}
	F(k) & = a F_S(a, b) \\
	E(k) & = \frac{1}{a} E_S(a, b).
\end{aligned}
$$

*are true.*
	
*Proof.* Let us prove the second equation with the first following similarly. Substituting, we get 

$$
\begin{aligned}
	E(k)
	& = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2 \theta} d \theta \\
	& = \int_0^{\pi/2} \sqrt{1 - (1-b^2/a^2) \sin^2 \theta} d \theta \\
	& = \int_0^{\pi/2} \sqrt{\cos^2 \theta + b^2/a^2 \sin^2 \theta} d \theta \\
	& = \frac{1}{a} \int_0^{\pi/2} \sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta} d \theta \\
	& = \frac{1}{a} E_S(a, b),
\end{aligned}
$$

and hence our result. $$ \blacksquare $$
