
import requests
import util

# 东方财富网网页请求头
request_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'}


###股票数据接口
# 获取单只个股最新的基本财务指标
def stock_info(code):
    '''code输入股票代码或简称'''
    stock_info_dict = {
        #'f57': '代码',
        #'f58': '名称',
        #'f162': '市盈率(动)',
        #'f167': '市净率',
        #'f127': '所处行业',
        #'f116': '总市值',
        'f117': '流通市值',
        #'f173': 'ROE',
        #'f187': '净利率',
        #'f105': '净利润',
        #'f186': '毛利率'
        }

    code_id = util.get_code_id(code)
    fields = ",".join(stock_info_dict.keys())
    params = (
        ('ut', 'fa5fd1943c7b386f172d6893dbfba10b'),
        ('invt', '2'),
        ('fltt', '2'),
        ('fields', fields),
        ('secid', code_id)
    )
    url = 'http://push2.eastmoney.com/api/qt/stock/get'
    json_response = requests.get(url,
                                headers=request_header,
                                params=params).json()
    items = json_response['data']
    return items

