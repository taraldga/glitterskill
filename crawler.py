# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import json
import re
import os

urlpoint = "http://m.finn.no/job/fulltime/search.json?occupation=0.23"


# Reading in first page of search results in order to fetch job page links
req = urllib2.Request(urlpoint)
response = urllib2.urlopen(req)
text = json.loads(response.read().decode("utf-8"))
links = text['pagingInfo']['pagingLinks']

list_of_link_pages = []
for page_link in links:
  list_of_link_pages.append(page_link['url'])


joblinks = text["displaySearchResults"]
print(joblinks)

for joblink in joblinks:
  print joblink["adId"]
  print joblink["adUrl"]
  print joblink["titleRow"]
# Må ha en sjekk for om hver utlysning har disse parameterene
