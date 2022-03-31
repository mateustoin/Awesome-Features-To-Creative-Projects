# -*- coding: iso-8859-1 -*-
import serial

# Abre porta Serial com seus devidos parâmetros
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)  

# Lê repetidamente e imprime qualquer mensagem que vem do arduino
while True:
    if arduino.in_waiting > 0:
        incoming_message = arduino.readline().decode('ascii')
        print(incoming_message)