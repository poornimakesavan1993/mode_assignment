import datetime
import requests
from test_config_data import *

class past_weather_data:
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.current_date = self.current_time.strftime("%m/%d/%Y")
        self.current_dt = int(datetime.datetime.strptime(self.current_date, "%m/%d/%Y").timestamp())
        self.avg_temp_hourly_aggregated_data=0
        self.avg_temp_daily=0
        self.weather_data = []
    def get_request(self,url,end_point,get_param_payload):
        get_response = requests.get(url+end_point,
                                    params=get_param_payload, timeout=300)
        get_response_data = get_response.json()
        return get_response_data
    def get_aggregated_hourly_weatherdata(self):
        for __iter_day in range(1,days_to_retrieve_past_data+1):
            get_temp_hourly=0
            past_date_hour = self.current_dt - (__iter_day * 24 * 60 * 60) - (60 * 60)
            for __iter_hour in range(1, 25):
                past_date_hour = past_date_hour + (60 * 60)
                get_response_data = self.get_request(url,hourly_weather_data_endpoint,
                                                     {"lat":city_latitude, "lon":city_longitude,
                                                      "dt":past_date_hour,"appid":api_key})
                get_temp_hourly = (get_temp_hourly+get_response_data["data"][0]["temp"])
                self.weather_data.append(get_response_data["data"][0]["weather"][0]["id"])
            self.avg_temp_hourly_aggregated_data = round(get_temp_hourly / 24, 2)
            print("Average temperature of "+datetime.datetime.fromtimestamp(past_date_hour).strftime('%Y-%m-%d')+
                  " is",self.avg_temp_hourly_aggregated_data,"K")
    def get_aggregated_daily_temp(self):
        for __iter_day in range(1,days_to_retrieve_past_data+1):
            past_date = datetime.datetime.fromtimestamp(self.current_dt - (__iter_day * 24 * 60 * 60)).strftime('%Y-%m-%d')
            get_response_data = self.get_request(url, daily_weather_data_endpoint,
                                                 {"lat": city_latitude, "lon": city_longitude, "date": past_date,
                                                  "appid": api_key})
            self.avg_temp_daily = (self.avg_temp_daily+round((get_response_data["temperature"]["min"] + get_response_data["temperature"]["max"]) / 2, 2))
        past_days_avg_temp = self.avg_temp_daily/days_to_retrieve_past_data
        print("Average temperature of past ",days_to_retrieve_past_data,"days is:",round(past_days_avg_temp,2),"K")
    def get_frequent_weather_condition(self):
        try:
            weather_ID = str(max(self.weather_data , key=self.weather_data .count))
            print("Today's Weather most likely to be", weather_desc_mapping[weather_ID])
        except ValueError:
            print("Please execute hourly data aggregation before check for frequent weather condition!!")

daily_average_weatherdata = past_weather_data()
daily_average_weatherdata.get_aggregated_hourly_weatherdata()
daily_average_weatherdata.get_aggregated_daily_temp()
daily_average_weatherdata.get_frequent_weather_condition()