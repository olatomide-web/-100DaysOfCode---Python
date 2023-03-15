from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Invicta-6981-Analog-Chronograph-Polyurethane/dp/B003MYYJD0?ref_=Oct_DLandingS_D_73d3039e_61")

# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)


driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events = {}


for n in range(len(event_times)):
    events[n] = {
        "time" : event_times[n].text,
        "name" : event_names[n].text
    }

print(events)



# driver.close()
# driver.quit()