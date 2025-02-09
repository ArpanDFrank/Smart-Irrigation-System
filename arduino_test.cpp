#include<Arduino.ino>
int led=13;
void setup()
{
    pinMode(13,OUTPUT);
    serial.begin(96500);
}
void loop()
{
    serial.digitalWrite(13,HIGH);
    serial.println("Test Successful")
    delay(1000);
    serial.digitalWrite(13,LOW);
    
}