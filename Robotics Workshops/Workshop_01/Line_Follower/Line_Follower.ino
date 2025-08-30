/////////////////////ROBOTICS CLUB///////////////////////
////////THIS CODE IS FOR IR LINE FOLLOWER ROBOT/////////
////////////////////////////////////////////////////////

int rightmotor1 = 3;
int rightmotor2 = 4;
int leftmotor1 = 5;
int leftmotor2 = 6; 

int en_right_motor = 2;
int en_left_motor = 7;

int LIR = A0;
int RIR = A1;

void setup() {
  
  pinMode(rightmotor1, OUTPUT);
  pinMode(rightmotor2, OUTPUT);
  pinMode(leftmotor1, OUTPUT);
  pinMode(leftmotor2, OUTPUT);

  pinMode(en_right_motor, OUTPUT);
  pinMode(en_left_motor, OUTPUT);

//  analogWrite(en_right_motor, 250);
//  analogWrite(en_left_motor, 250);
  
  pinMode (LIR, INPUT);
  pinMode (RIR, INPUT);
  
  Serial.begin(9600);
}



void loop() {
  delay(200);
  Serial.println("Right: ");
  Serial.println(digitalRead(RIR));
  Serial.println("Left: ");
  Serial.println(digitalRead(LIR));

  if (digitalRead(RIR) == LOW && digitalRead(LIR) == LOW) {
    Forward();
  }
  
  else if (digitalRead(RIR) == LOW && digitalRead(LIR) == HIGH) {

    Left();
//    delay(500);
    }
  
  else if (digitalRead(RIR) == HIGH && digitalRead(LIR) == LOW) {

    Right();
//    delay(500);
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
  analogWrite(en_right_motor, 100);
  analogWrite(en_left_motor, 100);
}
void Left() {
  
  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1,  LOW);
  digitalWrite(leftmotor2,  LOW);
  analogWrite(en_right_motor, 100);
  analogWrite(en_left_motor, 100);
}
void Right() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1,  HIGH);
  digitalWrite(leftmotor2,  LOW);
  analogWrite(en_right_motor, 100);
  analogWrite(en_left_motor, 100);
}
       
void Backward() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, HIGH);
  digitalWrite(leftmotor1,  LOW);
  digitalWrite(leftmotor2,  HIGH);
  analogWrite(en_right_motor, 100);
  analogWrite(en_left_motor, 100);
}

void Stopp() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1,  LOW);
  digitalWrite(leftmotor2,  LOW);
}
