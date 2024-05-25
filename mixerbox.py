import browser_cookie3
import json

import os
import time
import sys
import json

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from chrome_driver import create_driver, wait_for, wait_for_element, wait_for_id, get, wait_for_tag_name, wait_element_for_id

def read_json_from_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

settings_json = read_json_from_file("./settings.json")

driver = create_driver(enable_ui=True)
if driver is None:
    print("创建driver失败")
    sys.exit(1)
driver.get("https://mixerbox.ai/")

time.sleep(5)
# input_element = wait_element_for_id(driver, '//*[@id=":r0:"]')
# input_element.send_keys("今天是几月几号？")

# input = driver.find_element(By.ID, ':r0:')
# input.send_keys('今天是几月几号？')
# # //*[@id=":r0:"]
#
# driver.find_element(By.XPATH, '//*[@id="layout-inner"]/div[2]/div[3]/div/div[1]/div/button[2]').click()
#
# # time.sleep(10000)
#
# answer = driver.find_element(By.XPATH, '//*[@id="layout-inner"]/div[2]/div[2]/div/div[3]')
#
# print(answer.text)

cookies = driver.get_cookies()
for cookie in cookies:
    if cookie["name"] == "access_token":
        settings_json["cookie"] = cookie["value"]
        cookies_in_json = [cookie["value"]]
        settings_json["cookies"] = cookies_in_json
        print(cookie["value"])
        # json格式化后写入文件
        with open("./settings.json", "w") as f:
            json.dump(settings_json, f, indent=2)

# 检查git有没有变化，如果有变化就提交
os.system("git add .")
os.system("git commit -m 'update cookie'")
os.system("git push --rebase")
os.system("git push")


driver.quit()

# # 从Chrome中，读取https://mixerbox.ai/的cookie
# cookies = browser_cookie3.chrome(domain_name="mixerbox.ai")
# # key-value形式的cookie
# for cookie in cookies:
#     print(cookie.name, cookie.value)