#from cryptography.hazmat.primitives import serialization
#import asyncio
# from weatheralgo.clients import  KalshiWebSocketClient
import logging
import pytz
import asyncio
import zulu

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



# Initialize the WebSocket client
# ws_client = KalshiWebSocketClient(
#     key_id=client.key_id,
#     private_key=client.private_key,
#     environment=client.environment
# )

# Connect via WebSocket
# asyncio.run(ws_client.connect())



if __name__ == "__main__":
    
    x = weather_model.weather_model()
    print(x)
    try:
        asyncio.run(weather_model.weather_model())
    except KeyboardInterrupt:
        print("Program terminated by user.")
    
    # x = scrape_functions.xml_scrape(xml_url="https://forecast.weather.gov/MapClick.php?lat=39.8589&lon=-104.6733&FcstType=digitalDWML",
    #                                 timezone="America/Denver")
    # print(x)
    
    # y = scrape_functions.scrape_nws("https://www.weather.gov/wrh/timeseries?site=KDEN&hours=1")
    # print(asyncio.run(y)[0])
    # # pass
    #ticker='KXHIGHMIA-25MAY31-B91.5'
    # x = client.get_orders()
    # print(x['orders'][0])
    
    # current_temp = 62.06
    # market = "KXHIGHDEN"
    # temperatures = pd.Series([50,  62.6,  62.6,  62.6,  62.6,  62.6,  50,  62.6,  64.4,  62.6,  62.96, 64.4,
    #                 64.4,  62.6,  62.6,  62.6,  62.6,  62.6,  62.6,  62.6,  62.6,  62.6,  62.6,  4])
    # timezone = pytz.timezone('America/Chicago')
    
    # trade = trade_functions.max_or_trade_criteria_met(
    #                                                                current_temp=current_temp,
    #                                                                market=market, 
    #                                                                yes_price=inputs.yes_price,
    #                                                                count=inputs.count,
    #                                                                temperatures=temperatures, 
    #                                                                timezone=timezone
    #                                                                )
    # print(trade)
    
    # check = trade_functions.trade_criteria_met(temperatures=temperatures, lr_length=inputs.lr_length, market=market, yes_price=inputs.yes_price,
    #                                            count=inputs.count, timezone=timezone)
    # check
    # order_pipeline_check = util_functions.order_pipeline(highest_temp=64, market=market, timezone=timezone)
    # print(order_pipeline_check)
    
    # x = scrape_functions.xml_scrape(xml_url="https://forecast.weather.gov/MapClick.php?lat=39.8589&lon=-104.6733&FcstType=digitalDWML",
    #                                 timezone=pytz.timezone('America/Chicago'))
    # print(x)
    
    # x = trade_functions.max_or_trade_criteria_met(current_temp=100, market=market, yes_price=inputs.yes_price, count=inputs.count,
    #                                               temperatures=temperatures, timezone=timezone)
    # x
    


    
