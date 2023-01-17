#código motores paso a paso
from machine import Pin
import time


a= Pin (2, Pin.OUT) #IN1'
b= Pin (4, Pin.OUT)  #IN2
c= Pin (15, Pin.OUT)#IN3
d= Pin (18, Pin.OUT)  #IN4
t= 0.03
t2=0.005

def paso(la,lb,lc,ld):
    a.value(la)
    b.value(lb)
    c.value(lc)
    d.value(ld)


    
while True:
    
    for i in range (15):
        paso(1,0,0,0)
        time.sleep(t)
        paso(0,1,0,0)
        time.sleep(t)
        paso(0,0,1,0)
        time.sleep(t)
        paso(0,0,0,1)
        time.sleep(t)
    
    
    for i in range (100):
        paso(1,0,0,0)
        time.sleep(t2)
        paso(0,1,0,0)
        time.sleep(t2)
        paso(0,0,1,0)
        time.sleep(t2)
        paso(0,0,0,1)
        time.sleep(t2)