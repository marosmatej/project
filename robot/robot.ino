#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3); // RX, TX pins for Bluetooth communication


int leftMotorSpeed = 0;
int rightMotorSpeed = 0;

void setup() {
  Serial.begin(9600); // Start serial communication
  BTSerial.begin(9600); // Start Bluetooth serial communication
  // Initialize motor control pins or any other necessary setup
  
  // test
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
  if (BTSerial.available()) {
    char command = BTSerial.read(); // Read incoming command from Bluetooth
  
    // Perform actions based on the received command
    switch(command) {
      case 'F':
        leftMotorSpeed = 100; // Example speed values, adjust as needed
        rightMotorSpeed = 100;
        digitalWrite(LED_BUILTIN, LOW);
        Serial.println("F");
        break;
      case 'B':
        leftMotorSpeed = -100; // Example speed values, adjust as needed
        rightMotorSpeed = -100;
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println("F");
        break;
      case 'L':
        leftMotorSpeed = 80; // Example speed values, adjust as needed
        rightMotorSpeed = 120;
        Serial.println("F");
        break;
      case 'R':
        leftMotorSpeed = 120; // Example speed values, adjust as needed
        rightMotorSpeed = 80;
        Serial.println("F");
        break;
      default:
        leftMotorSpeed = 0;
        rightMotorSpeed = 0;
        break;
    }

    // Send motor speed values to control the motors
    // Code to control motors based on leftMotorSpeed and rightMotorSpeed
  }
}
