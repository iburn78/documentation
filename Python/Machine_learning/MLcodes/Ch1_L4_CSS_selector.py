# BeautifulSoup: analyzing HTML
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <div id="meigen">
            <h1 title="header title">Wikibooks texts</h1>
            <ul class="items art it book">
                <li>li text 01</li>
                <li>li text 02</li>
                <li>li text 03</li>
                <li>li text 04</li>
            </ul>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
header = soup.select_one("body > div > h1") # returns an element
list_items = soup.select("ul.items > li") # returns an array

print(header.string) # as this is an element

# accessing attrs: 
print(header.attrs["title"])
print(soup.select_one("ul").attrs)

for li in list_items: # as this is an array
    print(li.string)

# CSS selector: refer to the textbook for CSS selector
'''
- <tag>
- #<id name>
- class selector is most frequently used
- if there are multiple class items: 
   <ul class="item art it book">
   ul.item.art.it.book # no space
- connectors: 
    " ": select from all next generations
    ">": select from just next generation (children)
'''

