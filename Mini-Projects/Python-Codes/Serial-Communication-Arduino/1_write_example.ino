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