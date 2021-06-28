# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# form_class = uic.loadUiType("panhong.ui")[0]
# Menu = dict(zip(["1","2","3","4","5"] , ["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"]))
# Price = dict(zip(["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"] , [20000 , 80000 , 200000 , 500000 , 800000]))
# Option = dict(zip(["메이크업" , "헤어" , "의상대여"] , [30000 , 100000 , 150000]))

# class DeMoForm(QMainWindow , form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         print("Talyor 스튜디오 입니다.")
#         print("야외 촬영 , 바디프로필 , 내부촬영 , 증명사진 , 웨딩촬영 등이 있습니다.")
#         print("각 촬영의 가격은 메뉴에 기재되어 있으니 메뉴를 읽어보시고 예약부탁드립니다.")
#         print("다른 손님과의 날짜가 겹칠 경우 고지를 해드리며 촬영가능한 날짜를 전송해드립니다.")
#         print("타 문의 사항은 글을 남겨주시면 빠른시일내에 피드백을 해드리겠습니다.")
#         print()
#         text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
#     def FacePhoto(self):
#         self.label.setText("증명 사진")
#         self.label_4.setText("증명사진은 기본옵션은 없고 깔끔한 흰티나 검은색티로 준비하시는 것을 권고드립니다.")
#     def Price_1(self):
#         self.number = "1"
#         self.label_5.setText(str(Price[Menu[self.number]]))
#     def StudioPhoto(self):
#         self.label.setText("내부 촬영")
#         self.label_4.setText("내부촬영은 종류가 개인촬영과 단체촬영이 있습니다.")
#     def Studio_Price_1(self):
#         self.label_4.setText("개인촬영은 기본가격과 동일합니다. 옵션을 원하신다면 옵션을 선택해주시기바랍니다.")
#         self.number = "2"
#         # text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
#         self.label_5.setText(str(Price[Menu[self.number]]))
#     def Studio_Price_2(self):
#         self.label_4.setText("단체촬영은 촬영하시는 고객님 한분당 20000원 추가입니다. 이 점 이해해주시기 바랍니다. **옵션 추가 가능")
#     def OutPhoto(self):
#         self.label.setText("야외 촬영")
#         self.label_4.setText("야외 촬영은 기본적으로 추가기능은 없지만 지역 이동에 따라서 추가가격이 생겨나게 됩니다.")
#     def Out_Price_1(self):
#         self.Option_change.setText("서울 : 추가가격 없음")
#         self.number = "3"
#         self.label_5.setText(str(Price[Menu[self.number]]))
#     def Out_Price_2(self):
#         self.Option_change.setText("인천 , 경기 : + 10,000")
#         self.number = "3"
#         self.Option_change_Price.setText(str(Price[Menu[self.number]] + 10000))
#         # self.label_5.setText(str(Price[Menu[self.number]] + 10000))
#     def Out_Price_3(self):
#         self.Option_change.setText("충청 : + 20,000")
#         self.number = "3"
#         self.Option_change_Price.setText(str(Price[Menu[self.number]] + 20000))
#         self.label_5.setText(str(Price[Menu[self.number]] + 20000))
#     def Out_Price_4(self):
#         self.Option_change.setText("경상 : + 30,000")
#         self.number = "3"
#         self.Option_change_Price.setText(str(Price[Menu[self.number]] + 30000))
#         self.label_5.setText(str(Price[Menu[self.number]] + 30000))
#     def Out_Price_5(self):
#         self.Option_change.setText("호남 : + 40,000")
#         self.number = "3"
#         self.Option_change_Price.setText(str(Price[Menu[self.number]] + 40000))
#         self.label_5.setText(str(Price[Menu[self.number]] + 40000))
#     def Out_Price_6(self):
#         self.Option_change.setText("제주 : + 50,000")
#         self.number = "3"
#         self.Option_change_Price.setText(str(Price[Menu[self.number]] + 50000))
#         # self.label_5.setText(str(Price[Menu[self.number]] + 50000))
#     def BodyProfile(self):
#         self.label.setText("바디프로필")
#         self.label_4.setText("기본 옵션으로는 헤어,메이크업이 있습니다.")
#     def WaddingPhoto(self):
#         self.label.setText("웨딩 촬영")
#         self.label_4.setText("기본 옵션으로는 헤어,메이크업이 있습니다.")
#     def Option(self):
#         self.label_4.setText("메이크업 : 30,000 \n 헤어 : 100,000 \n 의상대여 : 150,000")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     demowindow = DeMoForm()
#     demowindow.show()
#     app.exec_()
    
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.lbl = QLabel(self)
#         self.lbl.move(60, 40)

#         qle = QLineEdit(self)
#         qle.move(60, 100)
#         qle.textChanged[str].connect(self.onChanged)

#         self.setWindowTitle('QLineEdit')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()

#     def onChanged(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

