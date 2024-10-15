
import datetime
import top10 #前10股东
import stockinfo #流通市值
import stockrealtime #实时价格
import candle #历史数据
import synctime
from tqdm import tqdm

#同步时间
synctime.sync()

#搜索范围
dingyu=open('./dingyue.txt').read().split()
dingyu=sorted({n for n in dingyu if len(n)>0})

#日志记录
f_log=open('log.txt','a')

list1=[]
for code in tqdm(dingyu,"搜索条件一三四"):

    #条件四：4十大股东持股总计超过40%。
    holders=top10.gettop10holder(code)
    chigubilis=[float(holder['ChiGuBiLi'][:-1])      for holder in holders]
    chigubili= sum(chigubilis) #持股比例
    f_log.write(f'{datetime.datetime.now()} 持股比例: {code} {chigubili}\n')
    #持股逻辑判断
    if chigubili<40:        continue

    #条件三: 流通市值超过30亿。
    o=stockinfo.stock_info(code)
    f117=o['f117'] #流通市值
    f_log.write(f'{datetime.datetime.now()} 流通市值: {code} {f117}\n')
    #流通市值逻辑判断
    if f117<30*10000*10000:        continue

    
    #条件一：历史最高价与这个价格之后的最低价之间跌幅超过90%。
    l=candle.get_all_data(code)
    l1=[ float(i[2]) for i in l]
    max_=max(l1)
    f_log.write(f'{datetime.datetime.now()} 历史最高: {code} {max_}\n')
    start=l1.index(max_)
    f_log.write(f'{datetime.datetime.now()} 历史最高距今: {code} {len(l)-start}个周期\n')
    min_=min([float(i[3])for i in l[start:]])
    f_log.write(f'{datetime.datetime.now()} 之后的历史最低: {code} {min_}\n')
    #逻辑判断
    if min_>max_*0.1:continue

    list1.append(code)
    
for code in tqdm(list1,"搜索条件二"):

    #条件二：股价目前在250均线之上。
    o=stockrealtime.stock_realtime([code])[0]
    f2=float(o['f2']) #当前价格
    f_log.write(f'{datetime.datetime.now()} 当前价格: {code} {f2}\n')

    l=candle.get_all_data(code)[:-250]
    l=[float(i[1]) for i in l]
    avg250= sum(l)/len(l) #250日均价
    f_log.write(f'{datetime.datetime.now()} 250均价: {code} {avg250}\n')
    #逻辑判断
    if f2<avg250:continue

    with open('result.txt','a') as f:
        f.write(f'{datetime.datetime.now()} {code} 满足条件\n')
    print(code,'满足条件')
    


