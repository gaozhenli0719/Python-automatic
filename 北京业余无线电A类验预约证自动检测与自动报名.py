from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import traceback

# Chrome WebDriver的路径(需自行更改)
chrome_driver_path = r'C:\Path\To\chromedriver.exe'

# 登录后的目标页面的URL
examplan_url = "https://xt.bjwxdxh.org.cn/static/member/#/static/member/examplan"

# 登录页面的URL
login_url = "https://xt.bjwxdxh.org.cn/static/member/#/static/member/user/login?redirect=%2Fhome"

# 账号和密码(需自行更改)
username = "username"
password = "password"

# PushPlus的Token(需自行更改)
pushplus_token = "your token"

# 设置Chrome选项
chrome_options = Options()

def send_pushplus_notification(title, content):
    url = 'https://www.pushplus.plus/send/'
    payload = {
        "token": pushplus_token,
        "title": title,
        "content": content
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("PushPlus消息发送成功")
    else:
        print(f"PushPlus消息发送失败，状态码: {response.status_code}")

def login():
    driver.get(login_url)
    time.sleep(2)  # 等待页面加载

    try:
        # 等待用户名输入框加载并输入账号
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(username)

        # 等待密码输入框加载并输入密码
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

        # 等待登录按钮并点击
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-btn.ant-btn-primary.ant-btn-lg"))
        )
        login_button.click()

        # 等待登录完成并访问目标页面
        WebDriverWait(driver, 30).until(
            EC.url_contains("/static/member/home")
        )
        driver.get(examplan_url)
    except Exception as e:
        print(f"登录过程中出现异常: {e}")
        send_pushplus_notification(
            "程序出错了",
            f"登录过程中出现异常: {e}\n{traceback.format_exc()}"
        )
        driver.quit()
        raise

def check_and_perform_actions():
    while True:
        current_url = driver.current_url
        
        if "user/login" in current_url:
            print("检测到登录页面，需要重新登录...")
            login()  # 重新登录
        else:
            try:
                # 检查是否存在“暂无数据”提示
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-empty-description"))
                )
                empty_description = driver.find_element(By.CSS_SELECTOR, ".ant-empty-description")
                if empty_description.is_displayed():
                    print("暂无数据，页面刷新中...")
                    driver.refresh()
                    time.sleep(10)  # 每隔10秒刷新一次
                else:
                    print("数据已加载，进行下一步操作...")
                    # 发送PushPlus通知
                    send_pushplus_notification(
                        "北京业余无线电考试A类报名开始了",
                        "北京业余无线电考试A类报名开始了，检测到“暂无数据”已消失"
                    )
                    
                    # 找到包含“A”的可点击元素并点击
                    clickable_elements = driver.find_elements(By.CSS_SELECTOR, ".ant-table-tbody a")
                    for element in clickable_elements:
                        if "A类不参加知识讲座" in element.text:
                            element.click()
                            break

                    # 等待并点击“能力验证”按钮
                    capability_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ant-btn.ant-btn-primary"))
                    )
                    capability_button.click()
                    break
            except Exception as e:
                print(f"执行页面操作过程中出现异常: {e}")
                send_pushplus_notification(
                    "程序出错了",
                    f"执行页面操作过程中出现异常: {e}\n{traceback.format_exc()}"
                )
                driver.refresh()
                time.sleep(10)  # 出现异常时刷新页面

def main():
    global driver
    driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path), options=chrome_options)
    
    send_pushplus_notification(
        "程序开始运行",
        "程序正在运行中"
    )
    
    driver.get(examplan_url)
    time.sleep(2)  # 等待页面加载

    try:
        check_and_perform_actions()
    except Exception as e:
        send_pushplus_notification(
            "程序出错了",
            f"在主程序中出现异常: {e}\n{traceback.format_exc()}"
        )
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
