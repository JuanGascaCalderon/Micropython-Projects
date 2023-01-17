from machine import Pin, PWM
import time

frequency = 240
duty_2 = 1023
duty_3 = 850 
duty = 950
duty_4 = 700
time_1 = 1650
time_2 = 500
time_3 = 700
time_4 = 250
time_5 = 220
motorA = PWM((Pin(13, Pin.OUT)), frequency)
motorB = PWM((Pin(12, Pin.OUT)), frequency)
motorC = PWM((Pin(27, Pin.OUT)), frequency)
motorD = PWM((Pin(26, Pin.OUT)), frequency)

def motor_1(on, off): #IZQUIERDO
    motorA.duty(on)
    motorB.duty(off)

def motor_2(on, off): #DERECHO
    motorC.duty(on)
    motorD.duty(off)

while True:
    motor_1(duty_2,0) #Forward
    motor_2(duty_3,0)
    time.sleep_ms(time_1)
    motor_1(0,0)#Stop
    motor_2(0,0)
    time.sleep_ms(time_4)
    motor_1(0,duty_2) #Left
    motor_2(duty,0)
    time.sleep_ms(time_4)
    motor_1(0,0)#Stop
    motor_2(0,0)
    time.sleep_ms(time_4)
    motor_1(duty,0) #Forward
    motor_2(duty,0)
    time.sleep_ms(time_3)
    motor_1(0,duty_2) #Left
    motor_2(duty,0)
    time.sleep_ms(time_5)
    motor_1(0,0) #Stop
    motor_2(0,0)
    time.sleep_ms(time_2)
    motor_1(duty_2,0) #Forward
    motor_2(duty_3,0)
    time.sleep_ms(time_1)
