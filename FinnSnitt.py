# -*- coding: utf-8 -*-
import os
from sets import Set
import os
import re
import collections


def fileread(fname): 
    script_dir = os.path.dirname(__file__)
    with open (os.path.join(script_dir,"ads", "ad-contents", fname)) as myfile:
        data=myfile.read()
    return data

def fileread2(fname): 
    script_dir = os.path.dirname(__file__)
    with open (os.path.join(script_dir,"ikkeData","ads", "ad-contents", fname)) as myfile:
        data=myfile.read()
    return data   
         

def dirListing(fileplacement):
    dirList = os.listdir(fileplacement)
    alldata = ''
    for fname in dirList:
        #print fname
        data = fileread(fname)
        #print data
        alldata = alldata + data
    return alldata

def dirListing2(fileplacement):
    dirList = os.listdir(fileplacement)
    alldata = ''
    for fname in dirList:
        #print fname
        data = fileread2(fname)
        #print data
        alldata = alldata + data
    return alldata
    


def main():
    
    fileplacement = r"C:\Users\BeateHaram\Documents\Eit\glitterskill\ads\ad-contents" #It-annonser
    filedeplacement = r"C:\Users\BeateHaram\Documents\Eit\glitterskill\ikkeData\ads\ad-contents" #Alle andre annonser
    alldata = dirListing(fileplacement)
    ikkedata = dirListing2(filedeplacement)
    Rawdata = alldata
    Stopwords = ikkedata
    ReRawdata=' '.join(filter(lambda x: x.lower() not in Stopwords,  Rawdata.split(' ')))
    words = re.findall('\w+', ReRawdata.lower())
    y = 60
    print collections.Counter(words).most_common(y)
    return collections.Counter(words).most_common(y)
    
    
if __name__ == '__main__':main()