from bs4 import BeautifulSoup
import urllib2
import json
import re
import os
import codecs

files = [os.path.join("ads", "ad-contents", "{}".format(filename)) for filename in os.listdir(os.path.join("ads", "ad-contents"))]

print files
for f in files:
    print(f.read())
