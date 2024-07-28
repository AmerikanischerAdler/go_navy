#!/opt/homebrew/bin/python3.11

import requests
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/history')
def gallery():
    return render_template('history.html')

@app.route('/student')
def profile():
    return render_template('nass.html')

@app.route('/career')
def sign():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)

