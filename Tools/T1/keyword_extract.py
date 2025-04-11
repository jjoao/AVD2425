
"""
keyterms [options] files
Options:
    -n 20       Number of keyterms (def.:30)
    -q          quiet (no confidence is presented) 
Descrition
  extract keywords from one or more files
"""
import sys
import textacy
from textacy import extract
import jjcli

def main():
    cl = jjcli.clfilter("qn:", man=__doc__)
    n = int(cl.opt.get("-n",30))

    for txt in cl.text():
        print("#", cl.filename() )
        doc = textacy.make_spacy_doc(txt, lang="pt_core_news_lg")
        for t, num in extract.keyterms.textrank(doc, normalize="orth", topn=n):
            if "-q" in cl.opt:
                print(f"{t}\t{num:.4f}")
            else:
                print(f"{t}")

if __name__ == "__main__":
    main()
