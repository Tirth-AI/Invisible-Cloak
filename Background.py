# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:29:29 2021

@author: Tirth Dalwadi
"""

import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,back = cap.read()
    if ret:
         cv2.imshow("BACKGROUND",back) 
    if cv2.waitKey(5) == ord('q'):
        cv2.imwrite("BACKg.jpg",back)
        break
cap.release()
cv2.destroyAllWindows()
