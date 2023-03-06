# Valorant aimbot (undetectable)

## Introduction:
This project is an aimbot for the game Valorant. The aimbot takes screenshots of the game and detects the position of the nearest enemy player's head on the screen using OpenCV computer vision library. It then sends the x and y coordinates of the enemy's head to an Arduino Leonardo which moves the computer's mouse to these coordinates, effectively allowing the player to aim at the enemy player's head automatically.

The reason this aimbot is undetectable is because it doesn't change or interact with the game's coding, instead it uses the Arduino Leonardo to move the mouse as a normal USB mouse.
here is a video of some kills using the aimbot : https://drive.google.com/file/d/1BP6h1CyDq9w-lInqAF0aBfWg3L0mPzTJ/view?usp=sharing

## Python Code:
The Python code uses the PyAutoGUI library to take screenshots of the game and the OpenCV computer vision library to detect the enemy player's head. The main steps in the code are:

* Importing necessary libraries including OpenCV, NumPy, PyAutoGUI, time, and serial.
* Initializing variables such as a counter for the number of screenshots taken and a connection to the Arduino Leonardo over a serial port.
* Starting a loop that takes screenshots of the game using PyAutoGUI and converts them to OpenCV format using NumPy.
* Applying a Laplacian pyramid filter to the image to highlight the edges of objects in the scene and applying a color mask to filter out   everything except for the enemy player's head.
* Finding the position of the enemy player's head in the masked image and calculating its distance from the center of the screen (the game's crosshair).
* Converting the x and y coordinates to a format that the Arduino Leonardo can understand and sending them over the serial port.
* Repeating the loop continuously, allowing the aimbot to continuously track and aim at the nearest enemy player's head in the game.

## Arduino Code:
The Arduino code reads the states of four pushbuttons (left button, right button, up button, and down button) and moves the mouse cursor based on the button states becouse we cant use two input devices as mouse at the same time. The main steps in the code are:

* Defining the pins for the pushbuttons and variables to store their states.
* Initializing the Mouse library and setting the pinMode for the pushbutton pins to INPUT.
* Reading the states of the pushbuttons.
* Moving the mouse cursor based on the button states.
* Checking for incoming serial data from the Python script.
* Parsing the x and y values from the input string and moving the mouse cursor to the specified x and y coordinates.
  Simulating a left mouse click if the absolute value of x and y is within a certain range.

# Limitations:
* This project is kind of slow and using the pushbutton to move around can be tricky.
* It can sometimes detect Reyna and Astra as enemies even when she is on the same team.

# Conclusion:
Note that this code is not intended for actual gameplay and is considered cheating in most online games. It is provided here for educational purposes only. The project can be improved by adding more features and incorporating machine learning algorithms.
I just wanted to use basic digital image processing methods for practice.