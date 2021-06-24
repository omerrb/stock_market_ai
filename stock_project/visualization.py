import matplotlib.pyplot as plt
from data_frame_creator import create_df
from tweets import get_trump_tweets, get_elon_tweets
from data_handling import (
    create_holidays_date,
    remove_duplicatives,
    convert_datetime_sec,
    convert_str_to_num,
    compare_dates_df_stock
)

stock_df = create_df()
new_stock = remove_duplicatives(stock_df)
new_stock = new_stock.reset_index(drop=True)
new_stock = convert_datetime_sec(new_stock)
new_stock = convert_str_to_num(new_stock)
trump = get_trump_tweets()
new_trump = remove_duplicatives(trump)
new_trump = new_trump.reset_index(drop=True)
new_trump = convert_datetime_sec(new_trump)
new_column = compare_dates_df_stock(new_stock, new_trump.date)
new_stock["is_trump_tweet"] = new_column


def create_plot_to_all_stocks(new_stock):
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle("Market dimensions and events throughout 2016-2021", fontsize=36)
    markers_on = []
    for index, row in new_stock.iterrows():
        if row['is_trump_tweet'] == 1:
            markers_on.append(row['date'])
    print(len(markers_on))
    timeline_stock = new_stock.date.tolist()
    stock_data = new_stock['s&p_close'].tolist()
    #s&p
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.set_title('s&p')
    ax1.plot(timeline_stock, stock_data, '-gD', markevery=markers_on)
    ax1.set_xlabel('X Axis')
    ax1.set_ylabel('Y Axis')
    # plt.legend(["fine data", "failed data"])
    # #nasdaq
    # fig_y1 = fig.add_subplot(3, 1, 2)
    # fig_y1.set_title('nasdaq')
    # fig_y1.plot(timeline_fine, fine_data, markevery=markers_on)
    # fig_y1.xlabel("time (s)")
    # fig_y1.ylabel("degrees")
    # plt.legend(["fine data", "failed data"])
    # #bitcoin
    # fig_z1 = fig.add_subplot(3, 1, 3)
    # fig_z1.set_title('bitcoin')
    # fig_z1.plot(timeline_fine, fine_data, markevery=markers_on)
    # fig_z1.xlabel("time (s)")
    # fig_z1.ylabel("degrees")
    # plt.legend(["fine data", "failed data"])
    plt.show()


create_plot_to_all_stocks(new_stock)