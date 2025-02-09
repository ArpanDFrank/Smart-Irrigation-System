#include <SoftwareSerial.h>

SoftwareSerial co2Serial(2, 3); // RX, TX pins

void setup() {
  Serial.begin(9600);
  co2Serial.begin(9600); // Change the baud rate according to your sensor's specifications

  Serial.println("Setup complete");
}

void loop() {
  while (co2Serial.available() > 0) {
    // Read the incoming byte
    char incomingByte = co2Serial.read();
    Serial.print("Received: ");
    Serial.println(incomingByte);
  }

  delay(1000);
  Serial.println("Loop iteration complete");
}
