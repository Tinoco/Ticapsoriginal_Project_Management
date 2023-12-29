# IMPORT BEAUTIFULSOUP TO READ WEB CONTENT
from bs4 import BeautifulSoup

# IMPORT OPERATIONAL SYSTEM LIB
import os

# IMPORT REQUESTS TO GET RESPONSES
import requests

# TQDM PROGRESS BAR
from tqdm import tqdm

# IDENTIFY LARGE XML FILE
import advertools as adv

# MAKE HTML T0 MARKDOWN PARSING
from markdownify import markdownify as md

# INDEXING YOUR LARGE SITEMAPS
sitemap = adv.sitemap_to_df("https://ticapsoriginal.com/static/sitemap15.xml")

# TYPE CASTING URL TO LIST
urls = sitemap["loc"].to_list()


# FUNCTION TO GET URL RESPONSES
def get_code(url) -> requests.Response:
    return requests.get(url)


# WALK ON ALL URLS
for item in tqdm(urls):
    urlg = (requests.get(item).text)
    mdcheck = md(urlg)
    clearitemname = str(item).replace("https://", "")
    clearitemname = clearitemname.replace(".", "")
    clearitemname = clearitemname.replace("/", "")
    f = open(clearitemname+".md", "x")
    f.write(str(mdcheck))
