---
layout: page
permalink: /teaching/
title: teaching
description: Materials for courses in the bachelors, and the masters level at TU Delft.
nav: true
nav_order: 6
---

<style>
  .course-grid{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
    gap:18px;
    margin:10px 0 8px;
  }
  .tcard{
    position:relative;
    display:flex;
    flex-direction:column;
    gap:9px;
    padding:20px 20px 18px;
    border:1px solid var(--global-divider-color);
    border-radius:14px;
    background:var(--global-card-bg-color);
    box-shadow:0 1px 2px rgba(20,30,50,.05),0 4px 14px rgba(20,30,50,.05);
    transition:transform .14s ease, box-shadow .14s ease, border-color .14s ease;
  }
  .tcard:hover{
    transform:translateY(-3px);
    border-color:var(--global-theme-color);
    box-shadow:0 2px 6px rgba(20,30,50,.08),0 12px 28px rgba(20,30,50,.10);
  }
  .tcard .level{
    display:inline-block;
    align-self:flex-start;
    font-size:11px;
    font-weight:600;
    letter-spacing:.04em;
    text-transform:uppercase;
    color:var(--global-theme-color);
    background:color-mix(in srgb, var(--global-theme-color) 12%, transparent);
    padding:3px 9px;
    border-radius:999px;
  }
  .tcard h3{
    margin:0;
    font-size:19px;
    line-height:1.25;
    color:var(--global-text-color);
  }
  .tcard .co{
    margin:0;
    font-size:13px;
    color:var(--global-text-color-light);
  }
  .tcard .desc{
    margin:0;
    font-size:13.5px;
    line-height:1.5;
    color:var(--global-text-color-light);
  }
  .tcard .foot{
    margin-top:auto;
    padding-top:6px;
    display:flex;
    align-items:center;
    flex-wrap:wrap;
    gap:8px 14px;
  }
  /* stretched link: the whole card is clickable to the dedicated page */
  .tcard .go{
    font-size:13.5px;
    font-weight:700;
    color:var(--global-theme-color);
  }
  .tcard .go::after{
    content:"";
    position:absolute;
    inset:0;
    border-radius:14px;
  }
  /* secondary links sit above the stretched overlay and stay clickable */
  .tcard .chip{
    position:relative;
    z-index:1;
    font-size:12px;
    font-weight:600;
    color:var(--global-text-color-light);
    border:1px solid var(--global-divider-color);
    padding:3px 9px;
    border-radius:999px;
    text-decoration:none;
  }
  .tcard .chip:hover{
    color:var(--global-theme-color);
    border-color:var(--global-theme-color);
  }
  .tcard a{text-decoration:none;}
</style>

<div class="course-grid">

  <div class="tcard">
    <span class="level">Bachelor's</span>
    <h3>Data Mining</h3>
    <p class="co">with Julian Urbano, Nergis Tömen</p>
    <p class="desc">Fundamental concepts and techniques of data mining — preprocessing, probabilistic counting, dimensionality reduction, clustering, anomaly detection, and mining text and graph data, with hands-on sessions.</p>
    <div class="foot">
      <a class="go" href="{{ '/assets/html/dm26-27/' | relative_url }}">Course page &rarr;</a>
      <a class="chip" href="https://studiegids.tudelft.nl/opleidingen/study-guide/educations/13603#/details/14273" target="_blank" rel="noopener">Study guide</a>
      <a class="chip" href="https://brightspace.tudelft.nl/d2l/home/774633" target="_blank" rel="noopener">Brightspace</a>
    </div>
  </div>

  <div class="tcard">
    <span class="level">Master's</span>
    <h3>Natural Language Processing</h3>
    <p class="co">with Jie Yang</p>
    <p class="desc">Theory and practice of NLP — text processing, language modeling, syntactic and semantic analysis, and large language models — with an emphasis on hands-on projects and real-world applications.</p>
    <div class="foot">
      <a class="go" href="{{ '/assets/teaching/nlp/' | relative_url }}">Course page &rarr;</a>
      <a class="chip" href="https://studiegids.tudelft.nl/courses/study-guide/educations/14803" target="_blank" rel="noopener">Study guide</a>
      <a class="chip" href="https://brightspace.tudelft.nl/d2l/home/864611" target="_blank" rel="noopener">Brightspace</a>
    </div>
  </div>

  <div class="tcard">
    <span class="level">Master's</span>
    <h3>Information Retrieval</h3>
    <p class="co">with Sole Pera, Jie Yang</p>
    <p class="desc">Principles and practice of information retrieval — search engine design, text indexing, query processing, and evaluation — with special topics in learning-to-rank, neural ranking models, and recommender systems.</p>
    <div class="foot">
      <a class="go" href="https://studiegids.tudelft.nl/courses/study-guide/educations/14768" target="_blank" rel="noopener">Study guide &rarr;</a>
      <a class="chip" href="https://brightspace.tudelft.nl/d2l/home/774748" target="_blank" rel="noopener">Brightspace</a>
    </div>
  </div>

</div>

---

### Past Courses (@Leibniz University Hannover)

---

### SS 2019 - 2021: Deep Learning

**Level**: Masters

**Course Description**: Foundations of Deep Learning with applications. The aim of this lecture is to provide a solid foundation about deep learning and its applications. We will first study regular machine learning and basic, simple deep learning architectures. Afterwards we will focus on the applications of deep learning/neural networks, including current cutting-edge research. The lecture has both theoretical and programmatic aspects. Students will be exposed to popular machine learning problems and datasets while being able to work hands on with frameworks such as TensorFlow and scikit-learn.

---

### SS 2016 - 2018: Algorithms for Big Data

**Level**: Masters

**Course Description**: Concepts and foundations of modern algorithms for Processing, Mining, and Learning for Big Datasets. The aim of this lecture is to learn efficient algorithms that are used for processing large datasets. The course involves learning scalable approaches to some of the fundamental problems involving finding similar items, clustering, recmmender systems and graph mining. The lecture has both theoretical and programmatic aspects. Students will be exposed to large distributed data processing frameworks like Hadoop and Spark.

---

### WS 2017 - 19: Foundations of Probabilistic Information Retrieval

**Level**: Masters

**Course Description**: The aim of this lecture is to learn the probabilistic underpinings of modern information retrieval techniques. We will study probabilistic modeling, machine learning, deep learning and how to apply concepts from these areas to improve search engines. The lecture has both theoretical and programmatic aspects. Students will be exposed to popular machine learning problems and datasets while being able to work hands on with frameworks such as tensorflow and scipy.

---

### WS 2014 - 2016: Temporal Information Retrieval

**Level**: Masters

**Course Description**: Masters level course on understanding temporal aspects and issues in Information Retrieval.

---

### Puzzling Problems in Computer Science

**Level**: Bachelors

**Course Description**: Bachelor course which presents computer science problems in the form of puzzles.

---
