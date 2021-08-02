# # 이미지 스켈레톤 그리기
# import cv2

# # MPII에서 각 파트 번호, 선으로 연결될 POSE_PAIRS
# BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
#                 "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
#                 "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
#                 "Background": 15 }

# POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
#                 ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
#                 ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
#                 ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]
    
# # 각 파일 path
# protoFile = "/Users/panhong/Desktop/openpose_sample/pose_deploy_linevec_faster_4_stages.prototxt"
# weightsFile = "/Users/panhong/Desktop/openpose_sample/pose_iter_160000.caffemodel"
 
# # 위의 path에 있는 network 불러오기
# net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

# # 이미지 읽어오기
# image = cv2.imread("/Users/panhong/Desktop/김광현.jpeg")

# # frame.shape = 불러온 이미지에서 height, width, color 받아옴
# imageHeight, imageWidth, _ = image.shape
 
# # network에 넣기위해 전처리
# inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (imageWidth, imageHeight), (0, 0, 0), swapRB=False, crop=False)
 
# # network에 넣어주기
# net.setInput(inpBlob)

# # 결과 받아오기
# output = net.forward()

# # output.shape[0] = 이미지 ID, [1] = 출력 맵의 높이, [2] = 너비
# H = output.shape[2]
# W = output.shape[3]
# print("이미지 ID : ", len(output[0]), ", H : ", output.shape[2], ", W : ",output.shape[3]) # 이미지 ID

# # 키포인트 검출시 이미지에 그려줌
# points = []
# for i in range(0,15):
#     # 해당 신체부위 신뢰도 얻음.
#     probMap = output[0, i, :, :]
 
#     # global 최대값 찾기
#     minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

#     # 원래 이미지에 맞게 점 위치 변경
#     x = (imageWidth * point[0]) / W
#     y = (imageHeight * point[1]) / H

#     # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로    
#     if prob > 0.1 :    
#         cv2.circle(image, (int(x), int(y)), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)       # circle(그릴곳, 원의 중심, 반지름, 색)
#         cv2.putText(image, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, lineType=cv2.LINE_AA)
#         points.append((int(x), int(y)))
#     else :
#         points.append(None)

# cv2.imshow("Output-Keypoints",image)
# cv2.waitKey(0)

# # 이미지 복사
# imageCopy = image

# # 각 POSE_PAIRS별로 선 그어줌 (머리 - 목, 목 - 왼쪽어깨, ...)
# for pair in POSE_PAIRS:
#     partA = pair[0]             # Head
#     partA = BODY_PARTS[partA]   # 0
#     partB = pair[1]             # Neck
#     partB = BODY_PARTS[partB]   # 1
    
#     #print(partA," 와 ", partB, " 연결\n")
#     if points[partA] and points[partB]:
#         cv2.line(imageCopy, points[partA], points[partB], (0, 255, 0), 2)


# cv2.imshow("Output-Keypoints",imageCopy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''=================================================================='''
# # 영상 스켈레톤 그리기 

# import cv2 as cv 
# import numpy as np
# import argparse
# import matplotlib.pyplot as plt

# net = cv.dnn.readNetFromTensorflow("/Users/panhong/Desktop/human-pose/graph_opt.pb")

# inWidht = 368
# inHeight = 368
# thr = 0.2

# BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
#                "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
#                "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
#                "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

# POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
#                ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
#                ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
#                ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
#                ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

# cap = cv.VideoCapture("/Users/panhong/Desktop/강백호.mov")
# cap.set(3,800)
# cap.set(4,800)

# if not cap.isOpened():
#     cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     raise IOError("Cannot open Video")
    
# while cv.waitKey(1) < 0:
#     hasFrame , frame = cap.read()
#     if not hasFrame:
#         cv.waitKey()
#         break
        
#     frameWidth = frame.shape[1]
#     frameHeight = frame.shape[0]
#     net.setInput(cv.dnn.blobFromImage(frame , 1.0 , (inWidht , inHeight) , (127.5 , 127.5 , 127.5) , swapRB = True , crop = False))
#     out = net.forward()
#     out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

#     assert(len(BODY_PARTS) == out.shape[1])

#     points = []
    
#     for i in range(len(BODY_PARTS)):
#         # Slice heatmap of corresponging body's part.
#         heatMap = out[0, i, :, :]

#         # Originally, we try to find all the local maximums. To simplify a sample
#         # we just find a global one. However only a single pose at the same time
#         # could be detected this way.
#         _, conf, _, point = cv.minMaxLoc(heatMap)
#         x = (frameWidth * point[0]) / out.shape[3]
#         y = (frameHeight * point[1]) / out.shape[2]
#         # Add a point if it's confidence is higher than threshold.
#         points.append((int(x), int(y)) if conf > thr else None)

#     for pair in POSE_PAIRS:
#         partFrom = pair[0]
#         partTo = pair[1]
#         assert(partFrom in BODY_PARTS)
#         assert(partTo in BODY_PARTS)

#         idFrom = BODY_PARTS[partFrom]
#         idTo = BODY_PARTS[partTo]

#         if points[idFrom] and points[idTo]:
#             cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
#             cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
#             cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

#     t, _ = net.getPerfProfile()
#     freq = cv.getTickFrequency() / 1000
#     cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    
#     cv.imshow("pose estimation Tutorial" , frame)
