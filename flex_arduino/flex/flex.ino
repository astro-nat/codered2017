const int flexpin = 0;

void setup() {
  // Begin Serial Monitoring
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int flexposition;    // Input value from the analog pin.
  int servoposition;   // Output value to the servo.

  // Read the position of the flex sensor (0 to 1023):

  flexposition = analogRead(flexpin);

  Serial.println(flexposition);

  delay(20);
}
