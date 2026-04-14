from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import requests
import os

#region App Setup
app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = os.urandom(20)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./Backend/drinks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

FASTAPI_URL = "http://127.0.0.1:8000"
#endregion

#region Standard Drinks
@app.route('/')
def home():
    response = requests.get(f"{FASTAPI_URL}/drinks/")
    drinks = response.json()
    return render_template("home.html", drinks=drinks)

@app.rout('/login')

@app.rout('/user/<username>')
def show_user_profile(username):

@app.rout('/itinerary')

@app.rout('/itinerary/<int:itinerary_id>')

@app.rout('/budget')

@app.rout('/map')


if __name__ == "__main__":
    app.run(debug=True)
