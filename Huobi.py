import requests
import json



def get_huobi_price_buy(crypto_currency):
    url = 'https://www.huobi.com/-/x/otc/v1/data/trade-market'
    params = {
        "coinId": 2 if crypto_currency == "usdt" else (1 if crypto_currency == "btc" else 3),
        "currency": 11,
        "tradeType": "sell",
        "currPage": 1,
        "payMethod": 0,
        "acceptOrder": 0,
        "country": "",
        "blockType": "general",
        "online": 1,
        "range": 0,
        "amount": "",
        "onlyTradable": "false",
        "isFollowed": "false"
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    data = response.json()
    buy_price = data['data'][0]['price']
    buyer_nickname=data['data'][0]['userName']
    buyer_complete_oreder_rate=data['data'][0]['orderCompleteRate']
    buyer_order_count=data['data'][0]['tradeMonthTimes']
    sell_paytype=data['data'][0]['payMethods'][0]['name']
    sell_min_limit=data['data'][0]['minTradeLimit']
    sell_max_limit=data['data'][0]['maxTradeLimit']
    
    
    return buy_price,buyer_nickname,buyer_complete_oreder_rate,buyer_order_count,sell_paytype,sell_min_limit,sell_max_limit
  

def get_huobi_price_sell(crypto_currency):
    url = 'https://www.huobi.com/-/x/otc/v1/data/trade-market'
    params = {
        "coinId": 2 if crypto_currency == "usdt" else (1 if crypto_currency == "btc" else 3),
        "currency": 11,
        "tradeType": "buy",
        "currPage": 1,
        "payMethod": 0,
        "acceptOrder": 0,
        "country": "",
        "blockType": "general",
        "online": 1,
        "range": 0,
        "amount": "",
        "onlyTradable": "false",
        "isFollowed": "false"
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    data = response.json()
    sell_price = data['data'][0]['price']
    seller_nickname=data['data'][0]['userName']
    seller_complete_oreder_rate=data['data'][0]['orderCompleteRate']
    seller_order_count=data['data'][0]['tradeMonthTimes']
    buy_paytype=data['data'][0]['payMethods'][0]['name']
    buys_min_limit=data['data'][0]['minTradeLimit']
    buy_max_limit=data['data'][0]['maxTradeLimit']

    return sell_price,seller_nickname,seller_complete_oreder_rate,seller_order_count,buy_paytype,buys_min_limit,buy_max_limit
  
