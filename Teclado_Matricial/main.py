from machine import Pin
from time import sleep

Filas = [13,12,14,27]
for i in range (4):
    Pin(Filas[i], Pin.OUT)
    
Columnas = [26,25,33,32]

col1 = Pin(Columnas[0],Pin.IN,Pin.PULL_DOWN)
col2 = Pin(Columnas[1],Pin.IN,Pin.PULL_DOWN)
col3 = Pin(Columnas[2],Pin.IN,Pin.PULL_DOWN)
col4 = Pin(Columnas[3],Pin.IN,Pin.PULL_DOWN)

#leds
leds= [15, 2, 4, 5, 18, 19, 21, 22, 3, 35]
a = " "
b = " "

led1=Pin(15, Pin.OUT)
led2=Pin(2, Pin.OUT)
led3=Pin(4, Pin.OUT)
led4=Pin(5, Pin.OUT)
led5=Pin(18, Pin.OUT)
led6=Pin(19, Pin.OUT)
led7=Pin(21, Pin.OUT)
led8=Pin(22, Pin.OUT)
led9=Pin(23, Pin.OUT)
led10=Pin(16, Pin.OUT)
def lectura(FILAS, CARACTERES):
    EnFilas = Pin(FILAS, Pin.OUT)
    EnFilas.on()
 
    if(col1.value()==1):
        a = str(CARACTERES[0])
        if a== "1" and led1.value()==0:
            led1.value(1)
            a= " "
        if a== "1" and led1.value()==1:
            led1.value(0)
        if a == "4" and led4.value()==0:
            led4.value(1)
            a= " "
        if a == "4" and led4.value()==1:
            led4.value(0)
        if a == "7"and led7.value()==0:
            led7.value(1)
            a= " "
        if a == "7"and led7.value()==1:
            led7.value(0)
        if a== "*":
            led1.value(0)
            led2.value(0)
            led3.value(0)
            led4.value(0)
            led5.value(0)
            led6.value(0)
            led7.value(0)
            led8.value(0)
            led9.value(0)
            led10.value(0)
    if(col2.value()==1):
        a = str(CARACTERES[1])
        if a== "2" and led2.value()==0:
            led2.value(1)
            a= " "
        if a== "2" and led2.value()==1:
            led2.value(0)
        if a == "5" and led5.value()==0:
            led5.value(1)
            a= " "
        if a == "5" and led5.value()==1:
            led5.value(0)
        if a == "8"and led8.value()==0:
            led8.value(1)
            a= " "
        if a == "8"and led8.value()==1:
            led8.value(0)

        if a =="0" and led10.value()==0:
            led10.value(1)
            a= " "
        if a =="0" and led10.value()==1:
            led10.value(0)

    if(col3.value()==1):
        a = str(CARACTERES[2])
        if a== "3" and led3.value()==0:
            led3.value(1)
            a= " "
        if a== "3" and led3.value()==1:
            led3.value(0)
        if a == "6" and led6.value()==0:
            led6.value(1)
            a= " "
        if a == "6" and led6.value()==1:
            led6.value(0)
        if a == "9"and led9.value()==0:
            led9.value(1)
            a= " "
        if a == "9"and led9.value()==1:
            led9.value(0)  
    if(col4.value()==1):
        a = str(CARACTERES[3])
        if a == "A":
            led1.value(1)
            led2.value(1)
            led3.value(1)
            led4.value(1)
            led5.value(1)
            led6.value(1)
            led7.value(1)
            led8.value(1)
            led9.value(1)
            led10.value(1)
    EnFilas.off()

while True:
    lectura(Filas[0], ["1","2","3","A"])
    lectura(Filas[1], ["4","5","6","B"])
    lectura(Filas[2], ["7","8","9","C"])   
    lectura(Filas[3], ["*","0","#","D"])
    sleep (0.2)