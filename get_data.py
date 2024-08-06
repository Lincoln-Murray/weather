import requests

key = '63b4a338308d4ce9a303215024220s7'
location = '-32.005938, 116.039676'

url = 'http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + location + '&aqi=yes'

response = requests.get(url)

if str(response) == '<Response [200]>':
    weather_json = open('weather.json', 'w')
    weather_json.write(str(response.json()).replace("'", '"'))
    weather_json.close()
else:
    print('Error: ' + str(response.json()['error']['code']) + ', ' + str(response.json()['error']['message']))
