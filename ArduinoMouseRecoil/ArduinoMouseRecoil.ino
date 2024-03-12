bool shouldClick = false;
int totalCPS = 300;
int retractionTime = 200;
int timeBetweenClicks = totalCPS -retractionTime;


void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    // read incoming serial data:
    char inChar = Serial.read();
    if(inChar == '2') {
      shouldClick = false;
    } else {
      shouldClick = true;
    }
  }
  if(shouldClick) {
    digitalWrite(2, HIGH);
    delay(retractionTime);
    digitalWrite(2, LOW);
    delay(timeBetweenClicks);
  }
}
