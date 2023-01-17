#Library's
from machine import Pin, PWM
from time import sleep_ms

#Definition of peepers
class GORILLACELL_BUZZER: 
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))
#buzzer = PWM(Pin(4, Pin.OUT), freq=40000000, duty=512)

    def play(self, melodies, wait, duty):
        for note in melodies:
            self.pwm.freq(note)
            self.pwm.duty(duty)
            sleep_ms(wait)
        # Disable the pulse, setting the duty to 0
        self.pwm.duty(0)
        # Disconnect the pwm driver
        #self.pwm.deinit() # remove to play the next melodies
#Definition of matricial
Filas = [13,12,14,27]
for i in range(4): #Mapeo
    Pin(Filas[i], Pin.OUT)

#Declaración de los pines de Filas cómo salida
Columnas = [26,25,33,32]
Col1 = Pin(Columnas[0],Pin.IN, Pin.PULL_DOWN)
Col2 = Pin(Columnas[1],Pin.IN, Pin.PULL_DOWN)
Col3 = Pin(Columnas[2],Pin.IN, Pin.PULL_DOWN)
Col4 = Pin(Columnas[3],Pin.IN, Pin.PULL_DOWN)

#beat
B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978

mario = [ 2637, 2637,  2637, 2093,  2637, 3136, 1568, 2093, 3136, 2637, 1760, 1976, 1865, 1760, 1568, 2637, 3136, 3520,
          2794, 3136, 2637, 2093, 23549, 1976, 2093, 1568, 1319, 1760, 1976, 1865, 1760, 1568, 2637, 3136, 3520, 2794,
          3136, 2637, 2093, 2349, 1976]

jinggle = [2637, 2637, 2637, 2637, 2637, 2637, 2637, 3136, 2093, 2349, 2637, 2794, 2794, 2794, 2794, 2794, 2637,
           2637, 2637, 2637, 2349, 2349, 2637, 2349, 3136, 2637, 2637, 2637, 2637, 2637, 2637, 2637, 3136, 2093, 2349, 2637,
           2794, 2794, 2794, 2794, 2794, 2637, 2637, 2637, 3136, 3136, 2794, 2349, 2093 ]
melody = [262, 294, 330, 349, 392, 440, 494, 523]
melody2 = [523, 494, 440, 392, 349, 330, 294, 262 ]
melody3 = [523, 494, 294, 262, 440, 392, 349, 330 ]
melody4 = [392, 440, 494, 523, 262, 294, 330, 349]
melody5 = [ 262, 294, 330, 349, 392, 440, 494, 523, 523, 494, 440, 392, 349, 330, 294, 262 ]
melody6 = [523, 494, 294, 262, 440, 392, 349, 330, 392, 440, 494, 523, 262, 294, 330, 349 ]
melody7 = [1, 1 , 1 ,1 , 1, 1]
a = " "
buzzer = GORILLACELL_BUZZER(4)
def lectura(filas, caracteres):
    EnFilas = Pin(filas, Pin.OUT)
    EnFilas.on()
    if (Col1.value()==1):
        a = str(caracteres[0])
        if a == "*":
            buzzer.play(melody7, 150, 0)
            sleep_ms(1000)
            a = " " 

        else:
            buzzer.play(melody7, 150, 512)
            if a == "1":
                buzzer.play(melody, 150, 512)
                sleep_ms(1000)
                a = " " 
            if a == "7":
                buzzer.play(mario, 150, 512)
                sleep_ms(1000)
                a = " " 
            if a == "4":
                 buzzer.play(melody2, 150, 512)
                 sleep_ms(1000)
                 a = " "    
    if (Col2.value()==1):
        a = str(caracteres[1])
        if a == "8":
            buzzer.play(melody7, 150, 0)
            sleep_ms(1000)
            a = " " 
        else:
            buzzer.play(melody7, 150, 512)
            if a == "2":
                buzzer.play(melody3, 150, 512)
                sleep_ms(1000)
                a = " "
            if a == "5":
                buzzer.play(melody2, 150, 512)
                sleep_ms(1000)
                a = " "
    if (Col3.value()==1):
        a = str(caracteres[2])
        if a == "6":
            buzzer.play(melody7, 150, 0)
            sleep_ms(1000)
            a = " " 

        else:
            buzzer.play(melody7, 150, 0)
            if a == "3":
                buzzer.play(melody5, 150, 512)
                sleep_ms(1000)
                a = " " 

            if a == "9":  
                buzzer.play(melody6, 150, 512)
                sleep_ms(1000)
                a = " "
    if (Col4.value()==1):
        a =str(caracteres[3])
        buzzer.play(melody7, 150, 0)
        if a == "A": 
                buzzer.play(jinggle, 150, 512)
                sleep_ms(1000)
                a = " "
    EnFilas.off()

try:
    while True:
        lectura(Filas[0],["1","2","3","A"])
        lectura(Filas[1],["4","5","6","B"])
        lectura(Filas[2],["7","8","9","C"])
        lectura(Filas[3],["*","0","#","D"])
        sleep_ms(30)

except KeyboardInterrupt:
    print("\nEl Programa Terminó")