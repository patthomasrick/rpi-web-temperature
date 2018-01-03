#!/usr/bin/python3

import spidev

import remi.gui as gui
from remi import start, App
from threading import Timer

# some constants
PORT = 8081
ADDRESS = "10.48.125.105"

# SPI variables
DELAY = 0.1
LDR_CHANNEL = 0

# create SPI
spi = spidev.SpiDev()
spi.open(0, 0)


def readADC(adc_num):
    # read spi data from the MCP3008, 8 channels in total
    if (adc_num > 7) or (adc_num < 0):
        return -1

    r = spi.xfer2([1, 8+adc_num << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data


class TemperatureApp(App):
    def __init__(self, *args):
        super(TemperatureApp, self).__init__(*args)

    def main(self):
        # create label that will display the info
        self.lbl = gui.Label("Hello world!", width=100, height=30)

        # call the display temperature function
        self.display_temperature()

        # return the root of the widget
        return self.lbl

    def display_temperature(self):
        self.lbl.set_text(str(readADC(LDR_CHANNEL))
        Timer(DELAY, self.display_temperature).start()

start(
    TemperatureApp, 
    address=ADDRESS,
    port=PORT, 
    multiple_instance=False,
    enable_file_cache=True,
    update_interval=DELAY, 
    start_browser=False
)
