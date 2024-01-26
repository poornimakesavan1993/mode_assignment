# mode_assignment
Completed assignment and updated README
1. Download Python 3.11
	Navigate to https://www.python.org/downloads/ and download Python 3.11 executable for the operating system you have


2. Install Python 3.11
	Right click on downloaded file and select Run as administrator.
	Check Add python.exe to PATH and click on Install Now.

3. Wait till the installation is complete and than click on Close

4. Verify Installation
	Open the command prompt and type "python --version" and you should see Python version in output

5. Set the environment variable using, 
	Open File Explorer.
	Right-click 'Computer' in the Navigation Tree Panel on the left.
	Select 'Properties' ---> 'Advanced system settings' ---> 'Environment Variables' ---> 'System Variables'
	Click on PATH
	Add python path usually as C:\ProgramFiles\Python3.11\python.exe
	Also, add  C:\ProgramFiles\Python3.11\Scripts
	Save and close the tab

6. Open command prompt and execute pip install requests.

7. Once reuqests library is installed, Navigate to the project folder and check for test_config_data.py
	Verify the URL and endpoints
	configure the past days count to run the historical data aggregation

8. Execute python weather_data.py
	
	
NOTE:	1. Latitude and Longtitude are configured for "Toronto". Each day average has been calculated from hourly data aggregation and overall past 5 days average has been calculated from daily data summary.
	2. Hourly temperature average has been calculated from MM-DD-YYYY 00:00:00 till MM-DD-YYYY 23:00:00 which is having slight difference(mostly less than a kelvin unit eg: 0.75 K) with day summary temperature. If these values aren't 	negligible then it is considered to be bug. Since, this difference is present, verification of average is not possible to implement now
	3. Since, API end point of hourly data returns data for specific hour, we need to run get response for all 24 intervals differently. So, this concludes 5*24=120 get requests to get data. The execution time is linear due to this 	scenario
	4. Instead of trying another 120 set get requests, the most recurring weather condition has been reported from get response of hourly data aggregation. Please execute get_aggregated_hourly_weatherdata and 	get_frequent_weather_condition methods together.



FORECAST IMPLEMENTATION:
========================

1. Weather data forecast uses different API end point that can be configured in test_data_config.py
2. API end point should exclude current,minute,daily and alerts concentrating only hourly values and its aggregation
3. By finding mean value of total hourly data will result daily average data, that further can be processed to get overall average temperature forecast
4. API end point parameters like startdate and enddate can be used to retrieve data for specific time period
5. Changing the unix timestamp calculation to retrieve data from response JSON
	
	Existing formula for past days: 
	self.current_time = datetime.datetime.now()
        self.current_date = self.current_time.strftime("%m/%d/%Y")
        self.current_dt = int(datetime.datetime.strptime(self.current_date, "%m/%d/%Y").timestamp()) 
	past_date_hour = self.current_dt - (__iter_day * 24 * 60 * 60) - (60 * 60) // For each day iteration starts from previous day last interval
	past_date_hour = past_date_hour + (60 * 60) // calculation begins from first interval of the day that is 00:00:00

	Formula for forecast:
	self.current_time = datetime.datetime.now()
        self.current_date = self.current_time.strftime("%m/%d/%Y")
        self.current_dt = int(datetime.datetime.strptime(self.current_date, "%m/%d/%Y").timestamp()) 
	future_date_hour = current_dt + (__iter_day * 24 * 60 * 60) // For each day iteration starts from first interval
	future_date_hour = future_date_hour + (60 * 60) // calculation begins from first interval of the day that is 00:00:00

6. Introducing a function inside a weather forecast class with above mentioned calculation will result the necessary data
7. For 16 days forecast, startdate and enddate along with timezone parameter customization can be done to get the data


CI INTEGRATION
==============


	
