import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import pulsectl

################################
wCam, hCam = 640, 480
################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)

        # Hand range 50-30
        # Volume range 0-1

        vol = np.interp(length, [50, 300], [0, 1])
        print(int(length), vol)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        with pulsectl.Pulse('volume-increaser') as pulse:
            for sink in pulse.sink_list():
                # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
                pulse.volume_set_all_chans(sink, vol)

        cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(img, (50, int(150 + (1-vol)*250)), (85, 400), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(vol*100)}%', (40, 450), cv2.FONT_HERSHEY_PLAIN,
                    2, (0, 255, 0), 3, cv2.LINE_AA, False)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 35), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 0, 0), 3, cv2.LINE_AA, False)

    cv2.imshow("Image", img)
    cv2.waitKey(1)