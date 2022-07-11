# Kevin Kraatz
# Weather App
# Sources -

from tkinter import *
from tkinter import ttk
import datetime, json, requests, conditions, radar, forecast

# Home GUI
root = Tk()
root.geometry("900x400")
root.resizable(0, 0)
root.title("Sun Buddy | Weather App")


def get_datetime():
    return str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day) + "-" + str(
        datetime.datetime.now().year)


location_input = StringVar()


def forecast_win():
    user_location = location_input.get()

    url = "http://api.openweathermap.org/data/2.5/forecast?zip=" \
          + user_location + ",us&appid=ab66a8bea15a972a3a415f37d5393bd2"

    r = requests.get(url)
    data = r.json()


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
search_button = Button(search_frame, text="Submit", command=forecast_win)
search_button.pack(side="right", anchor="s")

# Forecast GUI
forecast_frame = Toplevel()
forecast_box = Frame(forecast_frame)
forecast_box.pack(fill="both")
tfield = Text(forecast_box)
tfield.insert(INSERT, data)
tfield.pack(fill=X, padx=20)
radar_button = Button(forecast_box, text="Radar", command=radar.radar_win)
radar_button.pack(anchor="sw")

root.mainloop()
