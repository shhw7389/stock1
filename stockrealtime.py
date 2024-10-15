import requests
import util

# 东方财富网网页请求头
request_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}


trade_detail_dict = {
#    'f12': '代码',
#    'f14': '名称',
#    'f3': '涨幅',
    'f2': '最新',
#    'f15': '最高',
#    'f16': '最低',
#    'f17': '今开',
#    'f8': '换手率',
#    'f10': '量比',
#    'f9': '市盈率',
#    'f5': '成交量',
#    'f6': '成交额',
#    'f18': '昨收',
#    'f20': '总市值',
#    'f21': '流通市值',
#    'f13': '编号',
#    'f124': '更新时间戳',
}


# 获取单个或多个证券的最新行情指标
def stock_realtime(code_list):
    """
    获取股票、期货、债券的最新行情指标
    code_list:输入单个或多个证券的list
    """
    if isinstance(code_list, str):
        code_list = [code_list]
    secids = [util.get_code_id(code)
              for code in code_list]

    fields = ",".join(trade_detail_dict.keys())
    params = (
        ('OSVersion', '14.3'),
        ('appVersion', '6.3.8'),
        ('fields', fields),
        ('fltt', '2'),
        ('plat', 'Iphone'),
        ('product', 'EFund'),
        ('secids', ",".join(secids)),
        ('serverVersion', '6.3.6'),
        ('version', '6.3.8'),
    )
    url = 'https://push2.eastmoney.com/api/qt/ulist.np/get'
    json_response = requests.get(url,
                                headers=request_header,
                                params=params).json()
    return json_response['data']['diff']
#    rows = jsonpath(json_response, '$..diff[:]')
#    if not rows:
#        df = pd.DataFrame(columns=trade_detail_dict.values())
#    else:
#        df = pd.DataFrame(rows)[list(trade_detail_dict.keys())].rename(columns=trade_detail_dict)
#    df['市场'] = df['编号'].apply(lambda x: market_num_dict.get(str(x)))
#    del df['编号']
#    df['时间'] = df['更新时间戳'].apply(lambda x: str(datetime.fromtimestamp(x)))
#    del df['更新时间戳']
#    # 将object类型转为数值型
#    ignore_cols = ['名称', '代码', '市场', '时间']
#    df = trans_num(df, ignore_cols)
#    return df
#
#
if __name__=='__main__':
    o=stock_realtime('000001')
    print(o)
