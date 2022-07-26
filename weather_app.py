# Kevin Kraatz
# Sun Buddy Weather App
# CS361 Summer 2022 Individual Project

# Code and Info Sources:  - Weather data sourced from openweathermap.org API's.
#                         - Radar/map module sourced from https://github.com/TomSchimansky/TkinterMapView
#                         - Radar/map tiles sourced from Google Maps API and openweathermap.org Maps API
#                         - Tkinter/JSON/Requests information sourced from https://requests.readthedocs.io/en/latest/,
#                           https://docs.python.org/3/library/tkinter.html, https://docs.python.org/3/library/json.html

# Module imports
import datetime
import requests
import json
from tkinter import *
from tkintermapview import TkinterMapView
import microservice.send


# Main GUI Initialization
root = Tk()
root.geometry("900x400")
root.resizable(0, 0)
root.title("Sun Buddy | Weather App")


# -------#########################-------#
# -------# Application processes #-------#
# -------#########################-------#

def get_date():
    """Returns today's date in mmddyyyy format."""
    return str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "-" + str(
        datetime.datetime.now().year)


location_input = StringVar()


def get_forecast():
    """Takes user input zip code and fetches weather data from openweathermap.org API.
    Zip code entered must be valid in US, otherwise an error message will display.
    The data is returned in JSON format, and is parsed into daily weather data forecasts.
    The new Tkinter window displays the 7-day forecast, a button to close the window,
    a button to view the weather radar, and a button for all current conditions for the location."""
    user_location = location_input.get()
    save_zip = user_location

    url_zip = "http://api.openweathermap.org/data/2.5/forecast?zip=" \
              + str(user_location) + ",us&appid=ab66a8bea15a972a3a415f37d5393bd2"
    zr = requests.get(url_zip)
    loc_data = zr.json()

    if loc_data["cod"] == "400" or loc_data["cod"] == "404":
        error_frame = Toplevel()
        error_frame.geometry("200x100")
        error_frame.resizable(0, 0)
        error_msg = Label(error_frame, text="Please enter a valid location!")
        error_msg.pack(anchor="center")
        back_btn = Button(error_frame, text="Back", command=error_frame.destroy)
        back_btn.pack(pady=10)
        location_search.delete(0, "end")
        return

    lat = loc_data["city"]["coord"]["lat"]
    long = loc_data["city"]["coord"]["lon"]
    exclude = "minutely,hourly,alerts"
    url = "http://api.openweathermap.org/data/3.0/onecall?lat=" \
          + str(lat) + "&lon=" + str(long) + "&exclude=" + str(
        exclude) + "&units=imperial&appid=ab66a8bea15a972a3a415f37d5393bd2"

    r = requests.get(url)
    data = r.json()

    temp_high = []
    temp_low = []
    condition = []

    for i in (data["daily"]):
        temp_high.append(int(i["temp"]["max"]))
        temp_low.append(int(i["temp"]["min"]))
        condition.append(i["weather"][0]["main"])

    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    values = []
    for i in range(0, len(condition) - 1):
        values.append(
            (condition[i], ("high of " + str(temp_high[i]) + "\xb0F"), "low of " + str(temp_low[i]) + "\xb0F"))

    forecast = list(dict(zip(days, values)).items())
    day_1_fc = dict(enumerate(forecast[0]))
    day_1_fc = json.dumps(day_1_fc, indent=2)
    day_1_fc = microservice.send.microservice(day_1_fc)

    day_2_fc = dict(enumerate(forecast[1]))
    day_2_fc = json.dumps(day_2_fc, indent=2)
    day_2_fc = microservice.send.microservice(day_2_fc)

    day_3_fc = dict(enumerate(forecast[2]))
    day_3_fc = json.dumps(day_3_fc, indent=2)
    day_3_fc = microservice.send.microservice(day_3_fc)

    day_4_fc = dict(enumerate(forecast[3]))
    day_4_fc = json.dumps(day_4_fc, indent=2)
    day_4_fc = microservice.send.microservice(day_4_fc)

    day_5_fc = dict(enumerate(forecast[4]))
    day_5_fc = json.dumps(day_5_fc, indent=2)
    day_5_fc = microservice.send.microservice(day_5_fc)

    day_6_fc = dict(enumerate(forecast[5]))
    day_6_fc = json.dumps(day_6_fc, indent=2)
    day_6_fc = microservice.send.microservice(day_6_fc)

    day_7_fc = dict(enumerate(forecast[6]))
    day_7_fc = json.dumps(day_7_fc, indent=2)
    day_7_fc = microservice.send.microservice(day_7_fc)

    forecast_frame = Toplevel()
    forecast_frame.geometry("1500x400")
    forecast_frame.resizable(0, 0)

    date_box = Label(forecast_frame, text=get_date(), borderwidth=1, relief="solid")
    date_box.pack(side="left", anchor="nw", ipadx=5, ipady=5, padx=20, pady=10)

    back_btn = Button(forecast_frame, text="Back", command=forecast_frame.destroy)
    back_btn.pack(side="right", anchor="ne", ipadx=5, ipady=5, padx=20, pady=10)

    forecast_head = Label(forecast_frame, text="7-Day Forecast For Zip Code: " + user_location)
    forecast_head.pack(side="top", pady=10)

    forecast_box = Frame(forecast_frame)
    forecast_box.pack(fill=X, anchor="center", pady=40)
    week_frame = Frame(forecast_box)
    week_frame.pack(fill=X, side="bottom", anchor="s", padx=20)
    day_frame1 = Text(week_frame, width=22, height=10)
    day_frame1.insert(INSERT, day_1_fc)
    day_frame1.grid(row=0, column=0)
    day_frame2 = Text(week_frame, width=22, height=10)
    day_frame2.insert(INSERT, day_2_fc)
    day_frame2.grid(row=0, column=1)
    day_frame3 = Text(week_frame, width=22, height=10)
    day_frame3.insert(INSERT, day_3_fc)
    day_frame3.grid(row=0, column=2)
    day_frame4 = Text(week_frame, width=22, height=10)
    day_frame4.insert(INSERT, day_4_fc)
    day_frame4.grid(row=0, column=3)
    day_frame5 = Text(week_frame, width=22, height=10)
    day_frame5.insert(INSERT, day_5_fc)
    day_frame5.grid(row=0, column=4)
    day_frame6 = Text(week_frame, width=22, height=10)
    day_frame6.insert(INSERT, day_6_fc)
    day_frame6.grid(row=0, column=5)
    day_frame7 = Text(week_frame, width=22, height=10)
    day_frame7.insert(INSERT, day_7_fc)
    day_frame7.grid(row=0, column=6)

    radar_button = Button(forecast_frame, text="Weather Radar", command=lambda: get_radar(save_zip))
    radar_button.pack(side="left", anchor="sw", ipadx=5, ipady=5, padx=20, pady=30)

    conditions_button = Button(forecast_frame, text="Current Conditions",
                               command=lambda: get_current_conditions(save_zip))
    conditions_button.pack(side="right", anchor="se", ipadx=5, ipady=5, padx=20, pady=30)

    location_search.delete(0, "end")


def get_radar(zipcode):
    """"""
    user_location = zipcode
    url_zip = "http://api.openweathermap.org/data/2.5/forecast?zip=" \
              + str(user_location) + ",us&appid=ab66a8bea15a972a3a415f37d5393bd2"
    zr = requests.get(url_zip)
    loc_data = zr.json()

    lat = loc_data["city"]["coord"]["lat"]
    long = loc_data["city"]["coord"]["lon"]

    radar_frame = Toplevel()
    radar_frame.geometry("900x900")
    radar_frame.resizable(0, 0)

    radar_box = TkinterMapView(radar_frame)
    radar_box.pack(fill="both", expand=True)
    radar_box.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    radar_box.set_overlay_tile_server("https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{"
                                      "y}.png?appid=ab66a8bea15a972a3a415f37d5393bd2")
    radar_box.set_position(lat, long)
    radar_box.set_zoom(9)


def get_current_conditions(zipcode):
    """Takes user input zip code and fetches current weather data from openweathermap.org API.
    The data is returned in JSON format. The new Tkinter window displays the current conditions for
    the given zip code and a button to close the window and return to the forecast window."""
    user_location = zipcode
    url_zip = "http://api.openweathermap.org/data/2.5/forecast?zip=" \
              + str(user_location) + ",us&appid=ab66a8bea15a972a3a415f37d5393bd2"
    zr = requests.get(url_zip)
    loc_data = zr.json()

    lat = loc_data["city"]["coord"]["lat"]
    long = loc_data["city"]["coord"]["lon"]
    exclude = "minutely,hourly,daily,alerts"
    url = "http://api.openweathermap.org/data/3.0/onecall?lat=" \
          + str(lat) + "&lon=" + str(long) + "&exclude=" + str(
        exclude) + "&units=imperial&appid=ab66a8bea15a972a3a415f37d5393bd2"

    r = requests.get(url)
    data = json.loads(r.text)
    data = json.dumps(data, indent=2)

    current_conditions_frame = Toplevel()
    current_conditions_frame.geometry("900x500")
    current_conditions_frame.resizable(0, 0)

    date_box = Label(current_conditions_frame, text=get_date(), borderwidth=1, relief="solid")
    date_box.pack(side="left", anchor="nw", ipadx=5, ipady=5, padx=20, pady=10)

    back_btn = Button(current_conditions_frame, text="Back", command=current_conditions_frame.destroy)
    back_btn.pack(side="right", anchor="ne", ipadx=5, ipady=5, padx=20, pady=10)

    current_conditions_head = Label(current_conditions_frame, text="Current Weather For Zip Code: " + user_location)
    current_conditions_head.pack(side="top", pady=10)

    conditions_box = Frame(current_conditions_frame)
    conditions_box.pack(fill=X, anchor="center", pady=40)
    week_frame = Text(conditions_box)
    week_frame.insert(INSERT, data)
    week_frame.pack(fill=X, side="bottom", anchor="s", padx=20)


# -------#########################-------#
# -------# Main Page Processes #-------#
# -------#########################-------#

home_frame = Frame(root)
home_frame.pack(fill=X)

date_box = Label(home_frame, text=get_date(), borderwidth=1, relief="solid")
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

root.mainloop()
