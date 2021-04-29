import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import matplotlib.pyplot as plt
import os
import bs4 as bs
import requests
import pickle


stocks = {}
err_lists = []


def GetHuStock():
    res = requests.get('https://www.banban.cn/gupiao/list_sz.html')
    res.encoding = res.apparent_encoding
    soup = bs.BeautifulSoup(res.text, 'lxml')
    content = soup.find('div', {'class': 'u-postcontent cz'})
    for item in content.findAll('a'):
        now = item.text
        arr = now.split('(')
        stock_name = arr[0]
        stock_code = arr[1][:-1]+'.sz'
        if stock_name[0] == '*':
            stock_name = '_'+stock_name[1:]
        stocks[stock_code] = stock_name
    # with open('SH_Stock.pickle', 'wb') as f:
    #     pickle.dump(result, f)


def GetStockFromYahoo(isHaveStockCode=False):
    if not isHaveStockCode:
        GetHuStock()
    # with open('SH_Stock.pickle', 'rb') as f:
    #     stocks = pickle.load(f, encoding='gb2312')
    if not os.path.exists('SZ_Stock'):
        os.makedirs('SZ_Stock')

    stock_codes = stocks.keys()
    for stock_code in stock_codes:
        stock_name = stocks[stock_code]
        if os.path.exists('SZ_Stock/{}.csv'.format(stock_name+stock_code)):
            print('已下载')
        else:
            DownloadStock(stock_name, stock_code)
            print('下载{}中...'.format(stock_name))
    for err in err_lists:
        stocks.pop(err)
    with open('SZ_Stock.pickle', 'wb') as f:
        pickle.dump(stocks, f)


def DownloadStock(stock_name, stock_code):
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2021, 4, 8)
    try:
        df = web.DataReader(stock_code, 'yahoo', start, end)
    except Exception:
        print(stock_code)
        err_lists.append(stock_code)
        return
    df.to_csv('SZ_Stock/{}.csv'.format(stock_name+stock_code))


GetStockFromYahoo(False)
