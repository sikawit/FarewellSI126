#import libraries
from selenium import webdriver
import time
import datetime
import pandas as pd

def automate_sender(
    driverpath : str = "Path to chromedriver",
    sender_file_path : str = "sender.txt",
    sender_df_path : str = "mdcu71_namelist.csv",
    greeting_file_path : str = "greeting_mdcu.txt",
    in_production : bool = False
    ):

    """
    if you want to run this code in production mode, please toggle in_production to True
    """

    df = pd.read_csv(sender_df_path)
    mdcu_list = list(df.mdcu_name)
    
    num_letters = len(mdcu_list)
    letter_text = "letters"
    if(num_letters == 1):
        letter_text = "letter"

    mdcu_url = "https://docs.google.com/forms/d/e/1FAIpQLSe4W2RxromJwtqCq8ZzGvgHr6Zy6Bfm44nzcgDlgZeBuZfBGQ/viewform"

    if(not in_production):
        print("You are in the TEST mode.")
    print(f"This script will send {num_letters} {letter_text}.")
    

    with open(sender_file_path, 'r') as sender_file:
        sender_txt = f"{sender_file.read()}".format(**locals()).strip()

    # sending mail merge
    for i in range(len(mdcu_list)):
        # rest time from previous session
        driver = webdriver.Chrome(driverpath)
        time.sleep(1)

        sending_url = driver.get(mdcu_url)
        
        receiver = mdcu_list[i]

        now = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S UTC%Z")

        with open(greeting_file_path, 'r') as greeting_file:
            greeting_txt = f"{greeting_file.read()}".format(**locals()).strip()

        time.sleep(2)

        receiver_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        receiver_fill.send_keys(receiver)

        sender_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        sender_fill.send_keys(sender_txt)

        greeting_fill = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        greeting_fill.send_keys(greeting_txt)

        if (in_production):
            submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
            submit.click()

        time.sleep(2)

        driver.close()

        print(f"({i+1}/{num_letters}) Letter to {receiver} is sent!")

    print("*********************")
    print("ALL LETTERS ARE SENT!")
    print("*********************")

    return

if __name__ == "__main__" :
    automate_sender(in_production=True)