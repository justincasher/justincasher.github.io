---
layout: AI
permalink: /autoformalizer_pt_ii
feedformat: card
title: Autoformalizer, pt. II (2025)
---
<br>
**Abstract.** &nbsp; 


## Table of Contents

1. [Introduction](#1-introduction)
2. [Putnam Experiments](#2-putnam-experiments)
3. [Introducing Vantage](#3-introducing-vantage)
4. [Core Architecture](#4-core-architecture)
5. [Conclusion](#5-conclusion)


## 1. Introduction

&emsp; Previously, in [The need for an autoformalizer (2024)](/the_need_for_an_autoformalizer), I outlined the vision for a system capable of understanding and verifying mathematics expressed in natural language, translating it into a formal framework like Lean. Since that writing, the landscape of artificial intelligence, particularly large language models (LLMs), has continued its rapid evolution. Models have become significantly more capable, demonstrating increasingly sophisticated reasoning. While the challenge of ensuring mathematical rigor remains, the potential role of formal methods like Lean is perhaps shifting. It becomes less about teaching AI basic logic from scratch and more about providing a robust framework to formally check the outputs of these powerful models, guiding them towards verifiable results and ultimately automating aspects of mathematical research. A core principle remains: if we want computers to reliably *do* mathematics, we need a way for them (and us) to *verify* their work, which necessitates formalization.

&emsp; The progress in this domain has been remarkably swift. Within just the past year or two, leading models from Google (Gemini 2.5 Pro), OpenAI (o1 and successors), among other labs, have shown dramatic improvements in mathematical problem-solving. Driven by larger scale, refined training techniques, and explicit reasoning strategies (like step-by-step thinking), performance on challenging benchmarks has soared. For instance, top scores on the dynamic LiveBench math category leaped from around 50% in mid-2024 to approximately 90% by early 2025, with models now approaching or achieving scores comparable to top human participants on standardized tests like the AIME competition. This rapid advancement underscores the growing potential for AI in complex mathematical tasks.

&emsp; The original article contemplated the significant challenge of training a foundational model specifically for autoformalization. This approach, while theoretically appealing, faced practical hurdles. The work described herein takes a different, more feasible path. Instead of building a large model from the ground up, we leverage the power of existing state-of-the-art LLMs, specifically using API calls to Google's Gemini models. The goal is to utilize these advanced reasoning capabilities to help construct and manage an automated, verified knowledge base within Lean.

&emsp; This leads us to the introduction of the Vantage Project. The name stands for "vantage point," inspired by Alexander Grothendieck's description of mathematical discovery. He offered an analogy (from *Récoltes et Semailles*):

> The first analogy that came to my mind is of immersing the nut in some softening liquid, and why not simply water? From time to time you rub so the liquid penetrates better,and otherwise you let time pass. The shell becomes more flexible through weeks and months – when the time is ripe, hand pressure is enough, the shell opens like a perfectly ripened avocado!

We believe that building an extensive, interconnected, and formally verified knowledge base in Lean can serve as such a vantage point for mathematical exploration, both human and machine-driven. This project represents the first steps in constructing that base.

&emsp; In this article, we will first briefly review the core ideas from the original piece. We will then discuss some relevant experiments before diving into the specifics of the Vantage Project – its goals, its core architecture, and how it operates. Finally, we will conclude with reflections on the current progress and future directions.


## 2. Putnam Experiments

&emsp; Before embarking on the main development of the Vantage Project, some preliminary experiments were conducted using problems from the notoriously difficult Putnam Mathematical Competition. The central question was whether a relatively inexpensive, less powerful LLM – specifically Gemini 1.5 Flash, which is not primarily optimized for complex reasoning – could be guided towards solving such problems through sophisticated prompting techniques alone, without relying on formal methods or explicit proof generation tools at this stage.

&emsp; The core idea was to test the limits of prompting as a way to scaffold the model's reasoning process. Various strategies were employed, with a notable focus on prompting the model to perform targeted literature reviews. For a given Putnam problem, the model was asked: "What existing mathematical concepts, theorems, or techniques might be useful for solving this?" This approach yielded interesting results. For instance, when presented with problem A6 from the 2024 competition (a problem presumed to be outside the model's direct training data):

> **Putnam 2024 A6:** Let $c_0, c_1, c_2, \dots$ be the sequence defined so that
> $$ \frac{1 - 3x - \sqrt{1 - 14x + 9x^2}}{4} = \sum_{k=0}^{\infty} c_k x^k $$
> for sufficiently small $x$. For a positive integer $n$, let $A$ be the $n \times n$ matrix with $i, j$-entry $c_{i+j-1}$ for $i, j \in \{1, \dots, n\}$. Find the determinant of $A$.

The LLM correctly identified orthogonal polynomials and continued fractions as highly relevant topics. Crucially, the model did not simply identify these topics; it was able to retrieve and articulate key definitions and results related to them from its internal knowledge, without human intervention providing these details. This self-supplied information then enabled the model, through subsequent interactions, to outline some potentially viable solution strategies.

&emsp; However, these experiments also revealed a crucial limitation. While strategic prompting and literature retrieval could guide Gemini 1.5 Flash to identify *correct approaches*, the model fundamentally lacked the deeper reasoning capacity required to *execute* the solution and navigate the intricate steps involved in a full Putnam-level proof. Even with the right strategy laid out, it struggled to synthesize the information and complete the argument. This suggests that while prompting can significantly augment capabilities, there might be a ceiling imposed by the underlying model's reasoning power for sufficiently complex, novel problems. (It is plausible that newer, more powerful reasoning models, such as Gemini 1.5 Pro or its successors, may overcome this specific limitation.)

&emsp; Despite this, the experiments provided valuable takeaways that reinforce the direction of the Vantage Project. Firstly, they underscored the power of prompting for targeted information retrieval. LLMs excel at searching and synthesizing information from their training data, akin to accessing a vast internal library. Secondly, the difficulty the model faced in *applying* knowledge to solve a novel problem, even when guided, contrasts with its potential strength in processing and structuring *known* results. This suggests that the task of formalizing existing mathematical literature – translating established theorems and proofs into Lean – might be considerably more tractable for current AI than solving frontier problems from scratch.

&emsp; Furthermore, the experience with Putnam A6 highlighted the profound impact of accessible knowledge. It was later discovered that a paper exists containing a closed-form solution related to the problem. Had this specific result been readily available and identifiable to the model (i.e., part of a queryable, structured knowledge base), the problem would have become essentially trivial – a matter of lookup and verification rather than complex derivation. This powerfully illustrates the potential of a comprehensive, formalized mathematical knowledge base, which is precisely what the Vantage Project aims to build. Access to the right "vantage point" of existing knowledge can dramatically simplify or even solve otherwise formidable challenges.


## 3. Introducing Vantage



## 4. Core Architecture



## 5. Conclusion
