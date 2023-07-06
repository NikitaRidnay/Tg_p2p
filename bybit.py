import requests
import asyncio



def get_Bybit_price_buy(crypto_currency):
    url='https://api2.bybit.com/fiat/otc/item/online'
    params ={
    "userId": "",
    "tokenId": crypto_currency,
    "currencyId": "RUB",
    "payment": ["64", "75", "377"],
    "side": "1",
    "size": "10",
    "page": "1",
    "amount": "",
    "authMaker": False,
    "canTrade": False}
    with requests.Session() as session:
        headers={
        'accept':'application/json',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
        response=requests.post(url=url,headers=headers,json=params).json()
    USdt_price_buy= response['result']['items'][0]['price']
    Seller_name= response['result']['items'][0]['nickName']
    Seller_rate= response['result']['items'][0]['recentExecuteRate']
    Seller_order_count= response['result']['items'][0]['recentOrderNum']
    buy_paytype=response['result']['items'][0]['payments'][0]
    buy_min_lim=response['result']['items'][0]['minAmount']
    buy_max_lim=response['result']['items'][0]['maxAmount']
  
 
    return USdt_price_buy,Seller_name,Seller_rate,Seller_order_count,buy_paytype,buy_min_lim,buy_max_lim

def get_Bybit_price_Sell(crypto_currency):
    url='https://api2.bybit.com/fiat/otc/item/online'
    
    params ={
    "userId": "",
    "tokenId": crypto_currency,
    "currencyId": "RUB",
    "payment": ["64", "75", "377"],
    "side": "0",
    "size": "10",
    "page": "1",
    "amount": "",
    "authMaker": False,
    "canTrade": False}
    with requests.Session() as session:
        headers={
        'accept':'application/json',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
        response=requests.post(url=url,headers=headers,json=params).json()
    USdt_price_sell= response['result']['items'][0]['price']
    buyer_name= response['result']['items'][0]['nickName']
    buyer_rate= response['result']['items'][0]['recentExecuteRate']
    buyer_order_count= response['result']['items'][0]['recentOrderNum']
    sell_paytype=response['result']['items'][0]['payments'][0]
    sell_min_lim=response['result']['items'][0]['minAmount']
    sell_max_lim=response['result']['items'][0]['maxAmount']
    
    return USdt_price_sell,buyer_name,buyer_rate,buyer_order_count,sell_paytype,sell_min_lim,sell_max_lim


