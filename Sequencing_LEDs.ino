const int ledPin = 13;
const int ledPin2 = 12;
const int ledPin3 = 11;
const int switchPin = 2;
const int switchPin2 = 3;
const int switchPin3 = 4;
int switchRead = 0;
int switchRead2 = 0;
int switchRead3 = 0;

int counter = 0;

boolean pressing = false;
void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);

  pinMode(switchPin, INPUT);
  pinMode(switchPin2, INPUT);
  pinMode(switchPin3, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  //digitalWrite(ledPin, HIGH);
  switchRead = digitalRead(switchPin);
  switchRead2 = digitalRead(switchPin2);
  switchRead3 = digitalRead(switchPin3);
  //Serial.println(switchRead);
  if (switchRead == 1 || switchRead2 == 1 || switchRead3 == 1) {
    pressing = true;
  }

  //We want to check if the button is currently released and has been pressed before its been released
  if (switchRead == 0 && pressing == true) {
    //setting up for the next time we press
    pressing = false;
    //Do something
    counter++;
    Serial.println(counter);
 
      if (counter == 1) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin3, HIGH);
  } else if (counter == 2) {
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, HIGH);
    digitalWrite(ledPin3, LOW);
  } else {
    counter = 0;
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);
  }
  }

  if (switchRead2 == 0 && pressing == true) {
    //setting up for the next time we press
    pressing = false;
    //Do something
    counter++;
    Serial.println(counter);

      if (counter == 1) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin3, HIGH);
  } else if (counter == 2) {
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, HIGH);
  } else {
    counter = 0;
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, LOW);
  }
  }

  if (switchRead3 == 0 && pressing == true) {
    //setting up for the next time we press
    pressing = false;
    //Do something
    counter++;
    Serial.println(counter);

      if (counter == 1) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin3, HIGH);
    
  } else if (counter == 2) {
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, HIGH);
  } 
  
  else {
    counter = 0;
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, LOW);
  }
  }
}
