from machine import Pin,SoftI2C
from time import sleep_ms
from lcd_api import LcdApi
from i2c_lcd import I2cLcd


I2C_ADDR = 0x27 #the address of your LCD I2C device
#specify the number of rows and columns on the screen,
totalRows = 2 
totalColumns = 16

#initialize the SoftI2C method for ESP32 by giving it three arguments.
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

#This line is used to initialize the I2C connection for the library by creating an 'lcd' object.
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

from machine import Pin       #importing classes
from time import sleep    #Import sleep from time class

Motion_Detected = False  #Global variable to hold the state of motion sensor

def handle_interrupt(pin): #defining interrupt handling function
    global Motion_Detected
    Motion_Detected = True
    global interrupt_pin
    interrupt_pin = pin

led=Pin(19,Pin.OUT)   #setting GPIO14 led as output
PIR_Interrupt=Pin(13,Pin.IN)   # setting GPIO13 PIR_Interrupt as input
led2 = Pin(18,Pin.OUT)

#Attach external interrupt to GPIO13 and rising edge as an external event source
PIR_Interrupt.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)        

while True:
    if Motion_Detected:
        lcd.clear() #Erase all characters or anything written on the screen
        lcd.move_to(0,0) #Move to position based on row and col values
        lcd.putstr("Detect!") # Send a string of characters to the screen
        led2.value(1)
        sleep(8)
        led2.value(0)
        lcd.clear() #Erase all characters or anything written on the screen
        lcd.move_to(0,0) #Move to position based on row and col values
        lcd.putstr("Stop!") # Send a string of characters to the screen
        Motion_Detected = False
        
    else:
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)
        lcd.clear() #Erase all characters or anything written on the screen
        lcd.move_to(0,0) #Move to position based on row and col values
        lcd.putstr("No movimiento") # Send a string of characters to the screen