import serial

def getReading(port):
    ser = serial.Serial(port, 9600)
    weight = ser.readline().rstrip()
    weight = float(str(weight)[2:-1])
    return weight
