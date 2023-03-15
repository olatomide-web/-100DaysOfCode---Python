from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
#article_count.click()
#print(article_count.text)


all_pages = driver.find_element("link text", "Talk")
#all_pages.click()

search = driver.find_element("name", "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)