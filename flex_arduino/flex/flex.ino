// Flex Sensors
const int f_index  = 1; // A1 = Index
const int f_middle = 2; // A2 = Middle
const int f_ring   = 3; // A3 = Ring
const int f_pinky  = 4; // A4 = Pinky
const int f_thumb  = 0; // A0 = Thumb

const int dpps = 50; // data-points per second

void setup() {
  // Begin Serial Communication
  Serial.begin(57600);
}

void loop() {

  // data buffer
  int buff[5][dpps];
  
  int i;
  for (i = 0; i < dpps; i = i + 1) {
    buff[0][i] = analogRead(f_thumb);
    buff[1][i] = analogRead(f_index);
    buff[2][i] = analogRead(f_middle);
    buff[3][i] = analogRead(f_ring);
    buff[4][i] = analogRead(f_pinky);
    delay(1000/dpps);
  }

  // dump data onto serial
  int b;
  String tlm;
  for (b = 0; b < 5; b = b + 1) {
    tlm = String(b) + ":" + String(buff[b][0]);
    int x;
    for (x = 1; x < dpps; x = x + 1) {
     tlm += "," + String(buff[b][x]);
    }
    tlm += "asdf";
    Serial.println(tlm);
  }
}
