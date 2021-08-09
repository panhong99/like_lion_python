# 이미지 스켈레톤 그리기
import cv2

class motion_tracking:
    def tracking_motion(self , image):
        self.image = image
        # MPII에서 각 파트 번호, 선으로 연결될 POSE_PAIRS
        BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                        "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                        "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                        "Background": 15 }

        POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                        ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                        ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                        ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]
            
        # 각 파일 path
        protoFile = "/Users/panhong/Desktop/openpose_sample/pose_deploy_linevec_faster_4_stages.prototxt"
        weightsFile = "/Users/panhong/Desktop/openpose_sample/pose_iter_160000.caffemodel"
        
        # 위의 path에 있는 network 불러오기

        # 1번 인수는 .protext파일의 경로 
        # 2번 인수는 학습된 모델이 있는 .caffemodel파일의 경로
        net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

        # opencv를 이용하여 이미지 읽어오기
        # image = image

        # frame.shape = 불러온 이미지에서 height, width, color 받아옴
        # 1 = 이미지의 높이 , 2 = 이미지의 너비 , 3 = 이미지의 채널
        imageHeight, imageWidth, _ = image.shape


        # network에 넣기위해 전처리
        # blob = 동일한 방식으로 전처리된 동일한 너비 , 높이 , 채널 수를 가진 하나 이상의 이미지
        # 변수 설명
        # image = 입력 영상 , 이미지
        # scalefavtor = 입력 영상 픽셀 값에 곱할 값 , 기본값은 1 
        # size = 출력 영상의 크기(이 코드에서는 지정해놓은 weight , heigth의 값)
        # mean = 입력영상 각 채널에서 뺼 평균 값 , 기본값은 (0,0,0)
        # swapRB = R 과 B채널을 서로 바꿀것인지 결정하는 플래그 , 기본값은 False
        # crop = 크롭 수행 여부 , 기본값은 False
        inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (imageWidth, imageHeight), (0, 0, 0), swapRB=False, crop=False)
        
        # network에 넣어주기
        # 가져온 이미지를 입력
        net.setInput(inpBlob)

        # 결과 받아오기
        # 매개변수를 입력해주지 않아서 해석하면 전체네트워크에 대해 
        # 정방향 전달을 실행
        output = net.forward()

        # output.shape[0] = 이미지 ID, [1] = 출력 맵의 높이, [2] = 너비
        H = output.shape[2]
        W = output.shape[3]
        print("이미지 ID : ", len(output[0]), ", H : ", output.shape[2], ", W : ",output.shape[3]) # 이미지 ID

        # 키포인트 검출시 이미지에 그려줌
        points = []
        for i in range(0,15):
            # 해당 신체부위 신뢰도 얻음.
            probMap = output[0, i, :, :]
        
            # global 최대값 찾기
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

            # 원래 이미지에 맞게 점 위치 변경
            x = (imageWidth * point[0]) / W
            y = (imageHeight * point[1]) / H

            # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로    
            if prob > 0.1 :    
                cv2.circle(image, (int(x), int(y)), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)       # circle(그릴곳, 원의 중심, 반지름, 색)
                cv2.putText(image, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, lineType=cv2.LINE_AA)
                points.append((int(x), int(y)))
            else :
                points.append(None)

        # 점만 찍혀있는 이미지 출력
        cv2.imshow("Output-Keypoints",image)
        cv2.waitKey(0)

        # 이미지 복사
        imageCopy = image

        # 각 POSE_PAIRS별로 선 그어줌 (머리 - 목, 목 - 왼쪽어깨, ...)
        for pair in POSE_PAIRS:
            partA = pair[0]             # Head
            partA = BODY_PARTS[partA]   # 0
            partB = pair[1]             # Neck
            partB = BODY_PARTS[partB]   # 1
            
            print(partA," 와 ", partB, " 연결\n")
            if points[partA] and points[partB]:
                cv2.line(imageCopy, points[partA], points[partB], (255, 0, 0), 2)

            # 라인이 그려진 이미지를 출력
            cv2.imshow("Output-Keypoints",imageCopy)
            cv2.waitKey()
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)

