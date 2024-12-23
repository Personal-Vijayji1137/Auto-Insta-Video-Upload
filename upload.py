from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
import os
import json
import re
driver_path = "C://Program Files//Google//Chrome//Application//chrome.exe"  # Update this path to match your driver location
profile_path = "C://Users//perso//AppData//Local//Google//Chrome//User Data"  # Update this path
profile_name = "Profile 19"

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.arguments.append(f"--user-data-dir={profile_path}")
chrome_options.arguments.append(f"--profile-directory={profile_name}")
chrome_options.add_argument("--start-fullscreen")

# Initialize the browser
service = Service(driver_path)
chrome_options.use_chromium = True
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.instagram.com/")
# while True:
for i in range(20):
    json_file_path = os.path.join(os.getcwd(), 'data.json')
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
        if not existing_data:
            break
    else:
        break
    data = existing_data[0]
    video_path = data.get("path")
    caption = data.get("title")
    create_button = driver.find_element(By.XPATH, "//span[contains(text(),'Create')]")
    create_button.click()

    time.sleep(2)

    post_button = driver.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1 xn3w4p2']//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']")
    post_button.click()
    time.sleep(2)
    file_input = driver.find_element(By.CLASS_NAME, "_ac69")
    file_input.send_keys(video_path)

    time.sleep(10)

    Reel_button = driver.find_element(By.XPATH, "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1']//div//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1y1aw1k x1sxyh0 xwib8y2 xurb0ha x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k']//*[name()='svg']")
    Reel_button.click()

    time.sleep(2)

    Reel_button = driver.find_element(By.XPATH, "//span[normalize-space()='Original']")
    Reel_button.click()

    time.sleep(5)
    Next_button = driver.find_element(By.XPATH, "//div[contains(text(),'Next')]")
    Next_button.click()

    time.sleep(2)
    Next_button = driver.find_element(By.XPATH, "//div[contains(text(),'Next')]")
    Next_button.click()

    time.sleep(2)
    pyperclip.copy(caption)
    time.sleep(2)

    text_input_button = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r']")
    text_input_button.click()
    text_input_button.send_keys(Keys.CONTROL + 'v')
    time.sleep(2)

    Share_button = driver.find_element(By.XPATH, "//div[contains(text(),'Share')]")
    Share_button.click()

    element = WebDriverWait(driver, 180).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x1ms8i2q xo1l8bm x5n08af x2b8uid x4zkp8e xw06pyt x10wh9bi x1wdrske x8viiok x18hxmgj']"))
    )

    time.sleep(2)
    close_button = driver.find_element(By.XPATH, "//div[@class='x160vmok x10l6tqk x1eu8d0j x1vjfegm']//div[@role='button']")
    close_button.click()
    time.sleep(5)
    existing_data.pop(0)
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, indent=4, ensure_ascii=False)
driver.quit()