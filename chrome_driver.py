import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_tag_name(driver, tag: str, timeout=15):
    try:
        # 等待iframe加载
        wait = WebDriverWait(driver, timeout)
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, tag)))
        return iframe
    except Exception:
        print("wait_for() not found: ", tag)
        return None

# noinspection PyBroadException
def wait_for(driver, xpath: str, timeout=15):
    try:
        element: WebElement = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text
    except Exception:
        print("wait_for() not found: ", xpath)
        return None


# noinspection PyBroadException
def wait_for_element(driver, xpath: str, timeout=15):
    try:
        element: WebElement = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except Exception:
        print("wait_for() not found: ", xpath)
        return None

def wait_for_element_class_name(driver, xpath: str, timeout=15):
    try:
        element: WebElement = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.CLASS_NAME, xpath))
        )
        return element
    except Exception:
        print("wait_for() not found: ", xpath)
        return None

def wait_for_element_css(driver, xpath: str, timeout=15):
    try:
        element: WebElement = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.CLASS_NAME, xpath))
        )
        return element
    except Exception:
        print("wait_for() not found: ", xpath)
        return None

# noinspection PyBroadException
def wait_for_id(driver, element_id: str, timeout=15):
    try:
        element: WebElement = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.ID, element_id))
        )
        return element.text
    except Exception:
        print("wait_for_id() not found:", element_id)
        return None

def wait_element_for_id(driver, element_id: str, timeout=15):
    try:
        element: WebElement = WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((By.ID, element_id))
        )
        return element
    except Exception:
        print("wait_for_id() not found:", element_id)
        return None

def create_driver(enable_ui=False):
    chrome_options = webdriver.ChromeOptions()  # 实例化Option对象
    chrome_options.add_experimental_option("detach", True)  # 不关闭浏览器
    cache_dir = os.path.expanduser("~/Library/Caches/Selenium/3")
    chrome_options.add_argument("--user-data-dir=" + cache_dir)
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--window-size=580,1080')  # 设置浏览器分辨率
    # chrome_options.add_argument('--start-maximized')
    # headless模式
    if not enable_ui:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument(
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    )
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd(
            'Page.addScriptToEvaluateOnNewDocument',
            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
        )
    except Exception as e:
        print(e)
        # driver.quit()
        return None
    return driver


def get(driver, url, xpath=None):
    print("请求地址: " + url)

    driver.get(url)
    if xpath is not None:
        print("开始查找元素: " + xpath)
        element = wait_for_element(driver, xpath)
        return element
    return None