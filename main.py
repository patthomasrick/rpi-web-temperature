#!/usr/bin/python3

# import RPi.GPIO as GPIO

import remi.gui as gui
from remi import start, App
from threading import Timer

# some constants
V_OUT_PIN = 11
PORT = 8081
ADDRESS = "10.48.125.105"

# GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
# GPIO.setup(V_OUT_PIN, GPIO.IN)

class TemperatureApp(App):
    def __init__(self, *args):
        super(TemperatureApp, self).__init__(*args)

    def main(self):
        self.count = 0
        self.lbl = gui.Label("Hello world!", width=100, height=30)

        self.display_temperature()

        # return the root of the widget
        return self.lbl

    def display_temperature(self):
        self.lbl.set_text(str(self.count))
        self.count += 1
        Timer(1, self.display_temperature).start()

start(
    TemperatureApp, 
    address=ADDRESS,
    port=PORT, 
    multiple_instance=False,
    enable_file_cache=True,
    update_interval=0.1, 
    start_browser=False
)
