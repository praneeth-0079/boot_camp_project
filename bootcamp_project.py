import requests
api = '298c5dc93064a6f65f2124f2aec08b6f'
location = input("enter location(city name):")

api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
link = requests.get(api_link)
api_data = link.json()


temp_city = ((api_data['main']['temp']) - 273)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
with open('weather.txt' , 'w') as f:
    f.write("at ")
    f.write(location)
    f.write("\ntemperature in deg C:")
    f.write(format(temp_city))
    f.write("\nweather:")
    f.write(weather_desc)
    f.write("\nHumidity in %:")
    f.write(format(hmdt))
    f.write("\nwind speed in KMPH:")
    f.write(format(wind_spd))



