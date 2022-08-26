#create weather app using API
import tkinter as tk
import time
import requests

#create GUI canvas
canvas = tk.TK()
canvas.geometry("600*500")
canvas.tittle("Andy Weather App")

#define fonts to use in the canvas
font1 = ("poppins",15, "bold")
font2 = ("poppins",35, "bold")