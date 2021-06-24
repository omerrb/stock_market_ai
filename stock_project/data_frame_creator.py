import time
from urllib import request as us_req
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

stocks_symbol = {"s&p": "%5EGSPC"}
                 # "nasdaq": "%5EIXIC",
                 # "bitcoin": "BTC-USD"}
base_url = f"https://finance.yahoo.com/quote/"
date_range = f"/history?period1=1464739200&period2=1622505600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
driver = None
stocks_data = {}


def loading_page(url):
    try:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(30)
        driver.get(url)
        eop = driver.find_element_by_xpath('//span[contains(text(),"Close price adjusted for splits")]')
        for x in range(50):
            driver.execute_script("arguments[0].scrollIntoView();", eop)
            time.sleep(0.5)
    except Exception as ex:
        print("*** error:", ex)
    finally:
        driver.close()


def create_df():
    for stock in stocks_symbol:
        url = base_url + stocks_symbol[stock] + date_range
        loading_page(url)
        page = us_req.urlopen(url)
        soup = BeautifulSoup(page, "lxml")
        right_table = soup.find_all('table', class_='W(100%) M(0)')
        columns = {"date": [],
                  f"{stock}_open": [],
                  f"{stock}_high": [],
                  f"{stock}_low": [],
                  f"{stock}_close": [],
                  f"{stock}_adj": [],
                  f"{stock}_volume": []}
        for row in right_table[0].findAll('tr'):
            cells = row.findAll('td')
            if len(cells) == 7:
                for column, num in zip(columns, range(len(columns))):
                    columns[column].append(cells[num].find(text=True))
        stocks_data.update(columns)
    df = pd.DataFrame(data=stocks_data)
    return df

