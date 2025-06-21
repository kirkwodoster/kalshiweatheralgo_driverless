#from cryptography.hazmat.primitives import serialization
#import asyncio
# from weatheralgo.clients import  KalshiWebSocketClient
import logging
import pytz
import asyncio
import zulu
import pprint

from weatheralgo.model import weather_model
from weatheralgo import util_functions
from weatheralgo import scrape_functions
from weatheralgo import trade_functions
from weatheralgo.clients import client
from datetime import datetime, timedelta
import pytz
import time
import numpy as np
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dateutil import tz

from weatheralgo import inputs
from weatheralgo import scrape_functions

from weatheralgo.clients import client
from weatheralgo.model import weather_model
from selenium_driverless import webdriver

from weatheralgo.clients import KalshiWebSocketClient, KalshiClient # Import KalshiClient as well if you still use it for 'client' variable
from weatheralgo.clients import client as kalshi_http_client_instance # This is your existing 'client' instance

import warnings

# Initialize the WebSocket client
ws_client = KalshiWebSocketClient(
    key_id=client.key_id,
    private_key=client.private_key,
    environment=client.environment
)

# Connect via WebSocket
# asyncio.run(ws_client.connect())
# async def socket():
#     await ws_client.connect()
#     await ws_client.subscribe_to_fills(["KXHIGHMIA-25JUN20-B89.5", "KXHIGHMIA-25JUN20-B87.5"]) 

if __name__ == "__main__":
    
    
    # driver = scrape_functions.initialize_driver()
    
    # x = scrape_functions.scrape_nws(driver=driver, url='https://www.weather.gov/wrh/timeseries?site=KMIA&hours=4')
    
    # asyncio.run(x)
    
    # ticker_title = []
    # for i in inputs.event_list:
    #     markets = client.get_event(event_ticker=i)['markets']
    #     for j in range(0, len(markets)):
    #        result = markets[j]['result']
    #        if result == 'yes':
    #            ticker = markets[j]['ticker']
    #            title = markets[j]['no_sub_title']
    #            ticker_title.append([ticker, title])
    #        else:
    #            pass
           
    # print(ticker_title)
    
#    for i in range(0,(len(client.get_event(event_ticker='KXHIGHDEN-25JUN17')['markets']))):
#       if client.get_event(event_ticker='KXHIGHDEN-25JUN17')['markets'][i]['result'] == 'yes':
#           ticker = 
          

    
    # x = client.get_event(event_ticker='KXHIGHDEN-25JUN17')['markets'][0]
    
    # pprint.pprint(x)
    
    # y = client.get_market_order_book('KXHIGHMIA-25JUN20-B89.5')
    # print(y)
    try:
        asyncio.run(weather_model.weather_model())
    except KeyboardInterrupt:
        print("Program terminated by user.")
    


    
