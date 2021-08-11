# 영상 스켈레톤 그리기 
import cv2  
import numpy as np
import argparse
import matplotlib.pyplot as plt

class video_tracking:
    def tracking_video(self , cap):
        self.cap = cap
        
        net = cv2.dnn.readNetFromTensorflow("/Users/panhong/Desktop/human-pose/graph_opt.pb")

        inWidht = 368
        inHeight = 368
        thr = 0.2

        BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                       "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                       "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
                       "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

        POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                       ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                       ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
                       ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
                       ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

        
        fourcc = cv2.VideoWriter_fourcc(*"DIVX")
        out = cv2.VideoWriter("output.mov" , fourcc , 25.0 , (680 , 480))

        # 화면 크기 설정
        cap.set(3,800)
        cap.set(4,800)

        if not cap.isOpened():
            cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise IOError("Cannot open Video")  

        while cv2.waitKey(1) < 0:
            hasFrame , frame = cap.read()
            if not hasFrame:
                cv2.waitKey()
                break

            frameWidth = frame.shape[1]
            frameHeight = frame.shape[0]
            net.setInput(cv2.dnn.blobFromImage(frame , 1.0 , (inWidht , inHeight) , (127.5 , 127.5 , 127.5) , swapRB = True , crop = False))
            out = net.forward()
            out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

            assert(len(BODY_PARTS) == out.shape[1])

            points = []

            for i in range(len(BODY_PARTS)):
                # Slice heatmap of corresponging body's part.
                heatMap = out[0, i, :, :]

                # Originally, we try to find all the local maximums. To simplify a sample
                # we just find a global one. However only a single pose at the same time
                # could be detected this way.
                _, conf, _, point = cv2.minMaxLoc(heatMap)
                x = (frameWidth * point[0]) / out.shape[3]
                y = (frameHeight * point[1]) / out.shape[2]
                # Add a point if it's confidence is higher than threshold.
                points.append((int(x), int(y)) if conf > thr else None)

            for pair in POSE_PAIRS:
                partFrom = pair[0]
                partTo = pair[1]
                assert(partFrom in BODY_PARTS)
                assert(partTo in BODY_PARTS)

                idFrom = BODY_PARTS[partFrom]
                idTo = BODY_PARTS[partTo]

                if points[idFrom] and points[idTo]:
                    cv2.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
                    cv2.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)
                    cv2.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv2.FILLED)

            t, _ = net.getPerfProfile()
            freq = cv2.getTickFrequency() / 1000
            cv2.putText(frame, '%.2fms' % (t / freq), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            cv2.imshow("pose estimation Tutorial" , frame)

