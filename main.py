
import datetime
import top10
import stockinfo
from tqdm import tqdm
#搜索范围
dingyu=open('./dingyue.txt').read().split()
dingyu=sorted({n for n in dingyu if len(n)>0})

#日志记录
f_log=open('log.txt','a')

for code in tqdm(dingyu,"搜索股票"):

    #条件四：4十大股东持股总计超过40%。
    chigubili=0
    holders=top10.gettop10holder(code)
    for holder in holders:
        chigubili+=float(holder['ChiGuBiLi'][:-1])
    #记录日志
    f_log.write(f'{datetime.datetime.now()} 持股比例: {code} {chigubili}\n')
    if chigubili<40:
        continue

    #条件三: 流通市值超过30亿。
    o=stockinfo.stock_info(code)
    f117=o['f117']
    #记录日志
    f_log.write(f'{datetime.datetime.now()} 流通市值: {code} {f117}\n')
    if f117<30*10000*10000:
        continue
    break



