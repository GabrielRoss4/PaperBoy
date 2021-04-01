'''
This app will query the designated weather API every ten minutes and 
grab the weather from all specified zipcodes. The app will then store
all weather data in a database
'''

import time, requests, sqlite3, json, datetime
import tkinter as tk

def get_weather_data(zipCode="02460"):

	# Gotten from opweanweathermap.org
	apiKey = "227d84013f347b542827501bd6929b4d"
	baseURL = "http://api.openweathermap.org/data/2.5/weather?"
	fullURL = baseURL + "appid=" + apiKey + "&zip=" + zipCode + ",us" + "&units=imperial"
	try:
		responseRaw = requests.get(fullURL)
		APIresult = responseRaw.json()

		return [APIresult["name"], 
				APIresult["weather"][0]["main"], 
				round(APIresult["main"]["feels_like"]), 
				APIresult["timezone"]/3600]
	except:
		return "Failed to get website info"



""" def make_weather_GUI(weather_data):
	root = tk.Tk()
	root.geometry("400x300")

	def update_GUI_realtime():
		root.title("Current weather at " + str(datetime.datetime.now().strftime("Time: %H:%M:%S")))

		for i, location in enumerate(weather_data):
			for j, data in enumerate(location):
				tk.Label(root, text=data).grid(row=i, column=j)

		root.after(1000, update_GUI_realtime)
	update_GUI_realtime()

	root.mainloop() """

def main():

	zip_codes = ["02460", "98102"]

	'''
	thisWeather = get_weather_data()
	for i, item in enumerate(["City", "Weather", "Temperature (F)", "Timezone"]):
		this_label = tk.Label(root, text=item).grid(row=0, column=i)
	for i, item in enumerate(thisWeather):
		this_label = tk.Label(root, text=item).grid(row=1, column=i)
	'''
	root = tk.Tk()
	root.geometry("400x300")

	# Add the column headers for the table
	data_headers = ["City, State", "Weather", "Feels like (F)", "Timezone"]
	for i, header in enumerate(data_headers):
		tk.Label(root, text=header).grid(row=0, column=i)

	# Update time & weather data in realtime

	def update_GUI_realtime():
		#root.title("Current weather at " + str(datetime.datetime.now().strftime("Time: %H:%M:%S")))
		root.title("Weather at: " + str(datetime.datetime.now().strftime("Time: %H:%M")))

		for i, location in enumerate(zip_codes):
			location_data = get_weather_data(location)
			for j, data in enumerate(location_data):
				tk.Label(root, text=data).grid(row=i+1, column=j)

		root.after(60000, update_GUI_realtime) # Updates every 10mins
	update_GUI_realtime()

	root.mainloop()

if __name__ == "__main__":
	main()

'''
{'coord': {'lon': -71.2084, 'lat': 42.352}, 
'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}, 
{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}], 'base': 'stations', 
'main': {'temp': 278.63, 'feels_like': 274.15, 'temp_min': 278.15, 'temp_max': 279.82, 
'pressure': 998, 'humidity': 93}, 'visibility': 6437, 'wind': {'speed': 4.63, 'deg': 290}, 
'rain': {'1h': 1.41}, 'clouds': {'all': 90}, 'dt': 1614622380, 'sys': {'type': 1, 'id': 3486, 
'country': 'US', 'sunrise': 1614597603, 'sunset': 1614638072}, 'timezone': -18000, 'id': 0, 
'name': 'Newtonville', 'cod': 200}
'''