#!/usr/bin/env python
"""
Usage:
 txtfreq  [Options] files
 Options:
   -l        lemmas (default)
   -w        words
   -m 10     just the first 10 most common
   -r        relative freq per million
   -p        rank

Output
  - tab-separated-value (TSV) with
         lemma  absolute-freq
  (-r)   lemma  rel-freq-per-million
 
"""
import spacy
from  jjcli import *
from collections import Counter

pln=spacy.load("pt_core_news_lg")

def printtab(f,m=1000000):
    for pal,oco in f.most_common(m):
        print(f"{pal}\t{oco}")

def main():
    cl = clfilter("wlrm:", doc=__doc__ ) ### cl.opt
    
    # -m 10   how many values 
    num = int(cl.opt.get("-m",1000000))
    # -r      rel or abs
    isrel = False
    if "-r" in cl.opt: 
        rel = True

    freq = Counter()
    for txt in cl.text():
        dt = pln(txt)
        for tok in dt:
            if tok.pos_ == "SPACE": 
                continue 
            freq[ tok.lemma_] +=1 

    if isrel:
        tot = freq.total()
        freqrel = Counter()
        for pal,oco in freq.items():
            freqrel[pal] = oco / tot * 1000000
        printtab(freqrel, num)
    else:
        printtab(freq, num )

if __name__ == "__main__" : 
    main()
