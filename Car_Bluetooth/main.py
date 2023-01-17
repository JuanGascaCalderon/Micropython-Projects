from machine import Pin,PWM
import bluetooth
from BLE import BLEUART
import time #importing time

frequency = 240
duty = 320
duty2 = 300

# Defining motor pins
motorA = PWM((Pin(13, Pin.OUT)), frequency)
motorB = PWM((Pin(12, Pin.OUT)), frequency)
motorC = PWM((Pin(27, Pin.OUT)), frequency)
motorD = PWM((Pin(26, Pin.OUT)), frequency)


#Init Bluetooth - instances objects
name = 'ESP32' #Bluetooth name's
ble = bluetooth.BLE() #Instance the library
uart = BLEUART(ble,name) #Using library and instances parameters


#Functions
def motor_1(on, off): #LEFT
    motorA.duty(on)
    motorB.duty(off)

def motor_2(on, off): #RIGHT
    motorC.duty(on)
    motorD.duty(off)

#Bluetooth RX event
#Get and set mesagges
def on_rx():
    #Serial comunication
    # Read = read the message, decode = decodifing the message and strip = eliminate spaces
    rx_buffer = uart.read().decode().strip #Transmit and receive messages
    uart.write('ESP32 says: ' + str(rx_buffer)+'\n') #Return the value of rx_buffer

    #Logic to turn on a led
    if rx_buffer == 'A':
        motor_1(duty,0) #FORWARD
        motor_2(duty2,0)
    if rx_buffer == 'B':
        motor_1(0,duty) #BACKWARD
        motor_2(0,duty2)
    if rx_buffer == 'C':
        motor_1(0,duty) #LEFT
        motor_2(duty2,0)
    if rx_buffer == 'D':
        motor_1(duty,0) #RIGHT
        motor_2(0,duty2)    
    if rx_buffer == 'F':
        motor_1(0,0) #RIGHT
        motor_2(0,0)  

#Register Bluetooth event
uart.irq(handler = on_rx)