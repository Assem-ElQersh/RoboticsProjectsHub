/////////////////////ROBOTICS CLUB////////////////////
//////////////////////////////////////////////////////
//////THIS CODE FOR OBSTACLE AVOIDANCE ROBOT//////////
//////////////////////////////////////////////////////

#include <Ultrasonic.h>
Ultrasonic ultrasonic(A0, A1);
int distance;

//int ENA = 5;
int IN1 = 6;
int IN2 = 7;
int IN3 = 8;
int IN4 = 9;
int ENB = 10;
int ENA = 11;

int Speed = 250;

void forward()
{
  analogWrite(ENA,Speed);
  analogWrite(ENB,Speed);
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
}
void backward()
{
  analogWrite(ENA,Speed);
  analogWrite(ENB,Speed);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
}
void right()
{
//  analogWrite(ENA,Speed);
  analogWrite(ENB,Speed);
  digitalWrite(IN1,1);
  digitalWrite(IN2,0);
  digitalWrite(IN3,0);
  digitalWrite(IN4,1);
}
void left()
{
  analogWrite(ENA,Speed);
  analogWrite(ENB,Speed);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
}
void Stop()
{
  analogWrite(ENA,0);
  analogWrite(ENB,0);
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
}
void setup() {
  Serial.begin(9600);
  
  pinMode(ENA,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENB,OUTPUT);
}

void loop() {
  distance = ultrasonic.read();
  Serial.println(distance);
  //delay(500);
  if(distance < 10)
  {
    right();
    delay(500);
    Stop();
    delay(250);
    distance = ultrasonic.read();
    if(distance < 10)
    {
      left();
      delay(1000);
      Stop();
      delay(250);
      distance = ultrasonic.read();
      if(distance < 10)
      {
        Stop();
        delay(250);
      }
      else
      {
        forward();
      }
    }
    else
    {
      forward();
    }
  }
  else
  {   
    forward();  
  }

}
