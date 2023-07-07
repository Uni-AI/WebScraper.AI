import time
from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Chromium()

music = "https://www.youtube.com/watch?v=TbvWnJh9e-g&t=902s&ab_channel=RealScience"

music = "https://www.youtube.com/watch?v=TbvWnJh9e-g"
driver.get(music)
# driver.get("https://realpython.com/beautiful-soup-web-scraper-python/")
time.sleep(17)
driver.get("https://www.mail.com/")

driver.quit()