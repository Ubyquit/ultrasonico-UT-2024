#define LED_PIN 13
bool ledState = false; // false para apagado, true para encendido

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, ledState); // Inicializa el LED en su estado inicial (apagado)
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "1") {
      digitalWrite(LED_PIN, HIGH);
      ledState = true;
    } else if (command == "0") {
      digitalWrite(LED_PIN, LOW);
      ledState = false;
    } else if (command == "get_state") {
      Serial.println(ledState ? "1" : "0");
    }
  }
}
