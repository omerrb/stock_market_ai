from data_frame_creator import create_df
from tweets import get_trump_tweets, get_elon_tweets
from data_handling import (
    create_holidays_date,
    remove_duplicatives,
    convert_datetime_sec,
    convert_str_to_num,
    compare_dates_df_stock
)

holidays = create_holidays_date()
stock_df = create_df()
new_stock = remove_duplicatives(stock_df)
new_stock = new_stock.reset_index(drop=True)
new_stock = convert_datetime_sec(new_stock)
new_stock = convert_str_to_num(new_stock)
trump = get_trump_tweets()
new_trump = remove_duplicatives(trump)
new_trump = new_trump.reset_index(drop=True)
new_trump = convert_datetime_sec(new_trump)
elon = get_elon_tweets()
new_elon = remove_duplicatives(elon)
new_elon = new_elon.reset_index(drop=True)
new_elon = convert_datetime_sec(new_elon)
new_column = compare_dates_df_stock(new_stock, new_trump.date)
new_stock["is_trump_tweet"] = new_column
new_column = compare_dates_df_stock(new_stock, new_elon.date)
new_stock["is_elon_tweet"] = new_column
new_column = compare_dates_df_stock(new_stock, holidays)
new_stock["is_holiday"] = new_column

print(new_stock)