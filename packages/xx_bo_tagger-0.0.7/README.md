| Feature | Description |
| --- | --- |
| **Name** | `xx_bo_tagger` |
| **Version** | `0.0.7` |
| **spaCy** | `>=3.2.1,<3.3.0` |
| **Default Pipeline** | `tok2vec`, `morphologizer`, `parser` |
| **Components** | `tok2vec`, `morphologizer`, `parser` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [n/a]() |

### Label Scheme

<details>

<summary>View label scheme (19 labels for 2 components)</summary>

| Component | Labels |
| --- | --- |
| **`morphologizer`** | `POS=PRON`, `POS=PROPN`, `POS=NOUN`, `POS=ADP`, `POS=PUNCT`, `POS=VERB`, `POS=ADV`, `POS=NUM`, `POS=PART`, `POS=AUX`, `POS=CCONJ`, `POS=DET`, `POS=ADJ`, `POS=SCONJ`, `POS=INTJ`, `POS=X`, `POS=SYM` |
| **`parser`** | `ROOT`, `dep` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `POS_ACC` | 91.56 |
| `MORPH_ACC` | 99.64 |
| `MORPH_PER_FEAT` | 0.00 |
| `DEP_UAS` | 99.32 |
| `DEP_LAS` | 99.32 |
| `SENTS_P` | 99.86 |
| `SENTS_R` | 98.74 |
| `SENTS_F` | 99.30 |
| `TOK2VEC_LOSS` | 1026927.57 |
| `MORPHOLOGIZER_LOSS` | 1567145.12 |
| `PARSER_LOSS` | 8128438.31 |