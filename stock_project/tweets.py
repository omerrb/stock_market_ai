import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from twython import Twython
import pandas as pd


def get_elon_tweets():
    twitter = Twython("6XIS09lokX8e03iMkf9ob6B9v", "z5zsGfH0E27ATssf70028AgdDSKURTszlR5f4NAaSlRbeBabJg")
    elon_result = twitter.get_user_timeline(screen_name="elonmusk", count=200)
    elon_Dates = []
    elon_favorites = []
    elon_tweets = []
    elon_texts = []
    for status in elon_result:
        elon_Dates.append(status["created_at"])
        elon_favorites.append(status["favorite_count"])
        elon_tweets.append(status["retweet_count"])
        elon_texts.append(status["text"])

    elon_stats = pd.DataFrame(
        {
        "date" : elon_Dates,
        "Elon_Like": elon_favorites,
        "Elon_Tweet": elon_tweets,
        "Elon_Text": elon_texts,
        })

    elon_stats = elon_stats.reset_index(drop=True)
    return elon_stats


def get_trump_tweets():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(f"https://www.bloomberg.com/features/trump-tweets-market")
    try:
        checkbox = driver.find_element_by_id("recaptcha-anchor")
        checkbox.click()
        time.sleep(10)
    except Exception:
        pass

    trump_dates = []
    trump_text = []
    tweets = driver.find_elements_by_class_name("phone__tweet")
    for tweet in tweets:
        elements = tweet.find_elements_by_tag_name("p")
        trump_dates.append(elements[2].text[2:])
        trump_text.append(elements[3].text)

    trump_stats = pd.DataFrame(
        {
        "date" : trump_dates,
        "Trump_Tweet": trump_text,
        })

    driver.close()
    return trump_stats