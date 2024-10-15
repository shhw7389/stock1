

import re
import requests
import util
import datetime
import json

path_log='top10log.txt'
open(path_log,'a').close()
existed=[line.split(maxsplit=1) for line in open(path_log)]
existed={n1:n2 for n1,n2 in existed}

def gettop10holder(code):
    date=str(datetime.datetime.now()).split()[0]
    key=f'{code}-{date}-top10'
    if key in existed:
        return json.loads(existed[key])

    code_id=util.get_code_id(code)
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
    if len(l)<1:
        print(res)
        raise
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
    try:
        o=response.json()
        value=o['Result']['ShiDaLiuTongGuDongList']
    except:
        print(response)
        print(response.content)
        raise
    with open(path_log,'a') as f_log:        f_log.write(key+' '+json.dumps(value)+'\n')
    return value
if __name__=='__main__':
    o=gettop10holder('600415')
    print(o)
