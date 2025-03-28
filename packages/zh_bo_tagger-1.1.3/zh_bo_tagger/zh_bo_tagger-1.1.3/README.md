| Feature | Description |
| --- | --- |
| **Name** | `zh_bo_tagger` |
| **Version** | `1.1.3` |
| **spaCy** | `>=3.8.4,<3.9.0` |
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
| **`morphologizer`** | `POS=PUNCT`, `POS=NOUN`, `POS=ADV`, `POS=ADP`, `POS=CCONJ`, `POS=PRON`, `POS=VERB`, `POS=DET`, `POS=AUX`, `POS=SCONJ`, `POS=PART`, `POS=ADJ`, `POS=PROPN`, `POS=NUM`, `POS=INTJ`, `POS=SYM`, `POS=X` |
| **`parser`** | `ROOT`, `dep` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `POS_ACC` | 85.31 |
| `MORPH_ACC` | 93.40 |
| `MORPH_PER_FEAT` | 0.00 |
| `DEP_UAS` | 90.17 |
| `DEP_LAS` | 90.17 |
| `SENTS_P` | 94.12 |
| `SENTS_R` | 86.25 |
| `SENTS_F` | 90.02 |
| `TOK2VEC_LOSS` | 264178.33 |
| `MORPHOLOGIZER_LOSS` | 1154474.86 |
| `PARSER_LOSS` | 1081734.96 |