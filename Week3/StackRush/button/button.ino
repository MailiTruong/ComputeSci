int buttonPin = 2;    // Connect button to pin 2
int buttonState = 0;  // Variable to hold button state

bool button_pressed = false;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == LOW && !button_pressed) {
    Serial.println("BUTTON_PRESSED");
    button_pressed = true;
  } else if (buttonState == HIGH && button_pressed) {
    button_pressed = false;
  }

  delay(100);
}
