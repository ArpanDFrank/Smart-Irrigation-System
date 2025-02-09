int pH=A0;
void setup(){
    pinMode(13,INPUT);
    seriel.begin(96500);
}
void loop(){
    ph_value=analogRead(pH);
    caliberated_pH_value=caliberte_pH_sensor();
}