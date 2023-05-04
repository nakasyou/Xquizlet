from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from utils.config import get_config
import utils.panel as panel
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import json, sys
config, words = get_config()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

if "--no-headless" not in sys.argv:
    options.add_argument('--headless')

chrome_service = fs.Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(
    service=chrome_service,
    options=options
    )
driver.set_window_size(500,700)


driver.get(f'https://quizlet.com/{config["__id__"]}/match')
time.sleep(0.2)
with open("cookie.json") as f:
    for cookie in json.load(f):
        tmp = {"name": cookie["name"], "value": cookie["value"]}
        driver.add_cookie(tmp)
print("GO!")
time.sleep(0.2)
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/button").click()

panels = [driver.find_element(By.XPATH,panel.get_xpath(i)) for i in range(12)]
texts = [_.text for _ in panels]

for i,text in enumerate(texts):
    value = words.get(text)
    if value:
        panels[i].click()
        panels[texts.index(value)].click()
time.sleep(3)
print("END.")