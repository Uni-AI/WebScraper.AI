sch: [https://www.google.com/search?q=selenium+webdriver+chromium+python](python)

# Answer:
- https://stackoverflow.com/questions/72172923/selenium-for-chromium-in-python

# Source:
https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi

>Works fine!
>I used "driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')" and it worked good-
---
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://automatetheboringstuff.com')
```
>Enjoy. Resolved "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
