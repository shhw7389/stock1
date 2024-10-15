import requests
#缓存codeid表
code_id_dict=[line.strip() for line in open('./codeid.txt') ]
code_id_dict=[line.split() for line in code_id_dict if len(line)>0 ]
code_id_dict={i[0]:i[1] for i in code_id_dict}

def get_code_id(code):
    """
    生成东方财富股票专用的行情ID
    code:可以是代码或简称或英文
    """
    if code in code_id_dict.keys():
        return code_id_dict[code]
    url = 'https://searchapi.eastmoney.com/api/suggest/get'
    params = (
        ('input', f'{code}'),
        ('type', '14'),
        ('token', 'D43BF722C8E33BDC906FB84D85E326E8'),
    )
    response = requests.get(url, params=params).json()
    code_dict = response['QuotationCodeTable']['Data']
    if code_dict:
        with open('./codeid.txt','a') as f:
            f.write(f"{code} {code_dict[0]['QuoteID']}\n")
        return code_dict[0]['QuoteID']
    else:
        print('输入代码有误')


if __name__ == '__main__':
    code = '600415'
    print(get_code_id(code))
