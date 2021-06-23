# 다소 복잡한 nonlocal에 대한 설명을 코드로 나타내고 있다.
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x # 겹겹히 함수를 작성을 하고 nonlocal을 해주면 바로 근처의 변수를 찾아서 변경된 내용을 할당을 해준다.
            nonlocal y
            x = x + 30      # 가장 근처에 있는 x는 B함수에 있으므로 x = 20이 되고 출력되는 x의 값은 50이된다.
            y = y + 300     # y는 A의 함수에 있고 값은 100이므로 출력되는 y의 값은 400이 된다.
            print(x)
            print(y)
        C()
    B()
A()

x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x        # 전역변수 x를 사용하겠다고 지정을 해주었다.
            x = x + 30      # x = 1이 전역변수이므로 x + 30 이 되어 x의 출력값은 31이 된다.
            print(x)
        C()
    B()
A()

def calc():                 # 이중 함수이다.
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b            
    return mul_add          # return은 2번째 함수의 호출을 해주었다. 

c = calc()
print(c(1) , c(2) , c(3) , c(4) , c(5))     # 첫번째 함수를 호출해주었고 각각 1,2,3,4,5를 매개변수로 지정을 해주었으므로 값은 각각 8 , 11 , 14 , 17 ,20 으로 출력이 된다.

def calc():                                 # labmda 함수로 코드를 조금 간결하게 작성을 해주었다.
    a = 3
    b = 5
    return lambda x : a * x + b

c = calc()
print(c(1) , c(2) , c(3) , c(4) , c(5))

'''이 코드에 경우 total 변수의 값이 초기화 되지 않고 유지되는데 이유는 mul_add함수의 
위치에서 보면 외부의 값이 있으므로 total의 출력값은 초기화 되지 않는것이다.'''
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total  # 현재 함수에 바깥에 있는 total이라는 함수의 값을 사용
        total = total + a * x + b       # total값을 받아와 값을 변경 
        print(total)
    return mul_add

c = calc()
c(1)                    # total의 값은 초기화가 되지 않으므로 8 , 19 , 33이 출력이 된다.
c(2)
c(3)

def counter():
    i = 0
    def count():
        nonlocal i 
        i = i + 1
        return i # return을 사용해주어야 반환할 값이 생겨나므로 return이나 print를 사용해주어야 한다.
    return count
    


c = counter()           # counter 함수를 호출 
for i in range(10):     # 결과는 1 ~ 10이 출력이 되는데 위에 i + 1을 보면 갈증이 해소될수가 있다.
    print(c() , end = " ")  # 반복문의 i는 그저 반복을 위한 것이고 c의 값과 관련이 있는것은 counter 함수내에 count가 작동되고 i는 외각의 변수이므로 반복문이 진행하는 동안 + 1이 된다.
                            # 클로저라는 기능이라고 한다.

'''파일의 입출력 과정'''
'''키보드로 입력하는 것을 펴준입력 , 모니터로 출력하는 것을 표준출겨이라 함 , 
또 키보드와 모니터를 합쳐서 콘솔이라 함 '''

'''파일의 위치를 지정해서 그 파일의 내용을 읽어오는 함수'''
file = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")
inStr = file.readline()                 # file로 읽어온 내용들을 print해준다.
print(inStr , end = "")
inStr = file.readline()
print(inStr , end = "")
inStr = file.readline()
print(inStr , end = "")
inStr = file.readline()
print(inStr , end = "")
inStr = file.readline()
print(inStr , end = "")
file.close()

inFp = None                         # 값을 받을 변수 2개를 지정한다.
inStr = ""
inFp = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")  # inFp로 파일의 내용을 읽어들인다.
while True:                     # 반복문 생성 
    inStr = inFp.readline()     # inFp로 읽어들인 값을 inStr의 내용으로 업데이트를 해준다.
    if inStr == "":             # inStr의 내용을 모두 출력하여 초기의 빈 변수로 되면 반복문을 종료한다.
        break
    print(inStr , end="")       # 내용이 있을 동안 줄바꿈을 하지않고 지속해서 반복을 해준다. 기본적으로 파일의 내용을 불러올떄 2줄씩 줄바꿈이 되었으므로 1줄만 줄바꿈을 해주기 위해 줄바꿈처리를 해준다.

inFp.close()                    # 항상 파일을 개방하고 닫아주어야 한다.

'''readline 과 readlines 함수의 차이점은 readline는 파일의 한줄을 가져와 문자열로 변환을 하고 
readlines는 파일 내용 전체를 한번에 가져와 리스트로 반환을 해준다.'''

inFp = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8") # 후미에 encoding = "utf-8"로 지정을 해주어야 한글깨짐을 방지할 수 있다.
inList = []
inList = inFp.readlines() # <= readlines() 함수는 파일의 내용을 통으로 리스트에 저장
for i in inList:          # 반복문으로 읽어들인 파일의 내용을 출력
    print(i ,end="")
inFp.close()

file = input("파일명을 입력하세요. :")      # 사용자의 입력을 받아 파일을 선택하고 내용을 출력한다.
File = open(file , "r" , encoding="utf-8")
view = []
view = File.readlines()
for i in view:
    print(i , end="")
File.close()

outFp = None                    # 2개의 변수 생성 
outStr = ""
 
outFp = open("21.06.22_likelion(p)2.txt" , "w" , encoding="utf-8")      #파일이 있다면 해당 파일을 없다면 새로운 파일을 생성을 쓰기전용으로 불러온다.

while True:
    outStr = input("내용 입력 : ")                                        # input으로 받은 내용이 있다면 파일에 input을 작성을 해주고 
    if outStr != "":                                                    # 없다면 반복문을 종료해준다.
        outFp.write(outStr+ "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 써졌음 ---")

'''copy를 만들려면 리스트전체를 읽어와서 입력은 불가능하고 반복문을 통해서 한줄씩 카피파일에 입력을 시켜주어야 한다.'''

file = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")
File = file.readlines()
file2 = open("21.06.22_likelion(p.copy).txt" , "w" , encoding = "utf-8")
for i in File:
    file2.write(i)
file.close()
file2.close()

inFp , outFp = None , None 
inStr = ""
inFp = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")
outFp = open("21.06.22_likelion(p.copy).txt" , "w" , encoding = "utf-8")
inList = inFp.readlines()
outFp.writelines(inList)                # writelines함수를 이용해서 전체의 파일의 값을 받아오고 한번에 원하는 파일에 저장을 해줄 수 있다.
inFp.close()
outFp.close()
print("---정상적으로 파일이 복사되었음---")

'''암호화 시키기'''
# 변수 선언
inFp , outFp = None , None 
inStr , outStr = "" , ""
i = 0 
secu = 0

# 메인 코드 부분 
secuYN = input("1.암호화  2. 암호해석 중 선택 : ")
inFname = input("입력 파일명을 입력하세요. : ") 
outFname = input("출력 파일명을 입력하세요. : ")

if secuYN == "1" :                  # input이 "1"이라면 secu는 + 100
    secu = 100
elif secuYN == "2" :                # "2"라면 -100
    secu -= 100

inFp = open(inFname , "r" , encoding = "utf-8")     # 암호화를 시킬 파일
outFp = open(outFname , "w" , encoding = "utf-8")   # 암호화 시킨 내용을 저장할 파일 

while True:                                         # inStr변수에 값이 있는동안 반복 
    inStr = inFp.readline()
    if not inStr:
        break
    
    outStr = ""
    for i in range(0, len(inStr)):                  # inStr의 길이만큼 for문을 실행 
        ch = inStr[i]                               # ch라는 변수를 생성하고 inStr의 한 글자를 입력 
        chNum = ord(ch)                             # ch로 받아들인 문자를 아스키 코드로 변환 
        chNum = chNum + secu                        # 아스키 코드는 숫자이므로 변환된 숫자에 secu를 할당 (상단에 secu에 대한 내용이 작성되어 있음)
        ch2 = chr(chNum)                            # 2번 변환된 아스키코드를 chr함수를 사용해 특정 문자로 변경 
        outStr = outStr + ch2                       # outStr 함수에 암호화된 특정문자를 저장 

    outFp.write(outStr)                             # outFp에 암호화된 outStr을 저장 

outFp.close()                                       # 파일 닫기 
inFp.close()
print(" %s --> %s 변환 완료 " %(inFname , outFname))    # 파일들의 이름을 출력하여 변환이 완료 되었다고 알림 

import time                                         # 시간에 대한 내용들을 사용할 수 있게 해주는 time 라이브러리
import random                                       # random 라이브러리

game = open("Eng_LowData.txt" , "r" , encoding = "utf-8")   # 파일을 game라는 변수로 읽어준다.
Quiz = []                                           # 변수 2 개 생성 
Source = ""                                         

while True:     # 무한 루프 생성 
    Source = game.readline()    # Source변수로 game의 내용을 읽음     
    Source = Source.replace("," , "") # 한줄씩 받아들이면 각 문자마다  , 로 구분되어 있으므로 replace함수를 사용해서 하나의 문자열로 만들어준다.
    if Source == "":            # Source의 내용이 없다면 종료 
        break
    elif Source != "\n":        # Source의 내용중 "\n"과 같지않다면 
        print(Source , end = "")    # 줄바꿈 방지를 하고 출력
        Quiz.append(Source.rsplit())   # Quiz라는 미리 생성해놓은 빈 리스트에 내용을 저장 
game.close()        # 파일 닫기

print()
Start = input("게임을 시작할까요?")     # 게임 시작안내문자 
begin = time.time()                 # 타이머 시작 
i = 1
x = 0
result = random.choice(Quiz[x])        # result변수를 생성하고 random.choice()함수를 이용해 랜덤으로 Quiz의 내용을 받아옴 
while i <= 5:                       # i가 5보다 작을동안은 무한루프 
    print(result)                   # 사용자에게 문제를 보여준다.
    answer = input()                # 사용자가 정답을 입력할 input변수 생성 
    if answer == 0:                 # 사용자가 0을 입력한다면 게임 종료 
        print("게임을 종료합니다")
        break
    if result == answer:            # 입력과 문제의 정답이 일치한다면 정답이란 문구를 출력하고 i + 1
        print("정답입니다!")
        x += 1
        i += 1
        result = random.choice(Quiz[x])    # 정답을 맞췄을 시 새로운 문제를 생성 
    else:                               # 틀렸을시 오답 안내문구 출력 
        print("오답입니다.")
    
end = time.time()                       # 끝남과 동시에 타이머가 멈추고 소요시간 출력 
print("총 소요시간은 ",int(end - begin) , "분 입니다.")
    
'''GUI를 이용하는 방법 프런트를 파이썬으로 만들어 본다고 생각'''
'''Terminal에서만 결과를 보지않고 시각화를 해서 작성한 코드의 결과를 볼 수 있음'''
'''문법은 좀 다르나 html , css ,js와 같다고 생각을 하면 될것같다.'''
import tkinter as tk
root = tk.Tk() # tk.Tk 라는 매서드를 생성을 하면 root를 생성(빈 페이지를 생성한다고 생각하면됨)

lbl = tk.Label(root , text="EduCoding" , underline = 3)  # 페이지 제목이라고 생각
lbl.pack()           # 빈 창에 무언가 어떠한 도구들을 추가
 
txt = tk.Entry(root) # 텍스트를 입력하는 상자 
txt.pack()           


btn = tk.Button(root , text="OK" , activebackground = "red" , width = 5)
'''검색버튼이라고 생각 '''
btn.pack()

root.mainloop()

'''python으로 사용할 수 있는 GUI 툴 킷 찾아보기'''
'''python을 사용하지 않더라도 파이썬 코드를 받아 시각화 할 수 있는 GUI키트 찾아보기'''
import tkinter as tk
# Tk 객체 인스턴스 생성 
root = tk.Tk() 

# 라벨 생성 
label = tk.Label(root , text= "Hello world")

# 라벨 배치
label.pack()

# 라벨 표시
root.mainloop()

import tkinter as tk

root = tk.Tk() 

# 함수가 작동이 되면 pushed라고 문자열을 출력해라 
def func():
    print("Pushed")

# command 함수를 보면 버튼을 사용자가 클릭을 할때마다 event가 일어나서 command에 지정되어 있는 func함수를 실행한다.
button = tk.Button(root , text= "Push" , command = func)
# 라벨 배치
button.pack()

# 라벨 표시 
root.mainloop()


import tkinter as tk # GUI 라이브러리 python의 내장 함수

root = tk.Tk() 

def func(): # 함수 생성 
    label.config(text = "Pushed") # 버튼이 눌리면 pushed라고 변경

label = tk.Label(root , text = "Push Button") # Label을 만들고 라벨내에 텍스트를 push button 삽입 
label.pack() 

button = tk.Button(root , text = "Push!" , command = func) # 버튼이 클릭이 되는 이벤트가 발생할시 콜백함수로 인해 정해진 함수가 실행 
# 현재 발생하는 함수는 이벤트가 발생을 했으면 pushed라고 글자를 변경해줌 
button.pack()

root.mainloop() # 화면상에 실행한 GUI가 지속해서 실행될수 있게 해줌 

'''callback 함수'''
'''특정부분에 대한 이벤트만 관리하는 함수 
ex) 클릭이란 이벤트가 일어나는것만 관리하는 함수'''
