import requests
import asyncio


def get_garantex_price_buy(fiats):
    url='https://garantex.io/api/v2/depth?market='+fiats
    respons=requests.get(url=url).json()
    price_buy=respons['asks'][0]['price']
    return price_buy

def get_garantex_price_sell(fiats):
    url='https://garantex.io/api/v2/depth?market='+fiats
    respons=requests.get(url=url).json()
    price_sell=respons['bids'][0]['price']
    print(price_sell +" rub")
    return price_sell

get_garantex_price_sell("btcrub")
get_garantex_price_sell("usdtrub")
get_garantex_price_sell("ethrub")