---
layout: Writing
indent: true
permalink: /Hilberts-10th-problem
feedformat: card
title: Hilbert's 10th problem
---
<style>
    ol.custom {
        margin-top: -10px;
        margin-bottom: 20px;
        margin-left: -15px;
    }
    
    li {
        padding-top: 0px; 
        padding-bottom: 0px;
        margin-top: 0px;
        margin-bottom: 5px;
    }
}
</style>
<br>
**Abstract.** &nbsp; We follow the proof given in B. Poonen's expository article, [CITE], on how Turing machines and the Halting problem are used to show Hilbert's 10th conjecture is false.




## Table of Contents
1. [Turing machines](#1-introduction-to-infinity-categories)

4. [References](#4-references)




## 1. Turing machines

&emsp; A *Turing machine*, introduced by A. Turing, [\[CITE\]](#4-references), is a way to mathematically formalize the idea of an algorithm. We will not give the explicit definition here, as we will only need an informal notion for our purposes. A Turing machine can be thought of as a finite program having infinite memory, i.e., it is free of any physical memory constraints that a real computer has. It execeutes infinitely fast, meaning we are more concerned with whether a Turing machine *halts*, or stops after a finite number of steps, with respect to a given input rather than its run time.


&emsp; Visually, a Turing machine $ T $ can be viewed as string of code, which is equivalent to a finite piece of tape:

$$
1, 0, 0, 1, 1, 1
$$

Its memory $ M $ is likewise a piece of tape, but this time infinite, although at any point during the computation it can only contain finitely many 1's:

$$
\dots, 0, 0, 0, 1, 1, 0, 1
$$

Thus, $ M $ is initialized to some infinite sequence containing finitely many 1's, and then $ T $ acts on $ M $ until it halts; it is also possible that the machine does not halt.


&emsp; We can identify Turing machines with integers via any bijection between the natural numbers $ \mathbb{N} $ and the integers $ \mathbb{Z} $. Thus, we will write $ T \in \mathbb{Z} $. Likewise its initial input, since it only contains finitely many 1's, can also be identified with an integer $ a \in \mathbb{Z} $. We will denote inputting $ a $ to $ T $ by $ T(a) $. If our Turing machine halts or its memory converges to some infinite sequence, then we will also use $ T(a) $ to denote this value.


&emsp; Let $ P \subseteq \mathbb{Z} $ be a subset of the possible inputs. We say that a Turing machine $ T $ solve the decision problem $ P $ if, for each $ a \in \mathbb{Z} $, $ T(a) $ halts with output 1 if $ a \in P $ and 0 if $ a \not \in P $. There are uncountably many possible decision problems but only countably many Turing machines, so not every decision problem has a solution; we call such decision problems *unsolvable*.


&emsp; To shorten our terminology, we say a decision problem $ P $ is *recursive* if there exists a Turing machine which solves it. We say $ P $ is *listable* if there exists a Turing machine $ T $ which outputs $ P $ if left running forever, i.e., $ T(0) = P $.


**Proposition 1.1.** &nbsp; *Recursive implies listable.*


*Proof.* Let $ T $ solve $ P $, and let $ Z $ be a Turing machine which prints the integers $ 0, -1, 1, -2, 2, \dots $. Then taking each output of $ Z $ and inputting it to $ T $ lists $ P $. Q.E.D.


&emsp; The halting problem asks whether there exists a Turing machine $ H $ whose input is a pair $ (T, a) \subseteq \mathbb{Z} \times \mathbb{Z} $ (which we can, of course, identify with an integer), and whose output is whether $ T(a) $ halts. As it turns out, Turing showed that the halting problem is undecidable.


**Theorem 1.2** ([\[CITE\]]()). &nbsp; *The decision problem is undecidable.*


*Proof.* Suppose $ H $ exists. Then there would exist a Turing machine $ G $ such that $ G(a) $ halts if and only $ a(a) $ does not halt. But setting $ a $ to be $ G $, we see that $ G(G) $ halts if and only if $ G(G) $ does not halt, a contradiction. Q.E.D. 


**Corollary 1.3.** &nbsp; There exists a listable set $ P $ which is not recursive.


*Proof.* Set 

$$
P = \{2^T 3^a \mid T, a \in \mathbb{Z} \text{ and } T(a) \text{ halts} \}.
$$

Then $ T $ is not recursive by theorem 1.2. It is, however, listable: for each $ N \in \mathbb{N} $ and $ T, a \in \mathbb{Z} $ with $ \vert T \vert, \vert a \vert \leq N $, print $ 2^T 3^a $ if $T(a) $ it halts within $ N $ steps. Q.E.D.




## 2. Hilbert's 10th problem

&emsp; *Hilbert's 10th problem* asks whether there exists an algorithm which determines whether a polynomial with integer coefficients has a solution in the integers. We can rewrite this using Turing machines as follows. Let $ P $ be the decision problem 

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

The following result about diophantine sets was shown by J. Matijasevǐc, [\[CITE\]](#4-references), using the work of M. Davis, H. Putnam, and J. Robinson, [\[CITE\]](#4-references).

**Theorem 2.1** &nbsp; *Let $ S \subseteq \mathbb{Z}^n $. Then $ S $ is listable (after identifying $ \mathbb{Z}^n $ with $ \mathbb{Z} $) if and only if it is diophantine.*





## 3. Other results and applications





## 4. References

1. 