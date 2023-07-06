import requests
import asyncio



def get_binance_buy_paytype_info(crypto_currency):
    url='https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    params={
        "fiat": "RUB",
        "page": 1,
        "rows": 10,
        "tradeType": "BUY",
        "asset": crypto_currency,
        "countries": [],
        "proMerchantAds": False,
        "publisherType": None,
        "payTypes": ["TinkoffNew","RosBankNew","RaiffeisenBank"],
    }
    with requests.Session() as session:
        headers={
            'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        response = session.post(url=url, headers=headers, json=params).json()
    bnc_price_buy_paytype = response['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']
    bnc_price_buy = response['data'][0]['adv']['price']
    buyer_info = response['data'][0]['advertiser']['nickName']
    buyer_info_rate = response['data'][0]['advertiser']['monthFinishRate']
    buyer_info_count = response['data'][0]['advertiser']['monthOrderCount']
    minBuyerLimit=response['data'][0]['adv']['minSingleTransAmount']
    maxBuyerLimit=response['data'][0]['adv']['dynamicMaxSingleTransAmount']
    
    return bnc_price_buy_paytype,  bnc_price_buy,buyer_info, buyer_info_rate,buyer_info_count,minBuyerLimit,maxBuyerLimit

def get_binance_sell_paytype_info(crypto_currency):
    url='https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
    params={
        "fiat": "RUB",
        "page": 1,
        "rows": 10,
        "tradeType": "SELL",
        "asset": crypto_currency,
        "countries": [],
        "proMerchantAds": False,
        "publisherType": None,
        "payTypes": ["TinkoffNew","RosBankNew","RaiffeisenBank"],
    }
    with requests.Session() as session:
        headers={
            'accept':'*/*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        response = session.post(url=url, headers=headers, json=params).json()

    # initialize the variables to store the highest-priced offer with limits between 5000 and 500000
    highest_offer_price = 0
    highest_offer_details = None

    for offer in response['data']:
        # check if the offer limits are within the range of 5000 and 500000
        if float(offer['adv']['minSingleTransAmount']) >= 5000 and float(offer['adv']['dynamicMaxSingleTransAmount']) <= 500000:
            offer_price = float(offer['adv']['price'])
            if offer_price > highest_offer_price:
                highest_offer_price = offer_price
                highest_offer_details = offer

    if highest_offer_details:
        bnc_price_sell_paytype = highest_offer_details['adv']['tradeMethods'][0]['tradeMethodName']
        bnc_price_sell = highest_offer_details['adv']['price']
        seller_info = highest_offer_details['advertiser']['nickName']
        seller_info_rate = highest_offer_details['advertiser']['monthFinishRate']
        seller_info_count = highest_offer_details['advertiser']['monthOrderCount']
        minSellerLimit = highest_offer_details['adv']['minSingleTransAmount']
        maxSellerLimit = highest_offer_details['adv']['dynamicMaxSingleTransAmount']
        print(bnc_price_sell_paytype, bnc_price_sell, seller_info, seller_info_rate,seller_info_count,minSellerLimit,maxSellerLimit)
        return bnc_price_sell_paytype, bnc_price_sell, seller_info, seller_info_rate,seller_info_count,minSellerLimit,maxSellerLimit
    

    
