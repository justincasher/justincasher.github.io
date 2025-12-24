---
layout: Article
parent: "Artificial intelligence"
parent_url: "/blog"
subject: "AI"
permalink: /introducing_vantage
title: "Introducing Vantage: Towards highly-parallelized autoformalization"
date: "March 2025"
links:
  - type: "GitHub"
    url: "https://github.com/justincasher/vantage"
    display: "github.com/justincasher/vantage"
  - type: "Website"
    url: "https://www.vantageproject.org/"
    display: "vantageproject.org"
abstract: "This article introduces the Vantage Project, which uses AI (LLMs) to help build a large, verified mathematical knowledge base in the formal system Lean 4. While AI is good at finding math information, ensuring proofs are correct is hard. Vantage uses AI suggestions and Lean's checking power to create a trustworthy foundation—a \"vantage point\"—for automating mathematics."
toc:
  - title: "Introduction"
    anchor: "1-introduction"
  - title: "Putnam experiments"
    anchor: "2-putnam-experiments"
  - title: "Introducing Vantage"
    anchor: "3-introducing-vantage"
  - title: "System design and workflow"
    anchor: "4-system-design-and-workflow"
  - title: "Relationship with existing Lean libraries"
    anchor: "5-relationship-with-existing-lean-libraries"
  - title: "Conclusion"
    anchor: "6-conclusion"
---

## 1. Introduction

&emsp; Previously, in [The need for an autoformalizer (2024)](/the_need_for_an_autoformalizer){:target="_blank"}, I outlined the vision for a system capable of understanding and verifying mathematics expressed in natural language, translating it into a formal framework like Lean. Since that writing, the landscape of artificial intelligence, particularly large language models (LLMs), has continued its rapid evolution. Models have become significantly more capable, demonstrating increasingly sophisticated reasoning. While the challenge of ensuring mathematical rigor remains, the potential role of formal methods like Lean is perhaps shifting. It becomes less about teaching AI basic logic from scratch and more about providing a robust framework to formally check the outputs of these powerful models, guiding them towards verifiable results and ultimately automating aspects of mathematical research. A core principle remains: if we want computers to reliably *do* mathematics, we need a way for them (and us) to *verify* their work, which necessitates formalization.

&emsp; The progress in this domain has been remarkably swift. Within just the past year or two, leading models from Google (Gemini 2.5 Pro), OpenAI (o1 and successors), among other labs, have shown dramatic improvements in mathematical problem-solving. Driven by larger scale, refined training techniques, and explicitly teaching models to reason, performance on challenging benchmarks has soared. For instance, top scores on the dynamic LiveBench math category leaped from around 50% in mid-2024 to approximately 90% by early 2025, with models now approaching or achieving scores comparable to top human participants on standardized tests like the AIME competition. This rapid advancement underscores the growing potential for AI in complex mathematical tasks.

&emsp; The original article contemplated the significant challenge of training a foundational model specifically for autoformalization. This approach, while theoretically appealing, faced practical hurdles. The work I describe herein takes a different, more feasible path. Instead of building a large model from the ground up, I chose to leverage the power of existing state-of-the-art LLMs, specifically using API calls to Google's Gemini models. The goal is to utilize these advanced reasoning capabilities to help construct and manage an automated, verified knowledge base within Lean.

&emsp; This led me to the introduction of the Vantage Project. The name stands for "vantage point," inspired by Alexander Grothendieck's description of mathematical discovery. He offered an analogy (from *Récoltes et Semailles*):

> The first analogy that came to my mind is of immersing the nut in some softening liquid, and why not simply water? From time to time you rub so the liquid penetrates better,and otherwise you let time pass. The Sshell becomes more flexible through weeks and months – when the time is ripe, hand pressure is enough, the shell opens like a perfectly ripened avocado!

We believe that building an extensive, interconnected, and formally verified knowledge base in Lean can serve as such a vantage point for mathematical exploration, both human and machine-driven. This project represents the first steps in constructing that base.

&emsp; In this article, I will first briefly review the core ideas from the original piece. I will then discuss some relevant experiments before diving into the specifics of the Vantage Project—its goals, its core architecture, and how it operates. Finally, I will conclude with reflections on the current progress and future directions.


## 2. Putnam experiments

&emsp; To better understand the capabilities and limitations of current LLMs in mathematical problem-solving, particularly when using more economical models, I conducted experiments focusing on the challenging Putnam competition problems. The approach involved an agentic workflow using Gemini 2.0 Flash, structured around three interacting roles: a "Literature Bot" to identify relevant mathematical concepts and theorems, a "Proof Bot" to attempt solutions based on these ideas, and a "Review Bot" to critique the generated proofs. My central idea was to see if strategic prompting and this division of labor could compensate for the base model's less advanced reasoning abilities.

&emsp; The Literature Bot proved quite effective. Tasked with finding relevant background for specific problems, like Putnam 2024 A6:
> **Putnam 2024 A6:** Let $c_0, c_1, c_2, \dots$ be the sequence defined so that
> $$ \frac{1 - 3x - \sqrt{1 - 14x + 9x^2}}{4} = \sum_{k=0}^{\infty} c_k x^k $$
> for sufficiently small $x$. For a positive integer $n$, let $A$ be the $n \times n$ matrix with $i, j$-entry $c_{i+j-1}$ for $i, j \in \{1, \dots, n\}$. Find the determinant of $A$.

The difficulty of this particular problem is underscored by the official score distribution:

| Score Range | Number of Participants |
|-------------|------------------------|
| 0 points    | 429                    |
| 1–2 points  | 74                     |
| 9 points    | 1                      |
| Other       | 0                      |

The Literature Bot successfully identified key concepts like orthogonal polynomials and continued fractions and retrieved pertinent definitions and results autonomously. This highlighted the LLM's strength in accessing and synthesizing its vast internal knowledge base, providing valuable inspiration for the Proof Bot.

&emsp; However, two significant challenges emerged, highlighting the gap between identifying ideas and executing rigorous proofs. First, verifying the precise applicability and correctness of the retrieved concepts within the problem's context remained difficult for the system. This reflects a broader issue: much mathematical knowledge is locked in formats (like old papers or textbooks) that are not easily machine-verified, hindering reliable exploitation by AI. Second, the Proof Bot (using Gemini 2.0 Flash) lacked the fundamental reasoning power to correctly implement a proof strategy and navigate the intricate steps required, *even when some of the core ideas were identified* by the Literature Bot. While this limitation might be seen as a "failure" of the base model, it also serves as a positive indicator: the agentic system, particularly the Literature Bot, demonstrated capabilities (like identifying relevant, non-obvious concepts) that might exceed what the base model could achieve in isolation. I hope to experiment further with more advanced reasoning models in the near future to explore these dynamics.

&emsp; Notably, the more powerful Gemini 2.5 Pro model, whose training data *did* include the 2024 Putnam problems, was reportedly able to solve A6, illustrating the significant advantage conferred by having relevant information directly accessible within the model's training—further emphasizing the utility of LLMs for retrieving known results.

&emsp; These findings were instrumental in shaping the direction of the Vantage Project. The experiments suggested that while LLMs are powerful information retrieval tools (especially for information they were trained on), leveraging them for novel, complex problem-solving faces hurdles in both knowledge verification and deep reasoning. This reinforces the idea that a more tractable and immediately valuable application of current AI is the formalization of *existing* mathematical knowledge—knowledge that models like Gemini 2.5 Pro demonstrate they can effectively retrieve and utilize when available. Creating a comprehensive, accessible, and formally verified knowledge base addresses the verification challenge directly. Furthermore, building this structured "web of mathematics" provides the necessary context and reliable foundations (the "vantage point") needed to eventually tackle more complex problems—not just contest math, but any problem that can be better understood by situating it within the broader mathematical landscape.


## 3. Introducing Vantage

&emsp; Informed by the challenges and opportunities highlighted in my earlier experiments, the Vantage Project represents a concrete step towards the goal of automated mathematical verification and knowledge management. It is a software system designed specifically to build and maintain a large-scale, formalized mathematical knowledge base (KB) using the Lean 4 proof assistant. In essence, it acts as a "Lean Automator," orchestrating the process of incorporating mathematical knowledge into a verifiable digital format.

&emsp; The core objectives of the Vantage Project are threefold:
1. **Ingestion and Formalization:** To systematically take mathematical statements (definitions, theorems, axioms, examples) provided in various formats (potentially including natural language or LaTeX in the future) and, with the assistance of LLMs like Gemini, translate them into formal Lean 4 code.
2. **Rigorous Verification:** To leverage the power of Lean 4 and its build system (Lake) to ensure that every single item added to the knowledge base is logically sound and correctly proven according to the rules of the formal system. Verification is paramount; only proven items are fully integrated.
3. **Structured Storage and Interconnection:** To store these verified items, along with relevant metadata (like natural language descriptions, topics, dependencies), in a structured database (SQLite). This creates a queryable, interconnected "web" of mathematical facts, forming the foundation of the "vantage point" discussed earlier. A key aspect of this is maintaining a persistent, incrementally growing shared library of compiled Lean code, allowing new proofs to efficiently build upon already verified results.

&emsp; Technically, the Vantage Project is primarily built using Python, orchestrating interactions between the SQLite database, the Lean 4 toolchain (compiler and Lake), and external LLM APIs (currently Google's Gemini). The following section delves into the specific components and workflow that constitute the system's design.


## 4. System design and workflow

&emsp; The process of adding a new, verified mathematical item to the Vantage knowledge base involves a multi-stage, LLM-driven workflow, designed to move from informal ideas to formally verified Lean code. This workflow relies heavily on interaction with the existing knowledge base (KB) via a dedicated search mechanism.

&emsp; The core workflow, orchestrated by the system's logic, typically proceeds as follows:

1. **Statement Suggestion & Description:** An LLM agent proposes a new mathematical statement (e.g., a theorem or definition) deemed potentially valuable to include, perhaps based on gaps identified in the KB or external mathematical texts. It provides an initial natural language description of this statement.
2. **Natural Language Formulation & Proof:** The LLM elaborates on the proposed statement, writing it out formally in natural language. If it's a theorem, the LLM also attempts to generate a proof in natural language, i.e., an informal proof. Crucially, during this stage, the LLM interacts with a *search engine* component. This engine uses vector embeddings of existing items in the KB (stored in the SQLite database) to find and retrieve relevant definitions, theorems, or lemmas that might be useful for formulating the statement or constructing its proof.
3. **NL Review and Iteration:** The LLM reviews the natural language statement and proof it generated, potentially iterating multiple times to refine the logic, clarity, and correctness based on its internal reasoning and the context provided by retrieved KB items. The goal is to arrive at a natural language version that appears logically sound.
4. **Lean Translation:** Once the natural language version is deemed satisfactory by the LLM agent, it attempts to translate the formal statement (e.g., the theorem statement, definition) into Lean 4 syntax. Again, the search engine may be queried to find existing Lean definitions or notations in the KB that should be reused.
5. **Iterative Lean Proof Attempt & Verification:** For theorems, the LLM attempts to generate a formal proof in Lean 4. This is not typically a single-shot process. Instead, the LLM, guided by the natural language proof and leveraging relevant items retrieved by the search engine from the KB's *persistent shared library*, generates proof steps or tactics. These attempts are incrementally passed to the *formal verification engine* (Lean 4 via Lake). The engine provides immediate feedback: success for that step, failure, or specific error messages. The LLM uses this feedback to adjust its strategy, try alternative tactics, or backtrack, continuing this generate-verify-adjust loop until the entire proof is accepted by Lean or a maximum number of attempts is reached.

&emsp; Only when this iterative process successfully yields a complete Lean proof that is fully accepted by the formal verification engine is the item considered verified. At this point, its status in the KB is updated to PROVEN, and its Lean source code is integrated into the persistent shared library, making it a reliable building block for future work. Failed attempts within the proof loop, or an ultimate failure to find a proof after sufficient effort, result in a different status update (e.g., LEAN_VALIDATION_FAILED), potentially flagging the item for different strategies or manual review. This tight loop between LLM generation and Lean verification is central to ensuring the integrity of the knowledge base while automating the formalization process.

&emsp; Underlying this workflow is a conceptual shift away from viewing mathematics as a collection of independent papers or results. Instead, the Vantage Project treats mathematical knowledge as a highly interconnected *graph*. Each definition, theorem, or lemma is a node, and dependencies form the edges. The KB explicitly stores these dependencies, and the persistent shared library materializes them. This graph perspective is not just organizational; it enables a highly *parallelized workflow*. By understanding the dependency structure, the system can identify numerous "leaf" nodes—statements whose prerequisites are already verified—and assign LLM agents to work on formalizing many of them concurrently. This allows the knowledge base to potentially grow much faster than a purely linear, paper-by-paper approach would permit.


## 5. Relationship with existing Lean libraries

&emsp; It is important to situate the Vantage Project in the context of existing efforts within the Lean ecosystem, most notably the comprehensive Mathlib library. Mathlib represents a monumental, community-driven achievement in formalizing a vast breadth of undergraduate and graduate-level mathematics, primarily optimized for human understanding and contribution.

&emsp; The Vantage Project, while potentially utilizing parts of Mathlib as a foundation, explores a complementary but distinct approach. Its focus on automation necessitates certain differences:
* **Optimization for AI:** A primary goal of Vantage is to build a knowledge base structured for efficient processing and querying by AI agents, including the LLMs involved in the formalization loop itself. This might involve different organizational principles, metadata structures, or levels of granularity compared to a library primarily designed for human navigation. The automated workflow allows fine-grained control over these structural aspects, tailoring the KB for machine consumption.
* **Focus on AI Utility:** Consequently, the design choices within the Vantage KB prioritize utility for AI-driven tasks—such as automated proof search, verification of LLM outputs, and grounding LLM reasoning—over optimizing for human browsing or direct contribution in the style of Mathlib. This represents a shift towards developing knowledge bases *for* AI systems, recognizing their increasing role in mathematical exploration.
* **Rapid Domain Expansion:** The emphasis on LLM-assisted formalization aims to accelerate the process of building verified knowledge bases. This could potentially allow for the rapid bootstrapping of formalized libraries in new domains (e.g., physics, specialized engineering fields) where creating a dedicated, Mathlib-scale community project from scratch might be prohibitive.
* **Accelerated Formalization Potential:** Drawing inspiration from achievements like AlphaZero in chess, where AI systems reached world-class performance through rapid, iterative self-improvement, Vantage embodies an aspiration. By tightly integrating LLM generation with formal verification, the hope is to create a feedback loop that significantly accelerates the pace of formalization, potentially allowing large portions of mathematical knowledge to be rigorously verified and interconnected in a shorter timeframe than traditional methods allow. This iterative, AI-assisted process aims to rapidly expand the "vantage point" from which new mathematics can be explored and proven.

&emsp; Therefore, Vantage is less a replacement for Mathlib and more an exploration of an alternative, automation-centric methodology for building and structuring formalized mathematical knowledge, optimized for interaction with AI systems and potentially enabling faster expansion into new domains.


## 6. Conclusion

&emsp; The journey towards automated mathematical reasoning and formalization is ongoing, but the landscape is shifting rapidly. As demonstrated by experiments and the advancements in LLMs, the power to retrieve and process vast amounts of mathematical information is growing steadily. However, the critical need for rigorous verification remains paramount. The Vantage Project represents a pragmatic approach to this challenge, leveraging state-of-the-art LLMs not as standalone provers, but as powerful assistants in the construction of a formally verified knowledge base using Lean 4. By focusing on building this structured, interconnected, and trustworthy foundation—the "vantage point"—we aim to create a resource that enhances both human and machine mathematical capabilities.

&emsp; Looking forward, the integration of such formalization technologies with LLMs holds immense promise. Systems like Vantage can provide the crucial verification layer needed to ensure the correctness of LLM-generated mathematics and code. This synergy, where LLMs generate hypotheses or proofs and formal methods provide the guarantee of soundness, could pave the way for more reliable AI systems capable of contributing meaningfully to scientific discovery, engineering, and mathematical research itself. The continued development of the Vantage knowledge base is a step towards realizing this future, building a robust foundation for the next generation of automated reasoning.
