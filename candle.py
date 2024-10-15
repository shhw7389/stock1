import requests
import os
import util
from datetime import datetime

# 东方财富网网页请求头
request_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}




# 获取股票、债券、期货、基金历史K线数据
def web_data(code, start='19000101', end=None, freq='d', fqt=1):
    """
    获取股票、指数、债券、期货、基金等历史K线行情
    code可以是股票或指数（包括美股港股等）代码或简称
    start和end为起始和结束日期，年月日
    freq:时间频率，默认日，1 : 分钟；5 : 5 分钟；15 : 15 分钟；30 : 30 分钟；
    60 : 60 分钟；101或'D'或'd'：日；102或‘w’或'W'：周; 103或'm'或'M': 月
    注意1分钟只能获取最近5个交易日一分钟数据
    fqt:复权类型，0：不复权，1：前复权；2：后复权，默认前复权
    """
    if end in [None,'']:
        end=str(datetime.fromtimestamp(int(open('./synctime.txt').read())))[:10]
    if freq == 1:
        return get_1min_data(code)
    start = ''.join(start.split('-'))
    end = ''.join(end.split('-'))
    if type(freq) == str:
        freq = freq.lower()
        if freq == 'd':
            freq = 101
        elif freq == 'w':
            freq = 102
        elif freq == 'm':
            freq = 103
        else:
            print('时间频率输入有误')
    kline_field = {
        'f51': '日期',
        'f52': '开盘',
        'f53': '收盘',
        'f54': '最高',
        'f55': '最低',
        'f56': '成交量',
        'f57': '成交额',
        'f58': '振幅',
        'f59': '涨跌幅',
        'f60': '涨跌额',
        'f61': '换手率'}
    fields = list(kline_field.keys())
    columns = list(kline_field.values())
    #cols1 = ['日期', '名称', '代码', '开盘', '最高', '最低', '收盘', '成交量', '成交额', '换手率']
    #cols2 = ['date', 'name', 'code', 'open', 'high', 'low', 'close', 'volume', 'turnover', 'turnover_rate']
    fields2 = ",".join(fields)
    code_id = util.get_code_id(code)
    params = (
        ('fields1', 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13'),
        ('fields2', fields2),
        ('beg', start),
        ('end', end),
        ('rtntype', '6'),
        ('secid', code_id),
        ('klt', f'{freq}'),
        ('fqt', f'{fqt}'),
    )

    url = 'https://push2his.eastmoney.com/api/qt/stock/kline/get'
    # 多线程装饰器

    json_response = requests.get(
        url, headers=request_header, params=params).json()
    return json_response

def get_all_data(code):
    end=str(datetime.fromtimestamp(int(open('./synctime.txt').read())))[:10]
    f_log=open('candlelog.txt','a')
    uid=f'{code}:{end}'
    if uid not in {line.strip() for line in open('./candlelog.txt')}:
        os.makedirs('./candles',exist_ok=True)
        start='19000101'
        if code+'.txt' in os.listdir('./candles'):
            existed={line.split()[0] for line in open(f'./candles/{code}.txt')}
            start=sorted(existed)[-1]
        o=web_data(code,start,end)
        l=o['data']['klines']
        with open(f'./candles/{code}.txt','a') as f_kline:
            for kline in l:
                n1,n2=kline.split(',',maxsplit=1)
                f_kline.write(f'{n1} {n2}\n')
    f_log.write(uid+'\n')
    #注意，这里可能有重复的日期
    return [line.split() for line in open(f'./candles/{code}.txt')]


if __name__=='__main__':
    o=get_all_data('000001')
    print(len(o))
    print(o[0])


