#create weather app using API
from multiprocessing import Condition
import tkinter as tk
import time
from tkinter import font
import requests

#function to get JSON 
def getweather():
    cityname = textfield.get()
    apicall = "https://api.openweathermap.org/data/2.5/weather?q=" +cityname+ "&appid=1a39fad784dc2505bd8df8c31af4491c"
    json_data = requests.get(apicall).json() #get api data
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']


#create GUI canvas
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Andy Weather App")

#define fonts to use in the canvas
font1 = ("poppins",15, "bold")
font2 = ("poppins",35, "bold")

#create user entry field for the search
textfield = tk.Entry(canvas,font = font2)
textfield.pack(pady=20)
textfield.focus()

#creating labels to show data
label1 = tk.Label(canvas, font = font2)
label1.pack()
label2 = tk.Label(canvas, font = font1)
label2.pack()
