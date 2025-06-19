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
from selenium_driverless import webdriver
import warnings

# Initialize the WebSocket client
# ws_client = KalshiWebSocketClient(
#     key_id=client.key_id,
#     private_key=client.private_key,
#     environment=client.environment
# )

# Connect via WebSocket
# asyncio.run(ws_client.connect())


if __name__ == "__main__":
    
    try:
        asyncio.run(weather_model.weather_model())
    except KeyboardInterrupt:
        print("Program terminated by user.")
    


    
