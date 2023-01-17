from machine import Pin
from time import sleep_ms

boton1= Pin(13, Pin.IN, Pin.PULL_UP)
boton2= Pin(14, Pin.IN, Pin.PULL_UP)
pa = Pin(27, Pin.OUT)
pb = Pin(26, Pin.OUT)
pc = Pin(25, Pin.OUT)
pd = Pin(33, Pin.OUT)
pe = Pin(32, Pin.OUT)
pf = Pin(19, Pin.OUT)
pg = Pin(18, Pin.OUT)
count = 0
def display(a,b,c,d,e,f,g):
    pa.value(a)
    pb.value(b)
    pc.value(c)
    pd.value(d)
    pe.value(e)
    pf.value(f)
    pg.value(g)
display(1,1,1,1,1,1,0)
while True:
    while count >= 0:
        while count<=9:
            if (boton1.value()==1):
                sleep_ms(300)
                count+=1
                if count == 0:
                    display(1,1,1,1,1,1,0)
                elif count == 1:
                    display(0,1,1,0,0,0,0)
                elif count == 2:
                    display(1,1,0,1,1,0,1)
                elif count == 3:
                    display(1,1,1,1,0,0,1)
                elif count == 4:
                    display(0,1,1,0,0,1,1)
                elif count == 5:
                    display(1,0,1,1,0,1,1)
                elif count == 6:
                    display(1,0,1,1,1,1,1)
                elif count == 7:
                    display(1,1,1,0,0,0,0)
                elif count == 8:
                    display(1,1,1,1,1,1,1)
                elif count == 9:
                    display(1,1,1,0,0,1,1)
                elif count == 10:
                    count = 0
                    display(1,1,1,1,1,1,0)
            if (boton2.value()==1):
                sleep_ms(300)
                count=count-1
                if count == 0:
                    display(1,1,1,1,1,1,0)
                elif count == 1:
                    display(0,1,1,0,0,0,0)
                elif count == 2:
                    display(1,1,0,1,1,0,1)
                elif count == 3:
                    display(1,1,1,1,0,0,1)
                elif count == 4:
                    display(0,1,1,0,0,1,1)
                elif count == 5:
                    display(1,0,1,1,0,1,1)
                elif count == 6:
                    display(1,0,1,1,1,1,1)
                elif count == 7:
                    display(1,1,1,0,0,0,0)
                elif count == 8:
                    display(1,1,1,1,1,1,1)
                elif count == 9:
                    display(1,1,1,0,0,1,1)
                elif count == -1:
                    count = 9
                    display(1,1,1,0,0,1,1)