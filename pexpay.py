import requests
import asyncio


def get_pexpay_buy(crypto_currency):
    url='https://www.pexpay.com/bapi/c2c/v1/friendly/c2c/ad/search'
    params={
        
  "page": 1,
  "rows": 10,
  "tradeType": "BUY",
  "asset": crypto_currency,
  "transAmount": "",
  "fiat": "RUB",
  "payTypes": ["Tinkoff","RaiffeisenBankRussia","Sberbank"],
  "merchantCheck": False,
  "classifies": [],
  "filter": {
    "payTypes": []}
}
    with requests.Session() as session:
        headers={
        'accept':'*/*',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    } 
        response=requests.post(url=url,headers=headers,json=params).json()
        BuyPrice=response['data'][0]['adDetailResp']['price']
        minlimitUsdt=response['data'][0]['adDetailResp']['minSingleTransAmount']
        maxlimitUsdt=response['data'][0]['adDetailResp']['dynamicMaxSingleTransAmount'] 
        sellerNickname=response['data'][0]['advertiserVo']['nickName']
        comleteOrders=response['data'][0]['advertiserVo']['userStatsRet']['completedOrderNum']
        SellerRate=response['data'][0]['advertiserVo']['userStatsRet']['finishRate']*100
        buy_tradetype=response['data'][0]['adDetailResp']['tradeMethods'][0]['tradeMethodName']

        return BuyPrice,minlimitUsdt,maxlimitUsdt,sellerNickname,comleteOrders,SellerRate,buy_tradetype
       
    


def get_pexpay_sell(crypto_currency):
    url='https://www.pexpay.com/bapi/c2c/v1/friendly/c2c/ad/search'
    params={
        
  "page": 1,
  "rows": 10,
  "tradeType": "SELL",
  "asset": crypto_currency,
  "transAmount": "",
  "fiat": "RUB",
  "payTypes": ["Tinkoff","RaiffeisenBankRussia","Sberbank"],
  "merchantCheck": False,
  "classifies": [],
  "filter": {
    "payTypes": []}
}
    with requests.Session() as session:
        headers={
        'accept':'*/*',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    } 
        response=requests.post(url=url,headers=headers,json=params).json()
        SellPrice=response['data'][0]['adDetailResp']['price']
        minlimitUsdt=response['data'][0]['adDetailResp']['minSingleTransAmount']
        maxlimitUsdt=response['data'][0]['adDetailResp']['dynamicMaxSingleTransAmount'] 
        BuyerNickname=response['data'][0]['advertiserVo']['nickName']
        comleteOrders=response['data'][0]['advertiserVo']['userStatsRet']['completedOrderNum']
        BuyerRate=response['data'][0]['advertiserVo']['userStatsRet']['finishRate']*100
        sell_tradetype=response['data'][0]['adDetailResp']['tradeMethods'][0]['tradeMethodName']
        
        return SellPrice,minlimitUsdt,maxlimitUsdt,BuyerNickname,comleteOrders,BuyerNickname,BuyerRate,sell_tradetype
    
