from flask import Flask, render_template, request
import requests
import os
import pycountry

app = Flask(__name__)

KEY = os.getenv('API_KEY')

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/weather-info')
def weather_info():
    # get city and state info
    city_id = request.form.get('city_id')
    state_prov_id = request.form.get('state/prov_id')

    # get country info
    country_id = request.form.get('country_id')
    identified_countries = pycountry.countries.search_fuzzy(country_id)
    country_code = identified_countries[0].alpha_2

    geocode_list = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_id},{state_prov_id},{country_code}&appid={KEY}').json()

    weather_info = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={geocode_list[0]["lat"]}&lon={geocode_list[0]["lon"]}&units=imperial&appid={KEY}').json()

    if state_prov_id != None:
        return render_template('weather-info.html', city_id=city_id, country_id=country_id, state_prov_id=state_prov_id, weather_info=weather_info)
    else:
        return render_template('weather-info.html', city_id=city_id, country_id=country_id, weather_info=weather_info)