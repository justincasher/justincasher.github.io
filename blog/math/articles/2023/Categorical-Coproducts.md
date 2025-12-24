---
layout: Article
parent: "Mathematics"
parent_url: "/blog"
subject: "Math"
indent: true
permalink: /categorical-coproducts
title: Categorical coproducts and K-theory
date: "May 2023"
abstract: "We define products and coproducts for arbitrary categories, then use them to define K-theories. In particular, we discuss how the integers result from this construction, and we mention the Serre-Swan Theorem."
toc:
  - title: "Limits and colimits"
    anchor: "1-limits-and-colimits"
  - title: "Products and coproducts"
    anchor: "2-products-and-coproducts"
  - title: "K-theory"
    anchor: "3-k-theory"
  - title: "References"
    anchor: "4-references"
---
<div style="display: none;">
$$
\newcommand{\cC}{\mathcal{C}}
\newcommand{\CD}{\mathcal{D}}
\newcommand{\CI}{\mathcal{I}}
\newcommand{\CO}{\mathcal{O}}
\newcommand{\NN}{\mathbb{N}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\DeclareMathOperator{\colim}{colim}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Id}{Id}
\DeclareMathOperator{\Ob}{Ob}
$$
</div>

## 1. Limits and colimits

&emsp; A *category* $$ \cC $$ is a class of objects $$ \Ob(\cC) $$ and a class of morphisms $$ \Hom(A, B) $$ between any two objects equipped with a composition law, so that for any $$ A, B, C \in \Ob(\cC), $$ we have the following: 
<ol type="a" style="list-style-position: outside">
  <li>An associative composition operator $$ \circ \colon \Hom(B, C) \times \Hom(A, B) \to \Hom(A, C); $$</li>
  
  <li>Local identities \( \Id_A \colon A \to A \), such that for any \( f \colon A \to B \), we get \( f \circ \Id_A = f \) and \( \Id_B \circ f = f \).</li>
</ol>
We denote the class of all morphisms in $$ \cC $$ by $$ \Hom(\cC) $$.

&emsp; We define maps between categories $$ F \colon \cC \to \CD $$ on the level of pairs 

$$ 
F \colon (\Ob(\cC), \Hom(\cC)) \to (\Ob(\CD), \Hom(\CD)),
$$

meaning each object (resp. morphism) in $$ \cC $$ is mapped to an object (resp. morphism) in $$ \CD $$. We call $$ F $$ a *functor* if it preserves (a) the composition operator 

$$ 
F(f \circ g) = F(f) \circ F(g) 
$$ 

and (b) local identities $$ F(\Id_A) = \Id_{F(A)} $$.

**Remark 1.1.** &nbsp; When working with categories, we are interested in when a morphism factors through another one. Intuitively, this abstracts the notion of integers dividing each another, and it leads to the notion of categorical limits and colimits. 

&emsp; Let $$ F \colon \CI \to \cC $$ be a functor. Here, we call $$ F $$ a *diagram* and $$ \CI $$ the *indexing category*. We denote an object in the image of $$ F $$ by $$ F(i) = A_i $$. The *limit* of $$ F $$ is then an object $$ \lim A_i $$ in $$ \cC $$ equipped with a morphism

$$ 
f_m \colon \lim A_i \to A_m 
$$ 

for each $$ m \in \CI $$, such that:
<ol type="a" style="list-style-position: outside">
    <li>For any morphism \( \phi \colon m \to n \) in \( \CI \), we have \( F(\phi) \circ f_m = f_n \);</li>
    
    <li>Any other collection of morphisms \( g_m \colon \CO \to A_m \) factors through the limit, meaning there exists a unique \( h \colon \CO \to \lim A_i \) making this diagram commute: 
        $$ 
        \xymatrix{ 
            & \CO \ar@{.>}[d]|-{\exists !h} \ar@/_/[ddl]_{g_m} \ar@/^/[ddr]^{g_n} & \\
            & \lim A_i \ar[dl]^{f_m} \ar[dr]_{f_n} & \\
            A_m \ar[rr]_{F(\phi)} & & A_n.
        } 
        $$</li>
</ol>

&emsp; There is likewise the dual notion of the *colimit* of $$ F $$, which is given by reversing the arrows in the definition of a limit. Explicitly, the colimit is an object $$ \displaystyle \colim A_i $$ in $$ \cC $$ equipped with a morphism

$$ 
\displaystyle f_m \colon A_m \to \colim A_i
$$ 


for each $$ m \in \CI $$, such that:
<ol type="a" style="list-style-position: outside">
    <li>For any morphism \( \phi \colon m \to n \) in \( \CI \), we have \( f_m =  f_n \circ F(\phi); \)</li>
    
    <li>Any other collection of morphisms \( g_m \colon A_m \to \CO \) factors through the limit, meaning there exists a unique \( \displaystyle h \colon \colim A_i \to \CO \) making this diagram commute: 
        $$ 
        \xymatrix{ 
            A_m \ar[rr]^{F(\phi)} \ar@/_/[ddr]_{g_m} \ar[dr]^{f_m} & & A_n \ar@/^/[ddl]^{g_n} \ar[dl]_{f_n} \\
            & \colim A_i \ar@{.>}[d]|-{\exists !h} & \\
            & \CO &
        } 
        $$</li>
</ol>

&emsp; Let $$ f \colon A \to B $$ be a morphism. If there exists a map $$ f^{-1} \colon B \to A $$ such that $$ f \circ f^{-1} = \Id_Y $$ and $$ f^{-1} \circ f = \Id_X $$, then we call $$ f $$ an *isomorphism*. Likewise $$ A $$ and $$ B $$ are said to be *isomorphic*, which we denote $$ A \cong B $$. For sets an isomorphism is a bijection; for groups the usual notion of an isomorphism; for topological spaces it is a homeomorphism; etc. 

**Proposition 1.2.** &nbsp; The limit (resp. colimit) of a diagram is unique up to isomorphism.

*Proof.* Suppose $$ L_1 $$ and $$ L_2 $$ both are limits of a given diagram. Then there exists maps $$ h \colon L_1 \to L_2 $$ and $$ h^{-1} \colon L_2 \to L_1 $$. We observe $$ h \circ h^{-1} \colon L_1 \to L_1 $$ is a map making the diagram commute. Since there exists a unique map $$ L_1 \to L_1 $$ making the diagram commute by assumption, we conclude that $$ h \circ h^{-1} = \Id_{L_1} $$ and that $$ L_1 \cong L_2 $$. $$ \blacksquare $$

**Remark 1.3.** &nbsp; In arbitrary categories limits (resp. colimits) do not always exist. Hence, this definition describes limits, unique up to isomorphism, under the assumption that they can be constructed.



## 2. Products and coproducts

&emsp; We call the limit over a diagram $$ F \colon \CI \to \cC $$ such that $$ \CI $$ has only identity morphisms 

$$
\Hom_{\CI}(m, n) = 
\begin{cases}
    \Id_A & \text{ if } m = n \\
    \varnothing & \text{ if } m \neq n
\end{cases}
$$

a *product*, which is denoted

$$
\prod A_i = \lim A_i.
$$

This is the same as choosing an indexed subset of objects $$ \{ A_i \} $$ in $$ \cC $$, such that the following diagram commutes:

$$ 
\xymatrix{ 
    \CO \ar@{.>}[d]|-{\exists !h} \ar[dr]^{g_m} \\
    \prod A_i \ar[r]_{\pi_n} & A_m.
} 
$$

Here, we have replaced $$ f_m $$ with $$ \pi_m $$, which we call the *projection* onto $$ A_m $$*.

&emsp; We likewise define define the coproduct as the colimit over diagrams with no morphisms, which we denote 

$$
\coprod A_i = \colim A_i,
$$

This is equivalent to choosing an indexed subset of objects $$ \{ A_i \} $$ in $$ \cC $$, such that the following diagram commutes:

$$ 
\xymatrix{ 
    A_m \ar[dr]_{g_m} \ar[r]^{\iota_m} & \coprod A_i \ar@{.>}[d]|-{\exists !h} \\
    & \CO
} 
$$

We call the maps $$ \iota_m $$ the *inclusion* into $$ A_m $$*.

**Example 2.1.** &nbsp; The following table gives common names of products and coproducts in different categories. Note that schemes are more nuanced due the contravariant nature of the Spec functor and only finite products and coproducts necessarily existing.

| Category | Product | Coproduct |
| :--------: | :-------: | :---------: |
| Sets | Cartesian product | Disjoint union |
| Groups | Direct product | Free product |
| Abelian groups | Direct product | Direct sum |
| Rings | Direct product | Free product |
| Commutative rings | Direct product | Tensor product (over $$ \ZZ $$) |
| $$ R $$-modules | Direct product | Direct sum |
| $$ k $$-vector spaces | Direct product | Direct sum |
| Topological spaces | Box topology | Product topology |
| Pointed topological spaces | Box topology modulo basepoint | Wedge sum |
| Schemes | Fiber product (over $$ \ZZ $$) | Disjoint union of spaces, product of rings |
| Poset | Infimum | Supremum |

<hr style="height:8px; visibility:hidden;" />

&emsp; We briefly detail the last example: that for a poset, i.e. a partially ordered set, the product is the infimum and the coprodcut is the supremum. Recall that a set $$ X $$ equipped with a relation $$ \leq $$ is called a *poset* if it satisfies
<ol type="a" style="list-style-position: outside">
    <li>\( x \leq x \),</li>
    
    <li>\( x \leq y \) and \(y \leq x \) implies \( x = y \), and</li> 
    
    <li>\( x \leq y \) and \( y \leq z \) implies \( x \leq z \).</li>
</ol> 

&emsp; Associated to any poset $$ X $$ is a category whose objects are the elements of $$ X $$ and morphisms represent the relation, meaning

$$
\Hom(x, y) = 
\begin{cases}
    \text{a single morphism} & \text{ if } x \leq y \\
    \varnothing & \text{ else.}
\end{cases}
$$

We see that in this category for a family of elements $$ \{ x_i \} $$ in $$ X $$, the product diagram

$$ 
\xymatrix{ 
    y \ar@{.>}[d]|-{\exists !h} \ar[rd]^{g_m} \\
    \prod x_i \ar[r]_{\pi_n} & x_m.
} 
$$

reads as follows: “Any $$ y $$ which is less than each $$ x_n $$ is less than their product.“ Hence, their product is the greatest element less than our collection $$ \{ x_i \} $$, meaning it is their infimum. Likewise their coproduct is their supremum.

**Remark 2.2.** &nbsp; Recall that the class of sets is partially ordered by inclusion. For a collection of sets $$ \{X_i\} $$, the infimum is their intersection $$ \bigcap X_i $$, and the supremum is their union $$ \bigcup X_i $$. Hence, intersections and unions are category theoretic products and coproducts, respectively. This interests us since the natural numbers $$ \NN $$ are recursively constructed using unions; omitting details, we set $$ 0 = \varnothing $$ and define addition by $$ n+1 = n \cup \{ n \} $$. The integers $$ \ZZ $$ are then defined by formally appending elements $$ -n $$ such that $$ n + (-n) = 0 $$. This process (in some sense) motivates K-theory, which gives another construction of the integers.



## 3. K-theory

&emsp; Let $$ \cC $$ be a suitably nice category, i.e. abelian. Objects being isomorphic is an equivalence relation. Thus, if $$ A $$ and $$ B $$ are isomorphic, then we say that $$ A $$ and $$ B $$ belong to the same isomorphism class, which we denote $$ [A] = [B] $$. We further write $$ [\Ob(\cC)] $$ for the class of all isomorohism classes in $$ \cC $$.
 
&emsp; Suppose coproducts exist in $$ \cC $$, that every element in $$ \cC $$ is projective meaning $$ \cC $$ is semisimple, and that the collection of isomorphism classes form a set, i.e. $$ \cC $$ modulo isomorphism is a set. Then we can form a monoid with elements $$ [\Ob(\cC)] $$ and addition $$ [A] + [B] = [A \oplus B] $$, which is commutative since $$ A \oplus B \cong B \oplus A $$. (If we do not assume every object is projective, then we can define addition by $$ 0 \to A \to B \to C $$  implies $$ [B] = [A] + [C] $$.) We append inverses by as follows. 

&emsp; Write $$ (M, +) $$ for a commutative monoid and an element of $$ M \times M $$ as a pair $$ (m^+, m^-) $$. Consider two such pairs $$ (m_1^+, m_1^-) $$ and $$ (m_2^+, m_2^-) $$. We add them component-wise

$$
(m_1^+, m_1^-) + (m_2^+, m_2^-) = (m_1^+ + m_2^+, m_1^- + m_2^-),
$$

and we consider them to be equivalent if there exists an $$ a \in M $$ such that 

$$
m_1^+ + m_2^- + a = m_2^+ + m_1^- + a.
$$

We call $$ M \times M $$ modulo this equivalence relation the *Grothendieck group* of $$ M $$.

&emsp; Returning to $$ \cC $$, we call the resulting group $$ [\Ob(\cC)] $$ the *K-group* of $$ \cC $$. 

**Example 3.1.** &nbsp; In the category of finite sets, an isomorphism is a bijection, meaning we can associate with each isomorphism class a natural number, i.e. its cardinality. We see that the coproduct here is disjoint union

$$
X \coprod Y = X \times \{0\} \cup Y \times \{1\},
$$

which is indeed the usual notion of addition on $$ \NN $$. Thus, the $$ K $$-group of finite sets is $$ \ZZ $$. Furthermore, (Cartesian) products of sets allow us to define multiplication.

**Example 3.2.** &nbsp; Write $$ X $$ for a compact Hausdorff space, and consider the category of real vector bundles on $$ X $$ with the coproduct being given locally (i.e. the Whitney sum). We denote the K-group of this category $$ KO_0(X) $$. It is referred to as *real topological K-theory*.

**Example 3.3.** &nbsp; Let $$ R $$ be a ring, and consider the category of finitely generated projective modules on $$ X $$ with the usual coproduct. We denote the K-theory of this category $$ K_0(R) $$. It is referred to as *algebraic K-theory*.

&emsp; The following theorem motivates the use of projective modules in algebraic K-theory. Note that higher (and lower) K-groups can be defined; we have given the base case.

**Serre-Swan Theorem.** &nbsp; *Let $$ X $$ be compact Hausdorff and $$ \cC(X) $$ its algebra of continuous functionals $$ f \colon X \to \RR $$. Then the map sending any real vector bundle on $$ X $$ to its $$ \cC(X) $$-module of continuous sections yields an isomorphism $$ KO_0(X) \cong K_0(\cC(X)) $$.*

*Proof.* Serre originally proved a similar statement for the prime spectrum of commutative rings in [\[4\]](#4-references). The above statement was shown by Swan in [\[5\]](#4-references). A generalization is given in [\[3\]](#4-references). $$ \blacksquare $$



## 4. References

1. Alexander Grothendieck, *Sur quelques points d’algèbre homologique, I*, Tohoku Mathematical Journal **9** (1957), no. 2, 119–221.
2. Saunders Mac Lane, *Categories for the working mathematician*, Springer, 1978.
3. Archana S. Morye, *Note on the Serre-Swan theorem*, Mathematische Nachrichten **286** (2013), no. 2-3, 272–278.
4. Jean-Pierre Serre, *Vector bundles and projective modules*, Annals of Mathematics **61** (1955), no. 2, 197–278.
5. Richard Swan, *Vector bundles and projective modules*, Transactions of the American Mathematical Society **105** (1962), no. 2, 264–277.
