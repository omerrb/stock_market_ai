import bs4
from bs4 import BeautifulSoup
import pandas as pd
import scipy as sc
import numpy as np
import requests


def load_soup_object(page_link):
    r = requests.get(page_link)
    soup = BeautifulSoup(r.content, features="html.parser")
    return soup

sp_url = "https://finance.yahoo.com/quote/%5EGSPC/history?period1=1262476800&period2=1620000000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
r = load_soup_object(sp_url)
print(r.prettify())
# ul = r.find(id="market-summary")
# item = ul.find_all('a', href=True, text=True)
# symbol = [i.text for i in item]
# for i in item:
#     print(i.text)
#     print(i['href'])
#     new_page = load_soup_object(main_url + i['href'])
#     print(new_page.prettify())
#     break




