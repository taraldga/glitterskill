
from mechanize import Browser
from bs4 import BeautifulSoup, SoupStrainer
import sys
print sys.getdefaultencoding()

def open_page(url):
	links = []
	chk = 1
	count = 0
	print('connecting to ', url)
	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)
	print 'connected'
	soup = BeautifulSoup(br.response().read(),parseOnlyThese=SoupStrainer('a'))
	for link in soup:
		if link.has_attr('href'):
			if('stilling?' in link['href']):
				links.append(make_link(link))
				count = count + 1
	if(count == 0):
		chk = 0
	return chk, links
				
	
				 
def make_link(link):
	return 'https://tjenester.nav.no/stillinger' + link['href'][1:]


def traverse_link(link):
	save_data = {}
	br = Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(link)
	soup = BeautifulSoup(br.response().read())
	mydivs = soup.findAll("p", { "class" : "details clearfix" })
	my_blob = soup.get_text()
	my_blob = my_blob.encode('utf-8')
	raw_text = my_blob.split('Skriv ut')[1].split('Din side')[0].replace('\n', '-')	
	save_data['Firm'] = raw_text.split('-----')[1].split('--')[0]
	#save_data['PosID'] = raw_text.split('-Stillingsnummer: ')[1].split(' (')[0] 
	save_data['Place'] = raw_text.split('Arbeidssted')[1].split('Antall')[0].split('Type')[0]
	save_data['Deadline'] = raw_text.split('publiseringsdato')[1].split('Registrert')[0]
	save_data['Industry'] = 'Computer science'
	save_data['RawText'] = raw_text.replace('-','')


	f = open('fil.txt','w')

	f.write(save_data['RawText'])

	return save_data	

def main():
	chk = 1
	page = 0
	links = []
	complete_data = []
	base_string = 'https://tjenester.nav.no/stillinger/stillinger?s2=675878&sort=akt&rpp=100&p=0&rv=al'
	while chk:
		page_string = '&p=' + str(page) + '&'
		search_link = base_string.replace('&p=0&',  '&p=' + str(page) + '&')
		chk, saved_links = open_page(search_link)
		links = links + saved_links
		page = page + 1
	print 'fetched ' , len(links), ' jobs from NAV'
	print 'Starting traversing links',
	#for link in links:
	#	complete_data.append(traverse_link(link))
	#	print '.',
	print traverse_link(links[140])

	print complete_data
	
main()













