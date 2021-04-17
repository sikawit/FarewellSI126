#import libraries
from selenium import webdriver
import time
import datetime
import pandas as pd

def automate_sender(
    driverpath : str = "Path to your driver",
    sender_df_path : str = "si126_namelist.csv",
    sender_file_path : str = "sender.txt",
    greeting_file_path : str = "greeting.txt",
    in_production : bool = False
    ):

    """
    if you want to run this code in production mode, please toggle in_production to True
    """

    # load data from csv file
    df = pd.read_csv(sender_df_path)
    urllist = list(df[(df.friend_group == "GSX")].formlink)
    num_letters = len(urllist)

    print(f"This script will send {num_letters} letter(s)")

    with open(sender_file_path, 'r') as sender_file:
        sender_txt = f"{sender_file.read()}".format(**locals()).strip()

    # sending mail merge
    for i in range(len(urllist)):
        # rest time from previous session
        driver = webdriver.Chrome(driverpath)
        time.sleep(1)

        sending_url = driver.get(urllist[i])
        
        # Find Name base on Google Form's title
        titlename = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[1]/div/div[2]/div').text
        # Mirror to P'NAME NNN, split by space then choose 2nd elem, w/o "P'", w/o ()
        receiver = titlename.split(' ')[2].replace("P'","").replace('(', '').replace(')', '').strip()
        receiver_code = titlename.split(' ')[3].strip()

        now = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S UTC%Z")

        with open(greeting_file_path, 'r') as greeting_file:
            greeting_txt = f"{greeting_file.read()}".format(**locals()).strip()

        time.sleep(2)

        sender_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        sender_fill.send_keys(sender_txt)

        greeting_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
        greeting_fill.send_keys(greeting_txt)

        if (in_production):
            submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
            submit.click()

        time.sleep(2)

        driver.close()

        print(f"({i+1}/{num_letters}) Letter to {receiver}:{receiver_code} is sent!")

    print("*********************")
    print("ALL LETTERS ARE SENT!")
    print("*********************")

    return

if __name__ == "__main__" :
    automate_sender(in_production=True)