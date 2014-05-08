#!/usr/bin/env python -*- coding: utf-8 -*-

def semeval2014_task5(inputfilename):
  """ Original script used by PEZ to get sentences from task5 test data."""
  import libsemeval2014task5.format as format
  import string
  reader = format.Reader(inputfilename)
  for sentencepair in reader:
    left, frag,right = map(str, sentencepair.inputfragments()[0])
    left, frag,right = left.strip(), frag.strip(),right.strip()
    src = left+" "+right
    src =  "".join([i for i in src if i not in string.punctuation])
    sentence = " ".join([left, frag, right])
    
    print dir(sentencepair.inputfragments()[0][1])
    print sentencepair.inputfragments()[0][1].alternatives
    print sentencepair.inputfragments()[0][1].value
    yield sentence.strip(), frag, left, right

def task5_files(lang=None, option="gold"):
  """ Returns a list of files from task 5."""
  import os
  abspath = os.path.abspath(os.path.dirname(__file__))
  filedir = abspath+"/../data/"+option+"/"
  if lang:
    filename = lang+"."+option+".tokenised.xml"
    return filedir+filename
  else:
    return [filedir+i for i in  os.listdir(filedir) if \
            i.endswith('.tokenised.xml')]
    

def sensible_outputs(lang):
    import os
    abspath = os.path.abspath(os.path.dirname(__file__))
    if lang == "en-es":
        filepath = abspath+ \
        "/../data/sensible-submission/sensible.pez.wtmxlingyu.es-en.best.xml"
    elif lang == "en-de":
        filepath = abspath+ \
        "/../data/sensible-submission/sensible.pez.wtmxlingyu.de-en.best.xml"
    return filepath
  