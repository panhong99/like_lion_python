'''PyQt GUI'''
# 설치 명령어 Terminal에 pip install PyQt5 and PyQt-tools
# open -a Designer 터미널 명령어
# ui 파일을 py코드로 변환시키기 ==> pyuic5 파일이름.ui -o 파일이름.py 
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("21.06.24_likelion_mainform2.ui")[0]

class DemoForm(QDialog , form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def first(self):
        self.label.setText("첫번째 버튼을 클릭")
    def second(self):
        self.label.setText("두번째 버튼을 클릭")
    def third(self):
        self.label.setText("세번째 버튼을 클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demowindow = DemoForm()
    demowindow.show()
    app.exec_()

'''class 문법'''
'''클래스는 객체지향적으로 프로그래밍 된다.'''
'''매서드는 클래스 안에 들어있는 함수를 뜻함''' 
'''클래스는 붕어빵 틀이라고 생각하면 된다. 클래스 자체를 사용할 수 없지만 하단에 james처럼 인스턴스를 설정해주고 인스턴스를 사용해서 실행을 해준다.'''
class person():             # class의 기본적인 형태이다. 최상단에 클래스가 존재하고 매개변수인 함수를 설정하고 내용을 작성한다.
    def greeting(self):
        print("Hello")
'''인스턴스가 꼭 생성이 되어야지만이 클래스를 사용할 수 있다.'''
'''클래스를 통해서 인스턴스를 만든것이다.'''
james = person()            # james라는 변수에 class를 지정해주고  인스턴스 = 클래스
james.greeting()            # class에 매개변수인 greeting함수를 호출한다.

a = 10 
b = [0,1,2]
maria = person()

print(type(a))
print(type(b))
print(type(maria))

'''init메서드는 클래스 자체에 변수라고 생각하면 된다. 내가 클래스를 만들때 뭔가 초기화 하고 싶은게 있다면 그것을 입력하면 된다.'''
'''클래스에 init은 꼭 들어가야 하는 문법이다. self는 인스턴스 자기 자신을 의미함 init매겨변수에 self에 들어가는 값은 person()이라 할 수 있다.'''

class person():
    def __init__(self):     # 기본적으로 person이라는 클래스를 호출하면 자연스럽게 작성하게 되는 들여쓰기 같은것이다.
        self.hello = "안녕하세요 저는 사람입니다."  # 따로 인스턴스를 지정하지 않아도 person 클래스만 호출한다면 출력되게 된다.
    def greting(self):          # 함수를 호출하려면 인스턴스를 생성한다음 인스턴스이름.greting 이런식으로 호출해주면 된다.
        print(self.hello)       # self.hello를 호출하라고 되어있기때문에 인스턴스를 실행시키면 self.hello의 문구가 실행된다.

james = person()    # 다음과 같은 형식으로 클래스를 사용해주면 된다.
james.greting()

'''self는 class를 작성을 하면 본인을 나타내는 것이므로 팥빵 속에 팥이라고 생각을 하면 된다.'''

class person():
    def __init__(self , name , age , address): # self는 class 자체 , name age address는 매개변수이다. 그러므로 class를 호출할때 self를 제외한 3가지의 매개변수에 할당하는 값을 입력하고 호출을 해주어야 한다.
        self.hello = "안녕하세요."  # self.hello 같은 경우는 값을 할당해주었다. def __init__의 할당값이라고 생각을 하면 될 것 같다.
        self.name = name
        self.age = age
        self.address = address
    
    def gretting(self):
        print("{0} 저는 {1} 입니다.".format(self.hello , self.name))

name = input("이름이 뭐죠")
age = input("나이는요?")
address = input("주소는 뭐죠")
maria = person(name ,age , address)     # name , age , adress 를 input으로 입력을 받고 매개변수로 할당을 해주었다.

print("이름" , maria.name)              # maria.name의 값은 상단에 name으로 할당해 주었기때문에 호출을 하면 maria가 출력된다.
print("나이" , maria.age)               # 상단과 같은 개념이다.
print("주소" , maria.address)

name = input("이름이 뭐죠")
age = input("나이는요?")
address = input("주소는 뭐죠?")
james = person(name ,age , address)

print("이름" , james.name)
print("나이" , james.age)
print("주소" , james.address)

class person:
    def __init__(self , name , age , address , wallet): # self는 class 자체 , name age address는 매개변수이다. 그러므로 class를 호출할때 self를 제외한 3가지의 매개변수에 할당하는 값을 입력하고 호출을 해주어야 한다.
        self.hello = "안녕하세요."  # self.hello 같은 경우는 값을 할당해주었다. def __init__의 할당값이라고 생각을 하면 될 것 같다.
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet # 변수 앞에 .__를 붙여서 비공개 속성으로 만듦
    def pay(self , amount):     # 비공개 속성으로 된 self는 외부에서는 호출할 수 없지만 따로 변수를 생성하고 그 변수를 이용해서 결과를 알아볼수는 있다.
        self.__wallet -= amount
        print("이제 {0}원 남았네요.".format(self.__wallet))

# 비공개 속성은 person내에서만 확인 가능 
# 외부에서 접근을 하려하면 오류 발생 
maria = person("마리아" , 20 , "부산 서구" , 10000)
maria.pay(3000)

'''class의 문법사항으로 init과 self는 조건문에 들여쓰기를 해주는 것과 같다.'''
class Annie:
    def __init__(self  , health , mana , ability_power):
        self.체력 = health      # 앞에 self를 붙이는 이유는 class에서 본인이 관리하는것이라는 것을 표현해주기 위해 기본적으로 함께 작성을 해주어야 한다.
        self.mana = mana
        self.ability_power = ability_power
    
    def tibbers(self):
        print("티버 피해량 : {0}".format(self.ability_power * 0.65 + 400))  # 다음과 같이 함수내에 연산을 해주고 출력하면 연산된 값이 나오게도 가능하다.

health , mana , ability_power = map(float , input().split())

monster = Annie(health = health , mana = mana , ability_power = ability_power)
monster.tibbers()

'''오렌지박스 프로그램으로 클래스의 이해와 응용도를 높이기 위함으로 진행을 해보았다.'''
'''오렌지 박스는 각각 더하기 , 빼기 , 비우기 , 내부 확인 등으로 이루어져 있고 각각의 연산을 할당하는 함수를 클래스내에서 작성을 해주었다.'''
'''나름 가독성 있게 작성한것 같고 함수내의 연산과 작성한 코드의 양도 많지 않아 쉽게 이해를 할 수 있다.'''

class Orange_box:
    def orange(self , number): 
        self.orange = number
        print("현재 오렌지의 개수",self.orange)
    def add_orange(self , add):
        self.add = add
        self.orange += self.add         # self.add의 값을 self.orange 값에 더해준다.
        print("박스에" , self.add ,"를 추가해 현재는" , self.orange , "개 가 있습니다.")
    def minus(self , minus):
        self.minus = minus              # 빼준다.
        self.orange -= self.minus
        print("박스에" , self.minus ,"를 마이너스해서 현재는" , self.orange  , "개 가 있습니다.")
    def clear(self , clear):
        self.clear = clear              # 초기화 시켜준다.
        self.orange = self.clear
        print("박스가 깔끔합니다.")
    def check(self):
        self.__check = self.orange  # 현재 박스에 오렌지가 몇개인지 확인하는 함수이지만 비공개로 작성이 되있어 내부에서만 확인이 가능하다.
        print("현재 오렌지박스에 오렌지의 개수는" , self.orange ,"개 입니다.")
    def check_out(self , check_orange):
        self.check_orange = check_orange    # 오렌지의 남은개수를 확인하는 것은 비공개로 되어있어 확인이 어렵기 때문에 
        self.__check -= self.check_orange   # 새로운 함수를 만들어 self.__check에 영향을 주어 암묵적으로 확인을 할 수 있게 해주었다.
        if self.__check < 0:
            print("박스가 텅텅 비어있습니다.")
        else:
            print(self.check_orange ,"개를 박스에서 꺼냈더니" , self.__check , "개가 남았다.")

orange_status = Orange_box() # 10   각각의 함수의 매개변수를 할당 해주었다.
orange_status.orange(10) # 10
orange_status.add_orange(5)    # 15
orange_status.minus(5)  # 10 
orange_status.clear(0)  # 0
orange_status.check()   # status
orange_status.check_out(1) # status
