# Kevin Kraatz
# Weather App
# Sources -

from tkinter import *
from tkinter import ttk
from tkinterweb import HtmlFrame
import folium
from datetime import datetime
import json, requests, conditions, radar, forecast
import os
import urllib.request


def get_radar():
    latitude = 0
    longitude = 0

    url = "https://tile.openweathermap.org/map/precipitation_new/0/0/0.png?appid=ab66a8bea15a972a3a415f37d5393bd2"

    m = folium.Map(location=[latitude, longitude], zoom_start=4, tiles="OpenStreetMap")
    folium.TileLayer(url, attr="openweathermap.org").add_to(m)
    m.save("test_map.html")


def radar_win():
    radar_frame = Toplevel()
    radar_box = HtmlFrame(radar_frame)
    get_radar()
    radar_box.load_url("file:///C:/Users/kakra/Desktop/OSU/5 - Summer 22/CS361/Weather-App/test_map.html")
    radar_box.pack(fill="both")
