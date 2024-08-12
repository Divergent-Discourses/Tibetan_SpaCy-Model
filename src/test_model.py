import spacy
import src.functions
# import src.MicroTokenizer_spacy

# tokenizer and pos-tagger
nlp = spacy.load("/home/yuki/Dropbox/Arbeit/20240112_Divergierende_Diskurse/20240216_POS-Tagger/urz/models/archive/tibetan/20240806/model-best")
# nlp = spacy.load("./models/model-best", enable=['tok2vec', 'tagger'])
text = "བོད་སྐད་ནི་བོད་ཡུལ་དུ་བེད་སྤྱོད་བྱེད་པའི་སྐད་དེ། སྤྱིར་རོང་འབྲོག་གཉིས་ལས་འབྲོག་པའི་སྐད་ནི་འབྲོག་སྡེ་སྟོད་སྨད་བར་གསུམ་ཀུན་ཏུ་ཁྱད་པར་མེད་ཅིང་། སྒྲ་གདངས་དྲག་ཅིང་གྱོང་ཉམས་ཆེ་ལ་སྔོན་གྱི་སྒྲ་སྦྱོར་གྱི་ཟུར་མ་ཉམས་པར་ཐོན་པ་དང་། ཞིང་སྡེའི་ཡུལ་ལུང་རྣམས་སུ་སྐད་ཀྱི་ཁྱད་པར་སྣ་ཚོགས་ཡོད་པས་གདངས་འདོན་ཚུལ་སོགས་གཅིག་ཏུ་མ་ངེས། ད་ཆར་ཡོངས་གྲགས་སུ་བོད་ཀྱི་ཡུལ་གྲུ་སྟོད་སྨད་བར་གསུམ་ལ་ལྟོས་ཏེ་ནང་གསེས་རིགས་གསུམ་དུ་ཕྱེ་བ་སྟེ། སྟོད་དབུས་གཙང་གི་སྐད་དང་། བར་ཁམས་པའི་སྐད་དང་། སྨད་ཨ་མདོའི་སྐད་རྣམས་སོ། བོད་སྐད་ནི་ཧོར་སོག་ལ་སོགས་པ་གྲངས་ཉུང་མི་རིགས་གཞན་པ་ཁག་ཅིག་གིས་བེད་སྤྱོད་གཏོང་བཞིན་ཡོད་པར་མ་ཟད། བལ་པོ་དང་། འབྲས་ལྗོངས། འབྲུག་ཡུལ་བཅས་ཀྱི་རྒྱལ་ཁབ་རྣམས་སུའང་བེད་སྤྱོད་གཏོང་བཞིན་ཡོད།"
# text = "汉语又称华语，是汉族的语言，是由先秦雅言发展而来、书写使用表意文字（汉字）的东亚分析语，为汉藏语系最大的一支语族。如把整个汉语族视为单一语言，则汉语为世界上母语使用者人数最多的语言，目前全世界有五分之一人口将其作为母语或第二语言。"
# text = "Das Wort deutsch leitet sich vom althochdeutschen thiutisk ab, was ursprünglich „zum Volk gehörig“ bedeutete (germanisch *þeuðō, althochdeutsch thiot[a] „Volk“).[1] Mit diesem Wort wurde vor allem die Volkssprache aller Sprecher eines germanischen Idioms in Abgrenzung zum Welschen der romanischen Nachbarvölker, dem Französischen oder Italienischen und auch im Gegensatz zum Latein der christlichen Priester im eigenen Gebiet der germanischen Völker bezeichnet."
doc = nlp(text)
for token in doc:
    print('token:', token.text)
    print('pos-tag:', token.pos_)