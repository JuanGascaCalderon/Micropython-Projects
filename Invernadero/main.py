from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_ldc import I2cLcd
from time import sleep 
import dht
sensor= dht.DHT11(Pin(27))
vent= Pin(13, Pin.OUT)
bom= Pin (12,Pin.OUT)
I2C_ADDR = 0x27 
totalRows = 2 
totalColumns = 16


i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)


lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


while True:
        sleep(2)
        sensor.measure()
        temp=sensor.temperature()
        hum= sensor.humidity()
        print('temperatura:%3.1fC'%temp)
        print('humedad:%3.1fC'%hum)
        hum = str(hum) #Int to string
        temp = str(temp)
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("temperatura:"+temp+"c")
        lcd.move_to(0,1)
        lcd.putstr("humedad::"+hum+"%")
        sleep(4)

    
        if temp>"28" and temp< "40" :
            vent.value(0)
            bom.value(1)
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("  ventilacion ")
            lcd.move_to(0,1)
            lcd.putstr("    activa")
            sleep(4)
                
        if temp<="28":
            bom.value(0)
            vent.value(1)
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("  calefaccion ")
            lcd.move_to(0,1)
            lcd.putstr("    activa")
            sleep
        else:
            
            sleep(3)
    

