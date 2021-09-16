from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()  # 크롬 옵션 객체 생성
    options.add_argument('headless')  # 창 없이
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # 속도 향상을 위한 옵션 해제
    # prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2,
    #                                                     'geolocation': 2, 'notifications': 2,
    #                                                     'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2,
    #                                                     'mixed_script': 2, 'media_stream': 2, 'media_stream_mic': 2,
    #                                                     'media_stream_camera': 2, 'protocol_handlers': 2,
    #                                                     'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
    #                                                     'push_messaging': 2, 'ssl_cert_decisions': 2,
    #                                                     'metro_switch_to_desktop': 2, 'protected_media_identifier': 2,
    #                                                     'app_banner': 2, 'site_engagement': 2, 'durable_storage': 2}}
    # options.add_experimental_option('prefs', prefs)
    #driver_time = driver = webdriver.Chrome(executable_path="c:/chromedriver.exe", options=options)

    name = "이기명"
    phonenum = "90611814"
    resmonth = 9
    resdate = "9"
    driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
    url = 'https://keyescape.co.kr/web/home.php?go=rev.make'
    driver.get(url)
    test = True

    if not test :
        #네이비즘 시간 연동
        driver_time = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", options=options)
        driver_time.get("https://time.navyism.com/?host=keyescape.co.kr")
        wait = WebDriverWait(driver_time, 100)
        wait.until(EC.element_to_be_clickable((By.ID, "msec_check"))).click()

        print("wait till 12:00")
        while True:
            a = driver_time.find_element_by_id('time_area').text
            b = driver_time.find_element_by_id('msec_area').text

            print (a)
            times = re.findall("[0-9]+", a)
            i = 1

            if(times[4]=='59' and times[5]=='59'): # 분, 초
                msec = re.findall("[0-9]+", b)
                if(int(msec[0])>=900):
                    break

    # driver_time.close()
    
    wait = WebDriverWait(driver, 100)
    driver.refresh() 
  
    # zizum = wait.until(EC.element_to_be_clickable((By.XPATH, "// *[ @ id = \"zizum_data\"] / a[1] / li"))).click() #지점
    # print("zizum clicked")
    # wait = WebDriverWait(driver, 10)
    
    
    time.sleep(0.5)


    #######change month
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"calendar_data\"]/div/li[3]/a/img"))).click()
    # wait = WebDriverWait(driver, 10)
    # time.sleep(0.1)

    #have to change date
    dates = driver.find_elements_by_xpath("//*[@id=\"calendar_data\"]/table/tbody/tr/td/a") #일
    for date in dates:
        print(type(date.get_attribute("innerText")))
        if date.get_attribute("innerText") == resdate:
            date.click()
            break

    wait = WebDriverWait(driver, 10)
    print("date clicked")
    time.sleep(0.5)
    
    #theme select
    theme = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"theme_data\"]/a/li"))).click() # US
    #theme = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"theme_data\"]/a[3]/li"))).click()  # 고백
    wait = WebDriverWait(driver, 10)
    print("theme clicked")
    time.sleep(0.5)

    #time select
    wait = WebDriverWait(driver, 10)
    time = wait.until(EC.element_to_be_clickable((By.XPATH, "// *[ @ id = \"theme_time_data\"] / a[8] / li"))).click() #타임
    print("time clicked")
    
    enter = driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/div/a[1]")[0].click()
    
    #name
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"contents\"]/div/div/form/table/tbody/tr[5]/td/input"))).send_keys(name)
    
    #phone have to split
    driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[6]/td/input[1]")[0].send_keys(phonenum[:4])
    driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[6]/td/input[2]")[0].send_keys(phonenum[4:])
    
    #people num
    man4 = driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[7]/td/select/option[3]")[0].click()
    
    #spam
    spam = driver.find_elements_by_xpath("// *[ @ id = \"contents\"] / div / div / form / table / tbody / tr[11] / td / span[1]")[0].text
    print(spam)
    driver.find_elements_by_xpath("//*[@id=\"contents\"]/div/div/form/table/tbody/tr[11]/td/input[1]")[0].send_keys(spam)
    
    #agreeterm
    driver.find_elements_by_xpath("//*[@id=\"rev_agree\"]/input[1]")[0].click()

    # enter = driver.find_elements_by_xpath("//*[@id="but_exe"]")[0].click()

    while True:
        pass