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
2. [Review of original article](#2-review-of-original-article)
3. [Putnam experiments](#3-putnam-experiments)
4. [Introducing Vantage](#4-introducing-vantage)
5. [Core architecture](#5-core-architecture)
6. [Conclusion](#6-conclusion)


## 1. Introduction

&emsp; Previously, in "[The need for an autoformalizer (2024)](/the_need_for_an_autoformalizer)", I outlined the vision for a system capable of understanding and verifying mathematics expressed in natural language, translating it into a formal framework like Lean. Since that writing, the landscape of artificial intelligence, particularly large language models (LLMs), has continued its rapid evolution. Models have become significantly more capable, demonstrating increasingly sophisticated reasoning. While the challenge of ensuring mathematical rigor remains, the potential role of formal methods like Lean is perhaps shifting. It becomes less about teaching AI basic logic from scratch and more about providing a robust framework to formally check the outputs of these powerful models, guiding them towards verifiable results and ultimately automating aspects of mathematical research. A core principle remains: if we want computers to reliably *do* mathematics, we need a way for them (and us) to *verify* their work, which necessitates formalization. (We will delve into specific model advancements later in this discussion.)

&emsp; The original article contemplated the significant challenge of training a foundational model specifically for autoformalization. This approach, while theoretically appealing, faced practical hurdles. The work described herein takes a different, more feasible path. Instead of building a large model from the ground up, we leverage the power of existing state-of-the-art LLMs, specifically using API calls to Google's Gemini models. The goal is to utilize these advanced reasoning capabilities to help construct and manage an automated, verified knowledge base within Lean.

&emsp; This leads us to the introduction of the `vantage` project. The name stands for "vantage point," inspired by Alexander Grothendieck's description of mathematical discovery. Rather than attacking a difficult problem head-on, he spoke of immersing it within a larger, richer theoretical context – like the sea rising around an obstacle – until the solution becomes almost trivial from this new, higher perspective. We believe that building an extensive, interconnected, and formally verified knowledge base in Lean can serve as such a vantage point for mathematical exploration, both human and machine-driven. This project represents the first steps in constructing that base.

&emsp; In this article, we will first briefly review the core ideas from the original piece. We will then discuss some relevant experiments before diving into the specifics of the `vantage` system – its goals, its core architecture, and how it operates. Finally, we will conclude with reflections on the current progress and future directions.


## 2. Review of original article



## 3. Putnam experiments



## 4. Introducing Vantage



## 5. Core architecture



## 6. Conclusion
