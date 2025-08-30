/////////////////////ROBOTICS CLUB////////////////////////////
//////////////////////////////////////////////////////////////
///////////////THIS CODE FOR MAZE SOLVING ROBOT///////////////
//////////////////////////////////////////////////////////////
#include <Ultrasonic.h>
Ultrasonic ultrasonicF(6, 7);
int distanceF;

Ultrasonic ultrasonicR(8, 9);
int distanceR;

Ultrasonic ultrasonicL(10, 11);
int distanceL;

int leftmotor1 = 12;
int leftmotor2 = 13;
int rightmotor1 = 2;
int rightmotor2 = 4;

int en_motor1 = 3;
int en_motor2 = 5;

void setup() {
  // put your setup code here, to run once:
  pinMode(leftmotor1, OUTPUT);
  pinMode(leftmotor2, OUTPUT);
  pinMode(rightmotor1, OUTPUT);
  pinMode(rightmotor2, OUTPUT);

  pinMode(en_motor1, OUTPUT);
  pinMode(en_motor2, OUTPUT);

  analogWrite(en_motor2, 70);
  analogWrite(en_motor1, 80);
  Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:

  distanceF = ultrasonicF.read();
  Serial.print("F: ");
  Serial.print(distanceF);


  distanceR = ultrasonicR.read();
  Serial.print  ("    R:");
  Serial.print(distanceR);

  distanceL = ultrasonicL.read();
  Serial.print("    L:");
  Serial.println(distanceL);


  
  Forward();
  Serial.println("Going ahead");

  
    if (distanceF > 15 && (distanceR <= 5 || distanceL <= 5)) {
      if (distanceR < distanceL ) {
            Left();
            delay(20);
            Serial.println("Adjusting to Left");
          }
          if (distanceR > distanceL ) {
            Right();
            delay(20);
            Serial.println("Adjusting to Right");
          }}

          
  if (distanceF <= 15 && (distanceR >= 10 || distanceL >= 10)) {

    if (distanceR < distanceL ) {
      Left();
      delay(400);
      Serial.println("Left");
    }
    if (distanceR > distanceL ) {
      Right();
      delay(400);
      Serial.println("Right");

    }
  }
  else if (distanceF <= 15 && distanceR <= 5 && distanceL <= 5) {

    Right();
    Serial.println("return");


  }





}
void Forward() {
  digitalWrite(leftmotor1, HIGH);
  digitalWrite(leftmotor2, LOW);
  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
}
void Left() {
  digitalWrite(leftmotor1, LOW);
  digitalWrite(leftmotor2, HIGH);
  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
}
void Right() {
  digitalWrite(leftmotor1, HIGH);
  digitalWrite(leftmotor2, LOW);
  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, HIGH);
}
void Stopp() {
  digitalWrite(leftmotor1, LOW);
  digitalWrite(leftmotor2, LOW);
  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, LOW);
}
