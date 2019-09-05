import requests

city = input("Enter City:")
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=baa122dfd79a5dd4b64fb4f97ac88d38&units=metric'.format(city)

res = requests.get(url)

data = res.json()

print(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Wind Speed : {} m/s'.format(wind_speed))
print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))
print('Description : {}'.format(description))
