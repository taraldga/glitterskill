from bs4 import BeautifulSoup
import urllib2
import json
import re
import os
import codecs

files = [os.path.join("ads", "ad-contents", "{}".format(filename)) for filename in os.listdir(os.path.join("ads", "ad-contents"))]
with open(files[0]) as f1:
    print(f1.read())