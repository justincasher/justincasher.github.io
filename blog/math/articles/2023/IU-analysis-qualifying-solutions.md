---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /iu-analysis-qualifying-solutions
title: IU analysis qualifying solutions
date: "August 2023"
abstract: "These are solutions to some of the Indiana University analysis qualifying problems. They are indexed by \"[Year] [Semester] [Number]\". I also include in each section some theorems which might be useful. I would like to thank Chia-Tz Liang and Anuvertika Pandey for pointing out errors or suggesting solutions. Please email me if you find any errors or have any solutions you would like to add. I also omitted adding a section on integration."
toc:
  - title: "Compact spaces"
    anchor: "1-compact-spaces"
  - title: "Sequences and series"
    anchor: "2-sequences-and-series"
  - title: "Uniform continuity"
    anchor: "3-uniform-continuity"
  - title: "Uniform convergence"
    anchor: "4-uniform-convergence"
  - title: "Derivatives"
    anchor: "5-derivatives"
  - title: "Optimization"
    anchor: "6-optimization"
  - title: "Convergence of integrals"
    anchor: "7-convergence-of-integrals"
  - title: "Polynomials and Stone-Weierstrass"
    anchor: "8-polynomials-and-stone-weierstrass"
  - title: "Stoke's theorem"
    anchor: "9-stokes-theorem"
  - title: "Inverse and implicit function theorems"
    anchor: "10-inverse-and-implicit-function-theorems"
---

## 1. Compact spaces 

Fix a topological space $ X $. We say $ X $ is *compact* if every open cover $ \{U_{\alpha}\} $ of $ X $ admits a finite subcover $ U_1, \dots, U_n $. 

**Heine-Borel theorem.** &nbsp; *Let $ X $ be a subset of $ \mathbb{R}^n $. Then $ X $ is compact with respect to the Euclidean metric if and only if $ X $ is closed and bounded.*

**Proposition 1.1.** &nbsp; *Let $ X $ be a topological space. Then $ X $ is compact if and only if there exists a subbase $ \mathcal{B} $ of $ X $ such that every open cover by elements of $ \mathcal{B} $ admits a finite subcover.*

**Theorem 1.2.** &nbsp; *Let $ X $ be a metric space. Then $ X $ is compact if and only if every sequence in $ X $ has a convergent subsequence.*

#### Problems

**2019 F P5.** &nbsp; *Let $ f \colon \mathbb{R}^n \to \mathbb{R}^m $ be continuous ($ n, m < \infty $), and let $ K \subseteq \mathbb{R}^n $ be compact. Show $ f(K) $ is compact.*

*Proof.* We show this holds for any $ f \colon X \to Y $ continuous. Let $ \{U_{\alpha}\} $ cover $ f(K) $. Then $ \{f^{-1}(U_{\alpha})\} $ forms an open cover of $ K $ by (the topological definition of) continuity, and hence admits a finite subcover $ f^{-1}(U_1), \dots, f^{-1}(U_n) $. We conclude that $ U_1, \dots, U_n $ cover $ f(K) $. $ \blacksquare $ 

*Alternative proof.* Let $ \{ y_n \} $ be a sequence in $ f(K) $. Then it lifts to a (not necessarily unique) sequence $ \{x_n\} $ in $ K $, i.e. $ f(x_n) = y_n $. By theorem 1.2, this sequence has a convergent subsequence $ \{x_{n_i}\} $, whose image $ \{ y_{n_i} \} $ is a convergent subsequence of $ \{ y_n \} $ by continuity, i.e. $ \lim_i f(x_{n_i}) = f(\lim_i x_{n_i}) $. $ \blacksquare $

**2019 W P2.** &nbsp; *Let $ X $ be a compact metric space with open cover $ \{U_{\alpha}\} $. Show that for some $ \varepsilon > 0 $ every ball of radius $ \varepsilon $ is contained in some $ U_{\alpha} $.*

*Proof.* Suppose not. Then there exists a sequence $ \{x_n\} $ such that the ball of radius $ 1/n $ at $ x_n $, i.e. $ B(x_n, 1/n) $ is not contained in any $ U_{\alpha} $. By theorem 1.2, there exists a convergent subsequence $ \{x_{n_i}\} $. Consequently, for $ N \gg 0 $ large, we have $ i > N $ implies $ x_{n_i} $ is contained in some $ U_{\alpha} $. We conclude that for $ i $ large, we have  $ B(x_i, 1/n_i) $ is contained in $ U_{\alpha} $ as well, a contradiction. $ \blacksquare $

**2017 F P1.** &nbsp; *Let $ X $ be the set of sequences $ \{ a_n \} $ with $ a_n \in \{0, 1\} $. Equip $ X $ with the metric*

$$
d(\{a_n\}, \{b_n\}) = 
\begin{cases} 
    0 & \text{if } \{a_n\} = \{b_n\} \\
    2^{-m} & \text{if } m = \min\{n \mid a_n \neq b_n \}.
\end{cases}
$$

*(a) Prove $ (X, d) $ is compact, and (b) that there exists no isolated points.*

*Proof.* (a) Let $ \{ a_{n, m}\} $ be a sequence in $ X $ indexed by $ m $. Without loss of generality, there exists infinitely many $ m $ such that $ a_{1, m} = 0 $. Deleting every term with $ a_{1, m} = 1 $ yields us an infinite subsequence. Repeating this deletion process inductively gives us a convergent subsequence.

(b) Suppose $ \{a_n\} $ is an isolated point. Then there exists an $ N \gg 0 $ with $ B(\{a_n\}, 2^{-N}) $ only containing $ \{a_n\} $. But

$$
b_n = 
\begin{cases}
    a_n & \text{if } n \leq N \\
    1-a_n & \text{if } n > N
\end{cases}
$$

is an element of $ X $ distinct from $ \{a_n\} $ contained in $ B(\{a_n\}, 2^{-N}) $. $ \blacksquare $

**2014 F P2.** &nbsp; *Let $ K $ be a compact subset of $ \mathbb{R}^n $, and let $ f \colon K \to \mathbb{R} $ be continuous. Prove that there exists an $ M \geq 0 $ such that for all $ x, y \in K $,*

$$
\|f(x)-f(y)\| \leq M \|x-y\| + \varepsilon.
$$

*Show this is not necessarily true for $ \varepsilon = 0 $.*

*Proof.* By continuity, there exists a $ \delta > 0 $ such that $ \|x-y\| < \delta $ implies $ \|f(x) - f(y)\| \leq \varepsilon $; consequently, we can assume $ \|x-y\| \geq \delta $. Then the Heinel-Borel theorem and 2019 F P5 show that $ K $ and $ f(K) $ are bounded, i.e. $ \|f(x) - f(y)\| < C $ for a fixed $ C $. Consequently, 

$$
\|f(x) - f(y) \| \leq C/\delta \|x-y\| + \varepsilon,
$$

and we set $ M = C/\delta $.

For a counterexample, consider $ f \colon [0, 1] \to [0, 1] $ with $ f(x) = \sqrt{x} $. We see $ \lim_{x \to 0^+} f'(x) = \infty $ implies no such $ M $ exists. $ \blacksquare $.




## 2. Sequences and series


**Monotone convergence theorem.** &nbsp; *Let $ \{a_n\} $ be a monotonically increasing sequence in $ \mathbb{R} $. Then $ \{a_n\} $ has a limit if and only if it is bounded.*


**Theorem 2.1.** &nbsp; *In $ \mathbb{R}^n $ every Cauchy sequence convergences, i.e. it is a complete metric space.*


**Ratio Test.** &nbsp; *Let $ \sum a_n $ be a series in $ \mathbb{R} $. Write $ L = \lim_n \|a_{n+1}/a_n\| $. Then $ L < 1 $ implies absolute convergence; $ L > 1 $ implies divergence; and $ L = 1 $ is inconclusive.*


**Root Test.** &nbsp; *Let $ \sum a_n $ be a series in $ \mathbb{R} $. Write $ r = \limsup_n \|a_n\|^{1/n} $. Then $ < 1 $ implies absolute convergence; $ r > 1 $ implies divergence; and $ r = 1 $ is inconclusive.*


**Integral Test.** &nbsp; *Let $ f \colon \mathbb{R} \to \mathbb{R}^+ $ be nonnegative and monotonically decreasing with $ f(n) = a_n $. Then $ \sum a_n $ converges if and only if $ \int_1^{\infty} f(x) dx < \infty $.*


**P-Series Test.** &nbsp; *A series of the form $ \sum_n n^{-p} $ converges if and only if $ p > 1 $.* 


**Limit Comparison Test.** &nbsp; *Let $ \{a_n\} $ and $ \{b_n\} $ be sequences in $ \mathbb{R} $. Suppose $ L = \lim a_n / b_n $ exists. Then $ \sum a_n $ converges if and only if $ \sum b_n $ converges.*


**Alternating Series Test.** &nbsp; *Suppose $ \{a_n\} $ is a monotonically decreasing sequence in $ \mathbb{R}^+ $ with $ \lim_n a_n = 0 $. Then $ \sum (-1)^n a_n $ converges.*


**Theorem 2.2.** &nbsp; *Let $ \{a_n\} $ be a sequence in $ \mathbb{R}^+ $. Then $ \prod_n (1+a_n) $ converges if and only if $ \sum_n a_n $ converges. If $ 0 < a_n < 1 $, then $ \prod_n (1-a_n) \neq 0 $ if and only if $ \sum_n a_n $ converges.*


**Banach fixed point theorem.** &nbsp; *Let $ (X, d) $ be a complete metric space, and let $ f \colon X \to X $ be contractive. Then $ X $ has a unique fixed point $ f(x_\ast) = x_\ast $, which is given by taking n arbitrary $ x_0 \in X $, setting $ x_{n+1} = f(x_n) $, and evaluating $ \lim_n f(x_n) = x_\ast $.*



#### Problems


**2023 W P2.** &nbsp; *Consider the series $ \sum_{a, b \geq 0} p^{-a} p^{-b} $ for fixed $ p, q $ prime. Prove it converges and find its sum.*

*Proof.* For each $ r > 0 $ even, we see 

$$
\left( \sum_{a=0}^{r/2} p^{-a} \right) \left( \sum_{b=0}^{r/2} q^{-b} \right) \leq
\sum_{a+b \leq r} p^{-a} q^{-b} 
\leq \left( \sum_{a=0}^{r} p^{-a} \right) \left( \sum_{b=0}^{r} q^{-b} \right).
$$

Hence, as $ r $ goes to infinity, our sum goes to 

$$
\left( \sum_{a=0}^{\infty} p^{-a} \right) \left( \sum_{b=0}^{\infty} q^{-b} \right)
= \left( \frac{1}{1-p^{-1}} \right) \left( \frac{1}{1-q^{-1}} \right)
$$

giving us our limit. $ \blacksquare $


**2023 W P5.** &nbsp; *Show*

$$
\lim_n \left( \sum_{k=1}^{n} \frac{\sqrt{k}}{n} - \frac{2}{3} \sqrt{n} \right) = 0.
$$

*Proof.* We see 

$$
\int_1^n \frac{\sqrt{x}}{n} dx \leq \sum_{k=1}^{n} \frac{\sqrt{k}}{n} \leq \int_0^n \frac{\sqrt{x}}{n} dx.
$$

Integrating yields

$$
\frac{2}{3} - \frac{2}{3n} \leq \sum_{k=1}^{n} \frac{\sqrt{k}}{n} \leq \frac{2}{3} \sqrt{n}, 
$$

or equivalently 

$$
-\frac{2}{3n} \leq \sum_{k=1}^{n} \frac{\sqrt{k}}{n} - \frac{2}{3} \sqrt{n} \leq 0.
$$

Letting $ n $ approach infinity gives us the desired equality. $ \blacksquare $


**2022 F P1.** &nbsp; *Define $ \{x_n\} $ by $ 0 < x_1 < 1 $ and $ x_{n+1} = 1 - \sqrt{1-x_n} $. Prove that (a) $ \{x_n\} $ monotonically decreases to $ 0 $, and that (b) $ \lim_n x_{n+1}/x_n = 1/2 $.*

*Proof.* (a) Set $ y_n = 1-x_n $ so that $ y_{n+1} = \sqrt{y_n} $. Then $ y_1 \neq 0 $ implies $ \lim_n y_n = 1 $ (this is well known). Thus, $ \lim_n x_n = \lim_n 1-y_n = 0 $. To show $ x_n $ is monotonically decreasing, we observe $ y_n $ is monotonically increasing, i.e. $ \sqrt{x} > x $ for $ x \in (0, 1) $. 

(b) By L'Hôpital's Rule, 

$$
\lim_{n \to \infty} \frac{x_{n+1}}{x_n}
= \lim_{x \to 0} \frac{1-\sqrt{1-x}}{x} 
= \lim_{x \to 0} \frac{1}{2 \sqrt{1-x}} 
= \frac{1}{2},
$$

and so the limit is $ 1/2 $. $ \blacksquare $


**2022 W P2.** &nbsp; *Let $ \{a_n\} $ be a sequence in $ \mathbb{R} $. If $ \sum_n \| a_n - a_{n+1} \| < \varepsilon $, then the sequence is convergent.*
 
 *Proof.* Fix $ \varepsilon > 0 $. Then there exists an $ N \gg 0 $ such that $ m \geq n \geq N $ implies 
 
 $$
 \| a_n - a_m \| \leq \sum_{k=N}^{\infty} \| a_k - a_{k+1} \| < \varepsilon.
 $$
 
 We conclude that our sequence is Cauchy, and hence has a limit. $ \blacksquare $
 

 **2022 W P7.** &nbsp; *Suppose $ \{a_n\} $ is an unbounded increasing sequence in $ \mathbb{R}^+ $. Show $ \sum_n (a_{n+1}-a_n)/a_n $ diverges.*
 
 *Proof.* Fix $ N \gg 0 $. Since $ \{a_n\} $ is unbounded, there exists an $ M > N $ such that $ a_{M+1} > 2 a_N $. Hence, 
 
 $$
 \sum_{n=N}^{M} \frac{a_{n+1}-a_n}{a_n} 
 \geq \sum_{n=N}^{M} \frac{a_{n+1}-a_n}{a_{M+1}} 
 = \frac{a_{M+1} - a_N}{a_{M+1}}
 > 1/2.
 $$
 
We conclude that the partial sums do not converge. $ \blacksquare $
 
*Alternative proof.* The inequality $ x \geq \log(1+x) $ implies 

$$
\sum_n \frac{a_{n+1}-a_n}{a_n}
= \sum_n \frac{a_{n+1}}{a_n} - 1
\geq \sum_n \log(a_{n+1}/a_n)
= \lim_n a_n - a_1,
$$

which diverges since $ \{a_n\} $ is unbounded. $ \blacksquare $


**2022 W P6.** &nbsp; *Let $ t_0 \in \mathbb{R} $ and set $ t_{n+1} = \sin(\cos(t_n)) $. Prove this sequence converges with limit independent of $ t_0 $.*

*Proof.* Consider $ f(x) = \sin(\cos(x))) $ as a function $ f \colon [0, 2 \pi] \to [0, 2 \pi] $. Set $ g(x) = f(f(x)) $. Computing the derivative, we observe that $ \|g'(x)\| < 1 $ for each $ x \in [0, 2 \pi] $, so $ g $ is a contraction on $ [0, 2 \pi] $, and consequently $ g $ admits a unique fixed point by the Banach fixed point theorem. We conclude that our desired sequence has a unique limit independent of $ t_0 $, because $ f $ does not oscillate between 2 distinct points anywhere. $ \blacksquare $


**2021 F P6.** &nbsp; *Let $ a_0 \in (0, 1) $ and $ a_{n+1} = a_n^3 - a_n^2 + 1 $. Prove that (a) $ \{a_n\} $ converges and find its limit; and (b) that $ b_n = \prod_{i=1}^{n} a_i $ converges and find its limit.*

*Proof.* (a) We observe $ a_{n+1} > a_n $ is equivalent to $ a_n^3 - a_n^2 - a_n + 1 > 0 $.  Writing this as a polynomial $ f(x) = x^3 - x^2 - x + 1 $, we observe  $ f(x) = (x-1)^2 (x+1) $ and $ f(0) = 1 $. Hence $ f $ is strictly positive on $ (-1, 1) $, and our sequence is monotonically increasing. We further observe $ a_n^3 - a_n^2 +1 < 1 $ implies $ a_n < 1 $, which is true by assumption, so our sequence is bounded above by $ 1 $; thus, our sequence has a limit. To find the limit $ a_* $, we see 

$$
\lim_n a_{n+1} = \lim_n a_n^3 - a_n^2 + 1 
$$

implies 

$$
a_* = a_*^3 - a_*^2 + 1,
$$

and the only root of this polynomial on $ (0, 1] $ is $ 1 $. Thus, $ a _* = 1 $.


(b) Since $ \{b_n\} $ is a bounded monotonically decreasing sequence, its limit exists. The limit is $ 0 $, but I am not sure how to show this directly. $ \blacksquare $ 


**2021 F P8.** &nbsp; *Is the series* 

$$ 
\sum_{n = 100}^{\infty} \ln(n)^{-\ln(\ln(n))}
$$

*convergent?*

*Proof.* By the integral test, our series converges if and only if the integral

$$
I = \int_{100}^{\infty} \ln(x)^{-ln(ln(x))} dx
$$

does. Substituting $ u = \ln(x) $ and $ dx = e^u du $, we have 

$$
I = \int_{ln(100)}^{\infty} u^{-\ln(u)} e^u du.
$$

The following inequalities are equivalent:

$$
\begin{aligned}
e^x & > x^{\ln(x)} \\
\log_x(e^x) & > \ln(x) \\
\frac{\ln(e^x)}{\ln(x)} & > \ln(x) \\
x & > \ln(x)^2.
\end{aligned}
$$

We conclude that $ u^{-\ln(u)} e^u > 1 $, our interal diverges, and so does our series. $ \blacksquare $


**2020 F P1.** &nbsp; *Let $ x_0 > 0 $ and $ x_{n+1} = \frac{1}{2} (x_n + \frac{4}{x_n}) $. Show that (a) $ x_{n+1} \geq 2 $ for $ n \geq 0 $, (b) $ x_{n+1} \leq x_n $ if $ n \geq 1 $, (c) $ \lim x_n = x_\ast $ exists, and (d) find $ x_\ast $.*

*Proof.* (a) By the AM-GM inequality (cf. optimization), 

$$
x_{n+1}
= \frac{1}{2} (x_n + \frac{4}{x_n})
\geq \sqrt{x_n \frac{4}{x_n}}
= 2
$$

for $ n \geq 0 $. 

(b) We see $ x_{n+1} \leq x_n $ if and only if 

$$
\frac{1}{2}(x_n + \frac{4}{x_n}) \leq x_n,
$$

which reduces to $ 2 \leq x_n $. This is true by (a).

(c) Our sequence is bounded below and monotonically decreasing, so it has a limit.

(d) Write $ x_* = \lim_n x_n $. We observe

$$
\lim_n x_{n+1} = \lim_n \frac{1}{2} (x_n + \frac{4}{x_n})
$$

implies

$$
x_* = \frac{1}{2} (x_* + \frac{4}{x_*}).
$$

Solving this equation shows $ x_* = 2 $ is the only positive solution, and thus our limit.  

Alternatively, define $ f \colon [1.5, \infty) \to [1.5, \infty) $ by $ f = \frac{1}{2}(x + \frac{4}{x}) $. Then $ f'(x) = \frac{1}{2} (1 - \frac{4}{x^2}) $ is strictly less than $ 1 $ on our domain, so $ f $ is a contraction. Applying the Banach fixed point theorem to $ [1.5, \infty) $ tells us our sequence has a unique limit. Solving $ x_\ast = \frac{1}{2} \left( x_{*} + \frac{4}{x_\ast} \right) $ yields $ x_\ast = 2 $. $ \blacksquare $


**2020 W P1.** &nbsp; *Let $ \{a_n\} $ be a sequence in $ \mathbb{R}^+ $ with $ \lim a_n = 0 $. Show there exists infinitely many $ N \in \mathbb{N} $ such that $ n \geq N $ implies $ a_n \leq a_N $.*

*Proof.* Let 

$$ 
N = \sup\{n \mid a_n \geq a_0 \},
$$

which is finite since our sequence converges to 0. Then $ n \geq N $ implies $ a_n \leq a_N $. Now delete the first $ n $ terms and repeat to get infinitely many such $ N $. $ \blacksquare $


**2020 w P2.** &nbsp; *Write $ \{a_n\} $ for a sequence in $ \mathbb{R}^+ $ such that $ \lim_n a_n = 0 $ and $ \|a_n - a_{n+1}\| \leq n^{-2} $. Prove $ \sum_n (-1)^{n-1} a_n $ converges.*

*Proof.* We will show the partial sums converge. Fix $ \varepsilon > 0 $, and choose $ N \gg 0 $ such that $ a_n < \varepsilon/2 $ for $ n \geq N $ and 

$$ 
\sum_{k = \lfloor N/2 \rfloor}^{\infty} \frac{1}{n^2} < \frac{\varepsilon}{2}.
$$

(This is possible by the p-series, or integral, test.) Then for each $ M > N $, we see that if $ N $ is odd 

$$
|\sum_{n=N}^M (-1)^{n-1} a_n|
\leq \sum_{n=N/2}^{\lceil M/2 \rceil} |a_n - a_{n+1}|
< \frac{\varepsilon}{2}
$$

and if $ N $ is even

$$
|\sum_{n=N}^M (-1)^{n-1} a_n|
\leq |a_N| + |\sum_{n=N+1}^M (-1)^{n-1} a_n |
< \frac{\varepsilon}{2} + \frac{\varepsilon}{2}.
$$

Thus, our series converges. $ \blacksquare $


**2020 W P4.** &nbsp; *Show*

$$
a_n = \sqrt{2\sqrt{3\sqrt{\cdots\sqrt{n}}}}
$$

*converges in $ \mathbb{R} $.*

*Proof.* First we observe that our sequence is monotonically increasing, and hence we need to show it is bounded. Rewrite each term as 

$$
a_n = \prod_{k=2}^{n} k^{2^{-k}}.
$$

Since the logarithm is continuous, we see our sequence is bounded if and only if the sequence 

$$
\ln(a_n) 
= \sum_{k=1}^{n} \frac{1}{2^k} \ln(k)
$$

is. Since $ \ln(k) \leq \sqrt{k} $ and $ 2^k \geq k^2 $, we have 

$$
\lim_{n \to \infty} \ln(a_n)
\leq \sum_{k=1}^{\infty} \frac{1}{n^2} \sqrt{n}
\leq \sum_{k=1}^{\infty} \frac{1}{n^{3/2}},
$$

which is bounded by the p-series test. Thus, $ \{a_n\} $ is bounded. $ \blacksquare $




## 3. Uniform continuity


Let $ f, g \colon X \to Y $ be maps between metric spaces. We say $ f $ is *uniformly continuous* if for each $ \varepsilon > 0 $, there exists a $ \delta > 0 $ such that $ d_X(x, y) < \delta $ implies $ d_Y(f(x), f(y)) < \varepsilon $ for all $ x, y \in X $.


**Heine-Cantor theorem.** &nbsp; *Let $ f \colon  \to Y $ be continuous. If $ X $ is compact, then $ f $ is uniformly continuous.*



#### Problems


**2020 W P3.** &nbsp; *Let $ X $ be the space of sequences $ x = \{x_n\} $ with $ x_n \in [0, 1] $. Set $ d(x, y) = \sup_n \| x_n - y_n \| $. Suppose $ f \colon X \to \mathbb{R} $ is uniformly continuous. Prove that $ f $ is bounded.*

*Proof.* Choose a $ \delta > 0 $ such that $ d(x, y) \leq \delta $ implies $ \| f(x)-f(y) \| < 1 $. Set $ M = \lceil 1 / \delta \rceil $. Now fix $ x \in X $, and define $ x_n = \frac{n}{M} x $ for $ 0 \leq n \leq M $. Then, using that $ d(x_{n+1}, x_n) < \delta $, we have

$$
\|f(x)\| 
\leq \sum_{n=0}^{M-1} \|f(x_{n+1}) - f(x_n)\|
< M.
$$

Thus, $ f $ is a bounded function. $ \blacksquare $


**2020 W P7.** &nbsp; *Let $ f \colon \mathbb{R} \to \mathbb{R} $ be continuous and $ f' \colon \mathbb{R} \to \mathbb{R} $ uniformly continous. If $ \displaystyle \lim_{x \to \infty} f(x) = 0 $, does $ \displaystyle \lim_{x \to \infty} f'(x) $ exist?*

*Proof.* We will show the derivative goes to $ 0 $. Suppose not. Then there exists a sequence $ \{x_n\} $ such that $ \| f'(x_n) \| > C $ for some $ C > 0 $ and $ \lim_n x_n = \infty $. Without loss of generality, we suppose $ f'(x_n) > C $. Since $ f' $ is uniformly continuous, there exists a $ \delta > 0 $ so that $ \| x-y \| < \delta $ implies $ \| f'(x) - f'(y) \| < C/2 $. Therefore, 

$$
\int_{x_n - \delta}^{x_n + \delta} f'(x) dx 
\geq \int_{x_n-\delta}^{x_n+\delta} C/2 dx 
= \delta C,
$$

which implies $ f(x_n + \delta) \geq f(x_n - \delta) + \delta C $. This contradicts $ f $ having limit $ 0 $. $ \blacksquare $


**2019 W P5.** &nbsp; *Give an example of a continuous function $ f \colon (0, 1] \to \mathbb{R} $ that attains neither a maximum nor a minimum. (b) Show that if $ f $ is uniformly continuous, then it must attain a maximum or a minimum.*

*Proof.* (a) Consider $ f(x) = (1-x) \sin(\frac{1}{x}) $. This is a continuous function which obtains no maximum or minimum, because $ \sin(\frac{1}{x}) $ is oscillating, and $ (1-x) $ causes $ f $ to decrease in absolute value away from $ 0 $.

(b) Suppose not. Then there exists sequences $ \{x_n\} $ and $ \{y_n\} $ in $ (0, 1] $ with $ \lim_n x_n = 0 $ (resp. $ \lim y_n = 0 $), $ f(x_n) $ monotonically increasing (resp. $ f(y_n) $ monotonically decreasing), and $ \lim_n f(x_n) = \sup f(x) $ (resp. $ \lim_n f(y_n) = \inf f(x) $). Since $ f $ is uniformly continuous, there exists a $ \delta > 0 $ such that $ \|x-y\| < \delta $.


**2018 F P5.** &nbsp; *Let $ B $ be the closed unit ball in $ \mathbb{R}^2 $. Set $ \rho(x, y) = \|x-y\| $ if $ x $ and $ y $ are collinear and $ \rho(x, y) = \|x\| + \|y\| $ elsewise. This is a metric on $ B $. Suppose $ f \colon (B, \rho) \to \mathbb{R} $ is uniformly continuous. Show $ f $ is bounded.*

*Proof.* Using the same proof technique as 2020 W P3, we are reduced to showing $ \rho $ is a bounded function on $ B $. Clearly $ \rho(x, y) \leq 2 $. $ \blacksquare $


**2017 W P6.** &nbsp; *Let $ f \colon \mathbb{R}^n \to \mathbb{R} $ be continuous with $ n < \infty $. Suppose $ \displaystyle \lim_{\|x\| \to \infty} f(x) = 0 $. Prove that $ f $ is uniformly continuous.*

*Proof.* Fix $ \varepsilon > 0 $. Write $ D_r $ for the closed disk of radius $ r $ at $ 0 $. By assumption, there exists an $ r > 0 $ such that $ x, y \in \mathbb{R}^{n} \setminus D_r $ implies 

$$
\| f(x) - f(y) \|
\leq \|f(x)\| + \|f(y)\| 
< \frac{\varepsilon}{2} + \frac{\varepsilon}{2}
= \varepsilon.
$$

Thus, $ f $ is uniformly continuous on $ \mathbb{R}^n \setminus D_r $. Furthermore, $ D_{r+1} $ is compact, so $ f $ is uniformly continuous on $ D_{r+1} $ by the Heine-Borel theorem. Since our desired property is local and every point has a ball of radius $ 1/2 $ contained in $ D_{r+1} $ or $ \mathbb{R}^{n} \setminus D_r $, we get our result. $ \blacksquare $




## 4. Uniform convergence


Let $ X, Y $ be metric spaces, and let $ f, g \colon X \to Y $ be functions. Define the *uniform metric* by 

$$
\rho(f, g)
= \sup_{x \in X} d_Y(f(x), g(x)). 
$$

(This need not be a metric if $ d_Y $ is unbounded on $ f(X) $.) We say a sequence of functions $ f_n \colon X \to Y $ converges uniformly to $ f_* $ if it does with respect to $ \rho $. We say $ \{f_n\} $ is *uniformly equicontinuous* if for every $ \varepsilon > 0 $, there exists a $ \delta > 0 $ such that $ d_X(x, y) < \delta $ implies $ d_Y(f_n(x), f_n(y)) < \varepsilon $ for all $ n $.

Now assume $ K $ is a compact subset of $ \mathbb{R}^m $, and our sequence is $ f_n \colon K \to \mathbb{R}^n $. We say $ \{f_n\} $ is *uniformly bounded* if there exists an $ M $ such that 

$$
\sup_{x \in K, n \in \mathbb{N}} \|f_n(x)\| \leq M.
$$


**Ascoli-Arzelà theorem.** &nbsp; *Let $ K \subset \mathbb{R}^m $ be compact, and let $ f_n \colon K \to \mathbb{R}^n $ be a sequence of functions. If $ \{f_n\} $ is uniformly bounded and uniformly equicontinuous, then there exists a subsequence which converges uniformly.*


**Weierstrass M-Test.** &nbsp; *Let $ f_n \colon X \to \mathbb{R}^n $ be a sequence of functions defined on a set $ X $. Set $ M_n = \sup_x \| f_n(x) \| $. If $ \sum M_n $ converges, then $ \sum f_n(x) $ converges absolutely and uniformly.*


**Uniform limit theorem.** &nbsp; *Write $ X $ for a topological space and $ Y $ a metric space. If $ f_n \colon X \to Y $ are continuous and converge uniformly to $ f \colon X \to Y $, then $ f $ is continuous. (In other words, the space of continuous functions are closed with respect to $ \rho $.)*


**Theorem 4.1.** &nbsp; *Let $ f_n \colon [a, b] \to \mathbb{R} $ be integrable with uniform limit $ f $. Then $ \int_a^b f dx = \lim_n \int_a^b f_n dx $.*


**Theorem 4.2.** &nbsp; *Suppose $ f_n \colon [a, b] \to \mathbb{R} $ are differentiable such that their derivatives $ f_n' $ converge uniformly on $ [a, b] $. If $ f_n(x_0) $ converges for some point $ x_0 \in [a, b] $, then $ f_n $ converge uniformly to some $ f $, and $ f'(x) = \lim_n f_n'(x) $.*



#### Problems


**2023 W P1.** &nbsp; *Let $ f_n \colon [0, 1] \to \mathbb{R}^+ $ be monotonically increasing with uniform limit $ f $. Prove that*

$$
\lim_n \int_0^1 \left( \sum_{k=1}^{n} f_k(x)^n \right)^{1/n} dx 
= \int_0^1 f(x) dx.
$$

*Proof.* Recall that for the $ \ell^p $ norm on sequences, we have $$ \lim_p \| (a_n) \|_p = \| (a_n) \|_{\infty} $$. Hence, 

$$
f(x) = \lim_n \left( \sum_{k=1}^n f_k(x)^n \right)^{1/n}
$$

uniformly. Our result then follows from theorem 4.1. $ \blacksquare $

*Anuvertika's proof.* Set 

$$
a_n(x) = \left( \sum_{k=1}^n f_k(x) \right)^{1/n}.
$$

Fix $ x \in [0, 1] $; then

$$
f_n(x)
= (f_n(x)^n)^{1/n} 
\leq a_n
\leq \left( \sum_{k=1}^n f_n(x) \right)^{1/n}
= n^{1/n} f_n(x)
$$

combined with $ n^{1/n} \to 1 $ implies $ a_n(x) \to f(x) $ pointwise. Since $ \{ a_n(x) \} $ is monotonically increasing, we apply 2022 F P2 to show the convergence is uniform. $ \blacksquare $


**2023 W P3.** &nbsp; *Let $ f_n \colon [0, 1] \to \mathbb{R} $ be a sequence of function. Suppose that for some $ f \colon [0, 1] \to \mathbb{R} $, we have*

$$
\lim_n f_n(x_n) = f(\lim_n x_n)
$$

*for every sequence $ \{x_n\} $ in $ [0, 1] $. Show $ \{f_n\} $ converges uniformly to $ f $ or provide a counterexample.*

*Proof.* Suppose not. Then there exists sequences $ a_n \in \mathbb{N} $, $ a_n $ increasing and $ x_n \in [0, 1] $ such that 

$$
|f_{a_{2n}}(x_n) - f_{a_{2n+1}}(x_n) | > \varepsilon 
$$

for some fixed $ \varepsilon > 0 $. Since $ [0, 1] $ is compact $ x_n $ admits a convergent subsequence $ x_{n_k} $ with limit $ x_* $; let us assume without loss of generality $ x_n $ has limit $ x_* $. Define a sequence $ \{y_n\} $ by 

$$ 
y_{a_{2n}} = y_{a_{2n+1}} = x_n 

$$

and $ y_n = x_* $ elsewise. Then $ f_n(y_n) $ is not a Cauchy sequence by assumption, but $ \lim_n f_n(y_n) = f(x_*), $ a contradiction. 

This if false if the domain is not compact: consider $ f_n \colon \mathbb{R} \to \mathbb{R} $ given by $ f_n = x/n $. $ \blacksquare $

**2023 W P4.** &nbsp; *Does there exists a sequence of continuously differentiable functions that converge uniformly to a non-differentiable function?*

*Proof.* Yes, we see that $ f_n = \sqrt{x^2+1/n} $ is continuously differentiable, but $ f_n $ converge to $ \|x\| $ uniformly on $ \mathbb{R} $. $ \blacksquare $

**2022 F P2.** &nbsp; *Suppose $ f_n \colon [a, b] \to \mathbb{R} $ converge pointwise to $ f $ and that each $ f_n $ is monotonically increasing. Then $ f_n $ converge uniformly to $ f $.* 

*Proof.* Fix $ \varepsilon > 0 $. Observe that this implies $ f $ is monotonically increasing, so we can partition $ [a, b] $ into intervals $ [t_i, t_{i+1}] $ such that 

$$ 
\|f(t_{i+1}) - f(t_i) \| < \varepsilon/5.
$$ 

Choose an $ N \gg 0 $ such that for $ n \geq N $ we have 

$$ 
\| f_n(t_i) - f(t_i) \| < \varepsilon/5
$$

for each $ i $. We observe 

$$ 
\begin{aligned}
\| f_n(t_{i+1}) - f_n(t_i)\| & \leq \| f_n(t_{i+1}) - f(t_{i+1}) \| + \| f(t_{i+1}) - f(t_i) \| \\
& \quad + \| f(t_i) - f_n(t_i) \| \\
& < \frac{3\varepsilon}{5}.
\end{aligned}
$$

Therefore, for any $ x \in [t_i, t_{i+1}] $, we have 

$$
\begin{aligned}
\| f_n(x) - f(x) \| & \leq \| f_n(x) - f(t_{i+1}) \| + \| f(t_{i+1}) - f(x) \| \\
& < \| f_n(x) - f(t_{i+1}) \| + \frac{\varepsilon}{5} \\
& \leq \| f_n(x) - f_n(t_{i+1}) \| + \| f_n(t_{i+1}) - f(t_{i+1}) \| + \frac{\varepsilon}{5} \\
& < \| f_n(x) - f_n(t_{i+1}) \| + \frac{2\varepsilon}{5} \\ 
& \leq \| f_n(t_{i+1}) - f_n(t_i) \| + \frac{2\varepsilon}{5} \\ 
& < \varepsilon.
\end{aligned}
$$

Hence, $ f_n $ converges uniformly to $ f $. $ \blacksquare $

**2022 F P9.** &nbsp; *Define $ F \colon \mathbb{R} \to \mathbb{R} $ by*

$$
F(x) = \sum_{n=1}^{\infty} \frac{1}{n^x}.
$$

*(a) Prove that $ F $ converges uniformly on $ [1+\delta, \infty) $ for any $ \delta > 0 $ . Explain why $ f $ is continuous on $ (1, \infty) $. Is $ f $ continuous on $ [1, \infty) $? (b) Prove $ f $ is continuously differentiable on $ (1, \infty) $ with* 

$$
F'(x) 
= - \sum_{n=1}^{\infty} \frac{\ln(n)}{n^x}.
$$

*Proof.* (a) On $ [1+ \delta, \infty) $ we have $ n^{-x} \leq n^{-(1+\delta)} $. Since 

$$ 
\sum_{n=1}^{\infty} \frac{1}{n^{1+\delta}} 
$$ 

converges by the p-test, the Weierstrauss M-test implies $ F $ converges uniformly. $ F $ is continuous by the uniform limit theorem. $ F $ is not continuous at $ 1 $ since it approaches infinity as $ x $ approaches $ 1 $.

(b) We see that 

$$
\frac{d}{dx} \frac{1}{n^x} = - \ln(n) \frac{1}{n^x}.
$$

Again, in order to apply the Weierstrass M-Test for $ \delta > 0 $, we observe 

$$
\begin{aligned}
F'(1+\delta) & = -\sum_{n=1}^{\infty} \ln(n) \frac{1}{n^{-(1+\delta)}} \\
& \leq - \int_1^{\infty} \ln(x) x^{-(1+\delta)} dx;
\end{aligned}
$$

setting $ u = \ln(x) $ and $ du = x^{-1} $, 

$$
\begin{aligned}
F'(1+\delta) & = \int_0^{\infty} e^{-\delta u} du < \infty.
\end{aligned}
$$

We conclude that $ F'(x) $ converges uniformly, and that it is indeed the derivative of $ F $ by theorem 4.2. $ \blacksquare $

**2022 W P1.** &nbsp; *Define $ f_n \colon [0, 1] \to \mathbb{R} $ by*

$$
f_n(x) 
= \frac{1+x^n}{1+2^{-n}}.
$$

*Show $ \{f_n\} $ is not equicontinuous.*

*Proof.* Let $ x_n = (1/2)^{1/n} $ and $ y_n = (3/4)^{1/n} $. Then $ \lim_n \| x_n - y_n \| = 0 $, but 

$$
\lim_n \| f(x_n) - f(y_n) \| 
= \lim_n \frac{1/2 - 3/4}{1 + 2^{-n}}
= \frac{1}{4},
$$

so our sequence is not equicontinuous. $ \blacksquare $

**2021 F P7.** &nbsp; *Let $ f_n \colon [0, 1]^2 \to \mathbb{R} $ be a uniformly bounded sequence of continuous functions. Set*

$$
F_n(x, y) = \int_y^1 \int_x^1 s^{-1/2} t^{-1/3} f_n(s, t) ds dt.
$$

*(a) Show for each $ n $ that $ F_n(x, y) $ is well defined. (b) Show that $ \{F_n\} $ has a subsequence $ \{F_{n_j}\} $ which converges uniformly to a continuous $ F $.*

*Proof.* (a) Since the $ \{f_n\} $ are uniformly bounded there exists an $ M \in \mathbb{R} $ such that 

$$
\sup_{n \in \mathbb{N}, (x, y) \in \mathbb{R}^n} \| f_n(x, y) \| \leq M.
$$

Hence, 

$$ 
\begin{aligned}
\| F_n(x, y) \| & \leq M \int_y^1 t^{-1/3} dt \int_x^1 s^{-1/2} ds \\
& = M [\frac{3}{2} t^{2/3} \mid_y^1 ] [2 s^{1/2} \mid_x^1 ] \\
& = 3 M (1-y^{2/3})(1-x^{1/2}).
\end{aligned}
$$

This limit is bounded as $ (x, y) $ approaches $ 0 $, and hence $ F_n $ is well defined. 

(b) In (a) we showed that $ \{F_n\} $ is uniformly bounded by $ 3M $. Letting $ x_2 \geq x_1 $ and $ y_2 \geq y_1 $ with loss of generality, we see for each $ n \in \mathbb{N} $

$$
\begin{aligned}
\|F_n(x_1, y_1) - F_n(x_2, y_2)\| & = \| \int_{y_1}^{y_2} \int_{x_1}^{x_2} s^{-1/2} t^{-1/3} f_n(s, t) ds dt \| \\
& \leq 3M (y_2^{2/3} - y_1^{2/3})(x_2^{1/2} - x_1^{1/2}).
\end{aligned}
$$

Since both $ x^{1/2} $ and $ y^{2/3} $ are continuous functions, we see that $ \{F_n\} $ is equicontinuous. Hence, by the Ascoli-Arzelà theorem we can find our desired subsequence. $ \blacksquare $


**2020 F P9.** &nbsp; *Let $ f_n \colon [0, 1] \to [0, 1] $ converge uniformly to $ f \colon [0, 1] \to [0, 1] $ (a not necessarily continuous function). Suppose the $ f_n $ map compact sets to compact sets. Does $ f $ map compact sets to compact sets?*

*Proof.* Not necessarily. Set 

$$
f_0(x)) =
\begin{cases}
    0 & \text{if } x = 2^{-n} \text{ for some } n \\
    1 & \text{elsewise},
\end{cases}
$$

and inductively define

$$
f_{n+1}(x) =
\begin{cases}
    x & \text{if } x = 2^{-(n+1)} \\
    f_n(x) & \text{elsewise}.
\end{cases}
$$

Then the sequence $ \{f_n\} $ converges uniformly to the function 

$$
f(x) = 
\begin{cases}
    x & \text{if } x = 2^{-n} \text{ for some } n \\
    1 & \text{elsewise}.
\end{cases}
$$

Each $ f_n $ is compact (its image contains finitely many points). Although, the image of $ x_n = 2^{-n} $ by $ f $ is not compact: it contains $ 1 $ and $ 2^{-n} $ for each $ n $, but not $ 0 $. $ \blacksquare $

**2020 W P8.** &nbsp; *Let $ f \colon \mathbb{R} \to \mathbb{R} $ be continuous with $ f(x+1) = f(x) $. Define $ f_n \colon \mathbb{R} \to \mathbb{R} $ by $ f_1 = f $ and for $ n > 1 $*

$$
f_n(x) 
= \frac{1}{2} (f_{n-1}(x-2^{-n}) + f_{n-1}(x+2^{-n})).
$$

*Show that $ f_n $ converges uniformly on $ \mathbb{R} $.* $ \blacksquare $ 

*Proof.* Since $ f $ is periodic we can consider it as a bounded and uniformly continuous function on $ [0, 1] $. Let $ \varepsilon > 0 $, and choose an $ n \gg 0 $ such that $ \| x-y \| < 2^{-n} $ implies $ \|f(x) - f(y)\| < \varepsilon $. We observe that we can write $ f_n(x) $ as a sum of $ 2^n $ functions of the form $ f(x+a_i) $. In particular, we can write $ f_{n+k}(x) $ as a sum of $ 2^{n+k} $ functions of the form $ f(x+b_i) $, such that for each $ a_i $ the nearest $ 2^k $ of the $ b_i $ satisfy

$$
\|a_i - b_i\|
\leq \sum_{j=1}^{k} \frac{1}{2^{-n-j}} 
< \sum_{j=1}^{\infty} \frac{1}{2^{-n-j}}  
= 2^{-n}.
$$

Consequently, 

$$
\|f_{n+k}(x) - f_n(x) \|
<  \frac{1}{2^k} (2^k \varepsilon)
= \varepsilon. 
$$

We conclude that $ \{f_n\} $ is Cauchy with respect to the uniform metric, and thus converges uniformly. $ \blacksquare $

**2019 F P9.** &nbsp; *Let $ f_n \colon [a, b] \to \mathbb{R} $ be continuous with $ f_n(x) \leq f_{n+1}(x) $. Suppose $ f_n $ converge pointwise to a continuous $ f $. Show they converge uniformly to $ f $.*

*Proof.* We will show $ g_n = f-f_n $ converges uniformly to $ 0 $. Fix $ \varepsilon > 0 $. For each $ x \in [a, b] $, chose an $ N_x \gg 0 $ such that $ g_n(x) < \varepsilon R $ for all $ n > N_x $. Since our $ g_n $ are continuous, for each $ x $ there exisrts an $ r_x $ such that $ g_{N_x}(B(x, r_x)) \subseteq [0, \varepsilon) $. Since $ [a, b] $ is compact, we can choose a finite subcover $ B(x_1, r_1), \dots, B(x_{\ell}, r_{\ell}). $ Letting $ N = \max \{N_{x_0}, \dots, N_{x_\ell}\} $, we get $ g_n(x) < \varepsilon $ for all $ x \in [a, b] $ and $ n \geq N $. $ \blacksquare $

**2018 F P2.** &nbsp; *Show that*

$$
F(x) = \sum_{n=1}^{\infty} \frac{\sin(x^n)}{n!} 
$$

*converges uniformly and compute its derivative.*

*Proof.* Since $ \| \sin(x^n)/n! \| \leq 1/n! $, we have $ F(x) \leq e-1 $, so $ F $ converges uniformly by the Weierstrass M-Test. Likewise 

$$
\left\| \frac{d}{dx} \frac{\sin(x^n)}{n!} \right\|
= \left\| \frac{n x^{n-1} \cos(x^n)}{n!} \right\| 
\leq \left\| \frac{x^n}{(n-1)!} \right\|.
$$

Hence, locally the sum 

$$
F'(x) 
= \sum_{n=1}^{\infty} \frac{x^{n-1}}{(n-1)!} \cos(x^n)
$$

converges uniformly by the Weierstrass M-Test, and by theorem 4.2 it is the derivative of $ F $. $ \blacksquare $


**2018 F P7.** &nbsp; *Define $ f_n \colon [0, 2\pi] \to \mathbb{R} $ by $ f_n(x) = e^{\sin(nx)} $ and $ F_n(x) = \int_0^x f_n(y) dy $. Show there exists a subsequence of $ \{F_n\} $ that converges uniformly to a continuous function.*

*Proof.* We see that 

$$
\|F_n(x)\| 
\leq \int_0^{2\pi} \| f_n(y) \| dy
\leq \int_0^{2 \pi} e dy 
= 2 \pi e
$$

implies our sequence is uniformly bounded. Assuming $ y \geq x $, 

$$
\| F_n(y) - F_n(x) \|
= \left\| \int_x^y f_n(y) dy \right\|
\leq e (y-x)
$$

implies our sequence is uniformly equicontinuous since $ x $ is continuous. Thus, we can apply the Ascoli-Arzelà theorem to a get a uniformly convergent subsequence, and the uniform limit theorem to see that the limit of this subsequence is continuous. $ \blacksquare $

**2017 W P7.** &nbsp; *Let $ f_n \colon [0, 1] \to \mathbb{R} $ converge pointwise to $ f $. Assume $ f_n $ and $ f $ are continuous. (a) Does*

$$ 
\lim_n \int_0^1 f_n(x) dx = \int_0^1 f(x) dx?
$$

*(b) What if $ \|f_n(x)\| \leq M $ for all $ n $ and $ x $?*

*Proof.* (a) Consider bump functions of radius $ 2/n $ and equal volume:

$$
f_n(x)
= n \exp \left( - \frac{1}{1-(nx-1)^2} \right).
$$

Then our $ f_n $ converge pointwise to $ 0 $ but have constant nonzero integral.

(b) It is not hard to see that if the left limit is nonzero and the right limit is $ 0 $, then for each $ n $ there exists a set $ A_n $ of measure greater than some fixed constant $ C $, i.e. $ \mu(A_n) > C $, such that $ \|f_n(A_n)\| > D $ for some fixed constant $ D $. This contradicts pointwise convergence. $ \blacksquare $


## 5. Derivatives

**2022 W P3.** &nbsp; *Let $ f \colon \mathbb{R} \to [0, \infty) $ be a differentiable function such that $ f $ is decreasing and $ f' $ is increasing. Show $ \displaystyle \lim_{x \to \infty} f'(x) = 0 $.*

*Proof.* Suppose not. Then $ f'(x) < C $ for some $ C > 0 $ for all $ x $. Hence, $ f(x) \leq - Cx + f(0 ) $ implies $ \displaystyle \lim_{x \to \infty} f(x) = -\infty $, a contradiction. $ \blacksquare $

**2022 F P6.** &nbsp; *Define $ f \colon \mathbb{R}^2 \to \mathbb{R} $ by* 

$$
f(x, y)
= \frac{x^3}{x^2 + y^2}
$$

*for $ (x, y) \neq 0 $ and $ f(0, 0) = 0 $. (a) Show $ f $ is continuous at $ (0, 0) $. (b) Show $ f $ has every directional derivative at $ (0, 0) $. (c) Decide if $ f $ is differentiable at $ (0, 0) $.*

*Proof.* (a) We observe

$$
f(r \cos \theta, r \sin \theta)
= r^2 \cos^3 \theta,
$$

which approaches $ 0 $ as $ r $ goes to $ 0 $. 

(b) Set $ v = (a, b) $. Then 

$$
\begin{aligned}
\nabla_v f(0) & = \lim_{h \to 0} \frac{f(0+hv)-f(0)}{h} \\
& = \lim_{h \to 0} \frac{(ah)^3}{(ah)^2 + (bh)^2} \frac{1}{h} \\
& = \lim_{h \to 0} \frac{h^3 a^3}{h^3(a^2+b^2)} \\
& = \frac{a^3}{a^2+b^2}.
\end{aligned}
$$

(c) Suppose that the derivative $ D f(0) $ exists. Then, by linearity,

$$
\nabla_{(1, 1)} f(0) = \nabla_{(1, 0)} f(0) + \nabla_{(0, 1)} f(0)
$$

implies $ 1/2 = 1 $, a contradiction. Thus, the derivative does not exist. $ \blacksquare $

**2021 F P5.** &nbsp; *Let $ f^2 \colon \mathbb{R}^2 \to \mathbb{R} $. Suppose $ \frac{\partial f}{\partial x_1} $ exists at $ (0, 0) $, and that $ \frac{\partial f}{\partial x_2} $ exists in a neighborhood of $ 0 $ and is continuous at $ 0 $. Show $ f $ is differentiable at $ 0 $.*

*Proof.* Write

$$
f(x,y) - f(0, 0) = f(x, y) - f(x, 0) + f(x, 0) - f(0, 0)
$$

Denote our partials $ f_x $ and $ f_y $. Then, by the MVT, there exists a function $ a(x, y) \colon \mathbb{R}^2 \to \mathbb{R} $ such that 

$$
\begin{aligned}
f(x, y) - f(x, 0) & = f_y(x, a(x, y)) y \\
& = f_y(0, 0) y + \left[ f_y(x, a(x, y)) - f_y(0,0) \right] y \\
& = f_y(0, 0) y + O(y).
\end{aligned}
$$

Likewise

$$
\begin{aligned}
f(x, 0) - f(0, 0) &= f_x(0, 0) x + \left[ \frac{f(x, 0) - f(0, 0)}{x} - f_x(0, 0) \right] x \\
& = f_x(0, 0) x + O(x).
\end{aligned}
$$

Thus,

$$
f(x, y) - f(0, 0) = f_x(0, 0) x + f_y(0, 0) y + O(x) + O(y).
$$

so $ f $ is differentiable $ (0, 0) $. $ \blacksquare $

**2020 W P6.** &nbsp; *Let $ f \colon \mathbb{R} \to (0, \infty) $ be a differentiable function such that $ f'(x) > f(x) $ for every $ x\in \mathbb{R} $. Show there exists a $ k > 0 $ such that $ \displaystyle \lim_{x \to \infty} f(x) e^{-kx} = \infty $, and find the least upper bound on such $ k $.*

*Proof.* We see $ f'(x) > f(x) $ implies $ \frac{d}{dx} f(x) > 1 $, and hence $ \ln f(x) > x $ for $ x \gg 0 $. Consequently, $ f(x) > e^x $ for $ x \gg 0 $, yielding $ \displaystyle \lim_{x \to \infty} f(x) e^{-k} = \infty $ for $ 0 < k < 1 $. We see our least upper bound on such $ k $ is $ 1 $. $ \blacksquare $

**2020 F P7.** &nbsp; *Let $ f \colon \mathbb{R}^2 \to \mathbb{R}^2 $ be a differentiable map with $ f = f(f_1, f_2) $. Suppose that for all $ (x_1, x_2) \in \mathbb{R}^2 $*

$$
\left| \frac{\partial f_1}{\partial x_1}(x_1, x_2) - 2 \right|
+ \left| \frac{\partial f_1}{\partial x_2}(x_1, x_2) \right|
+ \left| \frac{\partial f_2}{\partial x_1}(x_1, x_2) \right|
+ \left| \frac{\partial f_2}{\partial x_2}(x_1, x_2) - 2 \right| < 1/2.
$$

*Prove $ f $ is globally injective.*

*Proof.* We start by showing $ Df $ is positive definite at every point. Indeed, set 

$$
Q(a, b) = \begin{bmatrix} a & b \end{bmatrix} 
\begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{bmatrix} 
\begin{bmatrix} a \\ b \end{bmatrix}.
$$

Then 

$$
Q(a, b) = a^2 \frac{\partial f_1}{\partial x_1} + b^2 \frac{\partial f_2}{\partial x_2} + ab \left( \frac{\partial f_1}{\partial x_2} + \frac{\partial f_2}{\partial x_1} \right).
$$

The inequality implies $ \frac{\partial f_1}{\partial x_1}, \frac{\partial f_2}{\partial x_2} \geq 1.5 $, so 

$$
Q(a,b) \geq 1.5(a^2 + b^2) + \left( \frac{\partial f_1}{\partial x_2} + \frac{\partial f_2}{\partial x_1} \right).
$$

In order to minimize the $ ab $ term we assume $ ab \geq 0 $ and set $ \frac{\partial f_1}{\partial x_2} + \frac{\partial f_2}{\partial x_1} = -1 $. Thus, 

$$
Q(a, b) \geq 1.5(a^2 + b^2) - ab.
$$

If $ a^2 \geq b^2 $, 

$$
Q(a, b) \geq 1.5(a^2 + b^2) - a^2
= 0.5 a^2 + 1.5 b^2.
$$

Thus, $ Df $ is positive definite. 

Now assume $ f(a) = f(b) $ for $ a \neq b $. We set $ \gamma(t) = a + t(b-a) $ and $ t \in [0, 1] $ and 

$$
F(t) = \left< f(\gamma(t)) - f(a), b-a \right>.
$$

Then $ F(0) = F(1) = 0 $, so the mean value theorem tells us $ F'(t) = 0 $ for some $ t \in (0, 1) $. Hence, by the chain rule,

$$
F'(t) = (b-a)^T Df(\gamma(t)) (b-a) = 0 
$$

contradicts $ Df $ being positive definite. $ \blacksquare $

**2019 F P1.** &nbsp; *Define $ f \colon \mathbb{R}^2 \to \mathbb{R} $ by*

$$
f(x, y)
= \frac{xy^2}{x^2 + y^4} 
$$

*for $ (x, y) \neq 0 $ and $ f(0, 0) = 0 $. (a) Show that $ f $ has every directional derivative at $ 0 $. (b) Show that $ f $ is not continuous at $ (0, 0) $.*

*Proof.* (a) Set $ v = (a, b) $. Then 

$$
\begin{aligned}
\nabla_v f(0) & = \lim_{h \to 0} \frac{f(0+hv)-f(0)}{h} \\
& = \lim_{h \to 0} \frac{ab^2 h^3}{a^2 h^2 + b^4 h^4} \frac{1}{h} \\
& = \lim_{h \to 0} \frac{ab^2}{a^2 + b^4 h^2}.
\end{aligned} 
$$

If $ a = 0 $ this limit evaluates to $ 0 $; elsewise it equals $ b^2/a $.

(b) For the path $ (t, t) $ we see 

$$
\lim_{t \to 0} f(t, t) 
= \lim_{t \to 0} \frac{t^3}{t^2+t^4} 
= \lim_{t \to 0} \frac{t}{1+t^2}
= 0
$$

While for the path $ (t, \sqrt{t}) $ we have 

$$
\lim_{t \to 0} f(t, \sqrt{t}) 
= \lim_{t \to 0} \frac{t^2}{t^2+t^2}
= \frac{1}{2}.
$$

Thus, $ f $ is not continuous at the origin. $ \blacksquare $

**2019 W P4.** &nbsp; *(a) Give an example of an everywhere differentiable function with discontinuous derivative. (b) Let $ f, g \colon \mathbb{R} \to \mathbb{R} $. Suppose for every $ \varepsilon > 0 $ there exists a $ \delta > 0 $ such that $ \| h \| < \delta $ implies*

$$
\left\| \frac{f(x+h)-f(x)}{h} - g(x) \right\| < \varepsilon
$$

*for all $ x \in \mathbb{R} $. Show that $ f $ is continuously differentiable.* 

*Proof.* (a) Consider the function $ f(x) x^2 \sin(\frac{1}{x}) $ continuously extended by $ f(0) = 0 $. Then $ f $ is everywhere differentiable with $ f'(0) = 0 $ but $ \displaystyle_{x \to 0} f(x) $ does not exist. 

(b) By definition $ f'(x) = g(x) $. Let $ \varepsilon > 0 $ and choose $ \delta > 0 $ as stated in the problem. Then for any $ x, y \in \mathbb{R} $ with $ \| x-y \| < \delta/2 $, we see $ y = x+h $ with $ \| h \| < \delta/2 $, and hence 

$$
\begin{aligned}
\| g(x) - g(y) \| & \leq \left\| g(x) - \frac{f(x+h) - f(x)}{h} \right\| + \left\| \frac{f(x+h) - f(x)}{h} - g(y) \right\| \\
& = \left\| \frac{f(x+h) - f(x)}{h} - g(x) \right\| + \left\| \frac{f(y-h)-f(y)}{-h} - g(y) \right\| \\
& < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon
\end{aligned}
$$

Thus, $ g $ is continuus and so is $ f' $. $ \blacksquare $

**2016 W P5.** &nbsp; *Assume that a function $ f \colon \mathbb{R}^2 \to \mathbb{R} $ satisfies*

$$
f(x_1+t, x_2+s) \geq f(x_1, x_2) - s^2 - t^2
$$

*for each $ (x_1, x_2) \in \mathbb{R}^2 $ and each $ (s, t) \in \mathbb{R}^2 $. Prove $ f $ must be constant.*

*Proof.* Let $ x, y \in \mathbb{R}^2 $ be arbitrary. Then we have 

$$
f(x) \geq f(y) - \| x-y \|^2 
$$

and 

$$
f(y) \geq f(x) - \| x-y \|^2.
$$

Hence,

$$
\| x-y \|^2 \geq f(x) - f(y) \geq -\| x-y \|^2,
$$

so

$$
\| x-y \| \geq \frac{\|f(x) - f(y)\|}{\|x-y\|}.
$$

Using this to take the derivative of $ f $ at $ x $ we get 

$$
\lim_{\| h \| \to 0} \frac{\|f(x+h) - f(x)\|}{\| h \|} \leq \lim_{\| h \| \to 0} \| h \| = 0.
$$

We conclude that $ f $ has zero derivative at every point, and therefore is constant. $ \blacksquare $


## 6. Optimization

**AM-GM Inequality.** &nbsp; *Let $ x_1, \dots, x_n \in \mathbb{R}^+ $ be positive reals. Then*

$$
\frac{1}{n} \sum_{i=1}^{n} x_i \geq \left( \prod_{i=1}^{n} x_i \right)^{1/n}.
$$

*This is an equality if and only if $ x_1 = \cdots = x_n $.*

**Jenson's Inequality.** &nbsp; *Let $ f \colon \mathbb{R} \to \mathbb{R} $ be convex. For $ x_1, \dots, x_n \in \mathbb{R} $ and $ a_1, \dots, a_n \in \mathbb{R}^+ $ we have*

$$
f(\left( \frac{\sum a_i x_i}{\sum a_i} \right) \leq \sum a_i \frac{f(x_i)}{\sum a_i}.
$$

#### Problems

**2016 F P7.** Let $ \Omega = \{(x, y) \in \mathbb{R} \mid y > 0 \} $, and define $ f \colon \Omega \to \mathbb{R} $ by

$$
f(x, y)
= \frac{2 + \sqrt{(1+x)^2 + y^2} - \sqrt{(1-x)^2 +y^2}}{\sqrt{y}}.
$$ 

*Show $ f $ achieves its minimum at a unique point $ (x_0, y_0) \in \Omega $ and find $ (x_0, y_0) $.*

*Proof.* We proceed by minimizing in each variable independently. Fix $ y = 1 $. Then 

$$
\frac{d}{dx}f(x, 1) 
= \frac{1+x}{\sqrt{(1+x)^2+1}} - \frac{1-x}{\sqrt{(1-x)^2+1}} = 0 
$$

if and only if 

$$
(1+x) \sqrt{(1-x)^2+1}
= (1-x)\sqrt{(1+x)^2+1}.
$$

Squaring both sides reduces the equation to $ (1+x)^2 = (1-x)^2 $, and hence our minimum is achieved when $ x = 0 $. Thus, fix $ x = 0 $. Then 

$$
\frac{d}{dy} f(0, y)
= \frac{y^2 - \sqrt{y^2+1}-1}{\sqrt{y^5+y^3}}
= 0
$$

if and only if $ y^2 - 1 = \sqrt{y^2+1} $, which implies $ y = \sqrt{3} $. Thus, our minimum is achieved at $ (0, \sqrt{3}) $. $ \blacksquare $

**2022 F P7.** &nbsp; *Let $ f_n \colon \mathbb{R}^2 \to \mathbb{R} $ be a sequence of continuously differentiable functions which converge pointwise to a continuously differentiable function $ f $. Suppose that for each $ n $ that $ (0, 0) $ is a local minimum for $ f_n $. Is it a local minimum for $ f $?*

*Proof.* Not necessarily. Since the projection $ \pi_1 \colon \mathbb{R}^2 \to \mathbb{R} $ is continuously differentiable, we can reduce ourselves to the case $ f_n \colon \mathbb{R} \to \mathbb{R} $. Set 

$$
f_n(x) = -x^2 + B_1(x, n) + B_2(x, n),
$$

where $ B_1(x, n) $ and $ B_2(x, n) $ are bump functions of height $ 1 $ from $ -1/n $ to $ 0 $ and from $ 0 $ to $ 1/n $, respectively. Then $ \{f_n\} $ converges to $ -x^2 $ pointwise and $ 0 $ is a local minimum for each $ n $ but not of the limit. $ \blacksquare $ 

**2021 F P2.** &nbsp; *Find all $ x, y > 0 $ which minimize $ f(x, y) = x/y + y/x $ on the curve $ x^2 + 2y^2 = 3 $.*

*Proof.* The AM-GM inequality implies

$$
\frac{x}{y} + \frac{y}{x} 
= \frac{1}{2} \left( \frac{2x}{y} + \frac{2y}{x} \right)
\geq \sqrt{4} 
= 2,
$$

and that this minimum is achieved only at $ (1, 1) $. We see that $ 1 + 2 = 3 $, and hence is our minimum on the curve. $ \blacksquare $

**2020 F P4.** &nbsp; *Find the absolute minimum of $ x^2 y + y^2 z + z^2 w + w^2 x $ for $ xyzw = 1 $ and $ x, y, z, w > 0 $.* 

*Proof.* The $ AM-GM $ inequality implies 

$$
\frac{1}{4} \left( 4x^2 y + 4y^2 z + 4z^2 w + 4w^2 x \right)
\geq (4^4 x^3 y^3 z^3 w^3)^{1/4}
= 4,
$$

and this minimum is obtained when $ x = y = z = w = 1 $. $ \blacksquare $

**2018 W P7.** &nbsp; *Find the absolute minimum of*

$$ 
f(x, y, z) = xy + yz + zx 
$$ 

*on*

$$ 
g(x, y, z) = x^2 + y^2 + z^2 = 12.
$$

*Proof.* We observe 

$$
2 f(x, y, z) = (x+y+z)^2 - g(x, y, z) \geq -12
$$

implies $ f(x, y, z) \geq -6 $. Since $ f(-\sqrt{6}, \sqrt{6}, 0) = -6 $ we conclude that this is the minimum. $ \blacksquare $


## 7. Convergence of Integrals

**Fubini-Tonelli theorem.** &nbsp; *Let $ f \colon [a, b] \times [c, d] \to \mathbb{R} $ be continuous. Then*

$$
\int_a^b \int_c^d f(x, y) dydx = \int_c^d \int_a^b f(y, x) dx dy.
$$

**2022 F P8.** &nbsp; *Does*

$$
I = \int_3^{\infty} \frac{\ln(x)}{x^p \ln(ln(x))} dx
$$

*converge for $ p \geq 0 $?*

*Proof.* The answer depends on the value of $ p $. Substitute $ u = \ln x $ and $ du = x^{-1} dx $. Then 

$$
I = \int_{\ln 3}^{\infty} \frac{u e^{-u(p-1)}}{\ln(u)} du.
$$

If $ p < 1 $, then $ -(p-1) > 0 $ implies for $ u $ large that $ u e^{-u(p-1)} > \ln(u)  $ and $ I $ diverges. If $ p = 1 $ then $ u > \ln(u) $ for $ u $ large and $ I $ diverges. Thus, we are reduced to the case when $ p > 1 $. Then

$$
I \leq \int_{\ln 3}^{\infty} u e^{-u(p-1)} du.
$$

Substitute $ y = u(p-1) $ and $ dy = (p-1) du $ we get

$$
I \leq \frac{1}{(p-1)^2} \int_{a}^{\infty} y e^{-y} dy,
$$ 

where $ a = \ln(3) (p-1) $. Integrating by parts shows

$$
I 
\leq \frac{1}{(p-1)^2} [-e^{-y} y - e^{-y}]_{a}^{\infty} 
= \frac{1}{(p-1)^2} e^{-a}(a-1).
$$

Thus $ I $ converges when $ p > 1 $. $ \blacksquare $

**2022 W P5.** &nbsp; *Does $ I = \int_0^{\infty} \cos(x^{2/3}) dx $ converge?*

*Proof.* Set $ u = x^{2/3} $ and $ dx = \frac{3}{2} \sqrt{u} du $. Then 

$$ 
I = \frac{3}{2} \int_0^{\infty} \sqrt{u} \cos(u) du.
$$

Hence, for each $ n \geq 0 $ we have 

$$
\begin{aligned}
\int_{n \pi - \pi/2}^{2 \pi + \pi/2} \sqrt{u} \cos(u) du & \geq \sqrt{n \pi - \pi/2} \int_{n \pi - \pi/2}^{n \pi+\pi/2} \cos(u) \\
& = \sqrt{n \pi - n/2}(\sin(\pi/2) - \sin(-\pi/2)) \\
& = 2 \sqrt{n \pi - \pi/2}.
\end{aligned}
$$

We conclude that the integral does not converge. $ \blacksquare $

**2022 W P8.** &nbsp; *Let $ f \colon \mathbb{R}^2 \to \mathbb{R} $ be a continuous compactly support function. Define $ g \colon \mathbb{R}^2 \to \mathbb{R} $ by*

$$
g(x) 
= \int_{\mathbb{R}^2} \frac{f(y)}{\|x-y\|} dy 
$$

*Prove that this integral converges (and $ g $ is continuous).* 

*Proof.* Without loss of generality, assume $ f $ is supported on $ D^2 $ and $ x = 0 $. Since $ f $ is compactly supported, there exists an $ M $ such that $ \sup \| f \| \leq M $. Thus, 

$$
g(0)
= \int_{D^2} \frac{f(y)}{\|y\|} dy 
\leq M \int_{D^2} \frac{1}{\|y\|} dy.
$$

Substituting polar coordinates yields 

$$
g(0)
\leq M \int_0^{2 \pi} \int_0^1 dr d \theta
= 2 \pi M.
$$

Thus, $ g $ converges. (I have not shown continuity.) $ \blacksquare $

**2021 F P5.** &nbsp; *Let $ f \colon \mathbb{R}^2 \to \mathbb{R} $ be continuous. Suppose $ \int_0^{\infty} f(x, y) dy $ exists for every $ x \in [0, 1] $. Assume there exists a $ C \geq 0 $ such that for $ z > 0 $,*

$$
\left\| \int_z^{\infty} f(x, y) dy \right\| \leq \frac{C}{\log(2+z)}
$$

*for every fixed $ x $. Show*

$$
\int_0^1 \left[ \int_0^{\infty} f(x, y) dy \right] dx
= \int_0^{\infty} \left[ \int_0^1 f(x, y) dx \right] dy.
$$

*Proof.* We apply the Fubini-Tonelli theorem as follows. For each $ z \in (0, \infty) $, we have 

$$
\begin{aligned}
\int_0^1 \left[ \int_0^{\infty} f(x, y) dy \right] dx 
& = \int_0^1 \int_0^z f(x, y) dx dy + \int_0^1 \int_z^{\infty} f(x, y) dy dx. 
\end{aligned}
$$

Observing

$$
\begin{aligned}
\lim_{z \to \infty} \int_0^1 \int_z^{\infty} f(x, y) dy dx & \leq \lim_{z \to \infty} \int_0^1 \left\| \int_z^{\infty} f(x, y) dy \right\| dx \\
& \leq \lim_{z \to \infty} \frac{C}{\log(2+z)} \\
& = 0
\end{aligned}
$$

we get our desired inequality. $ \blacksquare $

**2020 F P5.** &nbsp; *Set $ a _0 = 0 $ and for $ k \geq 1 $*

$$
a_k = \sqrt{1 + \frac{1}{2} + \cdots + \frac{1}{k}}.
$$

*Assume $ \{b_k\} $ is a sequence in $ \mathbb{R}^+ $ such that $ \sum_k b_k^2 < \infty $, and that $ f \colon \mathbb{R}^2 \to \mathbb{R}^+ $ is a continuous function such that $ f(x) \leq b_k $ when $ a_{k-q} \leq \|x\| \leq a_k $ . Show that $ \int_{\mathbb{R}^2} f(x) dA $ exists.*

*Proof.* Indeed, 

$$
\begin{aligned}
\int_{\mathbb{R}^2} f(x) dx & = \sum_{k=0}^{\infty} \int_0^{2 \pi} \int_{a_k}^{a_{k+1}} f(r \cos \theta, r \sin \theta) r dr d \theta \\
& \leq \sum_{k=0}^{\infty} \int_0^{2 \pi} \int_{a_k}^{a_{k+1}} b_{k+1} r dr d \theta \\
& \leq \sum_{k=0}^{\infty} \pi b_{k+1} [a_{k+1}^2 - a_k^2] \\
& = \sum_{k=0}^{\infty} \pi b_{k+1} \frac{1}{k+1} \\
& \leq \sum_{k=1}^{\infty} \pi \text{max} \{b_k^2, \frac{1}{k^2}\} \\
& \leq \pi \sum_{k=1}^{\infty} b_k^2 + \pi \sum_{k=1}^{\infty} \frac{1}{k^2} \\
& < \infty.
\end{aligned}
$$

We conclude that the limit exists. $ \blacksquare $

**2020 W P5.** &nbsp; *Let $ f \colon \mathbb{R}^2 \to \mathbb{R} $ be a differentiable function such that $ f(0, 0) = 0 $. Show that*

$$
I = \int \int_{x^2+y^2 \leq 1} \frac{f(x, y)}{(x^2+y^2)^{4/3}} dx dy   
$$

*converges.*

*Proof.* The following proof holds if $ f $ is $ C^1 $. Performing a polar substitution 

$$
g(r, \theta) = f(r \cos \theta, r \sin \theta)
$$

yields 

$$
\begin{aligned}
I & = \int_0^{2 \pi} \int_0^1 \frac{f(r \cos \theta, r \sin \theta)}{r^{5/3}} dr d \theta \\
& \int_0^{2 \pi} \int_0^1 \frac{g(r, \theta) - g(0, 0)}{r} \frac{1}{r^{2/3}} dr d \theta \\
\end{aligned}
$$

Since $ f $ is continuously differentiable and our domain is compact we see $ f' $ is bounded by som $ M $, and so $ g' $ is bounded by some $ N $. Fixing $ \theta $, the mean value theorem implies that for each $ r $ there exists an $ r_0 $ such that 

$$
\left\| \frac{g(r, \theta) - g(0, 0)}{r} \right\| 
= \left\| g'(r_0, \theta) \right\|
\leq N
$$

where the derivative is taken in the first variable. Hence,

$$
\begin{aligned}
I & \leq \int_0^{2 \pi} \int_0^1 \left\| \frac{g(r, \theta) - g(0, 0)}{r} \right\| \frac{1}{r^{2/3}} dr d \theta \\
& \leq N \leq \int_0^{2 \pi} \int_0^1 \frac{1}{r^{2/3}} dr d \theta \\
& 6 \pi N.
\end{aligned}
$$

Thus, our integral converges. $ \blacksquare $


## 8. Polynomials and Stone Weierstrass

**Stone-Weierstrass theorem.**  &nbsp; *Let $ f \colon [a, b] \to \mathbb{R} $ be continuous. Then there exists a sequence $ p_n \in \mathbb{R}[x] $ that converges uniformly to $ f $.*

#### Problems

**2023 W P9.** &nbsp; *For $ n \geq 2 $ let $ p \colon \mathbb{R}^n \to \mathbb{R} $ be*

$$
p(x_1, \dots, x_n) = \sum_{j=1}^n x_j^{2j+1}.
$$

*Suppose $ f = (f_1, \dots, f_n) \colon \mathbb{R}^n \to \mathbb{R}^n $ is continuously differentiable function with $ p (f(x)) = 0 $ for all $ x \in \mathbb{R}^n $. Prove $ \det f' = 0 $.*

*Proof.* Suppose not. Then there exists a point $ x = (x_1, \dots, x_n) \in \mathbb{R} $ with $ \det f'(x) \neq 0 $. Since $ \det f'(x) \neq 0 $ and the determinant and derivatives are continuous, we can assume $ f_j(x) \neq 0 $. The identity $ p(f) = 0 $ implies $ d [p(f)] = 0 $, or equivalently $ p'(f) f' = 0 $. Expanding this equation, we see that for each $ 1 \leq j \leq n $ we have

$$
(2j+1) f_j^{2j}(x_1, \dots, x_n) \left( \sum_{k=1}^{n} \partial_j f_k \right)
= 0. 
$$

Since $ f_j(x) \neq 0 $ for each $ j $, we have $ \sum_k \partial_j f_k = 0 $. This implies the rows of $ f'(x) $ sum to $ 0 $, and thus are linearly dependent, meaning $ \det f(x) = 0 $. This contradicts the assumption that $ \det f'(x) \neq 0 $. $ \blacksquare $

**2020 F P8.** &nbsp; *Let $ f \colon [0, 1] \to \mathbb{R} $ be continuous such that $ \int_0^1 f(x) x^n dx = 0 $ for $ n = 3, 4, \dots $. Prove $ f(x) = 0 $.*

*Proof.* The Stone-Weierstrass theorem implies we can approximate $ f(x) x^4 $ by polynomials $ p_n \in \mathbb{R}[x] $. Since this sequence converges uniformly, theorem 4.1 then implies 

$$
\lim_{n \to \infty} \int_0^1 [f(x) x^4] p(x) dx 
= \int_0^1 f(x)^2 x^8 dx.
$$

Each integral on the left hand side is $ 0 $, and hence the right hand side is too. This can only happen when $ f(x) = 0 $. $ \blacksquare $

**2018 W P10.** &nbsp; *Let $ f \colon \mathbb{R}^2 \to \mathbb{R} $ be a function such that $ f(x_0, y) $ is polynomial for fixed $ x_0 $ and $ f(x, y_0) $ is polynomial for fixed $ y_0 $. Show that $ f $ is polynomial.*

*Proof.* Write 

$$
f(x, y) 
= \sum_{n=0}^{\infty} c_n(y) x^n
$$

and 

$$
Y_n = \{ y_0 \in \mathbb{R} \mid \deg f(x, y_0) = n \}.
$$

Since $ \bigcup_n Y_n = \mathbb{R} $ and $ \mathbb{R} $ is uncountable while our union is indexed by a countable set, we see that for some $ N $ that $ Y_N $ is infinite. We denote the restriction of $ f $ to $ \mathbb{R} \times Y_N $ by $ Y_N $, where

$$
Y_n 
= \sum_{n=0}^{N} c_n(y) x^n. 
$$

Choosing $ N $ distinct reals $ x_0, \dots, x_N \in \mathbb{R} $ allows us to solve for the $ c_n $ on this subset:

$$
c_n(y) = \sum_{n=0}^{N} a_{j, n} f_N(x_j, y).
$$

Using that $ f_N $ is polynomial for each fixed $ x_j $ we see that 

$$ 
f_N(x, y) = \sum_{n=0}^{N} a_{j, n} f_N(x_j, y) x^n
$$

is polynomial in both variables. Finally, for each $ x \in \mathbb{R} $ we observe 

$$
f(x, y) - \sum_{n=0}^{N} a_{j, n} f(x_j, y) x^n
$$

is $ 0 $ for infinitely many $ y $, so

$$
f(x, y) = \sum_{n=0}^{N} a_{j, n} f_N(x_j, y) x^n.
$$

Thus, it is polynomial in both variables. $ \blacksquare $

**2010 W P5.** &nbsp; *Let $ g_n \colon [0, 1] \to \mathbb{R} $ be a sequence of continuous functions. Suppose the $ g_n $ are uniformly bounded by $ M $, and that there exists a continuous $ g \colon [0, 1] \to \mathbb{R} $ such that*

$$
\lim_n \int_0^1 g_n(x) p(x) dx = \int_0^1 g(x) p(x) dx
$$

*for every $ p \in \mathbb{R}[x] $. Show that $ \| g(x) \| \leq M $, and that*

$$
\lim_n \int_0^1 g_n(x) f(x) dx = \int_0^1 g(x) f(x) dx
$$

*for every continuous $ f \colon [0, 1] \to \mathbb{R} $.*

*Proof.* The second statement follows from the Stone-Weierstrass theorem in a manner similar to 2020 F P8. For the first statement, suppose $ g(x) \neq 0 $ and choose $ f(x) $ such that $ g(x) f(x) = M $. Then

$$
\lim_n \int_0^1 g_n(x) f(x) dx 
= \int_0^1 g(x) f(x) dx 
= M
$$

implies $ \| f(x) \| \geq 1 $ and $ \|g(x)\| \leq M $. $ \blacksquare $


## 9. Stoke's theorem

**Stoke's theorem.** &nbsp; *Let $ S $ be a smooth oriented surface in $ \mathbb{R}^3 $ with boundary $ \partial S $. If $ F \colon \mathbb{R}^3 \to \mathbb{R}^3 $ is a vector field with continuous first order partials, then*

$$
\int \int_S (\text{Curl} F \cdot n) dA
= \int_{\partial S} (F \cdot n) dB,
$$

*where $ n $ is the unit normal.*

**Divergence theorem.** &nbsp; *Let $ M $ be a smooth manifold in $ \mathbb{R}^n $ with boundary $ \partial M $. Then*

$$
\int_M \text{Div } F dV 
= \int_{\partial M} (F \cdot n) dS,
$$

*where $ n $ is the unit normal.*

#### Problems

**2022 F P3.** &nbsp; *Find the value of $ \int \int_E F \cdot n dS $ where $ F(x, y, z) = (x, ze^x, y^z) $,* 

$$
E = \{(x, y, z) \in \mathbb{R}^3 \mid \|(x, y, z) \| = 1, z \geq 0,
$$

*and $ n $ is the unit normal.*

*Proof.* Write 

$$
H = \{(x, y, z) \in \mathbb{R}^3 \mid \| (x, y, z) \| \leq 1, z \geq 0\}.
$$

The divergence theorem tells us

$$
\int_H \text{Div} F dV
= \int_E (F \cdot n) dS + \int_D^2 (F \cdot n) dS,
$$

where $ D^2 $ denotes the unit disk with $ z=0 $. We see 

$$
\int_H \text{Div} F dV 
= \int_H 1 dV
= \frac{2}{3} \pi.
$$

Next our unit normal on $ D^2 $ is $ (0, 0, -1) $, so 

$$
\int_{D^2} (F \cdot n) dS
= \int_{D^2} -y^2 dS
= - \frac{\pi}{4}.
$$

Thus, $ \int_E F \cdot n dS = \frac{2 \pi}{3} + \frac{\pi}{4} $. $ \blacksquare $

**2023 W P6.** &nbsp; *Let $ C $ be a simple closed curve that lies in the plane $ x + y + z = 1 $. Show*

$$
\int_C z dx - 2xdy + 3y dz
$$

*only depends on the region $ R $ enclosed by $ C $.*


*Proof.* The curl of $ (z, -2x, 3y) $ is $ (3, 1, -2) $. We see $ n = (1, 1, 1)/\sqrt{3} $. Hence, 

$$
\int_C z dx - 2xdy + 3y dz 
= \int \int_R 2 dA,
$$

and thus our integral is $ 2 \text{Vol}(R) $. $ \blacksquare $

**2022 W P9.** &nbsp; *Let $ F = (6yz, 2xz, 4xy) $, and define $ \alpha, \gamma \colon [-\pi, \pi] \to \mathbb{R}^3 $ by*

$$
\alpha(t) = (\cos(t), \sin(t), 0)
$$

*and*

$$
\gamma(t) 
= (\cos(t), \sin(t), 4t \sin(t) \cos(t^3)).
$$

*(a) Apply Stoke's theorem on*

$$
S = \{(\cos(t), \sin(t), z) \mid t \in [-\pi, \pi], 0 \leq z \leq 4t \sin(t) \cos(t^3)\}
$$

*to express $ \int_{\gamma} (F \cdot n) dA $ in terms of $ \int_{\alpha} (F \cdot n) dA$. (b) Use (a) to evaluate the first integral.*

*Proof.* (a) Stoke's theorem tells us 

$$
\int_S (\text{Curl} \cdot n) dS = \int_{\alpha} (F \cdot n) dA + \int_{\gamma} (F \cdot n) dA.
$$

Here, $ \text{Curl} F = (2x, 2y, -4z) $ and our unit normal is $ (\cos(t), \sin(t), 0) $. Therefore

$$
\begin{aligned}
\int_S (\text{Curl} F \cdot n) dS & = \int_{-\pi}^{\pi} \int_0^{4 \sin(t) \cos(t^3)} 2 \cos^2(t) + 2 \sin^2(t) dz dt \\
& = 2 \int_{- \pi}^{\pi} 4t \sin(t) \cos(t^3) dt \\
& = 16 \pi.
\end{aligned}
$$

Thus, 

$$
16 \pi = \int_{\alpha} (F \cdot n) dA + \int_{\gamma} (F \cdot n) dA.
$$

(b) We see 

$$
\begin{aligned}
\int_{\alpha} (F \cdot n) dA  & = \int_{-\pi}^{\pi} F(\alpha(t)) \cdot n(t) \\
& = \int_{-\pi}^{\pi} (0, 0, 4 \cos(t) \sin(t^3)) \cdot (-\cos(t), -\sin(t), 0) dt \\
& = 0.
\end{aligned}
$$

We conclude that $ \int_{\gamma} (F \cdot n) dA = 16 \pi $. $ \blacksquare $

**2021 F P4.** &nbsp; *Let $ E $ be the square-based pyramid in $ \mathbb{R}^3 $ with top vertex $ (1, 2, 5) $ and base $ (x, y, 0) $ with $ 0 \leq x, y, \leq 3 $, and let $ S_1, S_2, S_3, S_4 $ be the triangular sides of $ E $. Define $ F \colon \mathbb{R}^3 \to \mathbb{R}^3 $ by*

$$
F(x, y, z) = (3x-y+4z, x+5y-2z, x^2+y^2-z).
$$

*If $ n $ is the unit normal with positive component, find*

$$
\sum_{i=1}^4 \int \int_{S_i} F \cdot n d A.
$$

*Proof.* Let $ B = [0, 3] \times [0, 3] \times 0 $ denote the base of our pyramid. The divergence theorem tells us 

$$
\sum_{i=1}^4 \int \int_{S_i} F \cdot n d A 
= \int_E \text{Div} F dV - \int_B (F \cdot n) dA. 
$$

We see $ \text{Div} F = 7 $ and the volume of any pyramid is $ \frac{1}{3} b h $ where $ b = 9 $ and $ h = 5 $, so 

$$
\int_E \text{Div} F dV 
= 7 \text{Vol}(E) 
= 7 (\frac{1}{3} 9 \cdot 5) 
= 105.
$$

Likewise 

$$
\int_B (F \cdot n) dA
= \int_0^3 \int_0^3 (3x-y, x+5y, x^2+y^2) \cdot (0, 0, -1) 
= -54. 
$$

We conclude that our desired value is $ 105+54 = 159 $. $ \blacksquare $

**2020 F P2.** &nbsp; *Find the value of $ \int \int_E F \cdot n dS $, where $ F(x, y, z) = (yz^2, \sin x, x^2) $,*

$$ 
E = \{(x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 + 4z^2 = 1, z \geq 0\},
$$

*and $ n $ is the outward unit normal.*

*Proof.* Write 

$$
V = \{(x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 + 4z^2 \leq 1, z \geq 0\}.
$$

The divergence theorem tells us 

$$
\int \int_E (F \cdot n) dS 
= \int_V \text{Div} F dV - \int_{D^2} (F \cdot n) dA,
$$

where $ D^2 $ is the unit disk with $ z = 0 $. We see that $ \text{Div} F = 0 $ implies $ \int_V \text{Div} F dV = 0 $. On $ D^2 $ the unit normal is $ n = (0, 0, -1) $, and we compute

$$
\begin{aligned}
\int_D^2 (F \cdot n) dA & = \int_{D^2} - x^2 dA \\
& = \int_0^{2 \pi} \int_0^1 -r^3 \cos^2(\theta) dr d \theta \\
& = - \frac{\pi}{4}.
\end{aligned}
$$ 

Thus, $ \int \int_E (F \cdot n) dS = \pi/4 $. $ \blacksquare $

## 10. Inverse and implicit function theorems

**Inverse function theorem.** &nbsp; *Let $ \mathbb{R}^n \to \mathbb{R}^n $ be a continuously differentiable function. Then $ \det f'(x) \neq 0 $, i.e. $ f'(x) $ invertible as a linear transformation, if and only if $ f $ is invertible in a neighborhood of $ x $.*

**Implicit function theorem.** &nbsp; *Let $ f \colon D \subseteq \mathbb{R}^{n+m} \to \mathbb{R}^n $ be continuously differentiable with $ f(a, b) = 0 $ for some $ (a, b) \in D $. Put $ A = f'(a, b) $ and assume $ A_x $ is invertible. Then there exists open subsets $ U \subseteq D $ and $ W \subseteq \mathbb{R}^m $ with $ (a, b) \in U $ and $ b \in W $, such that there is a unique continuously differentiable $ g \colon W \to \mathbb{R}^n $ with $ g(b) = a $, $ f(g(y), y) = 0 $, and $ g'(b) = -(A_x)^{-1} A_y $.*

#### Problems

**2023 W P8.** &nbsp; *Define $ f^3 \colon \mathbb{R}^3 \to \mathbb{R} $ by $ f(x, y, z) = x^2y + e^x + z $. (a) Show there exists a continuously differentiable $ \phi $ defined in a neighborhood of $ (1, -1) $ such that $ \phi(1, -1) = 0 $ and $ f(\phi(y, z), y, z) = 0 $ for all $ (y, z) \in U $. (b) Find $ \nabla \phi(-1, 1) $.*

*Proof.* (a) Observe $ f(0, -1, 1) = 0 $ and $ \frac{\partial f}{\partial x}(0, -1, 1) = 1 $. Hence, we can apply the implicit function theorem to our $ U $ and $ \phi $.

(b) The implicit function theorem tells us 

$$
\nabla \phi(-1, 1)
= \phi'(-1, 1)^T
= - 1 \cdot \begin{bmatrix} 0 \\ 1 \end{bmatrix},
$$

so $ \nabla \phi(-1, 1) = (0, -1)^T $. $ \blacksquare $


**2022 F P4.** &nbsp; *(a) Let $ G \colon \mathbb{R}^3 \to \mathbb{R}^2 $ with $ G = (g_1, g_2) $ and $ G(x_0, y_0, z_0) = 0 $. When does there exist continuously differentiable $ \phi \colon I \to \mathbb{R} $ and $ \psi \colon I \to \mathbb{R} $ defined on an open interval $ x_0 \in I $ such that* 

$$
\{(x_1, x_2, x_3) \mid G(x_1, x_2, x_3) = 0 \}
= \{ (x_1, \phi(x_1), \psi(x_1) \mid x_1 \in I \}
$$

*in a neighborhood of $ (x_0, y_0, z_0) $?*

*(b) Suppose $ f \colon \mathbb{R}^2 \to \mathbb{R} $ is continuously differentiable, that $ f(1, 1) = 1 $, and $ \frac{\partial f}{\partial x_1}(1, 1) \neq 0 $, $ \frac{\partial f}{\partial x_2}(1, 1) \neq 0 $, and $ (\frac{\partial f}{\partial x_2}(1, 1))^2 \neq 1 $. Show the system*

$$
f(x_3, f(x_1, x_2)) = 1, \qquad f(f(x_1, x_3), x_2) = 1
$$

*defines functions $ x_2 = \phi(x_1) $ and $ x_3 = \psi(x_1) $ in a neighborhood of $ 1 $ satisfying*

$$
f(\psi(x_1), f(x_1, \phi(x_1))) = 1, \qquad f(f(x_1, \phi(x_2)), \phi(x_1)) = 1.
$$

*Proof.* (a) When the derivative $ A_x $ where $ x = (x_2, x_3) $ is invertible and $ G $ is continuously differentiable; i.e.  

$$
A_x = 
\begin{bmatrix}
\frac{\partial g_1}{\partial x_2} & \frac{\partial g_1}{\partial x_3} \\
\frac{\partial g_2}{\partial x_2} & \frac{\partial g_2}{\partial x_3} \\
\end{bmatrix}
$$

is invertible, which is equivalent to its derivative being nonzero.

(b) Set 

$$
G(x, y, z) 
= (f(z, f(x, y))-1, f(f(x, z), y)-1).
$$

Then 

$$
G' =
\begin{bmatrix}
\frac{\partial f}{\partial x_1} \frac{\partial f}{\partial x_2} & \left(\frac{\partial f}{\partial x_2} \right)^2 & \frac{\partial f}{\partial x_1} \\
\left(\frac{\partial f}{\partial x_1} \right)^2 & \frac{\partial f}{\partial x_2} & \frac{\partial f}{\partial x_1} \frac{\partial f}{\partial x_2}
\end{bmatrix}.
$$

Hence,

$$
\begin{aligned}
\det A_x(1, 1)
& = \det 
\begin{bmatrix}
\left(\frac{\partial f}{\partial x_2}(1, 1) \right)^2 & \frac{\partial f}{\partial x_1}(1, 1) \\
\frac{\partial f}{\partial x_2}(1, 1) & \frac{\partial f}{\partial x_1}(1, 1) \frac{\partial f}{\partial x_2}(1, 1)
\end{bmatrix} \\
& = \frac{\partial f}{\partial x_1}(1, 1) \frac{\partial f}{\partial x_2}(1, 1) \left [ \left( \frac{\partial f}{\partial x_2}(1, 1)\right)^2 - 1 \right] \\
& \neq 0.
\end{aligned}
$$

Thus, $ \phi, \psi $ exists by (a). $ \blacksquare $

**2022 W P4.** &nbsp; *Let $ G \subseteq \mathbb{R}^5 $ be the set of vectors $ A = (a_0, \dots, a_4) $ such that*

$$
P_A(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4
$$

*has $ 5 $ distinct roots. Show that $ G $ is open.*

*Proof.* Define $ f \colon \mathbb{R}^6 \to \mathbb{R} $ by $ f(A, x) = P_A(x) $; this is a $ C^1 $ function since it is polynomial. Fix an $ A_0 \in G $, and let $ \alpha $ be root of $ P_{A_0} $. Since our roots are distinct we have $ P_{A_0}'(\alpha) \neq 0 $. Hence, we can apply the implicit function theorem to find a unique function $ \phi_{\alpha} \colon U \to \mathbb{R} $, where $ U $ is a neighborhood of $ A_0 $, such that $ f(x, \phi_{\alpha}(x)) = 0 $. Since our $ \phi_{\alpha} $ are continuously differentiable, there exists a neighborhood of $ A_0 $ such that they do not intersect, i.e. $ P_A $ has distinct roots. $ \blacksquare $

**2019 F P8.** &nbsp; *Write $ F(x, y, z) = xe^{2y} + ye^z - ze^x $ and*

$$ 
G(x, y, z) = \ln(1+x+2y+3z) + \sin(2x-y+z).
$$

*(a) Prove that in a neighborhood of $ 0 $ the intersection of $ F = 0 $ and $ G = 0 $ can be represented as a continuously differentiable curve parameterized by $ x $. (b) Find a tangent vector to this curve at $ 0 $.* 

*Proof.* Define $ f \colon \mathbb{R}^3 \to \mathbb{R}^2 $ by 

$$ 
f(x, y, z) = (F(x, y, z), G(x, y, z)).
$$ 

Then $ f(0, 0, 0) = (0, 0) $ and 

$$
f'(0, 0, 0)
=
\begin{bmatrix}
1 & 1 & -1 \\
3 & 1 & 4 
\end{bmatrix}
$$

so 

$$ 
\det A_x 
= 
\det 
\begin{bmatrix}
1 & -1 \\
1 & 4
\end{bmatrix}
= 6.
$$ 

Thus, we can apply the implicit function theorem to get our curve $ \phi(x) $. 

(b) We see 

$$ 
\phi'(0, 0, 0) 
= -(A_x)^{-1} A_y 
= \frac{-1}{5} \begin{bmatrix} 4 & 1 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 3 \end{bmatrix}
= \begin{bmatrix} -7/5 \\ -2/5 \end{bmatrix}.
$$

We conclude that $ (-7/5, -2/5) $ is tangent to our curve at $ 0 $. $ \blacksquare $

**2018 W P8.** &nbsp; *Let $ f \colon \mathbb{R}^2 \to \mathbb{R}^2 $ be a continuously differentiable map such that $ f^{-1}(y) $ is a finite set for all $ y $. Show that the determinant $ \det df $ of the Jacobi matrix of $ f $ cannot vanish on any open subset of $ \mathbb{R}^2 $.*

*Proof.* Suppose $ \det df $ vanishes on $ U $. Then the inverse function theorem tells us the image $ f(U) $ cannot be locally isomorphic to $ \mathbb{R}^2 $, else it would be invertible in a neighborhood, and hence have nonvanishing determinant. Thus, the image of $ f $ is locally isomorphic to $ \mathbb{R} $. The kernel of a surjective map from a 2-manifold to a 1-manifold is a 1-manifold, and hence $ f $ has infinite kernel.

Note: It is also a well known fact that there exists no continuous bijections from $ \mathbb{R}^2 \to \mathbb{R} $ (this requires the Baire category theorem), and hence our map has infinite kernel. $ \blacksquare $
