---
layout: Post
indent: true
permalink: /Gauss-Legendre
feedformat: card
title: The Gauss-Legendre Algorithm
---
<br>
## Table of Contents
1. [History](##History)
2. [Elliptic Integrals](##Elliptic-Integrals)

## 1. History
	
&emsp; The methods used for approximating $$ \pi $$ span millennia and severely vary in complexity; we will describe a few of the popular and more rigorous methods. The reference here is \cite{Bailey1996}. Around 200 BC, Archimedes approximated the circumference $$ C $$ and radius $$ r $$ of a circle by inscribing it in a polygons of $$ n $$ sides. It is not hard to see that as $$ n $$ approaches infinity, we get $$ \pi $$ using the circumference formula $$ C = 2 \pi r $$. Then during the invention of calculus in the 1600s, Newton and others used integrals and power series expansions to calculate $$ \pi $$. For instance, the identity

$$
	\arctan(x) 
	= \sum_{n=0}^{\infty} (-1)^{n} \frac{x^{2n+1}}{2n+1}
$$

evaluated at $$ x = 1 $$ gives us 

$$\
	\frac{\pi}{4} 
	= 1-\frac{1}{3}+\frac{1}{5}+\frac{1}{7}-\cdots.
$$ 

&emsp; Furthermore, in the 1700s, Euler calculated the values of the Riemann zeta function. Famously, for $$ x=2 $$, we get that 

$$
	\zeta(2) 
	= \sum_{n=1}^{\infty} \frac{1}{n^2}
	= \frac{\pi^2}{6}.
$$

The underlying problem is this family of methods are slow, often taking hundreds of iterations to even yield a couple of digits.
		
&emsp; In contrast, the Gauss-Legendre algorithm has quadratic convergence. Let us say we want to calculate 512 decimal places of $$ \pi $$. Then the Gauss-Legendre algorithm only needs 9 iterations, while almost all of the older methods (normally) need at least 800 iterations, if not significantly more. As an aside, Ramanujan's equations for $$ \pi $$

$$
	\frac{1}{\pi} 
	= \frac{2 \sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)! (1103+26390n)}{(n!)^4 396^{4n}}.
$$

only need around $$ 65 $$ iterations to converge. They are also now used for large approximations due to computational complexity and storage restrictions. 
		

## 2. Elliptic integrals
	
Let $$ (a \cos \theta, b \sin \theta) $$ be an ellipse parameterized by $$ \theta \in [0, 2 \pi] $$. Then it's arc-length is given by 

$$
	\int_{0}^{2 \pi} \sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta} d \theta. \label{eq:Length}
$$

This integral is not easy to compute in itself, and it was generalized to the study of so-called elliptic integrals in the early 1700s. Now notice that in \eqref{eq:Length} all of the data concerning our specific ellipse's arc-length is contained within the interval $$ 0 \leq \theta \leq \pi/2 $$. Hence, it would make sense to reduce our study to complete elliptic integrals, meaning those with amplitude $$ \pi/2 $$. Furthermore, we will restrict ourselves to complete elliptic integrals of the first and second kind. For the proof that every elliptic integral is of the first, second, or third kind, see \cite{Leffler1923}.
		
**Definition** Let

$$ 
\begin{aligned}
	F(k) & = \int_0^{\pi/2} \frac{1}{\sqrt{1 - k^2 \sin^2 \theta}} d \theta, \\
	E(k) & = \int_0^{\pi/2} \sqrt{1 - k^2 \sin^2 \theta} d \theta, \\
	F_S(a, b) & = \int_0^{\pi/2} \frac{1}{\sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta}} d \theta, \\
	E_S(a, b) & = \int_0^{\pi/2} \sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta} d \theta.
\end{aligned}
$$

Then $$ F(k) $$ and $$ E(k) $$ are called *complete elliptic integrals of the first and second kinds*, respectively, with *symmetric forms* $$ F_S(a, b) $$ and $$ E_S(a, b) $$. We refer to $$ k $$ as the modulus of our integral.

		
From here on we will assume that by elliptic integral we mean a complete elliptic integral of the first or second kind. 
		
We see that the ordinary and symmetric forms of elliptic integrals are related by the following proposition.
		
**Proposition** Let $$ k^2 = 1 - b^2/a^2 $$. Then 

$$
\begin{alined}
	F(k) & = a F_S(a, b) \\
	E(k) & = \frac{1}{a} E_S(a, b).
\end{aligned}
$$
	
*Proof:* Let us prove the second equation with the first following similarly. Substituting, we get 

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
		
We also recall a result regarding the symmetry of these integrals originally discovered by Legendre.

**Proposition.** (Legendre's Identity) *Suppose $$ k_1^2 + k_2^2 = 1 $$. Then 

$$
	F(k_1) E(k_2) + F(k_2) E(k_1) - F(k_1) F(k_2) = \frac{\pi}{2}
$$

holds.*
	
*Proof.* We leave the details of this proof to the reader. Taking the derivative with respect to $k_1$ shows that the L.H.S. is constant. To see that this value is $\pi/2$, we take the limit as $k_1$ goes to $0$. $$ \blacksquare $$
	
	
## Main results
		
We now prove the Gauss-Legendre algorithm. We will not discuss error analysis, which is done in \cite{Salamin1976}.
		
**Definition** Let $$ a_0, b_0 \in \RR $$. Let $$ a_{n+1} = (a_n + b_n)/2 $$ and $$ b_{n+1} = (a_n + b_n)^{1/2} $$ be the arithmetic and geometric means, respectively, of the $$ n $$th terms. Then we call their common limit $$ \lim a_n = \lim b_n = M(a_0, b_0) $$ the arithmetic-geometric (AM-GM) mean of $$ a_0 $$ and $$ b_0 $$.
	
**Theorem** (Gauss-Legendre) *Set $a_0 = 1$ and $b_0 = \sqrt{2}/2$. Then
$$
	\pi = \frac{2 M (1, \sqrt{2}/2)^2}{1 - \displaystyle{\sum_{n=0}^{\infty} 2^n (a_n^2 - b_n^2)}}
$$
holds.*
		
We need two lemmas in order to prove our result. 
		
**Lemma** Let $$ a_0 = a $$ and $$ b_0 = b $$ as in Definition 3.1. Set

$$
	S = a^2 - \sum_{n=0}^{\infty} 2^{n-1} \left( a_n^2 - b_n^2 \right).
$$

Then $$ E_S(a, b) = S F_S(a, b) $$. $$ \blacksquare $$
	
\begin{proof}
This proof is taken from \cite{Para09}. Consider the integral 

$$
\begin{aligned}
	L(a, b)
	& = a^2 F_S(a, b) - E_S(a, b) \\
	& = (a^2 - b^2) \int_0^{\pi/2} \frac{\sin^2 \theta}{\sqrt{a^2 \cos^2 \theta + b^2 \sin^2 \theta}} d \theta.
\end{aligned}
$$

Substituting $$ x^2 = a^2 \cos^2 \theta + b^2 \sin^2 \theta $$, 

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

Since $$ 2^n(a_n^2 - b_n^2) \to 0 $$, we get $$ 2^n L(a_n, b_n) \to 0 $$, and hence repeatedly applying this identity we get

$$
	L(a, b)
	= \sum_{n=0}^{\infty} 2^{n-1} (a_n^2 - b_n^2) F_S(a, b).
$$

Rewriting this equation in terms of (2) gives us the result. $$ \blacksquare $$
	
		
**Lemma** *The identity*

$$
F_S(a, b) = \frac{\pi}{2 M(a, b)}
$$

*holds. In particular,*

$$
F_S(1, \sqrt{2}) = \frac{\pi}{2 M(1, \sqrt{2})}.
$$

		
*Proof.* It is not hard to calculate the power series expansion

$$
	F(k)
	= \frac{\pi}{2M(1+k, 1-k)}
	= \sum_{n=0}^{\infty} \left( \frac{(2n-1)!!}{(2n)!!} k^n \right)^2.
$$

Calculating the AM and GM means gives us $M(1+k, 1-k) = M(1, \sqrt{1-k^2})$. Hence, applying \autoref{Symmetric} for $b/a = \sqrt{1-k^2}$, we get

$$
	a F_S(a, b) = \frac{\pi}{2 M(1, b/a)} \\
	F_S(a, b) = \frac{\pi}{2 M(a, b)},
$$

with the last equality following from the identity $$ M(ca, cb) = cM(a, b) $$. $$ \blacksquare $$
		
We finally have the tools we need to prove the Gauss-Legendre algorithm.
		
*Proof (Gauss-Legendre).* Set $$ k = \sqrt{2}/2 $$ to be our modulus. Then we notice $$ 2k^2 = 1 $$, and hence we can apply \autoref{Legendre} to get

$$
	2 F (k) E (k) - F(k)^2 = \frac{\pi}{2}.
$$

Now let us evaluate these integrals by first converting them into symmetric form then applying our lemmas. Since $$ k^2 = 1 - 1/k^2 $$, we can set $$ a = 1 $$ and $$ b = k $$ in \autoref{Symmetric} to get

$$
	2 F_S(1, k) E_S(1, k) - F_S(1, k)^2 = \frac{\pi}{2}.
$$

Then applying \autoref{Lemma1} gives us an equation only dependent on $$ F_S(1, k) $$ 

$$
	(2 S - 1) F_S(1, k)^2 = \frac{\pi}{2}.
$$

Finally, we apply \autoref{Lemma2} to write our equation in terms of the AM-GM mean

$$				
	(2S-1) \left( \frac{\pi}{2 M(1, k)} \right)^2 = \frac{\pi}{2} \\
	\pi = \frac{2M(1, k)^2}{2S-1},
$$

with plugging in $$ S $$ gives us our result. $$ \blacksquare $$