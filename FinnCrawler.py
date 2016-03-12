# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import json
import re
import os
import numpy as np
import codecs
import sqlite3
import datetime


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
    conn = sqlite3.connect('database.db')
    conn.text_factory = str
    cursor = conn.cursor()

    with open(os.path.join("ads", "ad_urls")) as url_file:
        n_urls = int(url_file.readline().strip())
        for i, line in enumerate(url_file):
            url = line.strip()
            print("Processing, {} of {}".format(i+1, n_urls))
            #simple = 72308893
            #omplicqted = 72308957
            #url = "http://m.finn.no/job/fulltime/ad.html?finnkode=72308957"
            fetch_contents(url, cursor)
            #break #For testing, kjører kun gjennom en annonse
    print("--- Fetched ad contents ---")
    conn.commit()
    conn.close()

def fetch_contents(url, cursor):
    source = urllib2.urlopen(url).read().decode("utf-8")
    parser = BeautifulSoup(source, "html.parser")
    #text purification
    # job_description = re.sub("\s[^a-zA-Z������]\s", " ", job_description)
    # job_description = re.sub(r"([a-zA-Z������-]+)[\.,]\s", r"\1", job_description)
    # job_description = re.sub("\s+", " ", job_description)

    tables = parser.findAll("dl", {"class": ["r-prl", "mhn", "multicol"]})
    job_obj = {}
    for table in tables:
        keys = table.findAll('dt')
        values = table.findAll('dd')
        place = False
        for i in range(len(keys)):
            job_obj[keys[i].text] = values[i].text
            if place:
                if keys[i].text == "Frist":
                    place = False
                else:
                    if keys[i].text == "":
                        job_obj['Sted'] = values[i].text
            if keys[i].text == "Sted":
                place = True

    id = unique_id = re.search(".+?=([0-9]+)", url).group(1)

    job_obj['id'] = id
    description = "\n".join([re.sub("<.+?>", " ", str(element)) for element in parser.findAll("div", {"class": ["object-description", "mbl"]})])

    firm = None
    if 'Arbeidsgiver' in job_obj:
        firm = job_obj['Arbeidsgiver']

    city = None
    if 'Sted' in job_obj:
        location = job_obj['Sted'].split(" ")
        postcode = location[0].rstrip()
        city = location[1].rstrip()

    deadline = None
    if 'Frist' in job_obj:
        deadline = job_obj['Frist'].rstrip().strip()

    title = job_obj['Stillingstittel'].rstrip()
    branch = "it"
    source = "finn"

    date = datetime.datetime.now().isoformat()

    job_query = 'INSERT INTO  job(id, title, description, firm, city, postcode, branch, deadline, source, date)' + 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
    params = (id, title, description, firm, city, postcode, branch, deadline, source, date)

    cursor.execute(job_query, params)


def setup():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.exists(os.path.join("ads", "ad-contents")):
        os.makedirs(os.path.join("ads", "ad-contents"))
    print("--- Initial setup complete ---")



if __name__ == "__main__":
    #setup()
    fetch_ad_urls()
    fetch_ad_contents()
