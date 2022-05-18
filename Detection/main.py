import cv2
import numpy as np

import lane_detectorv2
import detection

#device = select_device("gpu")

def show_table(img,coordinat):



    if len(coordinat) != 0:
        #coordinat[0]
        frame = cv2.resize(img[int(coordinat[0][1]):int(coordinat[0][3]),int(coordinat[0][0]):int(coordinat[0][2])],(200,200))
        for i in range(1,len(coordinat)):

            new_frame = cv2.resize(img[int(coordinat[i][1]):int(coordinat[i][3]),int(coordinat[i][0]):int(coordinat[i][2])],(200,200))
            frame = np.hstack((frame, new_frame))
    else:
        frame = np.zeros((200, 200), dtype="uint8")


    return frame


dt=detection.detect()
cap = cv2.VideoCapture("lane3.mp4")

while True:

    ret,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    line = lane_detectorv2.detect(frame)
    result = dt.detectAndShow(frame)
    coordinat = result.xyxy

    #frame = cv2.bitwise_or(line,result)
    #cv2.imshow("line",line)
    cv2.imshow("line",line)
    cv2.imshow("Coordinat test",show_table(frame,coordinat[0]))
    cv2.imshow("frame",np.squeeze(result.render()))

    cv2.waitKey(1)


