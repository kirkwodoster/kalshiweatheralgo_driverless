import logging
from datetime import datetime
import logging
import gspread
from google.oauth2.service_account import Credentials
import pytz


from weatheralgo.clients import client

def weather_config(market, timezone): 
    try:

        today = datetime.now(timezone)
        todays_date = today.strftime('%y%b%d').upper()
        event_ticker = f'{market}-{todays_date}'
            
        event_list = []
        events = client.get_event(event_ticker)  # Ensure getEvent is defined or imported
        for i in range(len(events['markets'])):
            event_list.append(events['markets'][i]['ticker'])

        #temp_adj = []
        temp_adj = []

        event_list = [i.split('-', 2)[-1] for i in event_list]
        counter = 0
        for i in event_list:
            if "T" in i:
                counter += 1
                remove_t = i.strip('T')
                if counter == 1:
                    temp_adj.append(int(remove_t)-2)
                elif counter == 2:
                    temp_adj.append(int(remove_t)+1) # adjust for rounding error
                    
            elif "B" in i:
                remove_b = i.strip('B')
                temp_minus_5 = float(remove_b) - .5
                #temp_add_5 = float(remove_b) + .5
                #degree_range = [int(temp_minus_5) , int(temp_add_5)]
                temp_adj.append(int(temp_minus_5))

        degree_dictionary = {k: v for k, v in zip(event_list, temp_adj)}
       
        return degree_dictionary
    
    except Exception as e:
        logging.info(f'weather_config: {e}')
    

def order_pipeline(highest_temp: int, market: str, timezone):
    
    try:
        
        today = datetime.now(timezone)
        todaysDate = today.strftime('%y%b%d').upper()
        event = f'{market}-{todaysDate}'

    # tempMarket = None
        listofMarkets = weather_config(market=market, timezone=timezone)
        minMarketTemp = list(listofMarkets.values())[0]
        maxMarketTemp = list(listofMarkets.values())[-1]
        listofMarketsAdj = dict(list(listofMarkets.items())[1:-1])

        if highest_temp <= minMarketTemp:
            tempMarket = list(listofMarkets)[0]
        elif highest_temp >= maxMarketTemp:
            tempMarket = list(listofMarkets)[-1]
        else:
            for key, value in listofMarketsAdj.items():
                if highest_temp == value:
                    tempMarket = key

        if tempMarket:        
            return f'{event}-{tempMarket}'
        else:
            return False
            
    except Exception as e:
         if "tempMarket" not in  str(e):
            logging.info(f"order_pipeline {e}")
    except:
        None


# def to_sheets(sheet_name, data_input):
#     scropes = [
#     "https://www.googleapis.com/auth/spreadsheets"
# ]
#     credentials = 'util\credentials\kalshi-trade-data-f9799409bcc1.json'
#     creds = Credentials.from_service_account_file(credentials, scopes=scropes)
#     client = gspread.authorize(creds)

#     sheet_id = "f9799409bcc109173acefbb66a418282592211f3"
#     sheet = client.open_by_key(sheet_id)
    
#     sheet.worksheet(sheet_name).append_rows(data_input)
            
            
def logging_settings():
    return logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log format
    handlers=[logging.StreamHandler()]  # Output logs to the terminal
)
