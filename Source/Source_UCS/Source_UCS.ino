#include "HX711.h"
#include <Servo.h>


// =========================
// Constants
// =========================

#define USB0_cal 3040.0 // calibration factor
#define USB0_zero 178953      // zero factor

#define USB1_cal 3040.0 // USB1_weight calibration
#define USB1_zero -4100

#define BASE_WEIGHT 83  // grams, weight of empty bowl and bowl holding aparatus


// =========================
// Pin definitions
// =========================
#define DOUT  3
#define CLK  2
//#define servoPin 11


HX711 scale;
//Servo myservo;

int angle = 0;


void setup() {
  Serial.begin(9600);
  

  //myservo.attach(servoPin);
  //myservo.write(0);
  String port = "USB0";

  scale.begin(DOUT, CLK);

  if (port == "USB0") {
    scale.set_scale(USB0_cal);
    scale.set_offset(USB0_zero);    
  }
  if (port == "USB1") {
    scale.set_scale(USB1_cal);
    scale.set_offset(USB1_zero);    
  }


  // long zero_factor = scale.read_average(); //Get a baseline reading

  //scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0

}

void loop() {
  Serial.print(scale.get_units(), 1); //scale.get_units() returns a float
  Serial.println();
  delay(1000);

  
  //myservo.write(scale.get_units());



//  // Sweep from 0 to 180 degrees:
//  for (angle = 0; angle <= 180; angle += 1) {
//    myservo.write(angle);
//    delay(15);
//  }
//  // And back from 180 to 0 degrees:
//  for (angle = 180; angle >= 0; angle -= 1) {
//    myservo.write(angle);
//    delay(30);
//  }
//  delay(1000);
}
