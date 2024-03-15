from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/weather-info')
def weather_info():
    city_id = request.form.get('city_id')
    country_id = request.form.get('country_id')
    state_prov_id = request.form.get('state/prov_id')

    # response = requests.get(f'https://api.weather.gov/alerts/active/area/{state_id}').json()

    if state_prov_id != None:
        return render_template('weather-info.html', city_id=city_id, country_id=country_id, state_prov_id=state_prov_id)
    else:
        return render_template('weather-info.html', city_id=city_id, country_id=country_id)