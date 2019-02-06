########
# File download and use in the program
import urllib.request

url = "https://www.google.co.kr"

mem = urllib.request.urlopen(url).read() # to use in the progrma
print(mem)

# to handle Hangul
print(mem.decode("euc-kr")) # use either utf-8 or euc-kr

# to save 
savename = "savefile.data"
urllib.request.urlretrieve(url, savename) # to save (method 1)

with open(savename, mode="wb") as f: # to save (method 2)
    f.write(mem)

########
# Internet Access
'''
Method: GET, POST, PUT, DELETE
- With urllib library, GET method is usually used
- if Internet address is entered into web-browser, it is GET method
Target: http://media.daum.net -> Name of host
Additional Info: 
- path: /photo-viewer
- data: ?cid=318190&<var>=<val>&query=<val>
- hash: #1090923810932809

Encoding vs Decoding
- Encoding: <Korean> to %EC%AS... 
- Decoding: reverse of ecoding
'''

# import urllib.request 
import urllib.parse
# https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=3&acq=chzhf&qdt=0&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF

api = "https://search.naver.com/search.naver"
values = {   # parameters are in a dictionary format
    "sm": "top_sug.pre",
    "fbm": "1&acr=3",
    "acq": "chzhf",
    "qdt": "0",
    "ie": "utf8", 
    "query": "%EC%B4%88%EC%BD%9C%EB%A6%BF" # you may put Korean
}
params = urllib.parse.urlencode(values)
url = api+'?'+params # need ? to connect

data = urllib.request.urlopen(url).read()
print(data.decode("utf-8")) # or use euc-kr
