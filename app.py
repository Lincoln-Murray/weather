from flask import Flask, render_template, request
import requests as r

app = Flask(__name__)

location = ''

@app.route("/")
def index():
    with open('/etc/secrets/Secret_key') as secret_key: key = str(secret_key.read())  

    url = 'http://api.weatherapi.com/v1/forecast.json?key=' + key + '&q=' + location + '&days=3&aqi=yes&alerts=yes'

    response = r.get(url)

    if str(response) == '<Response [200]>':
        if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
            return render_template('index_m.html', json = response.json())
        else:
            return render_template('index.html', json = response.json())
    elif location == '':
        return render_template('loading_location.html')
    else:
        if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
            return render_template('error_m.html', json = response.json())
        else:
            return render_template('error.html', json = response.json())


@app.route("/positions", methods=['POST'])
def positions():
    global location
    location_response = request.get_json()
    location = str(location_response['latitude']) + ', ' + str(location_response['longitude'])
    return index()

@app.errorhandler(Exception)
def page_not_found(error):
    if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
        return render_template('error_m.html', error_message=error)
    else:
        return render_template('error.html', error_message=error)
