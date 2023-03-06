# Import necessary libraries
import cv2
import numpy as np
import pyautogui
import time
import serial

# uncomment  ## lines for better understanding and debugging

# Initialize variables
num = 0

#connect to the serial port of the Arduino leonardo
ser = serial.Serial('COM19', 9600)

# Loop infinitely to capture and process screenshots
while True:
    # Capture screenshot of the entire screen
    img = pyautogui.screenshot()

    # Convert screenshot to OpenCV image format
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    ## Create a copy of the original screenshot
    ## ogimg=img.copy()

    # Create Gaussian Pyramid list to reduce image size
    layer = img.copy()
    gaussian_pyramid_list = [layer]
    for i in range(6):
        layer = cv2.pyrDown(layer)     
        gaussian_pyramid_list.append(layer)

    # Create Laplacian Pyramid list to detect edges
    layer = gaussian_pyramid_list[5]
    laplacian_pyramid_list = [layer]
    for i in range(5, 0, -1):
        gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
        gaussian_extended = cv2.resize(gaussian_extended,(gaussian_pyramid_list[i-1].shape[1],gaussian_pyramid_list[i-1].shape[0]))     
        laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)     
        laplacian_pyramid_list.append(laplacian)
    
    # Get Laplacian Pyramid image with edges
    img = laplacian_pyramid_list[5]

    # Convert image to HSV format for color range detection
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    
    # Define lower and upper values of the color range to detect
    l_val = np.array([123,205,0])
    u_val = np.array([154,255,188])

    # Create a mask to filter out colors outside of the specified range
    mask = cv2.inRange(hsv,l_val,u_val)

    # Apply the mask to the original image
    masked = cv2.bitwise_and(img,img,mask=mask)

    # Crop the image to focus on the target area (original shape = (1680,1050) )
    # change based on resolution  
    masked = masked[200:,:1400]

    # Mask out unnecessary parts of the image
    masked[652:799,1054:1275] =0
    masked[10:100,1240:] =0

    # split the masked image into its RGB channels
    b,g,r = cv2.split(masked)
    
    # # define the paths to save the images
    # # path = "with\\aim{}.png".format(num)
    # # path3 = "original{}.png".format(num)
    # # path2 = "without\\noaim{}.png".format(num)

    ## increment the counter
    ## num+=1


    # find the coordinates of the enemy's head
    x = np.where((b >80) & (r>80))
    x=np.array(x)

    # if the enemy's head is not detected, continue to the next iteration of the loop
    if(x.size <=0):
        continue
    
    # Get the x, y coordinates of the head of the closest enemy
    (x,y) =  (x[1][0]+1, x[0][0]+1)

    ## cv2.imwrite(path2, masked)
    
    ## Print the x and y coordinates of the enemy head on the original screenshot
    ## cv2.putText(ogimg,str(x)+" "+str(y),(250,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    ## Draw a green circle at the location of the enemy head
    ## cv2.circle(masked, (x, y ),2, (0, 255, 0), -1)

    ## Draw a green circle at the location of the enemy head on the original screenshot
    ## cv2.circle(ogimg, (x, y+200 ),2, (0, 255, 0), -1)

    # Calculate the distance from the enemy head to the center of the screen
    y= y -325
    x-=840
    if(abs(x) >=70):
         x = int(127 * x / abs(x))
      
    elif(abs(x) >=25 and abs(x) <=70):
        x = int(x*1.8)
    
    if(abs(y) >=70):
        y = int(127 * y / abs(y))
    
    elif(abs(y) >=25 and abs(y) <=70):
        y = int(y*1.8)
    
    # # Print the x and y coordinates of the enemy head on the original screenshot
    # # cv2.putText(ogimg,str(x)+" "+str(y),(250,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    # Send the x and y coordinates to the Arduino Leonardo to move the mouse to that location
    ser.write((str(x) + "," + str(y) + "\n").encode())

    ## Save the masked image with a green circle around the enemy head
    # # cv2.imwrite(path3, ogimg)
    # # cv2.imwrite(path, masked)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()