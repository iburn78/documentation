# XML: extensible markup language  

'''
- <tag>{Contents} # element
      <tag>{Contents}</tag>
  </tag>
- <tag /> # no need to close

- attributes: "" -> string / {val} has to be in ""
  <tag attr="{val}" attr="{val}">{Contents}</tag>
  <tag attr="{val}" attr="{val}" />

- root tag: there is only one root tag
  <rss version="2.0"> 

- ![CDATA[...]] -> special tag / used to protect a long string / can be ignored when scrapping
'''

from bs4 import BeautifulSoup
import urllib.request

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
request = urllib.request.urlopen(url)
xml = request.read()

soup = BeautifulSoup(xml, "html.parser") # there is XML paser as well
seoul = soup.find_all("location")[0]
datas = seoul.find_all("data")

for data in datas:
    print(data.find("wf").text)


