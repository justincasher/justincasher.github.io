---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /hilberts-10th-problem
title: Hilbert's 10th problem
date: "January 2024"
abstract: "These are notes from a talk I gave on Hilbert's 10th problem, which asks if there exists an algorithm which determines whether a polynomial with integer coefficients has a solution in the integers. We follow the proof given in B. Poonen's expository article, [6], on how Turing machines, and specifically the Halting problem, are used to show Hilbert's 10th conjecture is false. We then mention generalizations and applications to Mazur's conjecture."
toc:
  - title: "Turing machines"
    anchor: "1-turing-machines"
  - title: "Hilbert's 10th problem"
    anchor: "2-hilberts-10th-problem"
  - title: "Hilbert's 10th problem for arbitrary rings"
    anchor: "3-hilberts-10th-problem-for-arbitrary-rings"
  - title: "Mazur's conjectures"
    anchor: "4-mazurs-conjectures"
  - title: "References"
    anchor: "5-references"
---

## 1. Turing machines

&emsp; A *Turing machine*, introduced by A. Turing, [\[7\]](#5-references), is a way to mathematically formalize the idea of an algorithm. We will not give the explicit definition here, as we will only need an informal notion for our purposes. A Turing machine can be thought of as a finite program having infinite memory, i.e., it is free of any physical memory constraints that a real computer has. It executes infinitely fast, meaning we are more concerned with whether a Turing machine *halts*, or stops after a finite number of steps, with respect to a given input rather than its run time.


&emsp; Visually, a Turing machine $ T $ can be viewed as a string of code, which is equivalent to a finite piece of tape:

$$
1, 0, 0, 1, 1, 1
$$

Its memory $ M $ is likewise a piece of tape, but this time infinite, although at any point during the computation, it can only contain finitely many 1's:

$$
\dots, 0, 0, 0, 1, 1, 0, 1
$$

Thus, $ M $ is initialized to some infinite sequence containing finitely many 1's, and then $ T $ acts on $ M $ until it halts; it is also possible that the machine does not halt.


&emsp; We can identify Turing machines with integers via any bijection between the natural numbers $ \mathbb{N} $ and the integers $ \mathbb{Z} $. Thus, we will write $ T \in \mathbb{Z} $. Likewise its initial input, since it only contains finitely many 1's, can also be identified with an integer $ a \in \mathbb{Z} $. We will denote inputting $ a $ to $ T $ by $ T(a) $. If our Turing machine halts or its memory converges to some infinite sequence, then we will also use $ T(a) $ to denote this value.


&emsp; Let $ P \subseteq \mathbb{Z} $ be a subset of the possible inputs. We say that a Turing machine $ T $ solves the decision problem $ P $ if, for each $ a \in \mathbb{Z} $, $ T(a) $ halts with output 1 if $ a \in P $ and 0 if $ a \not \in P $. There are uncountably many possible decision problems but only countably many Turing machines, so not every decision problem has a solution; we call such decision problems *unsolvable*.


&emsp; To shorten our terminology, we say a decision problem $ P $ is *recursive* if there exists a Turing machine solving it. We say $ P $ is *listable* if there exists a Turing machine $ T $ which outputs $ P $ if left running forever, i.e., $ T(0) = P $.


**Proposition 1.1.** &nbsp; *Recursive implies listable.*


*Proof.* Let $ T $ solve $ P $, and let $ Z $ be a Turing machine that prints the integers $ 0, -1, 1, -2, 2, \dots $. Then taking each output of $ Z $ and inputting it to $ T $ lists $ P $. Q.E.D.


&emsp; The halting problem asks whether there exists a Turing machine $ H $ whose input is a pair $ (T, a) \subseteq \mathbb{Z} \times \mathbb{Z} $ (which we can, of course, identify with an integer), and whose output is whether $ T(a) $ halts. As it turns out, Turing showed that the halting problem is undecidable.


**Theorem 1.2** ([\[7\]](#5-references)). &nbsp; *The decision problem is undecidable.*


*Proof.* Suppose $ H $ exists. Then there would exist a Turing machine $ G $ such that $ G(a) $ halts if and only $ a(a) $ does not halt. But by setting $ a $ to be $ G $, we see that $ G(G) $ halts if and only if $ G(G) $ does not halt, a contradiction. Q.E.D. 


**Corollary 1.3.** &nbsp; *There exists a listable set $ L \subseteq \mathbb{Z} $ which is not recursive.*


*Proof.* Set 

$$
L = \{2^T 3^a \mid T, a \in \mathbb{Z} \text{ and } T(a) \text{ halts} \}.
$$

Then $ L $ is not recursive by theorem 1.2. It is, however, listable: for each $ N \in \mathbb{N} $ and $ T, a \in \mathbb{Z} $ with $ \vert T \vert, \vert a \vert \leq N $, print $ 2^T 3^a $ if $T(a) $ it halts within $ N $ steps. Q.E.D.




## 2. Hilbert's 10th problem

&emsp; *Hilbert's 10th problem* asks if there exists an algorithm that determines whether a polynomial with integer coefficients has a solution in the integers. We can rewrite this using Turing machines as follows. Let $ P $ be the decision problem 

$$
P = \{ F \in \mathbb{Z}[X_1, \dots, X_n] \mid \exists a \in \mathbb{Z}^n \text{ s.t. } F(a) = 0 \};
$$

we are interested in whether $ P $ is recursive. 


&emsp; We say a set $ S \subseteq \mathbb{Z}^n $ is *diophantine* if there exists a polynomial

$$
F \in \mathbb{Z}[X_1, \dots, X_n, Y_1, \dots, Y_m],
$$ 

where $ S $ is the set of points $ a \in \mathbb{Z}^n $ such that there exists a $ b \in \mathbb{Z}^m $ with $ F(a, b) = 0 $. If we let $ \mathcal{V}(F) \subseteq \mathbb{Z}^{n+m} $ denote the zero locus of $ F $, this is the same as saying 

$$
S = \{ (a_1, \dots, a_n) \mid a \in \mathcal{V}(F) \}.
$$

The following result about diophantine sets was shown by Y. Matijasevǐc, [\[4\]](#5-references), using the work of M. Davis, H. Putnam, and J. Robinson, [\[2\]](#5-references).


**Theorem 2.1.** &nbsp; *Let $ S \subseteq \mathbb{Z}^n $. Then $ S $ is listable (after identifying $ \mathbb{Z}^n $ with $ \mathbb{Z} $) if and only if it is diophantine.*


*Proof.* In [\[2\]](#5-references), it is shown that every listable set is *exponential diophantine*, i.e., the zero set of a function created from integers and variables using addition, multiplication, and exponentiation. It is then shown in [\[4\]](#5-references) that the exponential relation $ y = C^x $ is, in fact, diophantine; this is done using sequences of integer solutions of the pell equation

$$
X_1^2 - n X_2^2 = 0,
$$

where $ n $ is not square. We will not go into too much detail here, and refer the reader to article [\[3\]]() for a short-ish, complete proof. Q.E.D.


**Corollary 2.2.** &nbsp; *Hilbert's 10th problem is undecidable.*


*Proof.* Recall the set $ L $ given in corollary 1.3 is listable but not recursive. Hence, it is diophantine, and there exists a polynomial $ F \in \mathbb{Z}[X_1, Y_1, \dots, Y_m] $ such that 

$$
L = \{ a \in \mathbb{Z} \mid \exists b \in \mathbb{Z}^m \text{ s.t. } F(a, b) = 0 \}.
$$

If Hilbert's 10th problem were true, then there would exist a Turing machine $ T $ such that, for each $ a \in \mathbb{Z} $, $ T(a) $ determines if $ F(a, X) $ has a solution $ X $. In particular, $ L $ would be recursive, a contradiction. Q.E.D.




## 3. Hilbert's 10th problem for arbitrary rings


&emsp; A natural question is whether Hilbert's 10th problem is decidable for rings other than $ \mathbb{Z} $. In [\[6\]](#5-references), the following chart is given:

| Ring | Hilbert's 10th problem |
| -------- | ---------- |
| $ \mathbb{Z} $ | False |
| $ \mathbb{C} $ | True |
| $ \mathbb{R} $ | True |
| $ \mathbb{F}_q $ | True |
| $ p $-adic fields | True |
| $ \mathbb{F}_q((t)) $ | Unknown |
| Number fields | Unknown |
| $ \mathbb{Q} $ | Unknown |
| Global funnction field | False |
| $ \mathbb{F}_q(t) $ | False |
| $ \mathbb{C}(t) $ | Unknown |
| $ \mathbb{C}(t, u) $ | False |
| $ \mathbb{R}(t) $ | False |
| $ \mathcal{O}_K $ | Unknown |


&emsp; Here, $ K $ is a number field and $ \mathcal{O}_K $ its ring of integers. We do know the decidability of Hilbert's 10th problem for certain $ \mathcal{O}_K $ but not all. Indeed, theorem 14.1 in loc. cit. tells us it is false when...

1. $ K $ is totally real.

2. $ K $ is a quadratic extension of a totally real number field or of an imaginary quadratic.

3. $ K $ has exactly one conjugate pair of nonreal embeddings.

4. There exists an elliptic curve $ E $ over $ \mathbb{Q} $ such that the abelian groups $ E(\mathbb{Q}) $ and $ E(K) $ both have rank 1.

5. For every Galois prime-degree extension $ L/K $, there exists an elliptic curve $ E $ over $ K $ such that $ E(K) $ and $ E(L) $ have the same positive rank.

See Poonen's paper for the remaining details.


&emsp; I do not believe there have not been any major changes to the table since its original writing. The recent survey [\[1\]](#5-references) mentions progress towards the rational case, and they explain developing local-global methods. 




## 4. Mazur's conjectures


&emsp; In [\[5\]](#5-references), for $ V $ a variety over $ \mathbb{Q} $, B. Mazur made a series of conjectures about the topological closure of the $ \mathbb{Q} $-valued points, $ V(\mathbb{Q}) $, in the $ \mathbb{R}$-valued points, $ V(\mathbb{R}) $. Let us $ \overline{V(\mathbb{Q})} $ the topological closure of $ V(\mathbb{Q}) $ in $ V(\mathbb{R}) $. Mazur's first conjecture was that, assuming $ V $ is smooth and $ V(\mathbb{Q}) $ Zariski dense in $ V $, $ \overline{V(\mathbb{Q})} $ is a finite union of connected components of $ V(\mathbb{R}) $; this is equivalent to the topological closure being open, and it was shown to be false. A subsequent conjecture of his is the following:


**Mazur's conjecture.** &nbsp; *$\overline{V(\mathbb{Q})} $ has at most a finite number of components.*


&emsp; Let us replace "variety" with "algebraic subset" in his conjecture. Write $ X $ for an algebraic subset of $ \mathbb{Q} $. We say $ S \subseteq X(\mathbb{Q}) $ is *diophantine over* $ \mathbb{Q} $ if there exists regular morphism $ f \colon Y \to X $ such that $ S = f(Y(\mathbb{Q})) $.


**Theorem 4.1.** &nbsp; *If Mazur's conjecture is true, then the closure of $ S $ in $ X(\mathbb{Q}) $ has at most finitely many components.*


*Proof.* Indeed, if Mazur's conjecture were true, then for some $ n \in \mathbb{N} $, $ \overline{Y(\mathbb{Q})} $ would have $ n $ connected components. Since $ f $ is continuous, $ f(\overline{Y(\mathbb{Q})}) $ has at most $ n $ components. Because the closure of a finite union is the union of the closures, $ \overline{f(\overline{Y(\mathbb{Q})})} $ has at most $ n $ connected components, meaning 

$$
\overline{S} = \overline{f(Y(\mathbb{Q}))} = \overline{f(\overline{Y(\mathbb{Q})})} 
$$

has at most $ n $ connected components. Q.E.D.


**Corollar 4.2.** &nbsp; *If $ \mathbb{Z} $ is diophantine over $ \mathbb{Q} $, then Mazur's conjecture is false.*




## 5. References

1. S. Anscombe, V. Karemaker, Z Kisakürek, V. Mehmeti, M. Pagano, and L. Paladino, *A survey of local-global methods for Hilbert's 10th problem*. (2023), arXiv:math/0703907v1. [Link](https://arxiv.org/abs/2309.14987)
2. Martin Davis, Hilary Putnam, and Julia Robinson, *The decision problem for exponential diophantine equations*, Ann. of Math. (2) **74** (1961), 425–436.
3. J.P. Jones and Y.V. Matijasevǐc, *Proof of recursive unsolvability of Hilbert’s tenth problem*, Amer. Math. Monthly **98** (1991), no. 8, 689–709.
4. Yuri Matijasevǐc, *The diophantineness of enumerable sets*, Dokl. Akad. Nauk SSSR **191** (1970), 279–282.
5. Barry Mazur, *The topology of rational points*, Experiment. Math. 1 (1992), no. 1, 35–45. 
6. Bjorn Poonen, *Hilbert's 10th problem over rings of number-theoretic interest*. Arizona Winter School 2003
7. Alan Turing, *"On Computable Numbers, with an Application to the Entscheidungsproblem*. Proceedings of the London Mathematical Society. Wiley. (1937) **s2-42** (1): 230–265.

