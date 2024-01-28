from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/weather-info/<city_name>')
def weather_info(city_name):

    return render_template('weather-info.html', city_name=city_name)