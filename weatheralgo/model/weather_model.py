from weatheralgo import trade_functions
from weatheralgo import scrape_functions
from weatheralgo import util_functions
from weatheralgo import inputs
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio
import warnings
import zulu

async def weather_model():
    
    scrape_window = inputs.scrape_window
        
    all_markets = inputs.all_markets

    all_markets_with_highs = scrape_functions.dict_of_high(
                                                          all_markets=all_markets,
                                                          scrape_window=scrape_window,
                                                          )
    print(all_markets_with_highs)
    min_zulu, max_zulu = scrape_functions.convert_to_zulu(all_markets_with_highs=all_markets_with_highs)
    print('min/max', min_zulu, max_zulu)
    zulu_bolean_check = scrape_functions.zulu_boolean(min_zulu=min_zulu, max_zulu=max_zulu)
    print('boolean', zulu_bolean_check)
    
    driver = await scrape_functions.initialize_driver()
    
    while True:

        for city in all_markets:
           market = all_markets[city]['SERIES']
           timezone = all_markets[city]['TIMEZONE']
             
           beg_scrape_func = await scrape_functions.beg_scrape(
                                                               driver=driver,
                                                               all_markets_with_highs=all_markets_with_highs,
                                                               city=city
                                                               )

           if beg_scrape_func and zulu_bolean_check:
                temperatures, current_temp, date_time = beg_scrape_func
                print(temperatures, date_time)
               
                trade = trade_functions.max_or_trade_criteria_met(
                                                                   current_temp=current_temp,
                                                                   market=market, 
                                                                   yes_price=inputs.yes_price,
                                                                   count=inputs.count,
                                                                   temperatures=temperatures, 
                                                                   timezone=timezone,
                                                                   lr_length=inputs.lr_length
                                                                   )
                if trade:
                    all_markets_with_highs[city]["TRADE_EXECUTED"] = True
                
        await asyncio.sleep(1)
                
                
                
      
            
            
            
            
       


    

        

