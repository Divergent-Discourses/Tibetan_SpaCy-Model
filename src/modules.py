import math
import os

def load_conllu(conllu_dir):
    conllu_str = ''
    for filename in os.listdir(conllu_dir):
        if filename.endswith(".conllu"):
            file_path = os.path.join(conllu_dir, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                conllu = file.read()
                conllu_str = conllu_str + conllu
    return conllu_str

def split_dataset(sentences, proportion):
    # Calculate the index for 80% of the list length
    split_index = math.ceil(len(sentences) * proportion)

    # Split the list into two parts
    train = sentences[:split_index]
    dev = sentences[split_index:]

    return train, dev

def make_space(sentences):
    for sentence in sentences:
        sent = ''
        for token in sentence:
            sent = sent + token['form'] + ' '
        sentence.metadata['text'] = sent
    return sentences

def None_replacement(token):
    for key, value in token.items():
        if value is None:
            token[key] = '_'
    return token

def generate_conllu(sentences):
    conllu_str = ''
    cnt = 1
    total = len(sentences)
    for sentence in sentences:
        sent_id = sentence.metadata['sent_id']
        text = sentence.metadata['text']
        content = ''
        print(cnt/total)
        for token in sentence:
            token = None_replacement(token)
            content = content + '\t'.join([str(token[key]) for key in token.keys()]) + '\n'
        conllu_str = conllu_str + '# sent_id = ' + sent_id + '\n' + '# text = ' + text + '\n' + content + '\n'
        cnt = cnt + 1
    return conllu_str

def export_conllu(conllu, conllu_name):
    with open(conllu_name, 'w', encoding="utf-8") as file:
        file.write(conllu)