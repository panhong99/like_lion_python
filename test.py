# # import numpy as np
# # import cv2

# # cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")

# # while cap.isOpened():
# #     ret , frame = cap.read()

# #     if not ret:
# #         print("not read cap")
# #         break
# #     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
# #     cv2.imshow("frame" , gray)
# #     if cv2.waitKey(1) == ord("q"):
# #         break
# # cap.release()
# # cap.destroyAllWidows()

# import cv2 
# import numpy as np

# def showcam():
#     try:
#         cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")
#         print("open cam")
#     except:
#         print("not working")
#         return

#     fourcc = cv2.VideoWriter_fourcc()
#     while True:
#         ret , frame = cap.read()
#         print(frame.shape)
#         center_frame = frame[195 : 995 , 438 : 1321]
#         if not ret:
#             print("error")
#             break
#         cv2.imshow("center_frame" , center_frame)
#         cv2.VideoWriter("오타니_1.mov" , center_frame)
#         k = cv2.waitKey(1) & 0xFF
#         if k == 27: 
#             break

#     cap.release()
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)
#     cv2.waitKey(1)
#     cv2.waitKey(1)
# showcam()


import numpy as np
import cv2

lowerBound = np.array([74, 70, 99])
upperBound = np.array([95, 110, 255])

def showcam():
    try:
        print ('open cam')
        cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")
    except:
        print ('Not working')
        return
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Gmask = cv2.inRange(hsv, lowerBound, upperBound)
        ret1, thr = cv2.threshold(Gmask, 127, 255, 0)
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            for i in range(len(contours)):
                # Get area value
                area = cv2.contourArea(contours[i])
                if area > 100:  # minimum yellow area
                    rect = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    frame = cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
        if not ret:
            print('error')
            break
        cv2.imshow('bitwise', Gmask)
        cv2.imshow('cam_load', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
showcam()
# # import numpy as np
# # import cv2

# # cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")

# # while cap.isOpened():
# #     ret , frame = cap.read()

# #     if not ret:
# #         print("not read cap")
# #         break
# #     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
# #     cv2.imshow("frame" , gray)
# #     if cv2.waitKey(1) == ord("q"):
# #         break
# # cap.release()
# # cap.destroyAllWidows()

# import cv2 
# import numpy as np

# def showcam():
#     try:
#         cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")
#         print("open cam")
#     except:
#         print("not working")
#         return

#     fourcc = cv2.VideoWriter_fourcc()
#     while True:
#         ret , frame = cap.read()
#         print(frame.shape)
#         center_frame = frame[195 : 995 , 438 : 1321]
#         if not ret:
#             print("error")
#             break
#         cv2.imshow("center_frame" , center_frame)
#         cv2.VideoWriter("오타니_1.mov" , center_frame)
#         k = cv2.waitKey(1) & 0xFF
#         if k == 27: 
#             break

#     cap.release()
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)
#     cv2.waitKey(1)
#     cv2.waitKey(1)
# showcam()


import numpy as np
import cv2

lowerBound = np.array([74, 70, 99])
upperBound = np.array([95, 110, 255])

def showcam():
    try:
        print ('open cam')
        cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")
    except:
        print ('Not working')
        return
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Gmask = cv2.inRange(hsv, lowerBound, upperBound)
        ret1, thr = cv2.threshold(Gmask, 127, 255, 0)
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            for i in range(len(contours)):
                # Get area value
                area = cv2.contourArea(contours[i])
                if area > 100:  # minimum yellow area
                    rect = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    frame = cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
        if not ret:
            print('error')
            break
        cv2.imshow('bitwise', Gmask)
        cv2.imshow('cam_load', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
showcam()
# # import numpy as np
# # import cv2

# # cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")

# # while cap.isOpened():
# #     ret , frame = cap.read()

# #     if not ret:
# #         print("not read cap")
# #         break
# #     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
# #     cv2.imshow("frame" , gray)
# #     if cv2.waitKey(1) == ord("q"):
# #         break
# # cap.release()
# # cap.destroyAllWidows()

# import cv2 
# import numpy as np

# def showcam():
#     try:
#         cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")
#         print("open cam")
#     except:
#         print("not working")
#         return

#     fourcc = cv2.VideoWriter_fourcc()
#     while True:
#         ret , frame = cap.read()
#         print(frame.shape)
#         center_frame = frame[195 : 995 , 438 : 1321]
#         if not ret:
#             print("error")
#             break
#         cv2.imshow("center_frame" , center_frame)
#         cv2.VideoWriter("오타니_1.mov" , center_frame)
#         k = cv2.waitKey(1) & 0xFF
#         if k == 27: 
#             break

#     cap.release()
#     cv2.waitKey()
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)
#     cv2.waitKey(1)
#     cv2.waitKey(1)
# showcam()


import numpy as np
import cv2

lowerBound = np.array([74, 70, 99])
upperBound = np.array([95, 110, 255])

def showcam():
    try:
        print ('open cam')
        cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")
    except:
        print ('Not working')
        return
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Gmask = cv2.inRange(hsv, lowerBound, upperBound)
        ret1, thr = cv2.threshold(Gmask, 127, 255, 0)
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            for i in range(len(contours)):
                # Get area value
                area = cv2.contourArea(contours[i])
                if area > 100:  # minimum yellow area
                    rect = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    frame = cv2.drawContours(frame, [box], -1, (0, 255, 0), 3)
        if not ret:
            print('error')
            break
        cv2.imshow('bitwise', Gmask)
        cv2.imshow('cam_load', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
showcam()
