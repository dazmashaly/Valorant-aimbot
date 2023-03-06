#include <Mouse.h>

// Define the pins for the pushbuttons
const int LB = 1;
const int RB = 8;
const int UB = 6;
const int DB = 3;

// Variables to store the states of the pushbuttons
int LBV = 0;
int RBV = 0;
int UBV = 0;
int DBV = 0;

void setup() {
  // Initialize the Mouse library
  Mouse.begin();

  // Set the pinMode for the pushbutton pins to INPUT
  pinMode(LB, INPUT);
  pinMode(RB, INPUT);
  pinMode(UB, INPUT);
  pinMode(DB, INPUT);

  // Initialize the serial communication at 9600 baud
  Serial.begin(9600);
}

void loop() {
  // Read the states of the pushbuttons
  LBV = digitalRead(LB);
  RBV = digitalRead(RB);
  UBV = digitalRead(UB);
  DBV = digitalRead(DB);

  // Move the mouse cursor based on the button states
  if (LBV != 0) {
    Mouse.move(-2, 0, 0);
  }
  if (RBV != 0) {
    Mouse.move(2, 0, 0);
  }
  if (UBV != 0) {
    Mouse.move(0, 2, 0);
  }
  if (DBV != 0) {
    Mouse.move(0, -2, 0);
  }

  // Check for incoming serial data
    if (Serial.available() > 0) {
    // Read the incoming data as a string
    String input = Serial.readStringUntil('\n');
    
    // Parse the x and y values from the input string
    int delimiter_index = input.indexOf(',');
    if (delimiter_index != -1) {
      int x = atoi(input.substring(0, delimiter_index).c_str());
      int y = atoi(input.substring(delimiter_index + 1).c_str());

      // Print the x and y values to the serial monitor
      // Serial.print("X = ");
      // Serial.print(x);
      // Serial.print(", Y = ");
      // Serial.println(y);
      
      // Move the mouse cursor to the specified x and y coordinates
      Mouse.move(x, y, 0);

       // left click a mouse click if the enemy is within a certain range
      if(abs(y) <=12 && abs(x) <=12){
        Mouse.press();
        Mouse.release();
        
        // Add a delay to prevent multiple clicks
        delay(150);
      }
    }
  }
}
