# 스튜디오 관리 

Menu = dict(zip([1,2,3,4,5] , ["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"])) # 스튜디오 메뉴를 딕셔너리로 작성 
Price = dict(zip(["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"] , [20000 , 80000 , 200000 , 500000 , 800000]))  # 메뉴들을 key로 하여 가격 작성 
Option = dict(zip(["메이크업" , "헤어" , "의상대여"] , [30000 , 100000 , 150000]))  # 옵션 딕셔너리 작성 

class Talyor_Studio:    
    def __init__(self):  # 프로그램을 실핼했을시 콘솔창에 기본적으로 안내메뉴를 출력하도록 함
        print("Talyor 스튜디오 입니다.")
        print("야외 촬영 , 바디프로필 , 내부촬영 , 증명사진 , 웨딩촬영 등이 있습니다.")
        print("각 촬영의 가격은 메뉴에 기재되어 있으니 메뉴를 읽어보시고 예약부탁드립니다.")
        print("다른 손님과의 날짜가 겹칠 경우 고지를 해드리며 촬영가능한 날짜를 전송해드립니다.")
        print("타 문의 사항은 글을 남겨주시면 빠른시일내에 피드백을 해드리겠습니다.")
        print()
        
    def Choice(self , Choice):  # 코드 시작
        self.choice = Choice    # 인스턴스를 생성할때 input문을 이용해서 사용자 입력을 받아 매겨변수로 입력
        if Menu[Choice]:        # Chocice를 변수로 입력받아 고객이 원하는 촬영선택 
            print(Menu[Choice] , "을 선택하셨습니다.")  # 선택한 촬영 안내
            if Choice == 1:
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.") # 딕셔너리를 이용해서 선택한 촬영의 가격출력
                # 촬영 각각의 안내문구 출력
                print("증명사진은 따로 촬영장내에서 가능한 메이크업이나 헤어서비스가 제공되지 않습니다. 촬영장내 기본적인 드라이기와 헤어용품들은 있으니 참고하시길 바랍니다.")
                print("가급적 단정한 복장으로 상의는 흰티나 검은티를 추천드립니다.")
                print()
                
            elif Choice == 2:
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("내부촬영은 개인 촬영과 단체 촬영이 있습니다. 세부적으로 어떤 촬영을 원하시는지 선택해 주시길 바랍니다.")
                Subject = input("원하시는 촬영을 입력해주세요. : ")
                if Subject == "개인촬영":
                    print("개인 촬영의 가격은 그대로이고 옵션을 원하신다면 선택해주시기 바랍니다.")
                    print("옵션을 원하신다면 옵션을 선택해주시기 바랍니다.")
                # 옵션 선택 1번 촬영을 제외하고부터는 모든 촬영에 옵션이 생성되어 있으므로 옵션에 관한 선택여부와 안내 및 가격 안내
                    Want = input("옵션을 선택하시겠습니까?? : ")
                    if Want: 
                        print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , Price[Menu[Choice]] + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                    else:
                        print("옵션선택은 없으시기 때문에 촬영은 기존의 선택하신대로 진행하도록 하겠습니다.")
                elif Subject == "단체촬영":
                    print("단체촬영은 명수당 20000원이 추가가 됩니다.")
                    Human_number = int(input(""))
                    total_price_number2 = Price[Menu[Choice]] + (20000 * Human_number)
                    print("총 촬영하시는 고객님은 " , Human_number , "분 이시고 총 가격은 " , total_price_number2 , "입니다." )
                    print("옵션을 원하신다면 옵션을 선택해주시기 바랍니다.")
                    Want = input("옵션을 선택하시겠습니까?? : ")
                    if Want: 
                        print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , total_price_number2 + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                    else:
                        print("옵션선택은 없으시기 때문에 촬영은 기존의 선택하신대로 진행하도록 하겠습니다.")
                print()
            elif Choice == 3:
                only_Subject3_Price = dict(zip(["서울"  , "인천 경기" , "충청" , "경상" , "호남" ,"제주"] , [0 , 10000 , 20000 , 30000 , 40000 , 50000]))
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("야외촬영은 날씨의 영향을 받을 수 있고 따로 날씨에 상관없이 고객님께서 촬영진행을 원하시면 따로 추가적 금액이 없이 촬영은 진행합니다.")
                print("야외촬영은 출장비가 추가가 될수가 있습니다. 가격표는 다음과 같습니다." , only_Subject3_Price )
                Place = input("지역이 어디인가요? :")
                total_price_number3 = Price[Menu[Choice]] + only_Subject3_Price[Place]
                if Place == "인천 경기":
                    print("인천경기로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "충청":
                    print("충청으로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "경상":
                    print("경상으로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "호남":
                    print("호남으로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "제주":
                    print("제주로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                else:
                    print("서울은 따로 추가금액 있지않습니다!")
                print("야외촬영시 착용할 의상과 신발은 넉넉히 준비를 해오시기 바랍니다. 촬영이 원활하게 진행될시 추가로 컷을 더 가져갈 수 있기때문에 조금 번거롭더라도 준비를 해오시길 권장드립니다!!")
                print("야외촬영은 옵션을 추가하실시 메이크업팀이 같이 동행을 하게 됩니다. 옵션을 원하신다면 옵션을 선택해주세요.")
                Want = input("옵션을 선택하시겠습니까?? : ")
                if Want != "아니요": 
                    print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , total_price_number3 + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                elif Want == "아니요":
                    print("옵션선택은 없으시기 때문에 촬영은 기존의 선택하신대로 진행하도록 하겠습니다. 최종 결재금액은" , Price[Menu[Choice]] , "입니다.")
            elif Choice == 4:
                only_Subject4_Price = dict(zip([1,2,3] , ["보정본 추가" , "컨셉 변경" , "동반촬영"])) 
                Price_Table = dict(zip(["보정본 추가" , "컨셉 변경" , "동반촬영"] , [50000 , 20000 , 100000]))
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("바디프로필은 촬영하시는분이 어느정도의 몸을 완성해오시다면 편집으로 충분히 더 부각되고 선멸하게 근육의 조정이 가능합니다.")
                print("하지만 10년후에 가지게 될 몸을 포토샵을 만들어 달라고 요청하시는 것은 불가하니 촬영당일까지 열심히 운동을 하시고 충분히 자신감을 내비칠 수 있는 수준을 만들어 오시길 바랍니다.")
                print("프로필 촬영의 옵션을 알려드리겠습니다." , only_Subject4_Price , "입니다.")
                print("프로필 촬영은 헤어 , 메이크업 옵션과 프로필 촬영만의 옵션이 있습니다. 옵션 추가를 원하시면 옵션을 선택해주세요.")
                Want = input("헤어 메이크업 옵션을 선택하시겠습니까?? : ")
                Want2 = input("프로필 옵션은 선택하시겠습니까?")
                if Want != "아니요" and Want2 == "아니요":
                    print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , Price[Menu[Choice]] + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                elif Want == "아니요" and Want2 != "아니요":
                    total_price_number4 = Price[Menu[Choice]] + Price_Table[Want2]
                    print("옵션을 선택하셨고 추가가격은" , Price_Table[Want2] , "이며 총 지불해주셔야 하는 금액은" , total_price_number4 , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                elif Want != "아니요" and Want2 != "아니요":
                    total_price_number4 = Price[Menu[Choice]] + Price_Table[Want2]
                    print("기본 옵션과 프로필 옵션을 선택하셨고 추가가격은" , Option[Want] + Price_Table[Want2] , "이며 총 합금액은 " , total_price_number4 + Option[Want] , "입니다.")
            elif Choice == 5:
                Wadding_dress = dict(zip([1 , 2 , 3] , ["드레스 및 턱시도" , "한복" , "둘 다"]))
                Dress_Price = dict(zip(["드레스 및 턱시도" , "한복" , "둘 다"] , [300000 , 400000 , 700000]))
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("웨딩촬영의 경우 시간적으로 여유가 필요하므로 최소 2개월전에 예약을 부탁드립니다.")
                print("드레스와 턱시도는 촬영장에서 대여가 가능하며 신부메이크업과 헤어 또한 가능합니다. 신부메이크업과 헤어의 가격은 신랑님과 신부님 합쳐 500000원 입니다.")
                print("웨딩촬영 또한 보정본이 추가될시 추가금액이 들어가며 그에 따른 의상대여금액도 추가가 됩니다.")
                print("컨셉은 다음과 같이 있으며 컨셉 변경 및 보정추가 금액은 장당 50000원씩입니다." , Wadding_dress )
                Concept = int(input("어떤 컨셉을 하시겠어요?? : "))
                Total_Wadding_price = Price[Menu[Choice]] + Dress_Price[Wadding_dress[Concept]]
                Want_Hair_Makeup = input("헤어와 메이크업은 촬영장 내에서 받으실 건가요?? : ")
                if Want_Hair_Makeup == "네":
                    Total_Wadding_price + 500000
                elif Want_Hair_Makeup == "아니요":
                    None
                if Concept == "드레스 및 턱시도":
                    print(Wadding_dress[Concept] , "를 선택하셨습니다. 가격은" , Total_Wadding_price , "입니다!")
                elif Concept == "한복":
                    print(Wadding_dress[Concept] , "를 선택하셨습니다. 가격은" , Total_Wadding_price , "입니다!")
                elif Concept == "지유복장":
                    print("자유복장은 추가금액이 없습니다! 그리고 자유복장의 헤어 , 메이크업은 기존에 옵션에서 선택을 해주시기 바랍니다. 옵션 : " ,Option )
                elif Concept == "둘 다":
                    print("컨셉을 2가지 선택을 해주셨고 현재 이벤트 진행중이므로 최종금액에서 10%를 할인해드립니다! 그러므로 최종금액은 " , Total_Wadding_price - (Total_Wadding_price * 10), "입니다.")
                Fixed_pic = int(input("보정 장수는 몇장을 하시겠어요?? : "))
                if Fixed_pic != 0 :
                    Total_Wadding_price + (50000 * Fixed_pic)
                    print("최종 가격은 ",Total_Wadding_price + (50000 * Fixed_pic) , "입니다.")
                else:
                    print("보정 장수 추가는 선택하지 않으셨습니다. 최종 가격은" , Total_Wadding_price , "입니다.")

# 인스턴스 생성 후 input으로 촬영을 선택
Client1 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client1.Choice(Choice)

Client2 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client2.Choice(Choice)

Client3 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client3.Choice(Choice)

Client4 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client4.Choice(Choice)

Client5 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client5.Choice(Choice)

'''===================================================================================================================================================='''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("Qt_Designer/Project.ui")[0]    # form class로 파일을 불러옵니다.

class DeMoForm(QMainWindow , form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
# 각각의 pushbutton의 함수를 달아서 클릭이라는 이벤트가 발생된 순간 다른 label 박스의 텍스가 변경되게 함
    def clicked_1(self):
            self.middle_option.setText("증명사진은 추가금액은 없으며 기본 옵션선택은 가능합니다.")
    def clicked_2(self):
            self.middle_option.setText("내부촬영은 개인촬영과 단체촬영이 있습니다. # 단체촬영시 + 명수 * 20,000")
    def clicked_3(self):
            self.middle_option.setText("야외 촬영은 지역이동시 추가금액이 있습니다. 세부항목을 확인해주시기 바랍니다.")
    def clicked_4(self):
            self.middle_option.setText("바디프로필은 헤어와 메이크업은 꼭 하도록 강조드리며 외부샵에서 시술을 받고 오셔도 무관합니다.")
    def clicked_5(self):
            self.middle_option.setText("웨딩촬영은 신랑 , 신부 메이크업이 준비되어 있으며 촬영의상대여 또한 금액이 추가됩니다.")
# 위와 비슷한 유형의 함수로서 lineedit박스에 글자를 입력하고 그 글자와 맞는 세부옵션사항을 text로 출력시켜줌
    def Text_Changed(self):
        if self.Enter:
            self.print_option.setText(str(self.lineEdit.text()))
        if self.print_option.text() == "증명사진":
            self.print_option.setText("증명사진은 추가금액은 없으며 기본 옵션선택은 가능합니다.")
        elif self.print_option.text() == "내부촬영":
            self.print_option.setText("단체촬영시 명당 + 20,000")
        elif self.print_option.text() == "야외촬영":
            self.print_option.setText("[서울 : 변동없음][인천 ,경기 : 10,000][충청 : 20,000][경상 : 30,000][호남 : 40,000][제주 : 50,000]")
        elif self.print_option.text() == "바디프로필":
            self.print_option.setText("[프로필 전용 헤어,메이크업 : 100,000]")
        elif self.print_option.text() == "웨딩촬영":
            self.print_option.setText("[드레스 , 슈트 : 100,000][한복 : 120,000]")
# 문제의 Luckey번호인데 제작의도는 럭키박스와 번호가 같으면 최종가격에서 10%를 할인해주는 함수를 작성하려고 했으나 TypeError: argument 1 has unexpected type 'QPushButton'라는 에러가 나와서 고민을 하게 되었고 아직까지 고민중이다.
    def Luckey_Button(self):
        self.Lucky_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Lucky_Button.setGeometry(QtCore.QRect(210, 100, 81, 26))
        Luckey_number = random.random.choice(1,10)
        if self.Luckey_Button:
            if Luckey_number == 7:
                self.event.setText("당첨입니다!!!!!")
            else:
                self.event.setText("어림도 없는 번호네요")

# 기본적으로 베이스 파일을 작성을 해놓은 다음 Designer을 사용해서 ui파일을 py파일로 변경시켜준 코드라 아래 문장들의 코드는 push button 또는 label정도이다. 
# ui파일을 py로 변경시켜주었을때 py형식으로만 작성을 하면 굉장히 오래걸렸을 내용들은 간단하게 구성할 수가 있었다.
# 파일 변경 명령어는 qtuic 파일이름.ui -o 파일이름.py 이다.
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(109, 10, 70, 21))
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(200, 10, 70, 21))
        self.Button_2.setObjectName("Button_2")
        self.Button_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(370, 10, 80, 21))
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(460, 10, 70, 21))
        self.Button_5.setObjectName("Button_5")
        self.Button_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(280, 10, 70, 21))
        self.Button_3.setObjectName("Button_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 580, 40))
        font = QtGui.QFont()
        font.setFamily("Sathu")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 260, 16))
        font = QtGui.QFont()
        font.setFamily(".SF NS Mono")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.event = QtWidgets.QLabel(self.centralwidget)
        self.event.setGeometry(QtCore.QRect(20, 440, 611, 41))
        self.event.setObjectName("event")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(210, 100, 81, 26))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Enter.setFont(font)
        self.Enter.setObjectName("Enter")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 170, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.print_option = QtWidgets.QLabel(self.centralwidget)
        self.print_option.setGeometry(QtCore.QRect(30, 180, 590, 60))
        self.print_option.setObjectName("print_option")
        self.middle_option = QtWidgets.QLabel(self.centralwidget)
        self.middle_option.setGeometry(QtCore.QRect(30, 140, 590, 20))
        self.middle_option.setObjectName("middle_option")
        self.Lucky_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Lucky_Button.setGeometry(QtCore.QRect(440, 450, 90, 30))
        self.Lucky_Button.setObjectName("Lucky_Button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Button_1.clicked.connect(MainWindow.clicked_1)
        self.Button_2.clicked.connect(MainWindow.clicked_2)
        self.Button_3.clicked.connect(MainWindow.clicked_3)
        self.Button_4.clicked.connect(MainWindow.clicked_4)
        self.Button_5.clicked.connect(MainWindow.clicked_5)
        self.lineEdit.editingFinished.connect(self.Enter.click)
        self.Enter.clicked.connect(MainWindow.Text_Changed)
        self.Lucky_Button.clicked.connect(MainWindow.Lucky_Button)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Talyor\'s Photo"))
        self.Button_1.setText(_translate("MainWindow", "증명사진 "))
        self.Button_2.setText(_translate("MainWindow", "내부촬영"))
        self.Button_4.setText(_translate("MainWindow", "바디프로필"))
        self.Button_5.setText(_translate("MainWindow", "웨딩촬영"))
        self.Button_3.setText(_translate("MainWindow", "야외 촬영"))
        self.label.setText(_translate("MainWindow", "메뉴"))
        self.label_2.setText(_translate("MainWindow", "[증명사진 : 20,000] [내부촬영 : 80,000] [야외촬영 : 100,000] [바디프로필 : 300,000] [웨딩촬영 : 500,000]"))
        self.label_3.setText(_translate("MainWindow", "Menu Table"))
        self.event.setText(_translate("MainWindow", "기본 헤어,메이크업 : 50,000 | 7월 이벤트! 행운번호 7을 뽑으시면 10% 할인!! | "))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.lineEdit.setText(_translate("MainWindow", "안녕하세요"))
        self.print_option.setText(_translate("MainWindow", "금액 추가 세부사항"))
        self.middle_option.setText(_translate("MainWindow", "옵션 세부사항"))
        self.Lucky_Button.setText(_translate("MainWindow", "행운번호 추첨!"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demowindow = DeMoForm()
    demowindow.show()
    app.exec_()