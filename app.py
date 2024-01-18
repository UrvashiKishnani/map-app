#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import random

DEVELOPMENT_ENV = True

GOOGLE_MAPS_API_KEY = 'API_KEY'

app = Flask(__name__)

app_data = {
    "name":         "Map App",
    "description":  "A Flask app using Google Maps API",
    "author":       "Urvashi Kishnani",
    "html_title":   "Map App",
    "project_name": "Map App",
    "keywords":     "flask, webapp, google, maps"
}

quotes = [
    '“Remember that happiness is a way of travel, not a destination.”',
    '“The world is a book and those who do not travel read only one page.”',
    '“Travel is the only thing you buy that makes you richer.”',
    '“My goal is to run out of pages in my passport.”',
    '“Not all those who wander are lost.”',
    '“Travel is an investment in yourself.”',
    '“The journey of a thousand miles begins with a single step.”',
    '“Some beautiful paths can’t be discovered without getting lost.”',
    '“Collect Moments, Not Things.”',
    '“Adventures are the best way to learn.”'
]


@app.route('/')
def index():
    rand_index = random.randint(0, len(quotes)-1)
    rand_quote = quotes[rand_index]
    return render_template('index.html', app_data=app_data, quote=rand_quote)


@app.route('/glance')
def glance():
    return render_template('glance.html', app_data=app_data)


@app.route('/advance')
def advance():
    return render_template('advance.html', app_data=app_data)


@app.route('/plans')
def plans():
    return render_template('plans.html', app_data=app_data)


if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)