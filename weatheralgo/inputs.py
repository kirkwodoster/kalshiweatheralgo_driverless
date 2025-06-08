
import pytz

lr_length = 7
hour = 4
scrape_window = [5000,6000]
yes_price = 1
count = 0
slope_min = 0



all_markets = {
            "DENVER": {
                "SERIES": "KXHIGHDEN",
                "TIMEZONE": pytz.timezone("America/Denver"),
                "URL": f"https://www.weather.gov/wrh/timeseries?site=KDEN&hours={hour}",
                "XML_URL": "https://forecast.weather.gov/MapClick.php?lat=39.8589&lon=-104.6733&FcstType=digitalDWML",
                "FORECASTED_HIGH_DATE": None,
                "SCRAPE_DATE_RANGE": None,
                "TRADE_EXECUTED": None
            },
            "CHICAGO": {
                "SERIES": "KXHIGHCHI",
                "TIMEZONE": pytz.timezone("America/Chicago"),
                "URL": f"https://www.weather.gov/wrh/timeseries?site=KMDW&hours={hour}",
                "XML_URL": "https://forecast.weather.gov/MapClick.php?lat=41.7842&lon=-87.7553&FcstType=digitalDWML",
                "FORECASTED_HIGH_DATE": None,
                "SCRAPE_DATE_RANGE": None,
                "TRADE_EXECUTED": None
            },
            "MIAMI": {
                "SERIES": "KXHIGHMIA",
                "TIMEZONE":  pytz.timezone("US/Eastern"),
                "URL": f"https://www.weather.gov/wrh/timeseries?site=KMIA&hours={hour}",
                "XML_URL": "https://forecast.weather.gov/MapClick.php?lat=25.7934&lon=-80.2901&FcstType=digitalDWML",
                "FORECASTED_HIGH_DATE": None,
                "SCRAPE_DATE_RANGE": None,
                "TRADE_EXECUTED": None
            },
            "AUSTIN": {
                "SERIES": "KXHIGHAUS",
                "TIMEZONE":  pytz.timezone("US/Central"),
                "URL": f"https://www.weather.gov/wrh/timeseries?site=KAUS&hours={hour}",
                "XML_URL": "https://forecast.weather.gov/MapClick.php?lat=30.1945&lon=-97.6699&FcstType=digitalDWML",
                "FORECASTED_HIGH_DATE": None,
                "SCRAPE_DATE_RANGE": None,
                "TRADE_EXECUTED": None
            },
            "PHILADELPHIA": {
                "SERIES": "KXHIGHPHIL",
                "TIMEZONE":  pytz.timezone("US/Eastern"),
                "URL": f"https://www.weather.gov/wrh/timeseries?site=KPHL&hours={hour}",
                "XML_URL": "https://forecast.weather.gov/MapClick.php?lat=39.8721&lon=-75.2407&FcstType=digitalDWML",
                "FORECASTED_HIGH_DATE": None,
                "SCRAPE_DATE_RANGE": None,
                "TRADE_EXECUTED": None
            },
            "LOS ANGELES": {
                "SERIES":"KXHIGHLAX",
                "TIMEZONE":  pytz.timezone("America/Los_Angeles"),
                "URL": f"https://www.weather.gov/wrh/timeseries?site=KLAX&hours={hour}",
                "XML_URL": "https://forecast.weather.gov/MapClick.php?lat=33.9425&lon=-118.409&FcstType=digitalDWML",
                "FORECASTED_HIGH_DATE": None,
                "SCRAPE_DATE_RANGE": None,
                "TRADE_EXECUTED": None
            }
        }

market_list = ["KXHIGHDEN", "KXHIGHCHI", "KXHIGHMIA", "KXHIGHAUS", "KXHIGHPHIL", "KXHIGHLAX"]



    

