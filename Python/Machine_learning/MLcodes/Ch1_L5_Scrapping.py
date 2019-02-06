import urllib.request
from bs4 import BeautifulSoup
import time

# url = "http://finance.naver.com/marketindex/"
url = "https://news.naver.com/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
# soup.select_one()
results = soup.select("div#today_main_news li a")

for result in results: 
    print(result.string)
    url_article = result.attrs["href"]
    res_article = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(res_article, "html.parser")
    print(url_article)
    try: 
        output = ""
        content = soup_article.select_one("div#articleBodyContents").contents # contents returns a list or a iterable
        for item in content:
            stripped = str(item).strip()
            if stripped == "": # IMPORTANT: item can be empty, so index out of bound error could raise
                continue
            if not (stripped[0] in "</"):
                output += stripped
        print(output.replace("본문 내용TV플레이어", "").strip())
        # use string or contents
    except:
        pass
    print()
    time.sleep(0.1)

# to automate, use CRON (refer to the textbook)

