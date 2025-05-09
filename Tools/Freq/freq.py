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

pln = spacy.load("pt_core_news_lg")
voc = pln.vocab
freqsum = Counter()
freqabs = Counter()
freqrel = Counter()

def gprinttab(fabs,frel,m=1000000):
    print(f"word\toccu\tfreq-per-mill\tusual\trank\tracio")
    for pal,oco in fabs.most_common(m):
        
        freqhabitual = freqsum[pal]/freqabs[pal]*1000000
        racio = frel[pal] / freqhabitual
        if (r:= voc[pal].rank) > 1000000 :
            r = "OFV"
        print(f"{pal}\t{oco}\t{frel[pal]:.2f}\t{freqhabitual:.2f}\t{r}\t{racio:.2f}")

def printtab(f,m=1000000):
    print(f"word\toccu\tfreq-per-mill\trank\tracio")
    for pal,oco in f.most_common(m):
        freqhabitual = freqsum[pal]/freqabs[pal]*1000000
        racio = oco / freqhabitual
        if (r:= voc[pal].rank) > 1000000 :
            r = "OFV"
        print(f"{pal}\t{oco:.2f}\t{freqsum[pal]/freqabs[pal]*1000000:.2f}\t{r}\t{racio:.2f}")

def rank2freq(w,voc):
    r= min( voc[w].rank , voc[w.lower()].rank)
    if r > 1000000 :
        r = 1000000
    return 1 / (r + 2.7)  ## Zipf law variant

def main():
    cl = clfilter("pwlrm:", doc=__doc__ ) ### cl.opt
    
    # -m 10   how many values 
    num = int(cl.opt.get("-m",1000000))
    
    # -r      rel or abs
    isrel = False
    if "-r" in cl.opt: 
        isrel = True

    for txt in cl.text():
        dt = pln(txt)
        for tok in dt:
            lem = tok.lemma_
            if tok.pos_ == "SPACE": 
                continue 
            if tok.pos_ != "PROPN":
                lem = re.sub(r" .*", r"", lem)
            else:
                lem = tok.text
            freqabs[lem] +=1 
            freqsum[lem] += rank2freq(tok.text, voc) 

    tot = freqabs.total()
    for pal,oco in freqabs.items():
        freqrel[pal] = oco / tot * 1000000
    if isrel:   ## relative freq
        gprinttab(freqabs, freqrel,num)
    else:
        printtab(freqabs, num )

if __name__ == "__main__" : 
    main()
