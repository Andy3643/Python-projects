
from tkinter import NO
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import requests 


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://andydb:pass123@localhost/weather'
db= SQLAlchemy(app)


@app.route('/',methods =['GET','POST'])
def index():
    condition=None
    if request.method =="POST":
        cityname = request.form.get('baluku').upper()
        apicall = "https://api.openweathermap.org/data/2.5/weather?q=" +cityname+ "&appid=1a39fad784dc2505bd8df8c31af4491c"
        json_data = requests.get(apicall).json() #get api data

    #create a dictionary to store the weather conditions
        condition = {
            "cityname":cityname,
            "temperature":int(json_data['main']['temp']- 273.15 ),
            "description":json_data['weather'][0]['description'],
            "icon":json_data['weather'][0]['icon']
        }

    return render_template ('index.html',condition=condition)


if __name__ == "__main__":
    app.run(debug=True)