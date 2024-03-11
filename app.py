from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/weather-info')
def weather_info():
    state_id = request.form.get('state_id')

    response = requests.get(f'https://api.weather.gov/alerts/active/area/{state_id}').json()

    features = response['features']

    alerts = {}

    for feature in features:
        areaDesc = feature['properties']['areaDesc']
        headline = feature['properties']['headline']
        alerts[areaDesc] = headline

    return render_template('weather-info.html', state_id=state_id, alerts=alerts)