---
layout: Statement
indent: true
permalink: /Gauss-Legendre-L3:1
feedformat: card
title: The Gauss-Legendre Algorithm
---
<br>
		
**Lemma 3.1.** &nbsp; Let $$ a_0 = a $$ and $$ b_0 = b $$ as in Definition 3.1. Set

$$
	S = a^2 - \sum_{n=0}^{\infty} 2^{n-1} \left( a_n^2 - b_n^2 \right).
$$

Then $$ E_S(a, b) = S F_S(a, b) $$. $$ \blacksquare $$
	
*Proof.* &nbsp; Consider the integral 

$$
    L(a, b)
	= a^2 F_S(a, b) - E_S(a, b) \tag{2}
$$

Explicitely, this expands to

$$
    L(a, b)
	= (a^2 - b^2) \int_0^{\pi/2} \frac{\sin^2 \theta}{\sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta}} d \theta.
$$

&emsp; Substituting $$ x^2 = a^2 \cos^2 \theta + b^2 \sin^2 \theta $$, 

$$
	L(a, b)
	= \int_b^a \sqrt{\frac{a^2-x^2}{x^2-b^2}} dx.
$$

Now substituting $$ y = (x+ab/x)/2 $$ and considering the associated AM-GM sequence,

$$
\begin{aligned}
	L(a, b) 
	& = \frac{1}{2} \int_{b_1}^{a_1} \frac{(a^2 - b^2) + 4(a_1^2 - y^2)}{\sqrt{(a_1^2 - y^2)(y^2 - b_1^2)}} dy \\
	& = \frac{1}{2} (a^2 - b^2) F_S(a, b) + 2 L(a_1, b_1),
\end{aligned} 
$$

and thus

$$
	\frac{L(a, b)}{F_S(a, b)} = \frac{1}{2}(a_0^2 - b_0^2) + 2 \frac{L(a_1, b_1)}{F_S(a, b)}.
$$

&emsp; Since $$ 2^n(a_n^2 - b_n^2) \to 0 $$, we get $$ 2^n L(a_n, b_n) \to 0 $$, and hence repeatedly applying this identity we get

$$
	L(a, b)
	= \sum_{n=0}^{\infty} 2^{n-1} (a_n^2 - b_n^2) F_S(a, b),
$$

or equivalently 

$$
    L(a, b)
    = - S F_S(a, b) + a^2 F_S(a, b).
$$

Combining this equation with (2) gives us the result. $$ \blacksquare $$
