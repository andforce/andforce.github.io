import json
import os
import sys
import time
import subprocess

from chrome_driver import create_driver


def run_command(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out, err


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

cookies = driver.get_cookies()
for cookie in cookies:
    if cookie["name"] == "access_token":
        settings_json["cookies"] = [cookie["value"]]
        print(cookie["value"])
        # json格式化后写入文件
        with open("./settings.json", "w") as f:
            json.dump(settings_json, f, indent=2)

out, err = run_command("git status")
if err:
    print(err)
    sys.exit(1)
else:
    print(out)

# 检查git有没有变化，如果有变化就提交
os.system("git add .")
os.system("git commit -m 'update cookie'")
os.system("git pull --rebase")
os.system("git push")

driver.quit()
