#!/usr/bin/env python3
'''
NAME
   jjconll

SYNOPSIS
   jjconll [options] files
   
DESCRIPTION
    Given an input text, shows the pos (part of speech), 
    entity type/lemma and syntactic dependency of each token. 

    Displays, optionally, the syntactic dependency tree of the input. 
    It uses a pre-trained model for text processing in Portuguese.

    options:
        -d     : enables the use of displacy to display the syntactic 
                    dependency tree of the input
        files  : uses the given file as its input (with no file provides, 
                    it reads the input from the stdin)
'''

import spacy
from jjcli import *

def retoken(doc):
    with doc.retokenize() as retokenizer:
        for entity in doc.ents:
            retokenizer.merge(entity)
    
def printconl(doc,voc):
    for sentence in doc.sents:
        for t in sentence:
            if t.is_space:
                continue
            print(f"{t.text}\t{t.pos_}\t{t.ent_type_ or t.lemma_}\t{t.dep_}\t{voc[t.text].rank}")
        print()

def main():
    cl = clfilter("di", doc=__doc__)

    nlp = spacy.load("pt_core_news_lg")
    voc = nlp.vocab

    content = ""
    for txt in cl.text():
        content += txt

    doc = nlp(content)
    retoken(doc)
    printconl(doc,voc)

if __name__ == '__main__':
    main()
