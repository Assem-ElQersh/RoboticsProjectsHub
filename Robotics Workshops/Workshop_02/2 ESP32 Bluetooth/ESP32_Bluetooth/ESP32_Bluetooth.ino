//Make sure you are choosing ESP32 as your Board(Choose the model written on your board).

#include <BluetoothSerial.h>

char t;
BluetoothSerial SerialBT;  // Define the Bluetooth Serial object
int rightmotor1 = 3;
int rightmotor2 = 4;
int leftmotor1 = 5;
int leftmotor2 = 6;

int en_right_motor = 2;
int en_left_motor = 7;


void setup() {

  pinMode(rightmotor1, OUTPUT);
  pinMode(rightmotor2, OUTPUT);
  pinMode(leftmotor1, OUTPUT);
  pinMode(leftmotor2, OUTPUT);

  pinMode(en_right_motor, OUTPUT);
  pinMode(en_left_motor, OUTPUT);

  SerialBT.begin("Your_ESP32Name");  // Initialize Bluetooth with your ESP32's name
  Serial.begin(9600);
}

void loop() {
  if (SerialBT.available()) {
    t = SerialBT.read();
    Serial.println(t);
  }

  if (t == 'F') {  // move forward 
    Forward();

  } else if (t == 'B') {  // move reverse 
    Backward();

  } else if (t == 'L') {  // turn right
    Left();


  } else if (t == 'R') {  // turn left 
    Right();

  } else if (t == 'S') {
    Stopp();  // STOP (all motors stop)
  }
}


void Forward() {

  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1, HIGH);
  digitalWrite(leftmotor2, LOW);
  digitalWrite(en_right_motor, 150);
  digitalWrite(en_left_motor, 150);
}
void Left() {

  digitalWrite(rightmotor1, HIGH);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1, LOW);
  digitalWrite(leftmotor2, LOW);
  digitalWrite(en_right_motor, 150);
  digitalWrite(en_left_motor, 150);
}
void Right() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1, HIGH);
  digitalWrite(leftmotor2, LOW);
  digitalWrite(en_right_motor, 150);
  digitalWrite(en_left_motor, 150);
}

void Backward() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, HIGH);
  digitalWrite(leftmotor1, LOW);
  digitalWrite(leftmotor2, HIGH);
  digitalWrite(en_right_motor, 150);
  digitalWrite(en_left_motor, 150);
}

void Stopp() {

  digitalWrite(rightmotor1, LOW);
  digitalWrite(rightmotor2, LOW);
  digitalWrite(leftmotor1, LOW);
  digitalWrite(leftmotor2, LOW);
}