# Exemplo de Comunicação Serial com Arduino

<!--
    Colocar aqui Thumbnail com link p/ o vídeo do YouTube quando tiver.
-->

> **Descrição da Comunicação Serial:**
> Sempre que você conecta uma placa de protipagem como um Arduino, ou ESP8266, ou ESP32, entre outras, no seu computador, você pode se comunicar com eles através de uma comunicação serial. Isso será aproveitado para que possamos coletar dados da placa e enviar dados para ela, integrando projetos de hardware para aumentar o potencial dos projetos que podem ser feitos.

## Pré-requisitos

### Python 3.6+

> Utilizado em todos os exemplos

Esses projetos foram testados em dois ambientes diferentes, com Python 3.10.2 e Python 3.8.5. Portanto, é bom ter uma versão atualizada não só para que possamos usurfruir das novidades mas para que também tenhamos certeza de que o próprio Python não será um problema na execução dos exemplos.

Caso não tenha o Python instalado ainda, você pode baixar e seguir as instruções no próprio [site deles](SiteAqui)

### Pacote PySerial

> Utilizado em todos os exemplos

Esse pacote para Python é o responsável por realizar a "mágica" de se conectar na placa de prototipagem através da programação. É essencial que tenha ele instalado para a execução dos exemplos. Você pode encontrar as instruções [nesse site](ColocarAquiSiteDoPypi) ou simplesmente executar o comando:

`pip install pyserial`

## Mini Projetos

Os códigos poderão ser encontrados nesta pasta no github e possuem comentários em inglês e português, pois foram feitos para serem facilmente entendidos. Caso tenha encontrado algum problema ou tenha alguma dúvida, fique a vontade para abrir uma issue nesse repositório!

<details>
<summary>Enviando informações p/ o Arduino</summary>

Esse exemplo possui o exemplo mais básico para utilizar A comunicação serial. O código em python é responsável por enviar comandos 'l' ou 'd' para o Arduino e o código p/ Arduino é responsável por receber esses comandos e ligar ou desligar o LED Onboard.

`Python Code`
```python
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
```

`Arduino Code`
```c
#define LED 13

void setup() {
    Serial.begin(9600);
    pinMode(LED, OUTPUT);
}

void loop() {
    if (Serial.available()){
        char incoming_char = Serial.read();
        if (incoming_char == 'l'){
            digitalWrite(LED, HIGH);
        }

        if (incoming_char == 'd'){
            digitalWrite(LED, LOW);
        }
    }
}
```

</details>

<details>
<summary>Recebendo informações do Arduino</summary>

Esse exemplo possui o exemplo mais básico para utilizar A comunicação serial. O código em python é responsável por receber mensagens do Arduino e o código p/ Arduino é responsável por enviar regularmente uma mensagem, como exemplo.

`Python Code`
```python
# -*- coding: iso-8859-1 -*-
import serial

# Abre porta Serial com seus devidos parâmetros
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)  

# Lê repetidamente e imprime qualquer mensagem que vem do arduino
while True:
    if arduino.in_waiting > 0:
        incoming_message = arduino.readline().decode('ascii')
        print(incoming_message)
```

`Arduino Code`
```c
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Message from Arduino!");
  delay(3000);
}
```

</details>
