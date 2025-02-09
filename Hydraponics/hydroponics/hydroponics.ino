int pHsensor = A1;         // pH sensor connected to A1
int waterSensor = A2;
int temp1 = A4;
int temp2 = A5;
int temp3 = A6; 
int temp4 = 13;     // MH038 water sensor connected to A2

void setup() {
  Serial.begin(9600);
  pinMode(pHsensor, INPUT);
  pinMode(waterSensor, INPUT);
  pinMode(temp1, INPUT);
  pinMode(temp2, INPUT);
  pinMode(temp3, INPUT);
  pinMode(temp4, INPUT);

}

void loop() {
  // Read pH sensor value
  int pHSensorValue = analogRead(pHsensor);
  float pHValue = pHSensorValue * (14.0 / 1023.0); // Mapping to pH scale from 0 to 14

  // Read water sensor value
  int waterSensorValue = analogRead(waterSensor);
  float waterLevel = waterSensorValue * (100.0 / 1023.0); // Mapping to water level from 0 to 100

  int temp1Value = analogRead(waterSensor);
  float temp1 = temp1Value * (100.0 / 1023.0); // Mapping to water level from 0 to 100

  int temp2Value = analogRead(waterSensor);
  float temp2 = temp2Value * (100.0 / 1023.0); // Mapping to water level from 0 to 100

  int temp3Value = analogRead(waterSensor);
  float temp3 = temp3Value * (100.0 / 1023.0); // Mapping to water level from 0 to 100


  int temp4Value = digitalRead(waterSensor);
  float temp4 = temp4Value * (100.0 / 1023.0);
  // Print values to Serial Monitor
  Serial.print("(");
  Serial.print(pHValue);
  Serial.print(",");
  Serial.print(waterLevel);
  Serial.print(",");
  Serial.print(temp1);
  Serial.print(",");
  Serial.print(temp2);
  Serial.print(",");
  Serial.print(temp3);
  Serial.print(",");
  Serial.print(temp4);
  Serial.println(")");


  
  delay(1000); // Delay between readings
}
