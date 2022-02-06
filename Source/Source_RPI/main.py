import Resources.leds as myLeds
import Resources.camera as myCamera
import Resources.serial as mySerial

import RPi.GPIO as GPIO
import csv
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import mpld3
import json
import neopixel, board

# Setup path variables
projBasePath = '/home/pi/CatFoodMonitor/Source_RPI/Output/'
csvDataFile = projBasePath + 'catfooddata.csv'
jsonGraphFile = projBasePath + 'mpld3.json'

# Setup usb Port variables
USB0 = 'USB0'
USB1 = 'USB1'


def collectImages():
    lastweight0 = 500
    lastweight1 = 500
    while True:
        USB0_weight = mySerial.getReading('/dev/tty' + USB0)
        USB1_weight = mySerial.getReading('/dev/tty' + USB1)

        if ((lastweight0 - USB0_weight) > 0.5) or ((lastweight1 - USB1_weight) > 0.5):
            myLeds.fadeOn(maxBrightness=150, delay = 2)
            myCamera.takePic()
            myLeds.fadeOff(maxBrightness=150, delay = 2)

        lastweight0 = USB0_weight
        lastweight1 = USB1_weight


    return



def getserialdata():
    
    # create new csv file and write header line
    with open(csvDataFile, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter = ',')
        filewriter.writerow(["time", USB0, USB1])
    
    while True:

        # get readings
        USB0_weight = mySerial.getReading('/dev/tty' + USB0)
        USB1_weight = mySerial.getReading('/dev/tty' + USB1)

        # get time
        curtime = datetime.datetime.now()
        curtime = curtime.strftime("%Y-%m-%d %H:%M:%S")

        # open csv file to add data
        with open(csvDataFile, 'a+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter = ',')

            # write row and delay
            filewriter.writerow([np.datetime64(curtime), USB0_weight, USB1_weight])
            time.sleep(4)
        
        # create and graph to be displayed on website
        genGraph()

    return


def genGraph():

    # Reads csv data file
    array = genfromtxt(csvDataFile, dtype=['datetime64[s]', float, float], delimiter=',', names=True)

    # Only create graph if we have at least 2 lines of data to prevent
    # a 1D array from being used and causing errors since this graph is expecting a 2D array.
    if array.ndim >= 1:

        fig, ax = plt.subplots()
        ax.plot_date(array['time'], array[USB0], label=USB0)
        ax.plot_date(array['time'], array[USB1], label=USB1)
        ax.legend()

        # Save graph to json format so it can be embedded on website and close
        mpld3.save_json(fig, jsonGraphFile)
        plt.close()

    return

# def getReading(port):
#     ser = serial.Serial(port, 9600)
#     weight = ser.readline().rstrip()
#     weight = float(str(weight)[2:-1])
#     time.sleep(1)
#     return weight



    
    
if __name__ == '__main__':
    print("hi")
    collectImages()
#     getserialdata()

