import urllib
# url = "http://www.buzzcapture.com/en/about-buzzcapture/team/"
# html_doc = urllib.urlopen(url, "r").read()
html_doc = open("team.html", "r").read()

# print html_doc

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(html_doc)
people = soup.findAll('div', {'class': 'col description'})
for person in people:
	desc = person.find('blockquote').text
	name, role = person.find('p').text.split(",")
	print desc

#print people

#print(soup.prettify())