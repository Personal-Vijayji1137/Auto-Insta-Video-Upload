from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import yt_dlp
import time
import os
import json
import re

driver_path = "C://Program Files//Google//Chrome//Application//chrome.exe"  # Update this path to match your driver location
profile_path = "C://Users//perso//AppData//Local//Google//Chrome//User Data"  # Update this path
profile_name = "Profile 2"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
service = Service(driver_path)
chrome_options.use_chromium = True
driver = webdriver.Chrome(service=service, options=chrome_options)

videos_folder = os.path.join(os.getcwd(), "videos")
os.makedirs(videos_folder, exist_ok=True)

json_file_path = os.path.join(os.getcwd(), 'data.json')
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = []

for i in range(1000):
    driver.get("https://www.youtube.com/shorts")
    time.sleep(10)
    video_url = driver.current_url
    video_id_match = re.search(r"\/shorts\/([a-zA-Z0-9_-]+)", video_url)
    if video_id_match:
        video_id = video_id_match.group(1)
    else:
        continue
    if any(video['id'] == video_id for video in existing_data):
        continue
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(videos_folder, f"{video_id}.mp4"),
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        title = info_dict.get('title', None)
        output_file = os.path.join(videos_folder, f"{video_id}.mp4")
        ydl.download([video_url])
        video_metadata = {
            'id': video_id,
            'title': title,
            'path': output_file
        }
        existing_data.append(video_metadata)
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
    time.sleep(2)
time.sleep(10)
driver.quit()