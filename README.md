[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/jwssRZI4)

## Assignment #2. Automation of the service delivery
## Prerequisites

## 1. Install Python
* Make sure that Python is installed in your machine. Othweise, please refer to this page .[Download Python](https://www.python.org/);
* You should have Python editor/IDE depending on your choise. Convenient choises include .[PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows) and .[Visual Studio Code](https://code.visualstudio.com/download);
* Download the latest Python version . This assignmented required Python 3.8 or higher (mine is Python 3.11.8).

## 2. Install Selenium 
### Install Selenium using Python's package manager. Open the command prompt or terminal and type the following command:
```
pip install selenium
```
## 3. Install Python Environment
### You are required to use pipenv. To install pipenv, run the following command from terminal or command line:
```
pip install pipenv
```

## 4. SetUp Webdriver
* You will neeed to install the latests versions of Google Chrome and Mozilla FireFox. You can prefer to use other browsers with Selenium WbeDriver;
* You will need to install the latests versions of the WebDriver executables for these browsers: .[ChromeDriver](https://chromedriver.chromium.org/downloads) for Chrome and .[geckodriver](https://github.com/mozilla/geckodriver/releases) for FireFox.

## 5. SetUp WebDriver for Windows OS
### In my case, I used ChromeDriver. To install ChromeDriver:
**Step 1:** Go to .[ChromeDriver - WebDriver for Chrome - Downloads page](https://chromedriver.chromium.org/downloads) to install the latest Wbedriver executables;

**Step 2:** Click on the **The Chrome for Testing availability dashboard**, indicated by redline under **Current Releases**;

**Step 3:** Depending on your Chrome version, refer to one of the listed channels. In my case, I selected **Stable**;

**Notes:** Type ```chrome://version/``` to learn the version of your Chrome you use.

**Step 4:** Select WebDriver from **Binary ** column corresponding to your OS. I selected ChromeDriver for **win64** and install this .[URL](https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/win64/chromedriver-win64.zip). The link will be download as zip file and unzip it;

**Step 5:** Locate the chromedriver.exe from the folder to a place on your machine. I copied chromedriver and pasted it in the C:\Program Files\Google\Chrome\Application. Also, don't forget to add path to the Environment Variables, as C:\Program Files\Google\Chrome path, under System Variables -> Path.




