import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

interpreter = tf.lite.Interpreter(model_path = "/Users/panhong/Downloads/lite-model_movenet_singlepose_lightning_3.tflite")
interpreter.allocate_tensors()

cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/김진욱.mov")
# cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera open failed")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

delay = round(1000 / fps)

out = cv2.VideoWriter('hello.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:                 # 무한 루프
    ret, frame = cap.read() # 카메라의 ret, frame 값 받아오기

    if not ret:             #ret이 False면 중지
        break

    inversed = ~frame # 반전

    edge = cv2.Canny(frame, 50, 150) # 윤곽선

    # 윤곽선은 그레이스케일 영상이므로 저장이 안된다. 컬러 영상으로 변경
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    out.write(edge_color) # 영상 데이터만 저장. 소리는 X

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)

    if cv2.waitKey(delay) == 27: # esc를 누르면 강제 종료
        break

cap.release()
out.release()
cv2.destroyAllWindows()

