"""
En primer lugar, se importa la clase SoftI2C y Pin del módulo de la máquina.
Además, se importa LcdApi de la biblioteca lcd_api  para cargar 
en la ESP32 e I2clcd de la biblioteca i2c_lcd.
"""
import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

I2C_ADDR = 0x27 #the address of your LCD I2C device
#specify the number of rows and columns on the screen,
#in our case, we are using a LDC 16x2
totalRows = 2 
totalColumns = 16

#initialize the SoftI2C method for ESP32 by giving it three arguments.
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

#This line is used to initialize the I2C connection for the library by creating an 'lcd' object.
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    lcd.clear() #Erase all characters or anything written on the screen
    lcd.move_to(0,0) #Move to position based on row and col values
    lcd.putstr("Juan Gasca") # Send a string of characters to the screen
    lcd.move_to(0,1) 
    lcd.putstr("Aprendiz")
    for i in range(21): #for loop to count for age
        lcd.move_to(12,1) #Move to position based on row and col values
        #Converts an integer value to a character string to display on the screen
        lcd.putstr(str(i)) 
        time.sleep(1) #time to show
    
    lcd.clear() #Erase all characteres before
    lcd.move_to(0,0) #Move to position initial of LCD
    lcd.putstr("Feliz Cumpleanos") #Send a string of characters to the screen
    lcd.move_to(0,1) #Move to position initial of LCD but in the second row
    lcd.putstr("Juan Gasca") #Send a string of characters to the screen
    time.sleep(2) #time to show
    