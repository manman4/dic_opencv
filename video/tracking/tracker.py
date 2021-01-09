# -*- coding: utf-8 -*

import cv2

# トラッカーを選択する
def select_tracker():
    print("Which Tracker API do you use?")
    print("0: Boosting")
    print("1: MIL")
    print("2: KCF")
    print("3: TLD")
    print("4: MedianFlow")
    choice = input("Please select your tracker number: ")

    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()


    return tracker

tracker = select_tracker()
tracker_name = str(tracker).split()[0][1:]

# 内臓webカメラに接続
cap = cv2.VideoCapture(0)

#webカメラの軌道に時間がかかる場合
import time
time.sleep(1)

ret, frame = cap.read()

roi = cv2.selectROI(frame, False)

ret = tracker.init(frame, roi)

# キャプチャーを実行
while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))

    if success:
        p1 = (x, y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame, p1, p2, (0,255,0), 3)
    else :
        cv2.putText(frame, "Tracking failed!!", (500,400), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),3)
    
    # 実行しているトラッカー名を画面に表示
    cv2.putText(frame, tracker_name, (20,600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3)
    cv2.imshow(tracker_name, frame)

    k = cv2.waitKey(1) & 0xff
    if k == 27 :
        break

cap.release()
cv2.destroyAllWindows()
