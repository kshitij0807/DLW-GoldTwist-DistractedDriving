int Buzzer = 13;
int ledPin = 12;

void setup () {
  pinMode(Buzzer, OUTPUT);
  pinMode(ledPin, OUTPUT);

}


int duration = 500;

void loop() {
  digitalWrite(ledPin , LOW);
  tone(8, 1400, duration);
  delay(200);
  tone(8, 800, duration);
  delay(200);
  tone(8, 1800, duration);
  delay(200);
  tone(8, 600, duration);
  delay(200);
}