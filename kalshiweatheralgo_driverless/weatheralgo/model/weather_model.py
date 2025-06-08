from weatheralgo import trade_functions
from weatheralgo import scrape_functions
from weatheralgo import util_functions
from weatheralgo import inputs
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio
import warnings

async def weather_model():
    
    scrape_window = inputs.scrape_window
        
    all_markets = inputs.all_markets

    all_markets_with_highs = scrape_functions.dict_of_high(
                                                          all_markets=all_markets,
                                                          scrape_window=scrape_window,
                                                          )
    
    warnings.filterwarnings("ignore", message="got execution_context_id and unique_context=True")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')  # Crucial for running as root or in some CI environments
    options.add_argument('--disable-dev-shm-usage') # Overcomes resource limits in /dev/shm
    options.add_argument('--disable-gpu') # Often recommended for headless
    
    driver = None
    
    print("Initializing WebDriver...")
    driver = await webdriver.Chrome(options=options)
    print("WebDriver initialized.")

    while True:
        
        for city in all_markets:
           market = all_markets[city]['SERIES']
           timezone = all_markets[city]['TIMEZONE']
             
           beg_scrape_func = await scrape_functions.beg_scrape(
                                                               driver=driver,
                                                               all_markets_with_highs=all_markets_with_highs,
                                                               city=city
                                                               )
           if beg_scrape_func:
                temperatures, current_temp, date_time = beg_scrape_func
                trade = trade_functions.max_or_trade_criteria_met(
                                                                   current_temp=current_temp,
                                                                   market=market, 
                                                                   yes_price=inputs.yes_price,
                                                                   count=inputs.count,
                                                                   temperatures=temperatures, 
                                                                   timezone=timezone
                                                                   )
                print(trade)
                if trade:
                    all_markets_with_highs[city]["TRADE_EXECUTED"] = True
                
        await asyncio.sleep(1)
                
                
                
      
            
            
            
            
       


    

        

