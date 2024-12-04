import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--handless')
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

broswer = webdriver.Chrome(options=chrome_options)
url = 'http://www.baidu.com'
broswer.get(url)

time.sleep(2)



