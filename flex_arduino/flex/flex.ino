#include <SoftwareSerial.h>

// Bluetooth Module TX->10
//                  RX->11
SoftwareSerial btComm(10, 11); // syntax: (RX, TX)

// Flex Sensors
const int f_index  = 0; // A0 = Index
const int f_middle = 1; // A1 = Middle
const int f_ring   = 2; // A2 = Ring
const int f_pinky  = 3; // A3 = Pinky
const int f_thumb  = 4; // A4 = Thumb

const int dpps = 50; // data-points per second

void setup() {
  // Begin PC Serial Communication
  Serial.begin(9600);

  // Begin Bluetooth Serial Commmunication
  btComm.begin(9600);
}

void loop() {

  // Read the position of the flex sensors (~512 to ~1024):
  int index = analogRead(f_index);
  int middle = analogRead(f_middle);
  int ring = analogRead(f_ring);
  int pinky = analogRead(f_pinky);
  int thumb = analogRead(f_thumb);
  
  // form telemetry string
  String tlm = String(index) + "," + String(middle) + "," + String(ring) + "," + String(pinky) + "," + String(thumb);

  btComm.println(tlm); // send to bluetooth
  Serial.println(tlm); // send to serial

  delay(1000/dpps);
}
