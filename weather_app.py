# Kevin Kraatz
# Weather App
# Sources -

import datetime
import requests
from tkinter import *
from tkintermapview import TkinterMapView

# Home GUI
root = Tk()
root.geometry("900x400")
root.resizable(0, 0)
root.title("Sun Buddy | Weather App")


def get_datetime():
    return str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "-" + str(
        datetime.datetime.now().year)


location_input = StringVar()


def get_forecast():
    user_location = location_input.get()

    url = "http://api.openweathermap.org/data/2.5/forecast?zip=" \
          + user_location + ",us&appid=ab66a8bea15a972a3a415f37d5393bd2"

    r = requests.get(url)
    data = r.json()

    forecast_frame = Toplevel()
    forecast_frame.geometry("1500x600")

    date_box2 = Label(forecast_frame, text=get_datetime(), borderwidth=1, relief="solid")
    date_box2.pack(side="left", anchor="nw", ipadx=5, ipady=5, padx=20, pady=10)

    back_btn = Button(forecast_frame, text="Back", command=forecast_frame.destroy)
    back_btn.pack(side="right", anchor="ne", ipadx=5, ipady=5, padx=20, pady=10)

    zip_code = Label(forecast_frame, text="5-Day Forecast For Zip Code: " + user_location)
    zip_code.pack(side="top", pady=10)

    forecast_box = Frame(forecast_frame)
    forecast_box.pack(fill=X, anchor="center", pady=40)
    week_frame = Text(forecast_box)
    week_frame.insert(INSERT, data)
    week_frame.pack(fill=X, side="bottom", anchor="s", padx=20)

    radar_button = Button(forecast_frame, text="Radar", command=get_radar)
    radar_button.pack(side="left", anchor="sw", ipadx=5, ipady=5, padx=20, pady=30)

    radar_button = Button(forecast_frame, text="Current Conditions")
    radar_button.pack(side="right", anchor="se", ipadx=5, ipady=5, padx=20, pady=30)

    location_search.delete(0, "end")


def get_radar():
    radar_frame = Toplevel()
    radar_frame.geometry("900x900")
    radar_box = TkinterMapView(radar_frame)
    radar_box.pack(fill="both", expand=True)
    radar_box.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en")


# Home features
home_frame = Frame(root)
home_frame.pack(fill=X)

date_box = Label(home_frame, text=get_datetime(), borderwidth=1, relief="solid")
date_box.pack(side="left", anchor="nw", ipadx=5, ipady=5, padx=20, pady=10)

app_head = Label(home_frame, text="Sun Buddy", borderwidth=1, relief="solid")
app_head.pack(side="right", anchor="ne", ipadx=5, ipady=5, padx=20, pady=10)

app_logo = Canvas(home_frame, width=195, height=195)
app_logo.pack(anchor="center", pady=30)
img = PhotoImage(file="logo.png")
app_logo.create_image(100, 100, image=img)

search_frame = Frame(root, width=400)
search_frame.pack()

location_head = Label(search_frame, text="Enter Zip Code:")
location_head.pack(pady=10)

location_search = Entry(search_frame, textvariable=location_input)
location_search.pack(side="left", anchor="center", padx=5)
search_button = Button(search_frame, text="Submit", command=get_forecast)
search_button.pack(side="right", anchor="s")

# Forecast GUI


root.mainloop()
