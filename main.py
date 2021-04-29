# import pandas as pd
#
# # http://quotes.money.163.com/service/chddata.html?code=0000001&start=19900101&end=
#
#
# # 沪市前面加0，深市前面加1，比如0000001，是上证指数，1000001是中国平安
# def get_daily(code, start='19900101', end=''):
#     url_mod = "http://quotes.money.163.com/service/chddata.html?code=%s&start=%s&end=%s"
#     url = url_mod % (code, start, end)
#     df = pd.read_csv(url, encoding='gb2312')
#     return df
#
#
# df = get_daily('0000001')  # 获取上证指数
#
# print(df)
import pandas as pd
import matplotlib.pyplot as plt
import baostock as bs
#### 登陆系统 ####
lg = bs.login()

#### 获取历史K线数据 ####
# query_history_k_data()
fields= "date,code,open,high,low,close"
rs = bs.query_history_k_data("sh.000001", fields,
    start_date='2000-01-01', end_date='2018-09-07',
    frequency="d", adjustflag="2")
#frequency="d"取日k线，adjustflag="3"默认不复权，
#1：后复权；2：前复权

data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
result.index=pd.to_datetime(result.date)
#### 结果集输出到csv文件 ####
#result.to_csv("c:/zjy/history_k_data.csv",
#        encoding="gbk", index=False)
result.head()
#### 登出系统 ####
#bs.logout()

result.info()

#将某些object转化numeric
result=result.apply(pd.to_numeric, errors='ignore')
result.info()

result.close.plot(figsize=(16,8))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()