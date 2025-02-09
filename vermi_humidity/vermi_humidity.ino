const int soilMoisturePin = 34; 

void setup() {
  Serial.begin(115200);
  delay(1000);
}

void loop() {
  int soilMoistureValue = analogRead(soilMoisturePin);
  
  Serial.print("Soil Moisture Value: ");
  Serial.println(soilMoistureValue);
  
  delay(1000);
}