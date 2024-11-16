---
layout: ML_Project
permalink: /the_need_for_an_autoformalizer
feedformat: card
title: The Need for an Autoformalizer (2024)
---
<br>
**Abstract.** &nbsp; I argue that the that the creation of an autoformalizer—a machine which can automatically formalize mathematics—would have monumental benefits both in academic research and in industrial applications. I then sketch how one might be created.

[GitHub repository](https://github.com/justincasher/Autoformalizer){:target="_blank"}

## Table of Contents

- [Table of Contents](#table-of-contents)
- [1. Introduction](#1-introduction)
- [2. Societal impact](#2-societal-impact)
- [3. Creation](#3-creation)
- [4. References](#4-references)



## 1. Introduction

In recent years, we have seen a boom in artificial intelligence capabilities, specifically in the field of natural language processing. Through sequence-to-sequence modeling, we now have machines, called *large language models* (LLMs), which are capable of many tasks which require logical reasoning, i.e., intelligence. In particular, unlike a typical search engine, LLMs are capable of synthesizing the data that they are trained on, allowing them to complete complex tasks using a variety of different ideas.

However, there are apparent limitations to our current systems, and it is unclear whether these limitations can be overcome without considerable theoretical advancements. When tasked with solving mathematical problems, even the most advanced reasoning models often struggle to play with definitions in the way that a mathematician would. While they understand what should come next, they do not know why, and while chain-of-thought prompting can help mitigate this, we have yet to see a model which can effectively tackle advanced mathematical problems.

There have been a variety of benchmarks developed to test AI; the figure below displays the results of some of the best models on a few common tests. One recent benchmark, FrontierMath [[1]](#4-references), composed of considerably more advanced problems, resulted in the best LLMs only achieving at best around 2\% accuracy; although, it should be noted each LLM was only given a single attempt at each problem. Overall, it appears current LLMs are statistically incapable of efficiently solving technical mathematical problems.

![LLM mathematics benchmarks](images/LLM_math_results.png)

Thus, in this essay we explore how this difficulty can be overcome by building an *autoformalizer*. This is a computer program capable of interpreting imprecise logic written in English and converting it into precise formal representations in a type-theoretic framework (e.g., Lean), where the resulting code can be run, verified, and formally proven. Furthermore, an autoformalizer would have much broader applications outside of checking synthetically generated theory, as it would be capable of verifying any piece of written math. However, the existence of such a philosophical object seems virtually impossible, as human language is not exact, meaning we would need to create an approximation of it.


## 2. Societal impact


## 3. Creation


## 4. References

1. Elliot Glazer et al. "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI," 2024. [Link](https://arxiv.org/pdf/2411.04872)