int pHsensor= A1, pHvalue=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pHsensor,INPUT);
}

void loop() {
  int sensorValue = analogRead(pHsensor);
  float pHValue = (sensorValue*(14/1023.0));
  Serial.print("pH Value: ");
  Serial.println(pHValue);
  delay(1000);
}
