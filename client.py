import cv2
import numpy as np
import time
import mouse
import socket
import keyboard
import win32con
import win32api

wScr, hScr = 1536, 900 #Enter your screen resolution here. Get screen resolution from here - https://bestfirms.com/what-is-my-screen-resolution/

wCam, hCam = 640, 480
frameR = 100     #Frame Reduction
smoothening = 7  #random value

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
cap = cv2.VideoCapture(0)
stop = 0
cap.set(3, wCam)
cap.set(4, hCam)
text = ''
canvas = 0
close = 0
frame_rate = 10
prev = 0
option = -1

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Define the host and the port on which the server is running
host = '10.90.2.127'
port = 8485

# Connect to the server
s.connect((host, port))

while True:
    # Step1: Find the landmarks
    data = s.recv(1024)
    
    # If data is received, decode it and split it
    if data:
        data_str = data.decode()
        option, x1, y1 = data_str.split(',')
        x1 = int(x1)
        y1 = int(y1)
        print('Received option:', option)
        print('Received x1:', x1)
        print('Received y1:', y1)
        
        #Clicking mode
        if option == '1':
            stop+=1
            if stop > 20:
                mouse.click(button='left')
                stop = 0
            
        #Right click
        if option == '2':
            stop+=1
            if stop>20:
                mouse.right_click()
                stop = 0
        
        # Alt tab
        if option == '3':
            stop+=1
            if stop>20:
                keyboard.press('alt + tab')
                stop=0
    
        # Step8: Both Index and middle are up: Clicking Mode
        if option == '4':
            stop+=1
            # Step5: Convert the coordinates
            xi = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            yi = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
            # Step6: Smooth Values
            clocX = plocX + (xi - plocX) / smoothening
            clocY = plocY + (yi - plocY) / smoothening
            # Step7: Move Mouse
            mouse.move(wScr - clocX, clocY)
            plocX, plocY = clocX, clocY

        if option == '5':
            stop+=1
            if stop>20:
                mouse.double_click(button='left')
                stop = 0
                
        if option == '6':
            if (y1>=(hCam/2)):
                mouse.wheel(delta=-1)
            else:
                mouse.wheel(delta=1)

        print('Option:', option)
        option = -1
    # Step2: Get the image
    if (cv2.waitKey(1) & 0xFF == ord('d')):
        break
cap.release()
cv2.destroyAllWindows()