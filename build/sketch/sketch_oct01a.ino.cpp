#include <Arduino.h>
#line 1 "c:\\Users\\emily\\Documents\\DLW-GoldTwist-Drowsiness-detection\\sketch_oct01a.ino"
int Buzzer = 13;
int ledPin = 12;

#line 4 "c:\\Users\\emily\\Documents\\DLW-GoldTwist-Drowsiness-detection\\sketch_oct01a.ino"
void setup();
#line 13 "c:\\Users\\emily\\Documents\\DLW-GoldTwist-Drowsiness-detection\\sketch_oct01a.ino"
void loop();
#line 4 "c:\\Users\\emily\\Documents\\DLW-GoldTwist-Drowsiness-detection\\sketch_oct01a.ino"
void setup () {
  pinMode(Buzzer, OUTPUT);
  pinMode(ledPin, OUTPUT);

}


int duration = 500;

void loop() {
  digitalWrite(ledPin , HIGH);
  tone(8, 1400, duration);
  delay(200);
  tone(8, 800, duration);
  delay(200);
  tone(8, 1800, duration);
  delay(200);
  tone(8, 600, duration);
  delay(200);
}
