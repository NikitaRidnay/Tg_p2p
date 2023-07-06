
from telebot.async_telebot import AsyncTeleBot

import asyncio

import requests
from binance import get_binance_sell_paytype_info,get_binance_buy_paytype_info
from garantex import get_garantex_price_buy,get_garantex_price_sell
from bybit import get_Bybit_price_buy,get_Bybit_price_Sell
from Huobi import  get_huobi_price_sell,get_huobi_price_buy
from pexpay import get_pexpay_buy,get_pexpay_sell


bot=AsyncTeleBot('6271043250:AAFKhiFalD1Lgl3thOJCPGHELcYCCATPO8s')


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Привет! 🤖 ')



@bot.message_handler(commands=['pexpay'])
async def get_pexpay(message):
    BuyPrice,BuyminlimitUsdt,BuymaxlimitUsdt,sellerNickname,SellercomleteOrders,SellerRate,buy_tradetype=get_pexpay_buy("usdt")
    SellPrice,SellminlimitUsdt,SellmaxlimitUsdt,BuyerNickname,BuyercomleteOrders,BuyerNickname,BuyerRate,sell_tradetype=get_pexpay_sell("usdt")

    await bot.send_message(message.chat.id,f"""Покупка 🔥{BuyPrice}🔥 RUB 
    -Ник 👉🏻{sellerNickname}
    -Статистика{SellerRate}%({SellercomleteOrders})
    -Лимиты {BuyminlimitUsdt} - {BuymaxlimitUsdt}
    -Способ оплаты: {buy_tradetype}

    Продажа 🔥{SellPrice}🔥 RUB
    -Ник 👉🏻{BuyerNickname}
    -Статистика {BuyerRate}%({BuyercomleteOrders})  
    -Лимиты {SellminlimitUsdt} - {SellmaxlimitUsdt}
    -Способ оплаты: {sell_tradetype}                             """)

@bot.message_handler(commands=['huobi'])
async def get_huobi_prices(message):
    sell_price,seller_nickname,seller_complete_oreder_rate,seller_order_count,buy_paytype,buys_min_limit,buy_max_limit = get_huobi_price_sell('usdt')
    buy_price,buyer_nickname,buyer_complete_oreder_rate,buyer_order_count,sell_paytype,sell_min_limit,sell_max_limit=get_huobi_price_buy('usdt')

    await bot.send_message(message.chat.id,f"""покупка: 🔥 {sell_price}🔥  RUB
    - Ник: 👉🏻{seller_nickname}
    -Статистика:{seller_complete_oreder_rate}% ({seller_order_count})
    -Лимиты: {buys_min_limit} - {buy_max_limit}
    -Тип оплаты: {buy_paytype}
    

    продажа: 🔥{buy_price}🔥 RUB
    - Ник: 👉🏻{buyer_nickname}
    -Статистика:{buyer_complete_oreder_rate}% ({buyer_order_count})
    -Лимиты: {sell_min_limit} - {sell_max_limit}
    -Тип оплаты: {sell_paytype}
    
    """)

@bot.message_handler(commands=['bybit'])
async def get_prices(message):
    
    USdt_price_buy,Seller_name,Seller_rate,Seller_order_count,buy_paytype,buy_min_lim,buy_max_lim=get_Bybit_price_buy("USDT")
    USdt_price_sell,buyer_name,buyer_rate,buyer_order_count,sell_paytype,sell_min_lim,sell_max_lim=get_Bybit_price_Sell("USDT")
    
    await bot.send_message(message.chat.id, f"""Самая низкая цена на покупку USDT :
                           
   
                           
    
 -Bybit Продавец 
🔥{USdt_price_buy}🔥  RUB
 -Ник: 👉🏻 {Seller_name}
 -Статистика:  {Seller_rate}% ({Seller_order_count})
 -Лимиты : {buy_min_lim} - {buy_max_lim} RUB
 -Тип оплаты : {buy_paytype}
 --------------------
 -Bybit Покупатель
 🔥{USdt_price_sell}🔥  RUB
 -Ник: 👉🏻 {buyer_name}
 -Статистика:  {buyer_rate}% ({buyer_order_count})
 -Лимиты : {sell_min_lim} - {sell_max_lim} RUB
 -Тип оплаты : {sell_paytype}
 """)




@bot.message_handler(commands=['garantex'])
async def get_garantex_price(message):
    price_buy=get_garantex_price_buy()
    price_sell=get_garantex_price_sell()
    await bot.send_message(message.chat.id,f"""-Покупка 🔥{price_buy}🔥 RUB
                           
-Продажа 🔥{price_sell}🔥RUB""")                 



@bot.message_handler(commands=['binance'])
async def get_Binance_price(message):

    
    bnc_price_buy_paytype,  bnc_price_buy,buyer_info, buyer_info_rate,buyer_info_count,minBuyerLimit,maxBuyerLimit=get_binance_buy_paytype_info("usdt")
    bnc_price_sell_paytype, bnc_price_sell, seller_info,seller_info_rate,seller_info_count,minSellerLimit,maxSellerLimit = get_binance_sell_paytype_info("usdt")
    await bot.send_message(message.chat.id,f"""Покупка (USDT) на Binance (RUB) Продавец c лучшей ценой:   
  👉🏻{buyer_info} 
   - Статистика: {buyer_info_rate*100}% ({buyer_info_count})
   - Цена:  🔥{bnc_price_buy}🔥 RUB
   - Лимиты: {minBuyerLimit} - {maxBuyerLimit} RUB
   - Типо оплаты: {bnc_price_buy_paytype}
   
   
   
   
  Продажа (USDT) на Binance (RUB) Покупатель c лучшей ценой: 👉🏻{seller_info}
   - Статистика: {seller_info_rate*100}% ({seller_info_count})
   - Цена:  🔥{bnc_price_sell}🔥 RUB
   - Лимиты: {minSellerLimit} - {maxSellerLimit} RUB
   - Типо оплаты: {bnc_price_sell_paytype}""")
   
   







if __name__=='__main__':
    asyncio.run(bot.polling())