#include <SPI.h>
#include <Wire.h>
#include "Adafruit_HTU21DF.h" // Assuming you have a library for the HTU21D sensor

// Define sensor pins
const int co2SensorPin = 3; // MH-Z19 PWM pin connected to digital pin 3
const int phSensorPin1 = A0; // Analog pin for the first pH electrode
const int phSensorPin2 = A3; // Analog pin for the second pH electrode
const int tdsSensorPin = A1; // Analog pin for TDS sensor
const int waterTempSensorPin = A2; // Analog pin for water temperature sensor

// Create an instance of the HTU21D sensor
Adafruit_HTU21DF htu;

void setup() {
  Serial.begin(9600);
  //Serial.println("Sensors test");

  Wire.begin(); // Initialize I2C communication
  if (!htu.begin()) {
    Serial.println("Couldn't find HTU21D sensor!");
    while (1);

  }
}

void loop() {
  float tdsValue = analogRead(tdsSensorPin);
  int co2Level = readCO2Level();
  double pHValue1 = readPHValue(phSensorPin1); // Read pH value from first sensor
  double pHValue2 = readPHValue(phSensorPin2); // Read pH value from second sensor

  // Read temperature and humidity from HTU21D
  float temp = htu.readTemperature();
  temp=temp+75;
  float rel_hum = htu.readHumidity();

  // Read water temperature
  int waterTempValue = analogRead(waterTempSensorPin);
  float waterTemp = map(waterTempValue, 0, 1023, 0, 100); // Assuming the sensor outputs a value proportional to temperature

  Serial.print("(");
  Serial.print(pHValue1);
  Serial.print(",");
  Serial.print(waterTemp);
  Serial.print(",");
  Serial.print(temp);
  Serial.print(",");
  Serial.print(tdsValue);
  Serial.print(",");
  Serial.print(co2Level);
  Serial.print(",");
  Serial.print(rel_hum*-1);
  Serial.print(",");
  Serial.print(pHValue2);
  Serial.println(")");

  delay(2000);
}

int readCO2Level() {
  int sensorValue = analogRead(co2SensorPin);
  // Convert analog reading to CO2 level (you may need to calibrate based on your sensor)
  int co2Level = map(sensorValue, 0, 1023, 0, 5000);
  return co2Level;
}

double readPHValue(int pin) {
  int sensorValue = analogRead(pin);
  // Convert analog reading to pH value (you may need to calibrate based on your sensor)
  double pHValue = map(sensorValue, 0, 1023, 0, 14);
  return pHValue;
}