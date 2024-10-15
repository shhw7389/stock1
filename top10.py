

import re
import requests
import util

def gettop10holder(code):
    code_id=util.get_code_id(code)
    num=2
    fields = {
        'GuDongDaiMa': '股东代码',
        'GuDongMingCheng': '股东名称',
        'ChiGuShu': '持股数(亿)',
        'ChiGuBiLi': '持股比例(%)',
        'ZengJian': '增减',
        'BianDongBiLi': '变动率(%)'}

    mk = code_id.split('.')[0]
    stock_code = code_id.split('.')[1]
    fc = f'{stock_code}02' if mk == '0' else f'{stock_code}01'
    data0 = {"fc": fc}
    url0 = 'https://emh5.eastmoney.com/api/GuBenGuDong/GetFirstRequest2Data'
    res = requests.post(url0, json=data0).content #.json()
    l=re.findall(b'"BaoGaoQi":"(\\d\\d\\d\\d-\\d\\d-\\d\\d)"',res)
    date=sorted(l)[-1].decode()

    #print(res)
    #res=res['Result']
    #n1=list(res.keys())[0]
    #res[n1

    #dates = jsonpath(res, '$..BaoGaoQi')
    #df_list = []

    data = {"fc": fc, "BaoGaoQi": date}
    url = 'https://emh5.eastmoney.com/api/GuBenGuDong/GetShiDaLiuTongGuDong'
    response = requests.post(url, json=data)
    response.encoding = 'utf-8'
    o=response.json()
    return o['Result']['ShiDaLiuTongGuDongList']
if __name__=='__main__':
    o=gettop10holder('600415')
    print(o)
