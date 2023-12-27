# TQDM PROGRESS BAR
from tqdm import tqdm

# IDENTIFY LARGE XML FILE
import advertools as adv

# PANDAS LIBRARY
import pandas as pd

# TIME FOR AWAITING
import time

# REQUEST TO GET RESPONSES
import requests

# GENERATE AND INPUT YOUT INDEXNOW KEY ( https://www.bing.com/indexnow )
key = '8888888888888888888888888'

# DEFINE SEARCH ENGINES MIRROS
# SEZNAM LINK https://www.seznam.cz
# BING LINK https://www.bing.com
# YANDEX LINK https://www.yandex.com

# INDEXING YOUR LARGE SITEMAPS
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemaps2.xml")

# TYPE CASTING
urls = sitemap["loc"].to_list()


def response():
    r = requests.post(
                     "https://bing.com",
                     data=data,
                     headers=headers
                     )
    return r


def await_new():
    print("AWAITING TO NEW REQUEST")
    time.sleep(10)
    r = response()
    print(r.status_code)


for item in tqdm(urls):
    data = {"host": "www.bing.com",
            "key": key,
            "urlList": item
            }
    try:
        headers = {
                "Content-type": "application/json", "charset": "utf-8"
                  }
        r = response()
        print(r.status_code)
        if r.status_code == 200:
            print(item)
        elif r.status_code != 200:
            await_new()
    except SomeException as error:
        await_new()
        continue
