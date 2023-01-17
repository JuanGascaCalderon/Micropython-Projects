#Librerias
from machine import Pin,PWM

frequency = 1000
duty = 310  
duty2= 390 
duty3 = 380
duty4 = 300

#Salidas digitales de los motores
motorA = PWM((Pin(13, Pin.OUT)), frequency)
motorB = PWM((Pin(12, Pin.OUT)), frequency)
motorC = PWM((Pin(27, Pin.OUT)), frequency)
motorD = PWM((Pin(26, Pin.OUT)), frequency)
#Entrada digitales de los sensores
right_ir = Pin(33, Pin.IN)
left_ir = Pin(32, Pin.IN)

#Funciones
def motor_1(on, off): #IZQUIERDO
    motorA.duty(on)
    motorB.duty(off)

def motor_2(on, off): #DERECHO
    motorC.duty(on)
    motorD.duty(off)
    

while True:

    right_val=right_ir.value() #Getting right IR value(0 or 1)
    left_val=left_ir.value() #Getting left IR value(0 or 1)
    
    print(str(right_val)+"-"+str(left_val))
    
    # Controlling robot direction based on IR value
    if right_val==0 and left_val==0:
        motor_1(duty2,0) #Forward
        motor_2(duty,0) 
    elif right_val==1 and left_val==0:
        motor_1(duty3,0) #Right
        motor_2(0,duty)
    elif right_val==0 and left_val==1:
        motor_1(0,duty) #Left
        motor_2(duty4,0)
    else:
        motor_1(0,0)
        motor_2(0,0)
    
    

