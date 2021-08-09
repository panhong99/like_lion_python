# import sys
# # common 폴더안에 utils.py가 있어야 함
# sys.path.append("/Users/panhong/Desktop/coding_study/Likelion_KDT/Jupyter_notebook/Common")

# import cv2
# # 행렬 정보 출력 함수 임포트
# from Common.utils import print_matInfo

# title1 , title2 = "color2gray" , "color2color"
# color2gray = cv2.imread("/Users/panhong/Desktop/coding_study/Likelion_KDT/Jupyter_notebook/Common/read_color.jpg" , cv2.IMREAD_GRAYSCALE)
# color2color = cv2.imread("/Users/panhong/Desktop/coding_study/Likelion_KDT/Jupyter_notebook/Common/read_color.jpg" , cv2.IMREAD_COLOR)
# if color2gray is None or color2color is None:
#     raise Exception("영상 파일 읽기 에러")

# print("행렬 좌표 (100 ,100) 화소값")
# # 한 화소값 표시
# print("%s %s" %(title1 , color2gray[100 ,100]))
# print("%s %s\n" %(title2 , color2color[100 ,100]))

# # 행렬 정보 출력
# print_matInfo(title1 , color2gray)
# print_matInfo(title2 , color2color)
# cv2.imshow(title1 , color2gray)
# # 행렬 정보 영상으로 띄우기
# cv2.imshow(title2 , color2color)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import numpy as np
# import cv2 
# import os 

# os.getcwd()

# os.chdir("/Users/panhong/Desktop/baseball")
# os.getcwd()

# cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")

# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# fps = cap.get(cv2.CAP_PROP_FPS)
# print("프레임 너비 : %d , 프레임 높이 : %d , 초당 프레임 : %d" %(width , height , fps))

# while cap.isOpened():
#     ret , frame = cap.read()
#     if not ret:
#         print("프레임을 수신할 수 없습니다.")
#         break
#     frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
#     cv2.imshow("otter" , frame)
#     if cv2.waitKey(42) == ord("q"):
#         break
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import sys

# cap = cv2.VideoCapture("/Users/panhong/Desktop/baseball/오타니.mov")

# if not cap.isOpened():
#     print("not open")
#     sys.exit()

# w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)
# fourcc = cv2.VideoWriter_fourcc(*"DIVX")
# delay = round(1000 / fps)

# fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

# if not cap.isOpened():
#     print("file open failed")
#     cap.release()

# while cap.isOpened():
#     ret , frame = cap.read()
#     if not ret:
#         break
#     fgmask = fgbg.apply(frame)
#     out = cv2.VideoWriter("black.mov" , fourcc , fps , (w , h))
#     if not out.isOpened():
#         print("file open failed")
#         cap.release()
#         sys.exit()
#     cv2.imshow("frame" , frame)
#     cv2.imshow("bgsub" , fgmask)
#     if cv2.waitKey(1) & 0xff == 27:
#         break 

# cap.release()
# cv2.destroyAllWindows()

