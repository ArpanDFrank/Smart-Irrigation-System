const int EnableL=5;
const int HighL=6;
const int LowL=7;

const int EnableR=10;
const int HighR=9;
const int LowR=8;

void setup() {
  // put your setup code here, to run once:
  pinMode(EnableL,OUTPUT);
  pinMode(HighL,OUTPUT);
  pinMode(LowL,OUTPUT);

  pinMode(EnableR,OUTPUT);
  pinMode(HighR,OUTPUT);
  pinMode(LowR,OUTPUT);
}
void Forward(){
  digitalWrite(HighL,LOW);
  digitalWrite(LowL,HIGH);
  analogWrite(EnableL,225);

  digitalWrite(HighR,LOW);
  digitalWrite(LowR,HIGH);
  analogWrite(EnableR,225);
}

void Backward(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);
  analogWrite(EnableL,225);

  digitalWrite(HighR,HIGH);
  digitalWrite(LowR,LOW);
  analogWrite(EnableR,225);
}

void loop() {
  // put your main code here, to run repeatedly:
  Forward();

}