# Python-automatic
使用Python写一些可以完成小功能的脚本。属于本人自接触Python以来的大量练手作品，欢迎大家的指正和批评。

# 北京业余无线电考试自动化脚本 Beijing Amateur Radio Exam Automation Script

本人于2020年（高二）接触业余无线电和相关知识，但是由于每个月的不参加知识讲座的验证名额有限，导致我如今2024年8月了仍然没有成功报名，因此结合我的专业写下了第一个具有一定实际使用意义的程序，励志本月一定要报上。
此脚本用于自动化检查和报名北京业余无线电考试（A类），它使用 Selenium 自动化浏览器操作，并通过 PushPlus 发送通知。
This script automates the process of checking and registering for the Beijing Amateur Radio Exam (A class) on the official website. It uses Selenium to automate browser interactions and PushPlus to send notifications.

## 功能特点 Features

- **自动登录：** 使用提供的用户名和密码自动登录到网站。
- **Automatic Login:** Automatically logs in to the website with the provided username and password.
- **页面监控：** 监控目标页面上的特定元素，以此判断是否开始预约。
- **Page Monitoring:** Monitors the target page for the presence of specific elements.
- **自动刷新：** 如果数据尚仍然存在，每10秒刷新一次页面。
- **Automatic Refresh:** Refreshes the page every 10 seconds if the data is not yet available.
- **动作触发：** 一旦数据可用，在页面上执行操作。
- **Action Trigger:** Executes actions on the page once the data becomes available.
- **错误处理：** 如果会话被重定向到登录页面，自动重新登录。
- **Error Handling:** Automatically logs back in if the session is redirected to the login page.
- **推送通知：** 当脚本启动、数据可用或发生错误时，通过 PushPlus 发送通知。
- **Push Notifications:** Sends push notifications via PushPlus when the script starts, when data is available, and when an error occurs.

## 环境要求 Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## 配置脚本： Configure the script:

打开 北京业余无线电A类验预约证自动检测与自动报名.py 并使用您的账户信息修改以下变量：
Open 北京业余无线电A类验预约证自动检测与自动报名.py in your text editor and modify the following variables with your own credentials:

- **账号和密码 Your credentials**
username = "your_username@example.com"
password = "your_password"

- **Chrome WebDriver 的路径 Path to Chrome WebDriver**
chrome_driver_path = r'C:\Path\To\chromedriver.exe'

- **填写PushPlus token input your PushPlus token:**

pushplus_token = "your token"

## 注意事项 Notes：

请确保 Chrome WebDriver 与您 Chrome 的版本兼容。
脚本设计为处理强制退出登录并重新验证后继续流程。
监控脚本的输出以查看任何意外行为或问题。
Ensure that the Chrome WebDriver is compatible with your version of Chrome.
The script is designed to handle forced logouts by re-authenticating and continuing the process.
Monitor the script’s output for any unexpected behavior or issues.

## 联系作者：

- **QQ:652694566**
- **Wechat:OokamiYAN**
- **E-mail：gaozhenli0719@gmail.com**
