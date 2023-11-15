
import os
import pandas as pd
import config as cfg
import zid_project2 as zp


def part1(df):
    stock_returns_df = zp.mk_ret_df(df)
    max_return = zp.get_avg(stock_returns_df, cfg.TICMAP.keys()[0], 2020)
    result = ''
    for ticker in cfg.TICMAP.keys():
        temp = zp.get_avg(stock_returns_df, ticker, 2020)
        if temp > max_return:
            max_return = temp
            result = ticker

    return result

def part2(df):
    stock_returns_df = zp.mk_ret_df(df)
    result = zp.get_ann_rets(zp.get_ew_rets(stock_returns_df, cfg.TICMAP.keys()), "2010-01-01", "2020-12-31")
    return result

def part3(df, ticker_result):
    stock_returns_df = zp.mk_ret_df(df)
    highest_average_stock = stock_returns_df.loc[:, ticker_result]
    result = zp.get_ann_rets(highest_average_stock, "2010-01-01", "2020-12-31")
    return result

def part4(df, ticker_result):
    stock_returns_df = zp.mk_ret_df(df)
    stock_abnormal_returns_df = zp.mk_aret_df(stock_returns_df)
    highest_average_stock = stock_abnormal_returns_df.loc[:, ticker_result]
    result = zp.get_ann_rets(highest_average_stock, "2010-01-01", "2020-12-31")
    return result

if __name__ == "__main__":

    ticker_result = part1(df)
    part2_result = part2(df)
    part3_result = part3(df, ticker_result)
    part4_result = part4(df, ticker_result)

    print(ticker_result)
    print(part2_result)
    print(part3_result)
    print(part4_result)