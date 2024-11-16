---
layout: ML_Project
permalink: /the_need_for_an_autoformalizer
feedformat: card
title: The need for an autoformalizer (2024)
---
<br>
**Abstract.** &nbsp; I argue that the that the creation of an autoformalizer—a machine which can automatically formalize mathematics—would have monumental benefits both in academic research and in industrial applications. I then sketch how one might be created.

[GitHub repository](https://github.com/justincasher/Autoformalizer){:target="_blank"}



## Table of Contents

1. [Introduction](#1-introduction)
2. [Societal impact](#2-societal-impact)
3. [Creating an autoformalizer](#3-creating-an-autoformalizer)
4. [References](#4-references)



## 1. Introduction

In recent years, we have seen a boom in artificial intelligence capabilities, specifically in the field of natural language processing. Through sequence-to-sequence modeling, we now have machines, called *large language models* (LLMs), which are capable of many tasks which require logical reasoning, i.e., intelligence. In particular, unlike a typical search engine, LLMs are capable of synthesizing the data that they are trained on, allowing them to complete complex tasks using a variety of different ideas.

However, there are apparent limitations to our current systems, and it is unclear whether these limitations can be overcome without considerable theoretical advancements. When tasked with solving mathematical problems, even the most advanced reasoning models often struggle to play with definitions in the way that a mathematician would. While they understand what should come next, they do not know why, and while chain-of-thought prompting can help mitigate this, we have yet to see a model which can effectively tackle advanced mathematical problems.

There have been a variety of benchmarks developed to test AI; the figure below displays the results of some of the best models on a few common tests. One recent benchmark, FrontierMath [[1]](#4-references), composed of considerably more advanced problems, resulted in the best LLMs only achieving at best around 2\% accuracy; although, it should be noted each LLM was only given a single attempt at each problem. Overall, it appears current LLMs are statistically incapable of efficiently solving technical mathematical problems.

![LLM mathematics benchmarks](images/LLM_math_results.png)

Thus, in this essay we explore how this difficulty can be overcome by building an *autoformalizer*. This is a computer program capable of interpreting imprecise logic written in English and converting it into precise formal representations in a type-theoretic framework (e.g., Lean), where the resulting code can be run, verified, and formally proven. Furthermore, an autoformalizer would have much broader applications outside of checking synthetically generated theory, as it would be capable of verifying any piece of written math. However, the existence of such a philosophical object seems virtually impossible, as human language is not exact, meaning we would need to create an approximation of it.



## 2. Societal impact

Before we dive into applications, let us briefly discuss what an autoformalizer is and what it could do. In the most basic sense, it is a math checker for any theorem, equation, etc. An autoformalizer would never make mistakes while being able to detect any written error. Albeit, this simplistic perspective disregards the interpretability that is innate to most human writing (at least outside of extremely precise mathematics), and hence would be theoretically impossible to create. Hence, we are interested in a machine which is capable flagging any *possible* mathematical mistake, whether it be due to a lack of clarity in the writing or a genuine error.


#### Example 1: Mars climate orbiter mishap

In 1999, a &dollar;327.6 million (~&dollar;630 million today) spacecraft was lost due to a unit conversion error. The software which controlled the ship's thrusters was built by Lockheed Martin, who assumed the input to be in imperial units (pound-force seconds), while NASA’s Jet Propulsion Laboratory used metric units (newton-seconds). This caused the thrusters to under-fire, resulting in the spacecraft coming too close to mars, either disintegrating or skipping off into space. An autoformalizer could have easily caught this unit mismatch.


#### Example 2: Knight Capital trading loss

In 2012, the high-frequency trading firm Knight Capital lost &dollar;440 million (~&dollar;612 million today) because of a software error. After updating some but mistakenly not all of their servers, Knight Capital's trading code had a logical error in it which resulted in buying stocks high and selling them low. An autoformalizer would have been able to gaurantee that the computer code matched the intended trading algorithm, flagging this error before trading began.

More broadly speaking, financial institutions and corporations must adhere to strict regulatory requirements. These often involve intricate mathematical models for risk assessment, tax calculations, or financial projections. Errors in these computations can result in substantial fines, reputational damage, or even financial collapse. An autoformalizer could flag inconsistencies in a given set of models, ensuring that calculations are both accurate and compliant with regulations.


#### Example 3: Civil engineering

The failure of infrastructure projects, such as bridges or dams, can often be traced back to calculation errors during the design phase. An autoformalizer could rigorously check all engineering calculations and ensure consistency in models, helping to prevent such disasters. 


#### Example 4: Automated paper review

Academic, and, in particular, mathematical, manuscripts often take months to properly review. However, an autoformalizer would be able to instantly check that all of the underlying mathematical theory is correct. Then, human reviewers could focus on the impact of the ideas, instead of laboring over small details. This will become increasingly important as AI helps write more papers, or even entire ones by itself, creating a need for a quick way to review this growing volume of information. Furthermore, I believe that this could help decentralize academia, allowing a more democratic process towards evaluating papers, as any mathematical paper could be put online with the reader knowing everything in it is logically sound.


#### Example 5: Mathematical superintelligence

As discussed in the introduction, current LLMs are poor at mathematical reasoning. Even if they do improve, I still believe a specialized program would be more efficient and be able to better index information. It seems apparent to me that the best way to train such a program would be on formalized mathematics, but we have only formalized an extremely small portion of the literature. Hence, an autoformalizer could be an important step towards technological acceleration via superintelligence: Many research areas have simply not been explored properly due to the limited capacity of human intelligence.



## 3. Creating an autoformalizer





## 4. References

1. Elliot Glazer et al. "FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI," 2024. [Link](https://arxiv.org/pdf/2411.04872)

2. Mars Climate Orbiter Mishap Investigation Board. "Mars Climate Orbiter Mishap Investigation Phase I Report," 1999. [Link](https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf)

3. Mars Climate Orbiter Mishap Investigation Board. "Report on Project Management in NASA: Lessons Learned from the Mars Climate Orbiter Failure," 1999. [Link](https://discovery.larc.nasa.gov/PDF_FILES/mars_climate_orbiter_phaseII.pdf)

4. NASA. "Mars Climate Orbiter (1998-073A) Spacecraft Details." NSSDC Master Catalog, 1998. [Link](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=1998-073A)