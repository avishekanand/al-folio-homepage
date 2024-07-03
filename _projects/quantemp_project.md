---
layout: page
title: QuanTemp
description: An open-domain benchmark to verify claims with quantities and temporal expressions
img: assets/img/quantemp-logo.png
importance: 3
category: work
---
  Automated fact checking has gained immense interest to tackle the growing
misinformation in the digital era. Existing systems primarily focus on
synthetic claims on Wikipedia, and noteworthy progress has also been made on
real-world claims. In this work, we release Numtemp, a diverse, multi-domain
dataset focused exclusively on numerical claims, encompassing temporal,
statistical and diverse aspects with fine-grained metadata and an evidence
collection without leakage. This addresses the challenge of verifying
real-world numerical claims, which are complex and often lack precise
information, not addressed by existing works that mainly focus on synthetic
claims. We evaluate and quantify the limitations of existing solutions for the
task of verifying numerical claims. We also evaluate claim decomposition based
methods, numerical understanding based models and our best baselines achieves a
macro-F1 of 58.32. This demonstrates that Numtemp serves as a challenging
evaluation set for numerical claim verification.


[Paper](https://arxiv.org/abs/2403.17169)


# QuanTemp

A benchmark of Quantitative and Temporal Claims. This repository contains data and code for Numerical Claims. It includes the first set of real-world numerical claims, a fine-grained taxonomy for numerical claims (statistical, temporal, comparison, and interval), and inference code for reproducing the best results in the paper. The repository also includes trained models and collected evidence snippets.


## Example Dataset

```json
{
        "country_of_origin": "usa",
        "label": "Conflicting",
        "url": "https://www.politifact.com/factchecks/2010/aug/08/donald-carcieri/carcieri-says-tax-repeal-spawned-new-business/",
        "lang": "en",
        "claim": "Repealing the sales tax on boats in Rhode Island has spawned 2,000 companies, 7,000 jobs and close to $2 billion a year in sales activity.",
        "doc": "The furor over U.S. Sen. John Kerry\u2019s yacht being docked on the tax-free shores of Rhode Island -- not in Massachusetts where he lives -- has subsided now that the senator\u2019s team has promised he will pay the $500,000 in owed taxes.But Rhode Island Governor Donald Carcieri did his part to make sure the underlying issue of Rhode Island\u2019s tax exemption for boats is not forgotten.",
        "taxonomy_label": "statistical",
        "label_original": "half-true"
    }
```

The pipeline consists of claim decomposition, evidence retrieval and stance detection steps.

##Setup

You can simply do a pip install to setup. 

```bash
pip install -r requirements.txt
```

Download the models from [here](https://drive.google.com/drive/folders/1FmaelDhJ7QwsRTs8H0B4vYliw_qjL7P-?usp=sharing) and dump it into models folder


The following is the project structure We release the BM25 results in this repo. However, for those interested the corpus is at the link below to encourage reporducability and need not be downloaded from search engines again. We release this as search results may drift over time.

[Link to Corpus](https://drive.google.com/drive/folders/1GYzSK0oU2MiaKbyBO3hE8kO4gdmxDjCv?usp=drive_link)


#File Structure

The file structure for the resources are in the following structure

```
├── data
│   ├── decomposed_questions
│   │   ├── test_claimdecomp.csv
│   │   └── test_programfc.json
│   ├── raw_data
│   │   ├── test_claims_quantemp.json
│   │   ├── train_claims_quantemp.json
│   │   └── val_claims_quantemp.json
│   └── bm25_scored_evidence
│       ├── bm25_top_100_claimdecomp.json
│       
├── code
│    ├── data_processing
│        ├──
│    │   ├── test_claimdecomp.csv
│    │   └── test_programfc.json
│    ├── utils
│    │   ├── load_veracity_predictor.py
│    ├── nli_inference
│    │   ├── veracity_prediction.py
├── requirements.txt
└── README.md
```

To reproduce results on paper for finqa-roberta-large (ELASTIC) run

```bash
python3 code/nli_inference/veracity_prediction.py --test_path data/raw_data/test_claims_quantemp.json --bm25_evidence_path data/bm25_scored_evidence/bm25_top_100_claimdecomp.json --base_model roberta-large-mnli --model_path models/finqa_roberta_claimdecomp_early_stop_2/model_weights.zip --questions_path data/decomposed_questions/test/test_claimdecomp.csv --output_path finqa_roberta_claimdecomp
```

followed by

```bash
python3 code/evaluation/eval_veracity_prediction.py --output_path output/finqa_roberta_claimdecomp.csv
```

### Citing & Authors

This work is done with [Venktesh Vishwanath](https://venkteshv.github.io/#home), [Abhijit Anand](https://abhijitanand.github.io) and [Vinay Setty](https://www.ux.uis.no/~vsetty/).

For citing please use the following bibtex  

```bibtex
@article{venky:sigir:24,
  author       = {Venktesh V and
                  Abhijit Anand and
                  Avishek Anand and
                  Vinay Setty},
  title        = {QuanTemp: A real-world open-domain benchmark for fact-checking numerical claims},
  journal    = {Proceedings of SIGIR Conference on
                  Research and Development in Information Retrieval},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2403.17169},
  doi          = {10.48550/ARXIV.2403.17169},
  arxiv    = {2403.17169},
}
```
