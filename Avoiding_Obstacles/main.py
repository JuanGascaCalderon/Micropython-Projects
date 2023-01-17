from machine import Pin, PWM #importing PIN and PWM
import time #importing time
from SERVO import Servo
from HCSR04 import HCSR04 

frequency = 240
duty = 400
duty2 = 500
duty3 =300
duty4 = 200

# Defining motor pins
motor1 = PWM((Pin(4, Pin.OUT)), frequency)
motor2 = PWM((Pin(16, Pin.OUT)), frequency)
motor3 = PWM((Pin(18, Pin.OUT)), frequency)
motor4 = PWM((Pin(19, Pin.OUT)), frequency)

# Defining ser motor and PWM
servoPin = Pin(15)
my_servo = Servo(servoPin, 50, 550, 2500, 180)
delay = 0.01
min = 0
max = 180
# Defining  Trigger and Echo pins
sensor = HCSR04(trigger_pin=23, echo_pin=22,echo_timeout_us=10000)


# Forward
def move_forward():
    motor1.duty(0)
    motor2.duty(duty2)
    motor3.duty(duty)
    motor4.duty(0)
    
# Backward
def move_backward():
    motor1.duty(duty)
    motor2.duty(0)
    motor3.duty(0)
    motor4.duty(duty)
    
#Turn Right
def turn_right():
    motor1.duty(0)
    motor2.duty(duty2)
    motor3.duty(0)
    motor4.duty(0)
    
#Turn Left
def turn_left():
    motor1.duty(0)
    motor2.duty(0)
    motor3.duty(duty2)
    motor4.duty(0)
   
#Stop
def stop():
    motor1.duty(0)
    motor2.duty(0)
    motor3.duty(0)
    motor4.duty(0)

#duty_cycle = 0 # Defining and initializing duty cycle PWM
#Defining function to set servo angle
my_servo.write_angle(40) 
while True:
    distance = sensor.distance_cm()
    #Defining direction based on conditions
    if distance <= 15:
        stop()
        time.sleep_ms(250)
        move_backward()
        time.sleep(0.5)
        stop()
        time.sleep(0.5)
        my_servo.write_angle(0)    #RIGHT
        time.sleep(1)
        x=1
        time.sleep(1)
        right_distance=sensor.distance_cm()
        #print(right_distance)
        time.sleep(1)
        my_servo.write_angle(90)    #FRONT
        time.sleep(1)
        x=0
        time.sleep(1) 
        left_distance=sensor.distance_cm()
        #print(left_distance)
        time.sleep(0.5)
        my_servo.write_angle(180)    #LEFT
        time.sleep(1)
        x=0
        time.sleep(0.5)

        if right_distance > left_distance:
            turn_right()
            time.sleep_ms(1000)
            stop()
        else:
            turn_left()
            time.sleep_ms(1000)
            stop()
    else:
        move_forward()

    time.sleep_ms(500)


    
