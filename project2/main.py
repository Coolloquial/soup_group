import config as cfg
import zid_project2 as zp


def part1(df):
    stock_returns_df = zp.mk_ret_df(df)
    max_return = zp.get_avg(stock_returns_df, cfg.TICKERS[0], 2020)
    result = ''
    for ticker in cfg.TICKERS:
        temp = zp.get_avg(stock_returns_df, ticker, 2020)
        if temp > max_return:
            max_return = temp
            result = ticker

    return result

def part2(df):
    stock_returns_df = zp.mk_ret_df(df)
    result = zp.get_ann_ret(zp.get_ew_rets(stock_returns_df, cfg.TICKERS), "2010-01-01", "2020-12-31")
    return result

def part3(df, ticker_result):
    stock_returns_df = zp.mk_ret_df(df)
    highest_average_stock = stock_returns_df.loc[:, ticker_result]
    result = zp.get_ann_ret(highest_average_stock, "2010-01-01", "2020-12-31")
    return result

def part4(df, ticker_result):
    stock_returns_df = zp.mk_ret_df(df)
    stock_abnormal_returns_df = zp.mk_aret_df(stock_returns_df)
    highest_average_stock = stock_abnormal_returns_df.loc[:, ticker_result]
    result = zp.get_ann_ret(highest_average_stock, "2010-01-01", "2020-12-31")
    return result

if __name__ == "__main__":

    tickers_list = cfg.TICKERS
    df = zp.mk_prc_df(tickers_list, 'adj_close')
    ticker_result = part1(df)
    part2_result = part2(df)
    part3_result = part3(df, ticker_result)
    part4_result = part4(df, ticker_result)

    print("Q1 answer:", ticker_result)
    print("Q2 answer:", part2_result)
    print("Q3 answer:", part3_result)
    print("Q4 answer:", part4_result)

