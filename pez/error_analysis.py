#!/usr/bin/env python -*- coding: utf-8 -*-

import urllib, urllib2, string, codecs, re
from bs4 import BeautifulSoup as bs

from util import semeval2014_task5, task5_files, sensible_outputs


for testfiles in task5_files():
    inxml = codecs.open(testfiles,'r','utf8').read()
    lang = testfiles.split('.')[0]
    lang =  testfiles.rpartition('/')[2].split('.')[0]
    if lang in ["en-es", "en-de"]:
        with codecs.open('sensible-error-anal-'+lang+'.xml', 'w', 'utf8') as fout:    
            sysxml = codecs.open(sensible_outputs(lang), 'r', 'utf8')
            inxml_soup = bs(inxml).find_all('s')
            
            inputs = {int(goldsent.get('id')):"<inp>"+unicode(goldsent).split('\n')[1][8:]+"</inp>"
                       for goldsent in inxml_soup}
            
            references = {int(goldsent.get('id')):goldsent.find('ref') \
                          for goldsent in  bs(inxml).find_all('s')}
            sysoutputs = {int(sysoutput.get('id')):sysoutput.find('output') \
                          for sysoutput in  bs(sysxml).find_all('s')}
            
            for i in sorted(references):
                if i in sysoutputs:
                    fout.write(inputs[i]+"\n")
                    fout.write(unicode(sysoutputs[i]).replace('output>', 'out>')+"\n")
                    fout.write(unicode(references[i])+"\n\n")
    

