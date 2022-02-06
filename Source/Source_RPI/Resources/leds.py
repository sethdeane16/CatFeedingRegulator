import time
import board
import neopixel


# Initialize neopixel object
pixels = neopixel.NeoPixel(
    pin = board.D12,                 # The pin to output neopixel data on.
    n = 8,                           # The number of neopixels in the chain.
    bpp = 4,                         # Bytes per pixele. 3 for RGB and 4 for RGBW pixles.
    brightness = 1,                  # Brigtness of the pixel between 0.0 and 1.0 where 1.0 is full brightness.
    auto_write = True,               # True if the neopixels should immediately change when set. If False, show must be called explicitly.
    pixel_order = neopixel.RGBW      # Set the pixel color channel order.
)


# fade leds on at a given delay and brightness
# -----
# maxBrightness (0-255): brightness of the LEDS
# delay (seconds): amount of time for the leds to achieve full brightness
def fadeOn(maxBrightness, delay):
    
    for i in range(0, maxBrightness):
        pixels.fill((0, 0, 0, i))
        time.sleep(delay/100)
    return


# fade leds on at a given delay and brightness
# -----
# maxBrightness (0-255): brightness of the LEDS
# delay (seconds): amount of time for the leds to achieve full brightness
def fadeOff(maxBrightness, delay):
    for i in range(maxBrightness, -1, -1):
        pixels.fill((0, 0, 0, i))
        time.sleep(delay/100)
    return

# turn off leds
# -----
def ledsOff():
    pixels.fill((0, 0, 0, 0))
    return
