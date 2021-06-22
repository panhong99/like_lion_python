def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x 
            nonlocal y
            x = x + 30
            y = y + 300
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
            global x 
            x = x + 30
            print(x)
        C()
    B()
A()

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(1) , c(2) , c(3) , c(4) , c(5))

def calc():
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
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)
c(2)
c(3)

def counter():
    i = 0
    def count():
        nonlocal i 
        i = i + 1
        return i # return을 사용해주어야 반환할 값이 생겨나므로 return이나 print를 사용해주어야 한다.
    return count
    


c = counter()
for i in range(10):
    print(c() , end = " ")

'''파일의 입출력 과정'''
'''키보드로 입력하는 것을 펴준입력 , 모니터로 출력하는 것을 표준출겨이라 함 , 
또 키보드와 모니터를 합쳐서 콘솔이라 함 '''

'''파일의 위치를 지정해서 그 파일의 내용을 읽어오는 함수'''
file = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")
inStr = file.readline()
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

inFp = None
inStr = ""
inFp = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr , end="")

inFp.close()

inFp = open("21.06.22_likelion(p).txt" , "r" , encoding = "utf-8")
inList = []
inList = inFp.readlines() # <= readlines() 함수는 파일의 내용을 통으로 리스트에 저장
for i in inList:
    print(i ,end="")
inFp.close()

file = input("파일명을 입력하세요. :")
File = open(file , "r" , encoding="utf-8")
view = []
view = File.readlines()
for i in view:
    print(i , end="")
File.close()

outFp = None
outStr = ""

outFp = open("21.06.22_likelion(p)2.txt" , "w" , encoding="utf-8")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
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
outFp.writelines(inList)
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

if secuYN == "1" :
    secu = 100
elif secuYN == "2" :
    secu -= 100

inFp = open(inFname , "r" , encoding = "utf-8")
outFp = open(outFname , "w" , encoding = "utf-8")

while True:
    inStr = inFp.readline()
    if not inStr:
        break

    outStr = ""
    for i in range(0, len(inStr)):
        ch = inStr[i]
        chNum = ord(ch)
        chNum = chNum + secu
        ch2 = chr(chNum)
        outStr = outStr + ch2

    outFp.write(outStr)

outFp.close()
inFp.close()
print(" %s --> %s 변환 완료 " %(inFname , outFname))

import time 
import random

game = open("Eng_LowData.txt" , "r" , encoding = "utf-8")
game_source = game.readline()

Quiz = []
Source = ""
while True:
    Source = game.readline()
    if Source == "":
        break
    elif Source != "\n":
        print(Source , end = "")
        Quiz.append(Source.rsplit())
game.close()

result = random.choice(Quiz)

Start = input("게임을 시작할까요?")
begin = time.time()
i = 1
while i <= 5:
    print(result)
    answer = input()
    if answer == 0:
        print("게임을 종료합니다")
        break
    if result == answer:
        print("정답입니다!")
        i + 1
        result = random.choice(Quiz)
    else:
        print("오답입니다.")
    
end = time.time()
print("총 소요시간은 ",end - begin , "입니다.")
    
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
