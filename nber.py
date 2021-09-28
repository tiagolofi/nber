"""
scrapping data from NBER
"""

from bs4 import BeautifulSoup as bs
from requests import get

def my_search_in_nber(q):

	base_url = 'https://www.nber.org/search?page=1&perPage=50'
	query = '&q='
	q = '%20'.join(q.split(' '))

	url = get(base_url + query + q)

	page = bs(url.content, 'html.parser')
	names = page.select('a')
	return names

print(my_search_in_nber(q='COVID-19'))
