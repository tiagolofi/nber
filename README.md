# Scrapping NBER

Scrapping data of working papers

routes in NBER URL

base URL: https://www.nber.org/search?page=1&perPage=50

| params | eg.|
|--------|----|
| &q= | 'elections' |
| facet=topics%3A | 'Labor%20Economics' | 
| &facet=contentType%3A | 'working_paper' |

req URL: https://www.nber.org/search?facet=topics%3ALabor%20Economics&facet=contentType%3Aworking_paper&page=1&perPage=50&q=accumulation