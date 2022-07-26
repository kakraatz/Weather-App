# some code adapted from: https://realpython.com/python-sockets/
import socket
import json
from datetime import date, timedelta


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 5000))
    s.listen()
    while True:

        conn, addr = s.accept()

        output = ""
        input = json.loads(conn.recv(1024).decode())

        # add day
        if input["0"] == "Day 1":
            output += "Today: \n"

        else:
            date_offset = (int(input["0"][4]) - 1)
            day = (date.today() + timedelta(days=date_offset))

            output += (day.strftime("%A") + ": \n")

        # add weather
        output += ("\n Weather conditions: \n\n " + input["1"][0] + "\n")

        # add temp
        output += ("\n With a " + input["1"][1] + "\n and a " + input["1"][2])

        conn.sendall(bytes(output, 'utf-8'))
