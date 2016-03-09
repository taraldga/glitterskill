# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import json
import re
import os
import numpy as np
import codecs


# ID BIGINT()
# Firm VARCHAR(100), KK
# Place VARCHAR(300),KK
# Deadline VARCHAR(10),
# Duration VARCHAR(50),
# NOPosition VARCHAR(5),
# Title VARCHAR(100), (B)
# Industry VARCHAR(100),(B)
# JobFunction VARCHAR(100)
# RawText VARCHAR(UNDEFINED) (done)

def fetch_ad_urls():
    result = json.loads(urllib2.urlopen("http://m.finn.no/job/fulltime/search.json?occupation=0.23").read().decode("utf-8"))
    ad_urls = ["http://m.finn.no{}".format(ad["adUrl"]) for ad in result["displaySearchResults"] if "adUrl" in ad]
    page_urls = ["http://m.finn.no{}".format(page["url"]).replace(".html", ".json") for page in result["pagingInfo"]["pagingLinks"] if not page["active"]]
    for page_url in page_urls:
        response = json.loads(urllib2.urlopen(page_url).read().decode("utf-8"))
        ad_urls += ["http://m.finn.no{}".format(ad["adUrl"]) for ad in response["displaySearchResults"] if "adUrl" in ad]
    with open(os.path.join("ads", "ad_urls"), "w") as url_file:
        url_file.write("{}\n{}".format(len(ad_urls), "\n".join(ad_urls)))
    print("--- Fetched URL's ---")

def fetch_ad_contents():
    with open(os.path.join("ads", "ad_urls")) as url_file:
        n_urls = int(url_file.readline().strip())
        for i, line in enumerate(url_file):
            url = line.strip()
            print("Processing, {} of {}".format(i+1, n_urls))
            fetch_contents(url)
            #break #For testing, kjører kun gjennom en annonse
    print("--- Fetched ad contents ---")

def fetch_contents(url):
    source = urllib2.urlopen(url).read().decode("utf-8")
    parser = BeautifulSoup(source, "html.parser")
    job_description = "\n".join([re.sub("<.+?>", " ", str(element)) for element in parser.findAll("div", {"class": ["object-description", "mbl"]})])
    job_description = re.sub("\s[^a-zA-ZæøåÆØÅ]\s", " ", job_description)
    job_description = re.sub(r"([a-zA-ZæøåÆØÅ-]+)[\.,]\s", r"\1 ", job_description)
    job_description = re.sub("\s+", " ", job_description)

    unique_id = re.search(".+?=([0-9]+)", url).group(1)
    print(unique_id)

    job_title = parser.findAll("h1", {"class": ["h1", "word-break", "mbn"]})

    boxes = parser.findAll("dl", {"class": ["r-prl", "mhn", "multicol"]})
    dicctionary = {}
    for box in boxes:
        keys = box.findAll('dt')
        values = box.findAll('dd')
        for i in range(len(keys)):
            dicctionary[keys[i].text] = values[i].text

    # for element in job_location:
    #     print element.text



    # print job_location

    with open(os.path.join("ads", "ad-contents", "content_{}.txt".format(unique_id)), "w") as content_file:
        content_file.write(job_description)


def setup():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(os.path.join("ads", "ad-contents")):
        os.makedirs(os.path.join("ads", "ad-contents"))
    print("--- Initial setup complete ---")

#def heisann():
#    os.chdir(os.path.join(os.path.dirname(__file__), "ads", "ad-contents"))
#    print(os.getcwd())
#    hei = np.loadtxt("content_71333019.txt", dtype=str, comments='#', delimiter=' ')
    # problem med ���, �=?, �=\xc3\xb8, �=\xc2\xb0
    # Vil egentlig ha en string og ikkje et numpyarray
    # https://docs.python.org/dev/library/stdtypes.html#str se 4.7.1 og nedover
#    print(hei)
#    print("tipp topp")

    #condition = hei == "nok"
    #sveis = np.extract(condition, hei)
    #print(sveis)
    #print("lollipop")


if __name__ == "__main__":
    setup()
    fetch_ad_urls()
    fetch_ad_contents()
