from machine import Pin, PWM
import time

time_1 = 1500
time_2 = 500
time_3 = 500

#frequency = 240
"""motorA = PWM(Pin(13, Pin.OUT), frequency)
motorA.duty(512)
motorB = PWM(Pin(12, Pin.OUT), frequency)
motorB.duty(512)
motorC = PWM(Pin(27, Pin.OUT), frequency) 
motorC.duty(512)
motorD = PWM(Pin(26, Pin.OUT), frequency)
motorD.duty(512)"""

motorA = (Pin(13, Pin.OUT))
motorB = (Pin(12, Pin.OUT))
motorC = (Pin(27, Pin.OUT))
motorD = (Pin(26, Pin.OUT))

def motor_1(on, off):
    motorA.value(on)
    motorB.value(off)

def motor_2(on, off):
    motorC.value(on)
    motorD.value(off)

while True:
    motor_1(1,0) #Forward
    motor_2(1,0)
    time.sleep_ms(time_1)
    motor_1(0,0) #Stop
    motor_2(0,0) 
    time.sleep_ms(time_2)
    motor_1(1,0) #Left
    motor_2(0,1)
    time.sleep_ms(time_2)
    motor_1(0,0) #Stop
    motor_2(0,0)
    time.sleep_ms(time_2)
    motor_1(1,0) #Forward
    motor_2(1,0)
    time.sleep_ms(time_3)
    motor_1(0,0) #Stop
    motor_2(0,0)
    time.sleep_ms(time_2)
    motor_1(1,0) #Left
    motor_2(0,1)
    time.sleep_ms(time_2)
    motor_1(0,0) #Stop
    motor_2(0,0) 
    time.sleep_ms(time_2)
    motor_1(1,0) #Forward
    motor_2(1,0)
    time.sleep_ms(time_1)
