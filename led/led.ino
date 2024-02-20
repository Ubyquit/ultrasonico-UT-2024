// Código para Arduino

#define LED_PIN 13

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read();
    if (receivedChar == '1') {
      digitalWrite(LED_PIN, HIGH); // Encender el LED
      Serial.println("LED Encendido");
    } else if (receivedChar == '0') {
      digitalWrite(LED_PIN, LOW); // Apagar el LED
      Serial.println("LED Apagado");
    }
  }
}
