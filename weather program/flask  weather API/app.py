from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests 


app = Flask (__name__)



@app.route('/')
def index():
    
    cityname = "london"
    apicall = "https://api.openweathermap.org/data/2.5/weather?q=" +cityname+ "&appid=1a39fad784dc2505bd8df8c31af4491c"
    json_data = requests.get(apicall).json() #get api data

    #create a dictionary to store the weather conditions
    condition = {
        "cityname":cityname,
        "temperture":json_data['main']['temp'],
        "description":json_data['weather'][0]['description'],
        "icon":json_data['weather'][0]['icon']
    }
    print(condition)

    return render_template ('index.html')


if __name__ == "__main__":
    app.run(debug=True)