from dht import DHT11
from machine import Pin,SoftI2C
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

#LCD
I2C_ADDR = 0x27 #the address of your LCD I2C device
#specify the number of rows and columns on the screen,
totalRows = 2 
totalColumns = 16
#initialize the SoftI2C method for ESP32 by giving it three arguments.
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
#This line is used to initialize the I2C connection for the library by creating an 'lcd' object.
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
#SENSOR DE TEMPERATURA
sensorDHT = DHT11 (Pin(15))

while (True):
    sleep (1)
    sensorDHT.measure() #Se conecta con el sensor y realiza la medición
    temp=sensorDHT.temperature() # Devuelve el valor de temperatura medido, en grados centígrados.
    hum=sensorDHT.humidity()#Devuelve el valor de humedad relativa medido, en porcentaje.
    lcd.clear() #Erase all characters or anything written on the screen
    lcd.move_to(0,0) #Move to position based on row and col values
    hum = str(hum) #Int to string
    temp = str(temp)
    lcd.putstr("Temperatura:"+temp+"C") # Send a string of characters to the screen
    lcd.move_to(0,1) #Move to position based on row and col values
    lcd.putstr("Humdedad: "+hum+"%") # Send a string of characters to the screen