import praw
import re
import requests
import os
import random
import ctypes
import sys
from PIL import Image


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
)

def clear_temp(dir="temp_data"):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

def get_image(subreddit="wallpaper", limit=30, time_filter="week", dir="temp_data"):
    subreddit = reddit.subreddit(subreddit)
    posts = subreddit.top(time_filter = time_filter,limit=limit)

    for post in posts:
        
        url = (post.url)
        if "https://v.redd.it" in url:
            break
        file_name = url.split("/")

        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        file_name = file_name[-1]

        if "." not in file_name:
            file_name += ".jpg"

        r = requests.get(url)
        if ".gif" not in file_name:
            with open(f"{dir}/{file_name}","wb") as f:
                f.write(r.content)

def test_image(file):
    try:
        im=Image.open(file)
        im.verify()
        return "valid"
    except Exception:
        return "invalid"

def set_wallpaper():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    img = random.choice(os.listdir("temp_data"))

    attempts = 0
    while test_image(f"{path}\\temp_data\\{img}") == "invalid":
        img = random.choice(os.listdir("temp_data"))
        attempts += 1
        if attempts > 100:
            break
    if test_image(f"{path}\\temp_data\\{img}") == "valid":
        SPI_SETDESKWALLPAPER = 20  
        SPIF_UPDATEINIFILE = 0 # Writes the new system-wide parameter setting to the user profile.
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, f"{path}\\temp_data\\{img}", SPIF_UPDATEINIFILE)

clear_temp()
# nur get_image(), wenn keine dateien in temp sind, oder dateien älter als x minuten sind x = variable für config
get_image(subreddit="wallpaper")
set_wallpaper()
