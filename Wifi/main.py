import time
from machine import Pin
import network
import socket
import usocket

led_pin1 = Pin(13, Pin.OUT, value = 0)
led_pin2 = Pin(12, Pin.OUT, value = 0)
led_pin3 = Pin(27, Pin.OUT, value = 0)
led_pin4 = Pin(26, Pin.OUT, value = 0)

ssid = 'Mi10'
password = 'Diego2001'
wlan = network.WLAN(network.STA_IF)

wlan.active(True)
wlan.connect(ssid, password)

while wlan.isconnected() == False:
    pass

print('Conexion con el WiFi %s establecida' % ssid)
print(wlan.ifconfig())

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind(('', 80))
a.listen(3)

def web_page():

  html =  """
    <h1><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Control Leds</h1></b><br>
    <body> 

        <b>&nbsp;Led 1&nbsp;&nbsp;</b>
        <a href="/?led1=on"><button style='width:100px; height:35px; background-color: #00ff00'>Encender</button></a>&nbsp;&nbsp;
        <a href="/?led1=off"> <button style='width:100px; height:35px; background-color: #ff5252'>Apagar </button></a><br><br>

        <b>&nbsp;Led 2&nbsp;&nbsp;</b>
        <a href="/?led2=on"><button style='width:100px; height:35px; background-color: #00ff00'>Encender</button></a>&nbsp;&nbsp;
        <a href="/?led2=off"> <button style='width:100px; height:35px; background-color: #ff5252'>Apagar </button></a><br><br>

        <b>&nbsp;Led 3&nbsp;&nbsp;</b>
        <a href="/?led3=on"><button style='width:100px; height:35px; background-color: #00ff00'>Encender</button></a>&nbsp;&nbsp;
        <a href="/?led3=off"> <button style='width:100px; height:35px; background-color: #ff5252'>Apagar </button></a><br><br>

        <b>&nbsp;Led 4&nbsp;&nbsp;</b>
        <a href="/?led4=on"><button style='width:100px; height:35px; background-color: #00ff00'>Encender</button></a>&nbsp;&nbsp;
        <a href="/?led4=off"> <button style='width:100px; height:35px; background-color: #ff5252'>Apagar </button>
    </body>
    """
  return html

while True:
    conn,addr = a.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)
    
    if (request.find('/?led1=on') == 6):
        print('Estado: Led 1 Encendido')
        led_pin1.on()
    if (request.find('/?led1=off') == 6):
        print('Estado Led 1 Apagado')
        led_pin1.off()
        
    if (request.find('/?led2=on') == 6):
        print('Estado: Led 2 Encendido')
        led_pin2.on()
    if (request.find('/?led2=off') == 6):
        print('Estado: Led 2 Apagado')
        led_pin2.off()
        
    if (request.find('/?led3=on') == 6):
        print('Estado: Led 3 Encendido')
        led_pin3.on()
    if (request.find('/?led3=off') == 6):
        print('Estado: Led 3 Apagado')
        led_pin3.off()
        
    if (request.find('/?led4=on') == 6):
        print('Estado: Led 4 Encendido')
        led_pin4.on()
    if (request.find('/?led4=off') == 6):
        print('Estado: Led 4 Apagado')
        led_pin4.off()
      
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()