import spacy
from spacy.tokens import Doc
from botok import WordTokenizer
from botok.config import Config
from pathlib import Path

class BoTokTokenizer:
    def __init__(self, nlp):
        # config = Config(dialect_name="general", base_path=Path.home())
        config = Config(dialect_name="custom")
        self.wt = WordTokenizer(config=config)
        self.vocab = nlp.vocab

    def __call__(self, text):
        tokens = self.wt.tokenize(text, split_affixes=False)
        words = [token.text for token in tokens]
        spaces = [True] * len(words)
        return Doc(self.vocab, words=words, spaces=spaces)

nlp = spacy.blank("xx")  
nlp.tokenizer = BoTokTokenizer(nlp)

text = "འདྲི་ཞིབ་བྱས་པ་བརྒྱུད་ཤེས་རྟོགས་བྱུང་བར། 2014ལོ་ནས་2018ལོ་བར། ཞུ་སྦྱོར་ཕྱི་མ་པེ་ཐེན་ཧུའེ་ཡིས་ཧྭ་རུང(ཤང་ཀང)རྒྱལ་སྤྱིའི་མ་རྐང་ཚོད་འཛིན་ཚད་ཡོད་ཀུང་སིའི་ལས་སྒོ་རྒྱ་སྐྱེད་པུའུ་གསུམ་པའི་འགན་འཁུར་བ་དང་། སྤྱི་ཁྱབ་སྤྱི་གཉེར། མ་འཇོག་དངུལ་ཁང་པུའུ་ཡི་ལས་འཛིན་སྤྱི་ཁྱབ་སྤྱི་གཉེར། ཀྲུང་གོ་ཧྭ་རུང་རྒྱལ་སྤྱིའི་མ་རྐང་ཚོད་འཛིན་ཚད་ཡོད་ཀུང་སིའི་མ་རྩ་གཉེར་སྐྱོང་གི་སྤྱི་ཁྱབ་ལྟ་ཞིབ་པ། སྤྱི་ཁྱབ་སྤྱི་གཉེར་གྱི་ལས་རོགས། ལས་འཛིན། སྤྱི་ཁྱབ་སྤྱི་གཉེར་གཞོན་པ། སྤྱི་ཁྱབ་སྤྱི་གཉེར་སོགས་ཀྱི་འགན་འཁུར་རིང་། འགན་གནས་ཀྱི་སྟབས་བདེ་སྤྱད་དེ་འབྲེལ་ཡོད་ཚན་པར་རྣམ་གྲངས་ཉོ་སྒྲུབ་དང་ཁེ་ལས་ཀྱི་མ་དངུལ་བསྡུ་སྒྲིལ་སོགས་ཀྱི་ཐད་རོགས་རམ་བྱས་པ་དང་། ཁྲིམས་འགལ་ངང་རྒྱུ་དངོས་བླངས་པ་མི་དམངས་ཤོག་སྒོར་ལ་ཕབ་ན་ཁྱོན་སྒོར་དུང་ཕྱུར་11དང་ས་ཡ་8ལྷག་ཙམ་ཟིན་ཡོད།"
doc = nlp(text)

for token in doc:
    print(token.text)