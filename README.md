## Train a model from scratch
- https://course.spacy.io/en/chapter4
- https://github.com/explosion/spaCy/discussions/12772
- https://spacy.io/usage/linguistic-features (Example 1: Basci whitespace tokenizer)

1. python3 -m spacy init fill-config config/base_config.cfg config/tibetan.cfg --code src/functions.py
2. python3 -m spacy convert your/path/corpus/conllu/train.conllu corpus/train -n 10
3. python3 -m spacy convert your/path/corpus/conllu/dev.conllu corpus/dev -n 10
4. python3 -m spacy train config/tibetan.cfg --output ./models --code src/functions.py --gpu-id 0
  - optional without gpu: python3 -m spacy train config/tibetan.cfg --output ./models --code src/functions.py

## Generate an installable Python package from an existing pipeline data
- https://spacy.io/api/cli#package
- python3 -m spacy package ./models/model-best ./packages --code src/functions.py --name bo_tagger --version 0.0.1 
