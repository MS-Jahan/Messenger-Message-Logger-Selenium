import pickle
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")

browser = webdriver.Chrome(executable_path = "./chromedriver", options=chrome_options)
#chrome_options.add_argument("user-data-dir=chrome-data")

browser.get('https://m.facebook.com/messages')

prev = ''
curr = ''
title = ''
sender = ''
time.sleep(5)
print("Script Started!\n\n")
while 1:
    try:
        sender = browser.find_element_by_xpath('//*[@id="threadlist_rows"]/div[1]/div[1]/div[2]/div/header/h3').text
        msg = browser.find_element_by_xpath('//*[@id="threadlist_rows"]/div[1]/div[1]/div[2]/div/header/span').text
    except:
        # If there is a new message
        sender = browser.find_element_by_xpath('//*[@id="threadlist_rows"]/div[1]/a/div/div[2]/div[1]').text
        sender = sender[:-4]
        msg = browser.find_element_by_xpath('//*[@id="threadlist_rows"]/div[1]/a/div/div[2]/div[2]').text

    
    #print(msg)
    curr = msg
    if curr != prev:
        print(sender + ": " + curr)
        with open('messages.txt', 'a+') as msg:
            msg.write(sender + ": " + curr + "\n\n")
    prev = curr
    time.sleep(1)
