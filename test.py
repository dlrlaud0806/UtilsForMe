from enum import Flag
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
# import re
# import time
from BookInfo import BookInfo

import datetime

now = datetime.datetime.today()
nowmonth = now.month

#사용자 정보 저장 class


class KeyEscape:
    def __init__(self, info):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.info = info
        self.driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", options=options)
    def control(self):
        self.driver.get("https://keyescape.co.kr/web/home.php?go=rev.make")
        # self.wait = WebDriverWait(self.driver, 100)
        self.zizum()

    def zizum(self):
        xpath = "//*[@id=\"zizum_data\"]/a[%c]/li" %self.info.zizum
        try:
            elm = self.driver.find_elements_by_xpath(xpath)
            elm[0].click()
            sleep(0.2)
            self.month()
  
        except exceptions.StaleElementReferenceException as e:
            sleep(0.1)
            print("zizum error")
            self.zizum()
    
    def month(self):
        if int(self.info.month) > nowmonth:
            try:
                xpath = "//*[@id=\"calendar_data\"]/div/li[3]/a/img"
                elm = self.driver.find_elements_by_xpath(xpath)
                elm[0].click()
                sleep(0.2)
                self.day()
  
            except exceptions.StaleElementReferenceException as e:
                sleep(0.1)
                print("month error")
                self.month()
        else:
            self.day()

    def day(self):
        try:
            flag=0
            dates = self.driver.find_elements_by_xpath("//*[@id=\"calendar_data\"]/table/tbody/tr/td/a") #일
            for date in dates:
                if date.get_attribute("innerText") == self.info.date:
                    date.click()
                    flag=1
                    break
            if flag:
                self.theme()
            else:
                sleep(0.1)
                self.day()

        except exceptions.StaleElementReferenceException as e:
            sleep(0.1)
            print("day error")
            self.day()

    def theme(self):
        xpath = "//*[@id=\"theme_data\"]/a[%c]/li" %self.info.theme
        try:
            elm = self.driver.find_elements_by_xpath(xpath)
            elm[0].click()
            sleep(0.2)
            self.time()
  
        except exceptions.StaleElementReferenceException as e:
            sleep(0.2)
            print("theme error", e)
            self.theme()
    
    def time(self):
        flag=0
        xpath = "//*[@id=\"theme_time_data\"]/a/li"
        try:
            times = self.driver.find_elements_by_xpath(xpath)
            for time in times:
                print(time.get_attribute("innerText"))
                if time.get_attribute("innerText") == self.info.time:
                    time.click()
                    flag=1
                    break
            if flag:
                self.submit()
            else:
                self.time()
  
        except exceptions.StaleElementReferenceException as e:
            sleep(0.1)
            print("time error")
            self.time()

if __name__ == '__main__':
    data = input("기존 데이터 사용? 예: 1 아니요 : 0 \n 입력 : ")
    MyInfo = BookInfo(data)
    robot = KeyEscape(MyInfo)
    robot.control()

    while True:
        pass