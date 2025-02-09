#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  float temperatureCelsius = sensors.getTempCByIndex(0);
  Serial.print("Temperature: ");
  Serial.print((temperatureCelsius));
  Serial.println(" °C");
  delay(1000);
}
