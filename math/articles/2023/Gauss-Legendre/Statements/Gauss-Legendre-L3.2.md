---
layout: Statement
indent: true
permalink: /gauss-legendre-l3:2
feedformat: card
title: The Gauss-Legendre algorithm
---
<br>

**Lemma 3.2.** &nbsp; *We have*

$$
F_S(a, b) = \frac{\pi}{2 M(a, b)}
$$

*In particular,*

$$
F_S(1, \sqrt{2}) = \frac{\pi}{2 M(1, \sqrt{2})}.
$$

		
*Proof.* It is not hard to calculate the power series expansion

$$
	F(k)
	= \frac{\pi}{2M(1+k, 1-k)}
	= \sum_{n=0}^{\infty} \left( \frac{(2n-1)!!}{(2n)!!} k^n \right)^2.
$$

(The "!!" means [double factorial](https://en.wikipedia.org/wiki/Double_factorial).) Calculating the AM and GM means gives us 

$$ 
    M(1+k, 1-k) = M(1, \sqrt{1-k^2}).
$$

Hence, applying [proposition 2.1](https://www.justinasher.me/gauss-legendre-p2:1){:target="_blank"} for $$ b/a = \sqrt{1-k^2} $$, we get

$$
	a F_S(a, b) = \frac{\pi}{2 M(1, b/a)} \\
	F_S(a, b) = \frac{\pi}{2 M(a, b)},
$$

with the last equality following from the identity $$ M(ca, cb) = cM(a, b) $$. $$ \blacksquare $$
