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
                print(time.get_attribute("innerText") , self.info.time)
                if time.get_attribute("innerText")[:-1] == self.info.time:
                    time.click()
                    flag=1
                    break
            if flag:
                sleep(0.1)
                self.enter()
            else:
                sleep(0.1)
                self.time()
  
        except exceptions.StaleElementReferenceException as e:
            sleep(0.1)
            print("time error")
            self.time()

    def enter(self):
        try:
            enter = self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/div/a[1]")[0].click()
            self.formin()
        except exceptions.StaleElementReferenceException as e:
            sleep(0.1)
            print("enter element error")
            self.enter()
        except exceptions.ElementClickInterceptedException as e:
            sleep(0.1)
            print("enter click error")
            self.enter()
    
    def formin(self):
        try:
            self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[6]/td/input")[0].send_keys(self.info.name)

            self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[7]/td/input[1]")[0].send_keys(self.info.phonenum[:4])
            self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[7]/td/input[2]")[0].send_keys(self.info.phonenum[4:])
 
            #people num
            self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[8]/td/select/option[3]")[0].click()
            #spam
            spam = self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[12]/td/span[1]")[0].text
            self.driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[12]/td/input[1]")[0].send_keys(spam)
            
            #agreeterm
            self.driver.find_elements_by_xpath("//*[@id=\"rev_agree\"]/input[1]")[0].click()

            self.driver.find_elements_by_xpath("//*[@id=\"but_exe\"]")[0].click()
        except exceptions.StaleElementReferenceException as e:
            sleep(0.1)
            print("form error")
            self.formin()
        except IndexError as e:
            sleep(0.1)
            print("index error")
            while True:
                pass
        except AttributeError as e:
            sleep(0.1)
            print("Attribute error")



if __name__ == '__main__':
    data = input("기존 데이터 사용? 예: 1 아니요 : 0 \n 입력 : ")
    MyInfo = BookInfo(data)
    robot = KeyEscape(MyInfo)
    robot.control()

    while True:
        pass