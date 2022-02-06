from picamera import PiCamera
import os
from os import listdir
from os.path import isfile, join

path = '/home/pi/CatFoodMonitor/Images/'



camera = PiCamera()

camera.rotation = 180
camera.brightness = 60
camera.exposure_compensation = 10


# Add a single photo named pic#.jpg to Images folder.
def takePic():
    
    imageIndex = 0

    # if folder is not empty
    if len(os.listdir(path)) > 0:

        # Get the index of the last photo taken so we don't overwrite previous photos
        fileNames = [f for f in listdir(path) if isfile(join(path, f))]
        for i in range(len(fileNames)):
            fileNames[i] = int(fileNames[i][3:-4])
        imageIndex = max(fileNames) + 1

    # The number of photos we want to take this round
    imageName = 'pic' + str(imageIndex)
    camera.capture(path + imageName + '.jpg')
    
    return
