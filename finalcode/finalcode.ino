#include <OneWire.h>
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 7

int pHsensor= A0, pHvalue=0;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  sensors.begin();
  pinMode(pHsensor,INPUT);
}

void loop() {
  int sensorValue = analogRead(pHsensor);
  float pHValue = sensorValue*(14.0/1023.0
  );
  Serial.print("pH Value: ");
  Serial.print(pHValue);
  Serial.print("\t\t\t\t");
  //delay(1000);

  sensors.requestTemperatures();
  float temperatureCelsius = sensors.getTempCByIndex(0);
  Serial.print("Temperature: ");
  Serial.print(temperatureCelsius);
  Serial.println(" °C");
  delay(1000);

}
