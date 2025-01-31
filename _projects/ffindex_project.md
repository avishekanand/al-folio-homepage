---
layout: page
title: Fast Forward Indexes
description: Fast-CPU based re-ranking 
img: assets/img/ffindex-logo.png
importance: 1
category: work
related_publications: false
---

We introduce a simple yet powerful vector forward index designed to enhance document ranking by combining lexical and semantic scores through interpolation called Fast Forward Indexes. Unlike traditional contextual re-rankers and dense indexes that rely on nearest neighbor search, Fast-Forward indexes leverage efficient sparse models for retrieval and pre-computed dense transformer-based vector representations. This approach allows for constant time lookup and fast CPU-based semantic similarity computation during query processing. Additionally, we propose innovative index pruning and early stopping techniques, grounded in theoretical foundations, to boost query processing throughput. 

Based on our work published in [TheWebConf'22](https://dl.acm.org/doi/abs/10.1145/3485447.3511955) and its extension in [TOIS 2024](https://dl.acm.org/doi/pdf/10.1145/3631939) we have demonstrated that Fast-Forward indexes outperform hybrid indexes in both performance and query processing efficiency using only CPUs. 

Following is the implementation of [Fast-Forward indexes](https://dl.acm.org/doi/abs/10.1145/3485447.3511955).

**Important**: As this library is still in its early stages, the API is subject to change!

## Installation

Install the package via `pip`:

```bash
pip install fast-forward-indexes
```

## Getting Started

Using a Fast-Forward index is as simple as providing a TREC run with retrieval scores:

```python
from pathlib import Path
from fast_forward import OnDiskIndex, Mode, Ranking
from fast_forward.encoder import TCTColBERTQueryEncoder

# choose a pre-trained query encoder
encoder = TCTColBERTQueryEncoder("castorini/tct_colbert-msmarco")

# load an index on disk
ff_index = OnDiskIndex.load(Path("/path/to/index.h5"), encoder, Mode.MAXP)

# load a run (TREC format) and attach all required queries
first_stage_ranking = (
    Ranking.from_file(Path("/path/to/input/run.tsv"))
    .attach_queries(
        {
            "q1": "query 1",
            "q2": "query 2",
            # ...
            "qn": "query n",
        }
    )
    .cut(5000)
)

# compute the corresponding semantic scores
out = ff_index(first_stage_ranking)

# interpolate scores and create a new TREC runfile
first_stage_ranking.interpolate(out, 0.1).save(Path("/path/to/output/run.tsv"))
```

## Documentation

A more detailed documentation is available [here](https://mrjleo.github.io/fast-forward-indexes/docs).

### Citing & Authors

This work is done with [Jurek Leonhardt](https://mrjleo.github.io).

For citing please use the following bibtex

```bibtex
@article{LeonhardtMRKAA:tois:24,
  author       = {Jurek Leonhardt and
                  Henrik M{\"{u}}ller and
                  Koustav Rudra and
                  Megha Khosla and
                  Abhijit Anand and
                  Avishek Anand},
  title        = {Efficient Neural Ranking Using Forward Indexes and Lightweight Encoders},
  journal      = {Transactions of Information Systems (TOIS)},
  volume       = {42},
  number       = {5},
  pages        = {117:1--117:34},
  year         = {2024},
  url          = {https://doi.org/10.1145/3631939},
  arxiv          = {2311.01263},
  pdf    = {https://arxiv.org/pdf/2311.01263},
  doi          = {10.1145/3631939},
}
``` 

```bibtex
@inproceedings{LeonhardtRKAA22:www:22,
  author       = {Jurek Leonhardt and
                  Koustav Rudra and
                  Megha Khosla and
                  Abhijit Anand and
                  Avishek Anand},
  title        = {Efficient Neural Ranking using Forward Indexes},
  journal    = {TheWebConference '22: The {ACM} Web Conference 2022, Virtual Event, Lyon, France,
                  April 25 - 29, 2022},
  pages        = {266--276},
  publisher    = {ACM},
  year         = {2022},
  arxiv       = {2311.01263},
  url          = {https://doi.org/10.1145/3485447.3511955},
  doi          = {10.1145/3485447.3511955}
}
```  
