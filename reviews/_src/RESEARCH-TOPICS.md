# Research topics — the taxonomy I sort conferences into

> **Generated from `topics.json` by `build_topics.py` — do not edit by hand.** Edit `topics.json`, then run the build.

A single, reusable list of the research directions I track, each with a one- or two-line note on *why I care*. The conference reports name their appendix themes from this list (or an alias below), and the cross-conference [`by-topic view`](/reviews/by-topic.html) is aggregated from it.

Tags: **[IR]** retrieval venues · **[ML]** ICML/NeurIPS-style · **[NLP]** ACL/EMNLP-style. **○ peripheral** = tracked but weighted down (kept, not dropped). Override: methods that transfer to ranking — distillation, learnt/dense representations — stay core.

---

## A. Retrieval & ranking (the core interest)

1. **Reasoning-first ranking & LLM rerankers** — [IR][ML][NLP]
   When the ranker reasons before it orders — listwise LLM rerankers, cross-encoders trained to think, reasoning-intensive retrieval. My interest: when a reasoning reranker actually beats a cheap cross-encoder, and what it costs per query.

2. **Dense / sparse / multi-vector retrieval & learnt representations** — [IR][ML]
   Learned representations for first-stage retrieval — dense bi-encoders, learned sparse, ColBERT-style late interaction, embedding models, ANN. My interest: representation quality vs. index/latency budget, and how small an encoder can get before recall breaks. (Learnt representations stay core even in otherwise-peripheral areas.)
   <br><sub>report aliases: “Dense / sparse / multi-vector retrieval & efficiency”; “Dense / sparse / multi-vector retrieval”</sub>

3. **Agentic retrieval, deep research & RAG** — [IR][ML][NLP]
   Retrieval as a multi-turn loop an agent drives — deep-research agents, iterative/agentic search, RAG training and robustness. My interest: closing the loop between retrieval and reasoning, and the cost/faithfulness trade-off of doing it agentically.
   <br><sub>report aliases: “Retrieval for agents, deep research, RAG & QA”; “Agents, tools & retrieval-augmented generation”</sub>

4. **Learning-to-rank theory, bias, click models & fairness** — [IR][ML] · **○ peripheral**
   The statistics of ranking from implicit feedback — unbiased LTR, position/selection bias, click models, exposure fairness.

5. **Query & intent understanding, search behavior** — [IR][NLP]
   What the user actually wants — query rewriting/expansion, intent, session/conversational search, and how generative answers change search behavior. My interest: where a generated answer should replace a ranked list, and where it shouldn't.
   <br><sub>report aliases: “Search behavior, query & intent understanding, GenAI-vs-search”</sub>

6. **Multimodal, cross-modal & structured retrieval** — [IR][ML] · **○ peripheral**
   Retrieval beyond plain text — visual-document retrieval, cross-modal embeddings, retrieval over tables/graphs/code.

7. **Evaluation, relevance judgments & LLM-as-judge** — [IR][ML][NLP]
   How we know a system is better — test-collection design, LLM-generated relevance judgments, judge reliability and bias. My interest: trusting an LLM to grade another LLM, and when that quietly breaks.
   <br><sub>report aliases: “Evaluation & LLM-as-judge”</sub>

8. **Fact-checking, verification & factuality** — [IR][NLP]
   Retrieval in service of truth — claim verification, evidence retrieval, hallucination/factuality, and detecting model-generated or harmful content in the corpus. My interest: retrieval that defends the pipeline rather than just feeds it.
   <br><sub>report aliases: “Fact-checking, verification & harmful-content detection”; “Safety, hallucination & factuality”</sub>

9. **Domain & specialized retrieval, resources** — [IR][NLP] · **○ peripheral**
   Retrieval in the hard verticals — legal, medical, scientific, code — plus the benchmarks and datasets that make progress measurable.
   <br><sub>report aliases: “Domain, specialized retrieval & resources”</sub>


## B. Recommendation

10. **Generative recommendation, semantic IDs & LLM recommenders** — [IR][ML] · **○ peripheral**
   Recommenders that generate item identifiers instead of scoring a fixed catalogue — semantic IDs, generative retrieval for recsys, LLM-as-recommender.

11. **Recommendation: sequential, multimodal, graph, CF, CTR & ads** — [IR][ML] · **○ peripheral**
   The rest of the recsys stack — sequential/session models, graph and collaborative filtering, CTR prediction and ads.


## C. Self-improvement (the throughline I track)

12. **Self-improving & self-evolving systems** — [ML][NLP]
   Agents that get better from their own experience — self-evolving memory, experience distillation, on-policy self-adaptation. My interest: whether "it improved on the benchmark" is really improvement, and how to check faithfulness.
   <br><sub>report aliases: “Self-improving & self-evolving agents”; “Self-improving & self-evolving LLM agents”</sub>

13. **Recursive self-improvement & self-play** — [ML][NLP]
   One level up: systems that evolve the machinery of improvement — memory architecture, reward, verifier — plus self-play, a model proposing and solving its own challenges. My interest: where the recursion compounds vs. plateaus, and keeping generator and solver honest.
   <br><sub>report aliases: “Self-play & self-reward”; “Recursive self-improvement & meta-evolution”; “Self-play”</sub>

15. **Self-reward, self-verification & self-consistency** — [ML][NLP]
   Where the reward comes from when nobody labels anything — self-rewarding models, intrinsic/verifiable rewards, self-consistency, weak-vs-strong verification.

16. **Self-correction, self-reflection & test-time RL** — [ML][NLP]
   Correction as an objective, not a decoding trick — test-time RL from self-generated labels, multi-attempt reasoning, self-refinement grounded in solvers/verifiers.
   <br><sub>report aliases: “Self-refinement, self-correction & self-critique”</sub>

17. **Self-training & self-distillation** — [ML][NLP]
   Bootstrapping supervision from the model itself — self-taught reasoners (STaR-style), on-policy self-distillation, error-aware self-reflection for distillation.


## D. General LLM / ML methods

18. **Reasoning & test-time compute** — [ML][NLP]
   Chain-of-thought, inference-time scaling, adaptive/efficient reasoning. My interest: buying accuracy with compute without paying for it on easy inputs.
   <br><sub>report aliases: “Reasoning & chain-of-thought”</sub>

19. **Agents, tool use & multi-agent systems** — [ML][NLP]
   LLMs that act — tool use, multi-agent coordination, agent benchmarks and robustness under noise.

20. **RL, RLHF & preference optimization** — [ML][NLP]
   Aligning and sharpening models with feedback — RLHF, DPO and variants, GRPO, robust preference learning, reward modeling.
   <br><sub>report aliases: “Alignment, RLHF & reward modeling”</sub>

21. **Alignment, safety & interpretability** — [ML][NLP]
   Making models safe and legible — jailbreak/defense, safety benchmarks, steering, interpretability.

22. **Efficiency: distillation, MoE, long-context & decoding** — [ML]
   Doing more with less — mixture-of-experts, KV-cache compression, speculative/sparse decoding, long-context. Distillation is core because it transfers to ranking.
   <br><sub>report aliases: “Efficiency: MoE, decoding & distillation”; “Efficiency & long-context”</sub>

23. **Diffusion & flow-based generation** — [ML] · **○ peripheral**
   The generative-modelling core — diffusion, flow matching, sampling theory and distillation.
   <br><sub>report aliases: “Generative modeling: diffusion & flow matching”</sub>

24. **Multilinguality & low-resource** — [NLP]
   Reasoning and retrieval across languages — cross-lingual transfer, low-resource languages, translation.
   <br><sub>report aliases: “Multilinguality”</sub>

25. **Multimodal & speech** — [ML][NLP] · **○ peripheral**
   Vision-language and speech models, multimodal reasoning and grounding.
   <br><sub>report aliases: “Multimodal & vision-language”</sub>

26. **Theory: optimization & generalization** — [ML]
   The why-it-works layer — scaling laws, generalization bounds, optimization dynamics.


## E. Meta

27. **Perspectives & position papers** — [IR][ML][NLP]
   Field-shaping arguments — where a subfield should go, what it's getting wrong. Usually one or two per report, flagged as opinion.

---

### Adding a conference
1. Write `<venue>_<year>_data.json` next to `build_topics.py`, naming each appendix theme from the list above (or add an alias to `topics.json`).
2. Run `python3 build_topics.py` — it regenerates the report, the by-topic view and this file, and **fails** if any theme isn't a known topic.
3. Commit. CI rebuilds and redeploys.
