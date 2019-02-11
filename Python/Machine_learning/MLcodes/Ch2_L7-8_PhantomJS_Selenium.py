# Phantom JS: web-browser without screen

#### Typical flow 
# browser = webdriver.PhantomJS()
# browser.implicitly_wait(3) # required to wait for 3 secs before loading
# browser.get(url)
# browser.save_screenshot("website1.png") # use screenshots to check progress
# browser.quit()

from selenium import webdriver
url = "https://nid.naver.com/nidlogin.login"

browser = webdriver.PhantomJS()
browser.implicitly_wait(3) # required to wait for 3 secs before loading
browser.get(url)
element_id = browser.find_element_by_id("id")
element_id.clear()
element_id.send_keys("***")
element_pw = browser.find_element_by_id("pw")
element_pw.clear()
element_pw.send_keys("***")

browser.save_screenshot("website1.png") # use screenshots to check progress

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()

browser.save_screenshot("website2.png") # use screenshots to check progress

# opening mail page example
browser.get("https://mail.naver.com")
browser.save_screenshot("website3.png")

titles = browser.find_element_by_css_selector("strong.mail_title")
for title in titles:
    print("-", title.text)

browser.quit()

'''
$ pip install selenuim == 3.0 to remove warnings 

Or, can use Chromedriver instead
usage: 
$ pip install chromedriver
use Chrome() instead of PhantomJS()
has to set Chrome(executable_path="./chromedriver") 

To use headless browser, there are settings for Chrome available
'''

print('------')
browser = webdriver.Chrome(executable_path="./chromedriver")

url = "http://www.naver.com/"

browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot("chrome_image.png")
browser.quit()