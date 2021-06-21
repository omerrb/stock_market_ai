import json
import datetime
import pandas as pd
import numpy as np
from time import strptime


def remove_duplicatives(df):
    return df.drop_duplicates(subset=['date'], keep='first')


def convert_datetime_sec(df):
    for date_tweet in df.date:
        old_date = date_tweet
        split_date = old_date.split(" ")
        if hasattr(df, 's&p_open'):
            m = strptime(split_date[0], '%b').tm_mon
            d = split_date[1][:2]
            y = split_date[2]
        elif hasattr(df, 'Trump_Tweet'):
            y = int(split_date[2]) + 2000
            d = split_date[0]
            m = strptime(split_date[1], '%b').tm_mon
        else:
            d = split_date[2]
            y = split_date[5]
            m = strptime(split_date[1], '%b').tm_mon
        if m < 10:
            m = f"0{m}"
        df.loc[df.date == date_tweet, 'date'] = datetime.datetime(int(y), int(m), int(d), 0, 0).strftime('%s')
    return df


def convert_str_to_num(df):
    for column in df.columns:
        if column == 'date':
            continue
        for row in df[column]:
            new_value = row.replace(",", "")
            df.loc[df[column] == row, column] = float(new_value)
    return df


def compare_dates_df_stock(stock_df, dates):
    is_exist_column = []
    for stock_date in stock_df.date:
        flag = False
        for date in dates:
            if stock_date == date:
                flag = True
                break
        if flag:
            is_exist_column.append(1)
        else:
            is_exist_column.append(0)
    return is_exist_column

def create_holidays_date():
    holidays = []
    dates = []
    with open('holidays.json') as json_file:
        data = json.load(json_file)
    for holiday in data:
        holidays.extend(data[holiday])
    for day in holidays:
        split_date = day.split("-")
        m = split_date[1]
        d = split_date[0]
        y = split_date[2]
        dates.append(datetime.datetime(int(y), int(m), int(d), 0, 0).strftime('%s'))
    data = np.array(dates)
    return pd.Series(data)


