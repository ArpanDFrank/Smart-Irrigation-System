#include <SPI.h>
#include <Wire.h>
#include "Adafruit_HTU21DF.h" // Assuming you have a library for the HTU21D sensor

// Define sensor pins
const int co2SensorPin = 3; // MH-Z19 PWM pin connected to digital pin 3
const int phSensorPin = A0; // Analog p-in for the pH electrode
int tdsSensorPin = A1;

// Create an instance of the HTU21D sensor
Adafruit_HTU21DF htu = Adafruit_HTU21DF();

void setup() {
  Serial.begin(9600);
  Serial.println("HTU21D-F test");

  if (!htu.begin()) {
    Serial.println("Couldn't find sensor!");
    while (1);
  }
}

void loop() {
  float tdsValue = analogRead(tdsSensorPin);
  int co2Level = readCO2Level();
  float pHValue = readPHValue();

  // Read temperature and humidity from HTU21D
    float temp = htu.readTemperature();
    float rel_hum = htu.readHumidity();
    Serial.print("pH Value: ");
    Serial.println(pHValue);
    Serial.print("CO2 Value: ");
    Serial.println(co2Level);
    Serial.print("TDS Value: ");
    Serial.println(tdsValue);
    Serial.print("Temperature: ");
    Serial.print(temp);
    Serial.print(" C");
    Serial.print("\t\t");
    Serial.print("Humidity: ");
    Serial.print(rel_hum);
    Serial.println(" \%");

    delay(500);
}

int readCO2Level() {
  int sensorValue = analogRead(co2SensorPin);
  // Convert analog reading to CO2 level (you may need to calibrate based on your sensor)
  int co2Level = map(sensorValue, 0, 1023, 0, 5000);
  return co2Level;
}

float readPHValue() {
  int sensorValue = analogRead(phSensorPin);
  // Convert analog reading to pH value (you may need to calibrate based on your sensor)
  float pHValue = map(sensorValue, 0, 1023, 0, 14);
  return pHValue;
}
