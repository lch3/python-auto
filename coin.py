import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import pyupbit
import numpy as np
import requests
import pandas as pd
import time

price = pyupbit.get_current_price("KRW-BTC")
price_min=price
price_max=price

while True:
    price = pyupbit.get_current_price("KRW-BTC")
    while price > price_max and price > price_min:
        if price < price_min*1.001 :
            upbit.buy_market_order("KRW-BTC", 10000)
            price_max=price
            price_min=price
    while price < price_max and price < price_min:
        if price < price_max*0.999 :
            upbit.sell_market_order("KRW-BTC", btc*0.9995)
            price_max=price
            price_min=price
    if price_max < price :
        price_max=price
    if price_min > price :
        price_min=price
    print(price_max)
    print(price)
    print(price_min)
    print('\n')
    time.sleep(2)
