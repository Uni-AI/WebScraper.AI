sch: [python](https://www.google.com/search?q=selenium+webdriver+chromium+python)

# Answer:
- https://stackoverflow.com/questions/72172923/selenium-for-chromium-in-python

# Source:
https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi
>For those struggling to find the path of the newly installed driver. The driver was installed in the chromium-browser folder in usr/lib.
>
>So I change my code from
>
>```from selenium import webdriver
>
>browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromium-browser-v7')
>browser.get('https://automatetheboringstuff.com')
>```
>to
>```
>from selenium import webdriver
>
>browser = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver')
>browser.get('https://automatetheboringstuff.com')
>```
>Hope that helps :D
