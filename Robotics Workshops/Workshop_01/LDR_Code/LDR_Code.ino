/////////////////////ROBOTICS CLUB///////////////////////////
/////////////////////////////////////////////////////////////
////////THIS CODE IS FOR LDR LIGHT FOLLOWING ROBOT///////////
/////////////////////////////////////////////////////////////


#define LDR_LEFT A0
#define LDR_RIGHT A1 
#define MOTOR_LEFT_FORWARD 4
#define MOTOR_LEFT_BACKWARD 7
#define MOTOR_RIGHT_FORWARD  8
#define MOTOR_RIGHT_BACKWARD 13
#define ENB 11
#define ENA 10

// Constants for motor speeds
#define MAX_SPEED 90
#define MIN_SPEED 45


void setup() {
  // Initialize LDR sensors and motor driver
  pinMode(LDR_LEFT, INPUT) ;
  pinMode(LDR_RIGHT, INPUT);
  pinMode(MOTOR_LEFT_FORWARD, OUTPUT) ;
  pinMode(MOTOR_LEFT_BACKWARD, OUTPUT) ;
  pinMode(MOTOR_RIGHT_FORWARD, OUTPUT) ;
  pinMode(MOTOR_RIGHT_BACKWARD, OUTPUT) ;
  pinMode(ENA, OUTPUT) ;
  pinMode(ENB, OUTPUT) ;

}

void loop() {
  // Read values from LDR sensors
  int ldr_left = analogRead(LDR_LEFT) ;
  int ldr_right = analogRead(LDR_RIGHT);
  Serial.println(ldr_left);

  // Calculate the difference between the LDR readings
  int diff = ldr_right - ldr_left;

  // Adjust motor speeds based on LDR readings
  if (diff > 40) {
    right();
    
  } else if (diff < -40) {
    left();    
  } else {


     forward();
  }
}
void right(){

  // LED rope light is to the right of the center of the robot

    digitalWrite(MOTOR_LEFT_FORWARD, HIGH) ;
    digitalWrite(MOTOR_LEFT_BACKWARD, LOW) ;
    digitalWrite(MOTOR_RIGHT_FORWARD, HIGH) ;
    digitalWrite(MOTOR_RIGHT_BACKWARD, LOW) ;
    analogWrite(ENA,MIN_SPEED);
    analogWrite(ENB,MAX_SPEED);

}
void left(){
  // LED rope light is to the left of the center of the robot

    digitalWrite(MOTOR_LEFT_FORWARD, HIGH) ;
    digitalWrite(MOTOR_LEFT_BACKWARD, LOW) ;
    digitalWrite(MOTOR_RIGHT_FORWARD, HIGH) ;
    digitalWrite(MOTOR_RIGHT_BACKWARD, LOW) ;
    analogWrite(ENA,MAX_SPEED);
    analogWrite(ENB,MIN_SPEED);
}
void forward(){
   // LED rope light is at the center of the robot
    digitalWrite(MOTOR_LEFT_FORWARD, HIGH);
    digitalWrite(MOTOR_LEFT_BACKWARD, LOW);
    digitalWrite(MOTOR_RIGHT_FORWARD, HIGH);
    digitalWrite(MOTOR_RIGHT_BACKWARD, LOW);
    analogWrite(ENA,MAX_SPEED);
    analogWrite(ENB,MAX_SPEED);
}
