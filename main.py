#!/usr/bin/python

import make_db, filter_f, extraction, nyt_scraper

url = "http://feeds.bbci.co.uk/news/rss.xml"

#make_db()
print "Making database... URL: {}".format(url)
facts_db = make_db.make_db(url)
#load_db()
print "Loading Database..."
facts_db = filter_f.load_db('facts_db.json')
#get articles
print "Scraping..."
articles = nyt_scraper.nyt_scraper("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
#extract facts
for article in articles:
  print "extracting facts..."
  facts = extraction.extractFacts(article)
  #filter facts
  for fact in facts:
    print "filtering facts..."
    report = filter_f.filter_facts(fact, facts_db)
    #deliver report
    print "Report: {}".format(report)
