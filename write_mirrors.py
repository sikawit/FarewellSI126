#import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pandas as pd

#path for webdriver
driverpath = "/Users/sikawit/OneDrive/_code/chromedriver"

#load data from csv file
df = pd.read_csv("si126_namelist.csv")
urllist = list(df[df.GSX == True].formlink)
namelist = list(df[df.GSX == True].nickname)


#sending mail merge

for i in range(len(urllist)):
    #rest time from previous session
    driver = webdriver.Chrome(driverpath)
    time.sleep(3)

    sending_url = driver.get(urllist[i])
    send_to = namelist[i]

    time.sleep(1)

    sender_txt = "@sikawit"
    greeting_txt = f"""Hi {send_to.strip()}! 

ยินดีด้วยครับคุณหมอ ในที่สุดก็เดินทางมาถึงเส้นชัยที่ยากที่สุดทางหนึ่งละครับ (ซึ่งผมขอหนีไปก่อน 555) ขอให้หมอเป็นหมอที่ดีครับ หวังว่าคงได้เจอกัน (คงไม่ใช่ในฐานะคนไข้นะ) หากมีอะไรที่ให้ช่วยได้ก็บอกมาได้ครัชช

ยินดีอีกครั้งครับ
Sake

*****
Generated from a bot on {datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S UTC%Z")}
Find out more at https://github.com/sikawit/FarewellSI126"""

    sender_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    sender_fill.send_keys(sender_txt)

    greeting_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    greeting_fill.send_keys(greeting_txt)

    submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
    submit.click()

    time.sleep(3)

    driver.close()


