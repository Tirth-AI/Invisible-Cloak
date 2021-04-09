# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:26:32 2021

@author: Tirth Dalwadi
"""


import cv2
import numpy as np
cap = cv2.VideoCapture(0)
back = cv2.imread('./BACKg.jpg')
 
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
       # cv2.imshow("HSV",hsv)
        red = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        L_red = np.array([0,100,100])  
        u_red = np.array([10,255,255])     
        mask = cv2.inRange(hsv,L_red,u_red)
        #cv2.imshow("mask",mask)      
        part1 = cv2.bitwise_and(back,back,mask = mask)
        #cv2.imshow("PART1",part1)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame,frame,mask=mask)
        #cv2.imshow("part2",part2)        
        cv2.imshow("Magic",part1 + part2)
                               
                               
                               
                               
                               
        if cv2.waitKey(5) == ord('q'):
 
            
            break       
cap.release()
cv2.destroyAllWindows()
