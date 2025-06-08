import asyncio
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from datetime import datetime, timedelta
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from google.oauth2.service_account import Credentials
import logging
import numpy as np
from weatheralgo import inputs

async def scrape_nws(driver, url):
    
        url_scrape = url
        print(f"Navigating to {url_scrape}")
        await driver.get(url_scrape)

        try:
            await asyncio.sleep(2)
            # Click Dew Point button
            dew_point = "//button[@aria-label='Show Dew Point']"
            dew_point_button = await driver.find_element(By.XPATH, dew_point, timeout=5)
            await dew_point_button.click()
            
            await asyncio.sleep(2)
            # Click Humidity button
            humidity = "//button[@aria-label='Show Relative Humidity']"
            humidity_button = await driver.find_element(By.XPATH, humidity, timeout=5)
            await humidity_button.click()
            
            await asyncio.sleep(2)
            # Open menu
            menu_button_selector = '.highcharts-contextbutton' 
            menu_button = await driver.find_element(By.CSS_SELECTOR, menu_button_selector, timeout=5)
            await menu_button.click()

            await asyncio.sleep(2)  # Short pause for menu animation
            
            # Click "View data table"
            data_table_xpath = "//li[@class='highcharts-menu-item' and contains(text(), 'View data table')]"
            data_table_item = await driver.find_element(By.XPATH, data_table_xpath, timeout=5)
            await data_table_item.click()

            await asyncio.sleep(2)  # Wait for table to render
            
            # Find table - using more flexible selector since ID might change
            table = await driver.find_element(By.CSS_SELECTOR, "table[summary='Table representation of chart.']", timeout=5)
            
            await asyncio.sleep(2)
            
            # Extract headers
            # headers = []
            date_elements = await table.find_elements(By.TAG_NAME, "th")
            # for header in header_elements:
            #     headers.append(await header.text)
            
            await asyncio.sleep(3)
            
            dates = [await header.text for header in date_elements]
            dates = dates[2:]
    
        
            temps = []
            rows = await table.find_elements(By.CSS_SELECTOR, "tbody tr")
            
            await asyncio.sleep(2)
            
            for row in rows:
                cells = await row.find_elements(By.TAG_NAME, "td")
                # temps = [await cell.text for cell in cells]
                for cell in cells:
                    temps.append(await cell.text)
                    
            scrape_df = pd.DataFrame({'Temp': temps, 'Datetime': dates})
            scrape_df['Temp'] = scrape_df['Temp'].astype(float)
            scrape_df['Datetime'] = pd.to_datetime(scrape_df['Datetime'])
            
            temp = scrape_df['Temp']
            datetime = scrape_df['Datetime']
            
            return temp, datetime  
         
        except Exception as e:
            print(f"scrape_nws: {e}")
            
def xml_scrape(xml_url, timezone):

    try:
        response = requests.get(xml_url)
        root = ET.fromstring(response.content)

        start_times = root.findall('.//start-valid-time')
        dates = [time.text for time in start_times]

        temperature_element = root.find('.//temperature[@type="hourly"]')
        value_elements = temperature_element.findall('.//value')
        temp = [int(value.text) for value in value_elements if isinstance(value.text, str)]
        temp_length = len(temp)
 
        forecasted = pd.DataFrame({'DateTime': dates[:temp_length], 'Temperature': temp})
        forecasted['DateTime'] = pd.to_datetime(forecasted['DateTime'])
        forecasted = forecasted.sort_values(by='DateTime')

    
        today = datetime.now(timezone).day

        next_day_high = forecasted[forecasted['DateTime'].dt.day == today]['Temperature'].idxmax()#[::-1]
        date = forecasted['DateTime'].iloc[next_day_high]
        hour_of_high = forecasted['DateTime'].iloc[next_day_high].hour
        temp_high = forecasted['Temperature'].iloc[next_day_high]

        return [date, hour_of_high, temp_high]

    except Exception as e:
      logging.info(f'xml_scrape: {e}')
      
    
    
def dict_of_high(all_markets, scrape_window):
    
    for i in  all_markets:
        
        try:
            xml_url =  all_markets[i]['XML_URL']
            timezone =  all_markets[i]['TIMEZONE']
            
            forecasted_high_date = xml_scrape(xml_url=xml_url, timezone=timezone)[0]
            scrape_begin =  forecasted_high_date - timedelta(minutes=scrape_window[0])
            scrape_end = forecasted_high_date + timedelta(minutes=scrape_window[1])
            
            if forecasted_high_date:               
                all_markets[i]['FORECASTED_HIGH_DATE'] = forecasted_high_date
                all_markets[i]['SCRAPE_DATE_RANGE'] = [scrape_begin, scrape_end]
            else:
                False
                
        except Exception as e:
            logging.info(f'dict_of_high: {e}')
            
    return all_markets

async def beg_scrape(driver, all_markets_with_highs, city):    
    
    try:
       
        timezone = all_markets_with_highs[city]['TIMEZONE']
        current_datetime = datetime.now(timezone)
        scrape_lower = current_datetime >= all_markets_with_highs[city]["SCRAPE_DATE_RANGE"][0]
        scrape_upper = current_datetime <= all_markets_with_highs[city]["SCRAPE_DATE_RANGE"][1]
        trade_not_executed = all_markets_with_highs[city]["TRADE_EXECUTED"] == None
        
        if all([scrape_lower, scrape_upper, trade_not_executed]):
            scrape_output = await scrape_nws(driver=driver, url=all_markets_with_highs[city]["URL"])
            
            temperatures = scrape_output[0]
            current_temp =  temperatures.iloc[-1]
            date_time = scrape_output[1]

            return temperatures, current_temp, date_time
        else:
            return False
            
    except Exception as e:
        logging.info(f'beg_scrape: {e}')
           
            


