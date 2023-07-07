import time
from selenium import webdriver

driver = webdriver.Chrome()

music = "https://www.youtube.com/watch?v=TbvWnJh9e-g&t=902s&ab_channel=RealScience"
driver.get(music)
time.sleep(150)
driver.get("https://www.mail.com/")

driver.quit()