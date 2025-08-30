int leftmotor1 = 6;
int leftmotor2 = 7;
int rightmotor1 = 8;
int rightmotor2 = 9;
int en_right_motor = 10;
int en_left_motor = 5;
int Rspeed =80;
int Lspeed =70;
int delaytime=1000;
////////////////////
int LIR = A5;
int RIR = A4;

void setup() {
  pinMode(rightmotor1, OUTPUT);
  pinMode(rightmotor2, OUTPUT);
  pinMode(leftmotor1, OUTPUT);
  pinMode(leftmotor2, OUTPUT);
  pinMode(en_right_motor, OUTPUT);
  pinMode(en_left_motor, OUTPUT);
  pinMode (LIR, INPUT);
  pinMode (RIR, INPUT);
  Serial.begin(9600);
}



void loop() {
  Serial.println("Right: ");
  Serial.println(digitalRead(RIR));
  Serial.println("Left: ");
  Serial.println(digitalRead(LIR));

  if (digitalRead(RIR) == LOW && digitalRead(LIR) == LOW) {
    Forward();
  
  }
  
  else if (digitalRead(RIR) == LOW && digitalRead(LIR) == HIGH) {

    Left();    
  
    }
  
  else if (digitalRead(RIR) == HIGH && digitalRead(LIR) == LOW) {

    Right();
  
  }
  
  else {
    Stopp();
  }
  
}



void Forward() {

  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1,  HIGH);
  digitalWrite(leftmotor2,  LOW);
  analogWrite(en_right_motor, Rspeed);
  analogWrite(en_left_motor, Lspeed);
}
void Left() {
  
  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1,  LOW);
  digitalWrite(leftmotor2,  HIGH);
  analogWrite(en_right_motor, 180);
  analogWrite(en_left_motor, 150);
}
void Right() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, HIGH);
  digitalWrite(leftmotor1,  HIGH);
  digitalWrite(leftmotor2,  LOW);
  analogWrite(en_right_motor, 180);
  analogWrite(en_left_motor, 150);}
       
void Backward() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, HIGH);
  digitalWrite(leftmotor1,  LOW);
  digitalWrite(leftmotor2,  HIGH);
  analogWrite(en_right_motor, Rspeed);
  analogWrite(en_left_motor, Lspeed);
}

void Stopp() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1,  LOW);
  digitalWrite(leftmotor2,  LOW);
}