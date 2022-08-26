#create weather app using API
import json
from multiprocessing import Condition
from pickle import GET
import tkinter as tk
import time
from tkinter import font
import requests

#function to get JSON 
def getweather(canvas):
    cityname = textfield.get()
    apicall = "https://api.openweathermap.org/data/2.5/weather?q=" +cityname+ "&appid=1a39fad784dc2505bd8df8c31af4491c"
    json_data = requests.get(apicall).json() #get api data
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S",time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%H:%M:%S",time.gmtime(json_data['sys']['sunset']))

    final_info = condition + "\n" + str(temperature) + " degrees"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "Pressure" + str(pressure) + "\n" + "Humidity" + str(humidity) + "\n" + "Wind speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "Sunset: " + sunset 

    label1.config(text = final_info)
    label2.config(text = final_data)

#create GUI canvas
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Andy Weather App")

#define fonts to use in the canvas
font1 = ("poppins",15, "bold")
font2 = ("poppins",35, "bold")

#create user entry field for the search
textfield = tk.Entry(canvas,font = font2, justify = 'center')
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>',getweather)

#creating labels to show data
label1 = tk.Label(canvas, font = font2)
label1.pack()
label2 = tk.Label(canvas, font = font1)
label2.pack()
 
canvas.mainloop()