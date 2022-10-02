# 1 "c:\\Users\\emily\\Documents\\DLW-GoldTwist-Drowsiness-detection\\sketch_oct01a.ino"
int Buzzer = 13;
int ledPin = 12;

void setup () {
  pinMode(Buzzer, 0x1);
  pinMode(ledPin, 0x1);

}


int duration = 500;

void loop() {
  digitalWrite(ledPin , 0x1);
  tone(8, 1400, duration);
  delay(200);
  tone(8, 800, duration);
  delay(200);
  tone(8, 1800, duration);
  delay(200);
  tone(8, 600, duration);
  delay(200);
}
