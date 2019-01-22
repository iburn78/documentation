Machine Learning
---------------------
---------------------
[Ch1. Crolling and Scrapping]
Internet Information Request
- Method: GET (POST, PUT, DELETE)
- Target: http://media.daum.net => name of host
- Additional info: 
    path e.g., /photo-viewer  
    data e.g., ?cid=318190  
        <key>:<data>&<key>:<data>&... &query=<%...%...: Korean language encoding
- BeautifulSoup example code

----------------
import urllib.request
from bs4 import BeautifulSoup

url = ""
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
result_one = soup.select_one()
print(result_one.string, result_one.attrs['href'], result_one.attrs['class']
results = soup.select()
for result in results:
    print(results.string)
----------------

- 
