| Feature | Description |
| --- | --- |
| **Name** | `xx_bo_tagger` |
| **Version** | `0.1.2` |
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
| **`morphologizer`** | `POS=PUNCT`, `POS=NOUN`, `POS=ADV`, `POS=ADP`, `POS=CCONJ`, `POS=PRON`, `POS=VERB`, `POS=DET`, `POS=AUX`, `POS=SCONJ`, `POS=PART`, `POS=ADJ`, `POS=PROPN`, `POS=NUM`, `POS=INTJ`, `POS=SYM`, `POS=X` |
| **`parser`** | `ROOT`, `dep` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `POS_ACC` | 85.10 |
| `MORPH_ACC` | 93.40 |
| `MORPH_PER_FEAT` | 0.00 |
| `DEP_UAS` | 90.22 |
| `DEP_LAS` | 90.22 |
| `SENTS_P` | 94.15 |
| `SENTS_R` | 86.34 |
| `SENTS_F` | 90.08 |
| `TOK2VEC_LOSS` | 358747.53 |
| `MORPHOLOGIZER_LOSS` | 1843383.03 |
| `PARSER_LOSS` | 1252759.15 |