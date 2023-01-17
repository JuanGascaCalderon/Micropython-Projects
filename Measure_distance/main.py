#Distance of Ultrasonic

from machine import Pin
import time

# Defining  Trigger and Echo pins
trigger = Pin(33, Pin.OUT)
echo = Pin(32, Pin.IN)


def get_distance():
    #Sent a pulse to trigger and listen on echo pin
    trigger.value(0) #Stabilizer the sensor
    time.sleep_us(2000)
    trigger.value(1)
    time.sleep_us(5000)
    trigger.value(0)
    while echo.value() == 0:
        signaloff = time.ticks_us() #To get in mycroseconds
    while echo.value() == 1:
        signalon = time.ticks_us() #To get in microseconds
    timepassed = signalon - signaloff #To get the time of signal
    dist = (timepassed * 0.0343) / 2 # Get the distance
    return dist

while True:
    distance=get_distance()
    print("Distance", distance, "cm")