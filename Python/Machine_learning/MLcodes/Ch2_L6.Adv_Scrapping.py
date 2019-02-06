# Requests module 
# session.get(url) 
# session.post(url)
# session.put(url)
# session.delete(url)

import requests

# using get with requests module
'''
session = requests.session() # session only needs to be created once
url = "http://google.com"
data = {
    "a":"10", 
    "b":"20"
}
response = session.get(url, data=data)
response.raise_for_status()
print(response.text)
'''

# using post/put/delete with requests module
# it is easier to use post/put/delete with requests module than with urllib
'''
- F12 in Chrome: goes to developer mode
- check network recoding (red dot) and check preserve log box
- move to Doc
- then it is possible to check where login happens
- for example: 
      if login happened in login_proc.php, then check Form Data tab to figure out what data has been submitted
      check General tab to check Request URL and Request Method
'''
from bs4 import BeautifulSoup

session = requests.session() # session only needs to be created once
url = "http://www.hanbit.co.kr/member/login_proc.php"
login_data = {
    "retun_url": "http://wwww.hanbit.co.kr/index.html", # it seems that "retun_url" is a typo in the website 
    "m_id": "andyml",
    "m_passwd": "andyml78"
}
response = session.post(url, data=login_data) # note of using post instead of get / specifid in the developer page of google
response.raise_for_status()

url = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
response = session.get(url) # as indicated in the developer tool of Chrome
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
# print(response.text)
text = soup.select_one("dl.mileage_section1 span").get_text()
print(text)

'''
# .contents: generates a list that captures all the nodes and tags
# .string: returns internal string that belongs to itself
# .get_text(): returns all the internal texts
'''