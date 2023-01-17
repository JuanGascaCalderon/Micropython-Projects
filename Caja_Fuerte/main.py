from machine import Pin, PWM, SoftI2C
from time import sleep, sleep_ms
from lcd_api import LcdApi
from i2c_ldc import I2cLcd

I2C_ADDR = 0x27 
totalRows = 2 
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

Filas = [15,2,4,5]
for i in range (4):
    Pin(Filas[i], Pin.OUT)
    
Columnas = [18,19,13,12]

col1 = Pin(Columnas[0],Pin.IN,Pin.PULL_DOWN)
col2 = Pin(Columnas[1],Pin.IN,Pin.PULL_DOWN)
col3 = Pin(Columnas[2],Pin.IN,Pin.PULL_DOWN)
col4 = Pin(Columnas[3],Pin.IN,Pin.PULL_DOWN)



contraseña= ["1", "2", "3", "4", "5", "6"]
caja_fuerte= []
led= Pin(32, Pin.OUT)
led.value(0)

led2= Pin(33, Pin.OUT)
led2.value(0)

lcd.move_to(0,0)
lcd.putstr("GET PASSWORD")

def lectura(FILAS, CARACTERES):
    EnFilas = Pin(FILAS, Pin.OUT)
    EnFilas.on()
 
    if(col1.value()==1):
        a = str(CARACTERES[0])
        caja_fuerte.append(a)
        lcd.clear()
        lcd.putstr(caja_fuerte)
    if(col2.value()==1):
        a = str(CARACTERES[1])
        caja_fuerte.append(a)
        lcd.clear()
        lcd.putstr(caja_fuerte)
    if(col3.value()==1):
        a = str(CARACTERES[2])
        caja_fuerte.append(a)
        lcd.clear()
        lcd.putstr(caja_fuerte)
    if(col4.value()==1):
        a = str(CARACTERES[3])
        caja_fuerte.append(a)
        lcd.clear()
        lcd.putstr(caja_fuerte)
    EnFilas.off()

Motion_Detected = False  #Global variable to hold the state of motion sensor

def handle_interrupt(pin): #defining interrupt handling function
    global Motion_Detected
    Motion_Detected = True
    global interrupt_pin
    interrupt_pin = pin

PIR_Interrupt=Pin(27,Pin.IN,Pin.PULL_DOWN)
#Attach external interrupt to GPIO13 and rising edge as an external event source
PIR_Interrupt.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    estado = PIR_Interrupt.value()
    sleep_ms(10)
    if(estado == 1):
        led2.value(1)
    if(estado == 0 ):
        led2.value(0)

    lectura(Filas[0], ["1","2","3","A"])
    lectura(Filas[1], ["4","5","6","B"])
    lectura(Filas[2], ["7","8","9","C"])   
    lectura(Filas[3], ["*","0","#","D"])
    sleep (0.1)
    
    if contraseña == caja_fuerte:
        lcd.clear()
        lcd.move_to(5,0)
        lcd.putstr("RIGHT")
        lcd.move_to(4,1)
        lcd.putstr("PASSWORD")
        led.value(1)
        caja_fuerte.clear()
    elif len(caja_fuerte) == 6:
        lcd.clear()
        lcd.move_to(6,0)
        lcd.putstr("WRONG")
        lcd.move_to(4,1)
        lcd.putstr("PASSWORD")
        caja_fuerte.clear()
    elif len(caja_fuerte) == 1:
        led.value(0)
    
