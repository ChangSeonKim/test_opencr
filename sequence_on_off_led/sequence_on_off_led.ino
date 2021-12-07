void setup() {
  // put your setup code here, to run once:
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  digitalWrite(22, 1);
  digitalWrite(23, 1);
  digitalWrite(24, 1);
  digitalWrite(25, 1);
  
  digitalWrite(22, 0);
  delay(1000);
  digitalWrite(23, 0);
  delay(1000);
  
  digitalWrite(24, 0);
  delay(1000);
  digitalWrite(25, 0);

  
}
