import pyautogui as pg
from bs4 import BeautifulSoup
import requests
import re
from pygame import mixer
import time
from selenium import webdriver
from urllib.parse import quote
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
import webbrowser as web

# Data entry
coin = input('coin is:')
limit = input('limit is:')
limit = float(limit)
slop = input('Please select your desired slope with less and more:')
number_phone = input("Enter your phone number without zero:")
alarm = input("Do you want to use the alarm?(y/n)")
number_phone = "+98" + number_phone
now = datetime.now() + timedelta(minutes=2)
hour = now.hour
minute = now.minute 
volum = 50
my_music_file = "Data/beautiful_spring_melody (online-audio-converter.com).wav"

def prnt_sleeptm():
    return sleeptm

def sendwhatmsg(phone_no, message, time_hour, time_min, wait_time=20, print_waitTime=True):
    '''Sends whatsapp message to a particulal number at given time
Phone number should be in string format not int
***This function will not work if the browser's window is minimised,
first check it by calling 'check_window()' function'''

    global sleeptm
    timehr = time_hour

    if time_hour not in range(0,25) or time_min not in range(0,60):
        print("Invalid time format")
    
    if time_hour == 0:
        time_hour = 24
    callsec = (time_hour*3600)+(time_min*60)
    
    curr = time.localtime()
    currhr = curr.tm_hour
    currmin = curr.tm_min
    currsec = curr.tm_sec

    if currhr == 0:
        currhr = 24

    currtotsec = (currhr*3600)+(currmin*60)+(currsec)
    lefttm = callsec-currtotsec

    if lefttm <= 0:
        lefttm = 86400+lefttm
    
    date = "%s:%s:%s"%(curr.tm_mday,curr.tm_mon,curr.tm_year)
    time_write = "%s:%s"%(timehr,time_min)
    file = open("pywhatkit_dbs.txt","a",encoding='utf-8')
    file.write("Date: %s\nTime: %s\nPhone number: %s\nMessage: %s"%(date,time_write,phone_no,message))
    file.write("\n--------------------\n")
    file.close()
    sleeptm = lefttm-wait_time
    if print_waitTime :
        print(f"In {prnt_sleeptm()} seconds web.whatsapp.com will open and after {wait_time} seconds message will be delivered")
    time.sleep(sleeptm)
    parsedMessage = quote(message)
    options = Options()
    options.add_argument("user-data-dir=Data/tarun")
    driver = webdriver.Chrome("Data/chromedriver", chrome_options=options)
    driver.maximize_window()
    driver.get('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(wait_time-2)
    pg.press('enter')

while True:
    website = requests.get('https://coinmarketcap.com/currencies/%s/' % coin)
    soup = BeautifulSoup(website.text, 'html.parser')
    price = soup.find('div', {"class": "priceValue___11gHJ"})
    price = price.text
    price = re.sub(r'\,', '', price)
    price = re.findall(r'\$(.*)', price)
    price = float(price[0])
    print(price)

    if slop == 'less':
        if price <= limit:
            if alarm == 'y':
                mixer.init()
                mixer.music.set_volume(volum)
                mixer.music.load(my_music_file)
                mixer.music.play(-1)
            sendwhatmsg(number_phone, "The price is less than specified. Buy !!!", hour, minute)
            break

    elif slop == 'more':
        if price >= limit:
            if alarm == 'y':
                mixer.init()
                mixer.music.set_volume(volum)
                mixer.music.load(my_music_file)
                mixer.music.play(-1)
            sendwhatmsg(number_phone, "The price is more than specified. Sell !!!", hour, minute)
            break

    time.sleep(300)
