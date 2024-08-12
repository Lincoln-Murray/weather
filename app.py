from flask import Flask, render_template, request
import requests as r

app = Flask(__name__)

location = ''

@app.route("/")
def index():
    key = 'ad261dda6b984968bd560251243107'
    url = 'http://api.weatherapi.com/v1/forecast.json?key=' + key + '&q=' + location + '&days=3&aqi=yes&alerts=yes'

    response = r.get(url)

    if str(response) == '<Response [200]>':
        return render_template('index.html', json = response.json())
    elif location == '':
        return render_template('loading_location.html')
    else:
        return render_template('error.html', json = response.json())


@app.route("/positions", methods=['POST'])
def positions():
    global location
    location_response = request.get_json()
    location = str(location_response['latitude']) + ', ' + str(location_response['longitude'])
    return index()
