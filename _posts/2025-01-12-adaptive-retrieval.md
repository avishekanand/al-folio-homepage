---
layout: post
title: Adaptive Retrieval
date: 2025-01-12 12:00:00
description: A blog post about adaptive retrieval techniques
tags: retrieval machine-learning research
categories: research
related_posts: false
---

# From Graphs to LLMs: Our Journey in Adaptive Retrieval

When Sean MacAvaney introduced the idea of **Adaptive Retrieval** at ECIR 2024’s _ironGraphs_ workshop, it immediately resonated with me. Sean had first formalized adaptive retrieval in 2022 [1], showing how re-rankers could dynamically expand their view of the corpus by exploiting document-to-document relationships. For me, this clicked with an open challenge I’d been discussing with my PhD student, Mandeep, on the intersection of graphs and retrieval. The fit was perfect: graph signals could be a natural substrate for adaptive re-ranking.

From that starting point, we began exploring how to push adaptive retrieval further. Over the last few years, this work has crystallized into a series of papers: **QUAM (WSDM)**[2], **SlideGAR (ECIR)**[3], **ORE (SIGIR)**[4], and most recently, **SUNAR**[5]. Each represents a step in broadening the scope of adaptive retrieval—from graph-based reranking, to LLM-based re-rankers, to online estimation, and finally to incorporating LLM feedback itself.

## QUAM: Query Affinity Modelling for Adaptive Retrieval

Our first step was **QUAM** (_Query Affinity Modelling for Adaptive Retrieval_). While GAR (Graph-based Adaptive Retrieval) showed the potential of corpus graphs, it treated all neighborhoods the same. In QUAM, we introduced a more nuanced view: instead of blindly alternating between initial retrieval results and graph neighbors, we prioritized neighbors based on their _query affinity_.

This led to substantial improvements in recall without excessive overhead, showing that adaptive retrieval could be made both smarter and more efficient.

## SlideGAR: Adaptive Retrieval Meets LLM Re-rankers

As large language models emerged as powerful **listwise re-rankers**, we faced a new challenge. Adaptive retrieval methods like GAR and QUAM assumed pointwise rankers that output independent scores. LLM re-rankers, however, work on batches of documents at once, producing only an ordering.

In **SlideGAR**, we introduced a **sliding window strategy** that fed batches of documents to an LLM ranker, while still pulling in new candidates from the corpus graph. This bridged the gap between adaptive retrieval and listwise LLM ranking.

## ORE: Online Relevance Estimation Beyond Graphs

Our next step was **ORE (Online Relevance Estimation)**, which generalized adaptive retrieval into a broader **bandit-based framework**. Instead of committing to a fixed top-_k_ pool (as in telescoping pipelines), ORE continuously updated relevance estimates for documents during reranking. This allowed us to dynamically reprioritize documents—even those initially overlooked.

ORE achieved remarkable recall gains, outperforming both telescoping pipelines and earlier adaptive retrieval methods. It showed that adaptive retrieval could be reframed as _online estimation_, bridging hybrid, graph-based, and LLM-driven search.

## SUNAR: LLM Feedback for Complex QA

Most recently, we introduced **SUNAR (Semantic Uncertainty-based Neighborhood Aware Retrieval)** for **complex QA**. SUNAR brings a new dimension: it uses **LLM feedback** to guide retrieval. Specifically, it leverages the _uncertainty_ of interim LLM-generated answers to promote or penalize candidate documents in a neighborhood-aware retrieval process.

The insight is simple but powerful: if the LLM shows uncertainty or inconsistency in its answers, retrieval should adapt by exploring alternative evidence. SUNAR achieved up to **31.8% performance improvements** on complex QA datasets like MusiqueQA and 2WikiMultiHopQA, substantially outperforming strong retrieve-and-reason baselines.

## Looking Ahead

What began as a question—_can re-ranker based retrieval be improved by exploiting graph structure?_—has evolved into a much broader research direction. We now see re-rankers not just as the final layer of search, but as **active agents** that integrate signals from graphs, hybrid retrievers, bandit-style estimation, and even **LLM feedback**.
Graph-based signals remain important, but they are just one piece of a larger picture. The future lies in **feedback-driven adaptive retrieval**: building systems where re-rankers and LLMs iteratively inform each other, reducing uncertainty, improving recall, and delivering more trustworthy answers.

With QUAM, SlideGAR, ORE, and SUNAR, we’ve traced a path from graph-enhanced reranking to feedback-driven retrieval. And we believe this is only the beginning.

---

## References

[1] Sean MacAvaney, Nicola Tonellotto, and Craig Macdonald. _Adaptive Re-Ranking with a Corpus Graph_. CIKM 2022. [paper](https://arxiv.org/pdf/2208.08942)

[2] Mandeep Rathee, Sean MacAvaney, and Avishek Anand. _QUAM: Adaptive Retrieval through Query Affinity Modelling_. WSDM 2024. [paper](https://dl.acm.org/doi/pdf/10.1145/3531681.3531706)

[3] Mandeep Rathee, Venktesh V, Sean MacAvaney, and Avishek Anand. _SlideGAR: Adaptive Retrieval for Listwise Re-Rankers_. ECIR 2024. [paper](https://arxiv.org/pdf/2501.09186)

[4] Mandeep Rathee, Venktesh V, Sean MacAvaney, and Avishek Anand. _Breaking the Lens of the Telescope: Online Relevance Estimation over Large Retrieval Sets_. SIGIR 2025. [paper](https://dl.acm.org/doi/pdf/10.1145/3726302.3729910)

[5] Venktesh V, Mandeep Rathee, and Avishek Anand. _SUNAR: Semantic Uncertainty based Neighborhood Aware Retrieval for Complex QA_. NAACL 2025. [paper](https://aclanthology.org/2025.naacl-long.300.pdf)
