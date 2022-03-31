# Importa biblioteca para acessar as portas Seriais
from serial import Serial

# Inicia conexão na porta em que o Arduino está plugado
# Se for windows, port = 'COMX'
arduino = Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

while True:
    # Espera mensagem do usuário
    message = input('Send a message to Arduino: ')

    # Envia mensagem do usuário
    arduino.write(bytes(message, encoding='utf-8'))