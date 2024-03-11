from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/weather-info')
def weather_info():
    city_name = request.form.get('city_name')

    url = 'https://api.weather.gov/alerts/active/zone/'

    return render_template('weather-info.html', city_name=city_name)