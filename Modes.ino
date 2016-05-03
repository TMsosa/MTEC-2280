int ledPin = 3;
int ledPin2 = 6;
int switchPin = 2;
int switchRead = 0;
int mode = 0;

boolean pressing = false;

//Mode 2 Variables
int counter = 0;

long pMillis = 0;

int interval = 100;

boolean flipFlop = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(switchPin, INPUT);
  Serial.begin(9600);
}

void loop() {

  switchRead = digitalRead(switchPin);
  //Serial.println(switchRead);

  if (switchRead == 1) {
    pressing = true;
  }

  if (switchRead == 0 && pressing == true) {
    pressing = false;
    //do something
    //counter = counter + 1;
    mode++;
    Serial.println(mode);
  }

  if (mode == 0) {
    //Reset of Off Condition
    digitalWrite(ledPin, LOW);
    digitalWrite(ledPin2, LOW);
    Serial.println("Mode 0");
    counter = 0;
  }
  else if (mode == 1) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPin2, HIGH);
    Serial.println("Mode 1");

  } else if (mode == 2) {
    //run fade program
    Serial.println("Mode 2");
    
    if (millis() - pMillis >= interval) {
      pMillis = millis();
      if (flipFlop == false) {
        counter++;
      } else {
        counter--;
      }
      Serial.println(counter);
    }
    analogWrite(ledPin2, counter);
    analogWrite(ledPin,counter);


    if (counter >= 255) {
      flipFlop = true;
    }

    if (counter <= 0) {
      flipFlop = false;
    }


  } else {
    mode = 0;
  }

}
