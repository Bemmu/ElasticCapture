# Scrapes BuzzCapture team page and uploads to ElasticSearch.
# http://awstutorialelastic-1527363486.us-east-1.elb.amazonaws.com:9200/_plugin/head/

from BeautifulSoup import BeautifulSoup
import json
import requests

team_url = "http://www.buzzcapture.com/en/about-buzzcapture/team/"
elasticsearch_endpoint = "http://awstutorialelastic-1527363486.us-east-1.elb.amazonaws.com:9200/team/profile"

soup = BeautifulSoup(requests.get(team_url).text)
people = soup.findAll('div', {'class': 'col description'})

for person in people:
	desc = person.find('blockquote').text
	name, role = person.find('p').text.split(",")

	data = json.dumps({
	    "name" : name,
	    "role" : role,
	    "desc" : desc
	})

	print "Would insert: %s" % data
#	r = requests.post(elasticsearch_endpoint, data=data)
#	print r.content
