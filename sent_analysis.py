import nltk
import numpy
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize


def analysis(sent):
    tokens = nltk.word_tokenize(sent)
    tagged = nltk.pos_tag(tokens)
    entities =  nltk.chunk.ne_chunk(tagged)
    sent = entities
    return sent

def wsd(): 
    c = lesk(word_tokenize('That was really cool!'), 'cool')
    print(c, c.definition())
