import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')


def test():
    music = "https://www.youtube.com/watch?v=TbvWnJh9e-g&t=902s&ab_channel=RealScience"

    driver.get(music)
    time.sleep(17)
    driver.quit()
