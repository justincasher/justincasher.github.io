---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /gauss-legendre
title: The Gauss-Legendre algorithm
date: "October 2022"
abstract: "We prove the following approximation of $\\pi$: $$\\pi = \\frac{2M(1,\\sqrt{2}/2)^2}{\\left(1 - \\sum_{n=0}^{\\infty} 2^n(a_n^2 - b_n^2\\right))},$$ which is derived from the arithmetic-geometric mean of $1$ and $\\sqrt{2}/2$. Throughout this article tedious steps are often skipped to illustrate the main picture; in particular, computing integral substitutions and power series expansions."
toc:
  - title: "History"
    anchor: "1-history"
  - title: "Elliptic integrals"
    anchor: "2-elliptic-integrals"
  - title: "Main results"
    anchor: "3-main-results"
  - title: "References"
    anchor: "4-references"
---

## 1. History
	
&emsp; The methods used for approximating $ \pi $ span millennia and severely vary in complexity; we will describe a few of the popular methods. The reference here is [\[1\]](#4-references). Around 200 BC, Archimedes approximated the circumference $ C $ and radius $ r $ of a circle by inscribing it in a polygon with $ n $ sides. It is not hard to see that as $ n $ approaches infinity, we get $ \pi $ using the circumference formula $ C = 2 \pi r $. Then during the invention of calculus in the 1600s, Newton and others used integrals and power series expansions to calculate $ \pi $. For instance, the identity

$$
	\arctan(x) 
	= \sum_{n=0}^{\infty} (-1)^{n} \frac{x^{2n+1}}{2n+1}
$$

evaluated at $ x = 1 $ gives us 

$$
	\frac{\pi}{4} 
	= 1-\frac{1}{3}+\frac{1}{5}+\frac{1}{7}-\cdots.
$$ 

&emsp; Furthermore, in the 1700s, Euler calculated the values of the Riemann zeta function. Famously, for $ x=2 $, we get that 

$$
	\zeta(2) 
	= \sum_{n=1}^{\infty} \frac{1}{n^2}
	= \frac{\pi^2}{6}.
$$

The underlying problem is this family of methods are slow, often taking hundreds of iterations to even yield a couple of digits.
		
&emsp; In contrast, the Gauss-Legendre algorithm has quadratic convergence. Let us say we want to calculate 512 decimal places of $ \pi $. Then the Gauss-Legendre algorithm only needs 9 iterations, while almost all of the older methods (normally) need at least 800 iterations, if not significantly more. As an aside, Ramanujan's equation for $ \pi $

$$
	\frac{1}{\pi} 
	= \frac{2 \sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)! (1103+26390n)}{(n!)^4 396^{4n}}.
$$

only need around $ 65 $ iterations to converge [\[3\]](#4-references). His equations are now used for large approximations of $ \pi $ due to computational complexity optimization and storage restrictions. 
		

## 2. Elliptic integrals
	
&emsp; Let $ (a \cos \theta, b \sin \theta) $ be an ellipse parameterized by $ \theta \in [0, 2 \pi] $. Then it's arc-length is given by 

$$
	\int_{0}^{2 \pi} \sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta} d \theta. \tag{1}
$$

This integral is not easy to compute in itself, and it was generalized to the study of so-called elliptic integrals in the early 1700s. Now notice that in (1) all of the data concerning our specific ellipse's arc-length is contained within the interval $ 0 \leq \theta \leq \pi/2 $. Hence, it would make sense to reduce our study to complete elliptic integrals, meaning those with amplitude $ \pi/2 $. Furthermore, we will restrict ourselves to complete elliptic integrals of the first and second kind. For the proof that every elliptic integral is of the first, second, or third kind, see [\[2\]](#4-references).
		
**Definition.** &nbsp; Let

$$ 
\begin{aligned}
	F(k) & = \int_0^{\pi/2} \frac{1}{\sqrt{1 - k^2 \sin^2 \theta}} d \theta, \\
	E(k) & = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2 \theta} d \theta, \\
	F_S(a, b) & = \int_0^{\pi/2} \frac{1}{\sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta}} d \theta, \\
	E_S(a, b) & = \int_0^{\pi/2} \sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta} d \theta.
\end{aligned}
$$

Then $ F(k) $ and $ E(k) $ are called *complete elliptic integrals of the first and second kinds*, respectively, with *symmetric forms* $ F_S(a, b) $ and $ E_S(a, b) $. We refer to $ k $ as the modulus of our integral.

		
&emsp; From here on we will assume that by elliptic integral we mean a complete elliptic integral of the first or second kind. We see that the ordinary and symmetric forms of elliptic integrals are related by the following proposition.
		
**Proposition 2.1.** &nbsp; *Let $ k^2 = 1 - b^2/a^2 $. Then the identities*

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

and hence our result. $ \blacksquare $
		
&emsp; We also recall a result regarding the symmetry of these integrals originally discovered by Legendre.

**Proposition 2.2.** (Legendre's Identity). &nbsp; *Suppose $ k_1^2 + k_2^2 = 1 $. Then*

$$
	F(k_1) E(k_2) + F(k_2) E(k_1) - F(k_1) F(k_2) = \frac{\pi}{2}
$$

*holds.*
	
*Proof.* We leave the details of this proof to the reader. Taking the derivative with respect to $ k_1 $ shows that the L.H.S. is constant. To see that this value is $ \pi/2 $, we take the limit as $ k_1 $ goes to $ 0 $. $ \blacksquare $
	
	
## 3. Main results
		
&emsp; We now prove the Gauss-Legendre algorithm. We will not discuss error analysis, which is done in [\[4\]](#4-references).
		
**Definition.** &nbsp; Let $ a_0, b_0 \in \mathbb{R} $. Let $ a_{n+1} = (a_n + b_n)/2 $ and $ b_{n+1} = (a_n b_n)^{1/2} $ be the arithmetic and geometric means, respectively, of the $ n $th terms. Then we call their common limit 

$$ 
    \lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = M(a_0, b_0) 
$$ 

the *arithmetic-geometric (AM-GM) mean* of $ a_0 $ and $ b_0 $.
	
**Theorem** (Gauss-Legendre). &nbsp; *Set $ a_0 = 1 $ and $ b_0 = \sqrt{2}/2 $. Then the series*

$$
	\pi = \frac{2 M (1, \sqrt{2}/2)^2}{1 - \displaystyle{\sum_{n=0}^{\infty} 2^n (a_n^2 - b_n^2)}}
$$

*converges to $ \pi $.*
		
&emsp; We need two lemmas in order to prove our result. 
		
**Lemma 3.1.** &nbsp; *Let $ a_0 = a $ and $ b_0 = b $ as in definition 3.1. Set*

$$
S = a^2 - \sum_{n=0}^{\infty} 2^{n-1} \left( a_n^2 - b_n^2 \right).
$$

*Then $ E_S(a, b) = S F_S(a, b) $.*
	
*Proof.* This proof is taken from [\[5\]](#4-references). Consider the integral 

$$
    L(a, b)
	= a^2 F_S(a, b) - E_S(a, b) \tag{2}
$$

Explicitly, this expands to

$$
    L(a, b)
	= (a^2 - b^2) \int_0^{\pi/2} \frac{\sin^2 \theta}{\sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta}} d \theta.
$$

&emsp; Substituting $ x^2 = a^2 \cos^2 \theta + b^2 \sin^2 \theta $, 

$$
	L(a, b)
	= \int_b^a \sqrt{\frac{a^2-x^2}{x^2-b^2}} dx.
$$

Now substituting $ y = (x+ab/x)/2 $ and considering the associated AM-GM sequence,

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

&emsp; Since $ 2^n(a_n^2 - b_n^2) \to 0 $, we get $ 2^n L(a_n, b_n) \to 0 $, and hence repeatedly applying this identity we get

$$
	L(a, b)
	= \sum_{n=0}^{\infty} 2^{n-1} (a_n^2 - b_n^2) F_S(a, b),
$$

or equivalently 

$$
    L(a, b)
    = - S F_S(a, b) + a^2 F_S(a, b).
$$

Combining this equation with (2) gives us the result. $ \blacksquare $
	
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

(The "!!" means [double factorial](https://en.wikipedia.org/wiki/Double_factorial){:target="_blank"}.) Calculating the AM and GM means gives us 

$$ 
    M(1+k, 1-k) = M(1, \sqrt{1-k^2}).
$$

Hence, applying proposition 2.1 for $ b/a = \sqrt{1-k^2} $, we get

$$
	a F_S(a, b) = \frac{\pi}{2 M(1, b/a)} \\
	F_S(a, b) = \frac{\pi}{2 M(a, b)},
$$

with the last equality following from the identity $ M(ca, cb) = cM(a, b) $. $ \blacksquare $
		
&emsp; We finally have the tools we need to prove the Gauss-Legendre Algorithm does indeed converge to $ \pi $.
		
*Proof (Gauss-Legendre).* Set $ k = \sqrt{2}/2 $ to be our modulus. Then we notice $ 2k^2 = 1 $, and hence we can apply proposition 2.2 to get

$$
	2 F (k) E (k) - F(k)^2 = \frac{\pi}{2}.
$$

Now let us evaluate these integrals by first converting them into symmetric form then applying our lemmas. Since $ k^2 = 1 - 1/k^2 $, we can set $ a = 1 $ and $ b = k $ in proposition 2.1 to get

$$
	2 F_S(1, k) E_S(1, k) - F_S(1, k)^2 = \frac{\pi}{2}.
$$

Then applying lemma 3.1 gives us an equation only dependent on $ F_S(1, k) $ 

$$
	(2 S - 1) F_S(1, k)^2 = \frac{\pi}{2}.
$$

Finally, we apply lemma 3.2 to write our equation in terms of the AM-GM mean

$$
\begin{aligned}				
	\frac{\pi}{2} & = (2S-1) \left( \frac{\pi}{2 M(1, k)} \right)^2  \\
	\pi & = \frac{2M(1, k)^2}{2S-1}.
\end{aligned}
$$

Plugging in $ S $ gives us our result. $ \blacksquare $


## 4. References

1. David H. Bailey, Simon M. Plouffe, Peter B. Borwein, and Jonathan M. Borwein, *The quest for $ \pi $*, The Mathematical Intelligencer **19** (1997), no. 1, 50–56.
2. Gosta Mittag-Leffler, *An introduction to the theory of elliptic functions*, Annals of Mathematics **24** (1923), no. 4, 271–351.
3. Srinivasa Ramanujan, *Modular equations and approximations to $ \pi $*, The Quarterly Joural of Pure and Applied Mathematics **45** (1914), 350372.
4. Eugene Salamin, *Computation of $ \pi $ using arithmetic-geometric mean*, Mathematics of Computation **30** (1976), no. 135, 565–570.
5. Paramanand Singh, *$ \pi $ and the AGM: Evaluating elliptic integrals*, 2009. [Link](https://paramanands.blogspot.com/2009/08/pi-and-the-agm-evaluating-elliptic-integrals.html#.Y2CvFILMJb8){:target="_blank"}.
