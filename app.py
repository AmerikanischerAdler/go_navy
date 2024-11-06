#!/opt/homebrew/bin/python3.11

import requests
from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# History
@app.route('/history')
def gallery():
    return render_template('history.html')

@app.route('/interests')
def interests():
    return render_template('interests.html')

@app.route('/aspirations')
def aspirations():
    return render_template('aspirations.html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/father')
def father():
    return render_template('father.html')

@app.route('/ggpa')
def ggpa():
    return render_template('ggpa.html')

@app.route('/sarlo')
def sarlo():
    return render_template('sarlo.html')

@app.route('/kindergarten')
def kindergarten():
    return render_template('kindergarten.html')

@app.route('/seals')
def seals():
    return render_template('seals.html')

@app.route('/sumsem')
def sumsem():
    return render_template('sumsem.html')

# Student
@app.route('/student')
def profile():
    return render_template('nass.html')

# Career
@app.route('/career')
def sign():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)

