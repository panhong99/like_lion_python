'''유저와 주고받는 것을 GUI라고 한다.'''
# Grapic user interface

import tkinter as tk

root = tk.Tk()    # 부모 객체 인스턴스 생성 

Swich = False       # Swich라는 전역변수를 생성하고 False라고 지정을 해줌
print(type(Swich))
def func():     # 버튼처리 함수 생성 
    global Swich    # 전역변수를 사용하겠다고 global함수로 처리 
    if Swich:       # Swich가 True 일때
        label.config(text = "apple")   # 이벤트가 생성이 되면 apple 변경 
        Swich = False                  # Swich의 값을 False로 변경 
    else:  
        label.config(text = "orange")   # 이벤트가 생성이 되면 orange로 변경 
        Swich = True                    # Swich의 값을 True로 변경 

# config는 label의 속성을 변경할때 사용하는 함수 
label = tk.Label(root , text = "Push Button")   #label생성 후 텍스트는 Push Button이라고 입력 
label.pack()    # label을 tk.Tk로 생성을 해놓은 부모객체에 팩킹 

button = tk.Button(root , text = "Push" , command = func)   # Push라는 텍스트가 입력되어 있는 Button 생성 
button.pack()   # Button을 부모객체에 팩킹 

root.mainloop() # root를 지속적으로 표시


import tkinter as tk

root = tk.Tk()

# 두개의 함수를 작성 
def func():     # 특정 이벤트 발생 시 text를 Pushed로 변경 
    label.config(text = "Pushed")

def func_event(ev): # 특정 이벤트 발생 시 text를 Leave으로 변경 
    label.config(text = "Leave")

def func_event2(ev): # 특정 이벤트 발생 시 text를 Enter 로 변경 
    label.config(text = "Enter")

label = tk.Label(root ,text = "Push Button")    # 라벨 생성 
label.pack()

button = tk.Button(root , text = "Push!" , command = func)  # Button 클릭 이벤트 발생을 체크하는 함수 이벤트가 생기면 func함수를 실행 
button.pack()

# bind는 button에 여러가지 이벤트를 처리해주는 역할을 한다. 지금은 Leave라는 이벤트가 발생이 되면 func_event함수를 실행시킨다.
button.bind("<Leave>" , func_event)  # Leave함수는 마우스 커서가 위젯밖으로 나갔을 때 발생하는 이벤트이다.
button.bind("<Enter>" , func_event2) # Enter함수는 마우스 커서가 위젯안으로 들어왔을때 발생하는 이벤트이다.

root.mainloop()

import tkinter as tk

root = tk.Tk()

def func():
    label.config(text = "Pushed")

def func_event_click(ev):
    disp = str(ev.x) + "/" + str(ev.y) # ev는 x , y의 좌표를 알고있는 함수이므로 이벤트가 발생했을시 x , y의 좌표를 str로 변경해주고 text를 각 x , y의 좌표로 변경해준다.
    label.config(text = disp)

label = tk.Label(root , text = "P B") # 기본 label의 text
label.pack()
button = tk.Button(root , text = "Push" , command = func)
button.pack()

button.bind("<Button-1>" , func_event_click) # Button-1은 왼쪽 마우스이고 왼쪽 마우스가 클릭이 되었을때 발생하는 이벤트이다.

root.mainloop()

def Action1():
    lbl.config(text = "Option 1")
def Action2():
    lbl.config(text = "Option 2")

root = tk.Tk()
# underline 이라는것은 텍스트에 3번째 문자 밑에 밑줄을 쳐주겠다는 뜻이다.
lbl = tk.Label(root ,text = "EduCoding" , underline = 3)
lbl.pack()

# Radiobutton은 체크박스와 같다고 생각하면된다. 중복체크는 불가하지만 남 , 여 ,/ 나이대 선택 등등을 할때 사용한다. 
rbvar = ""
rb1 = tk.Radiobutton(root , text = "Option 1" , variable = rbvar , value = "a" ,
                            indicatoron = 0 , command = Action1)
                            # idicatoron 은 0이 아니라 다른 번호를 작성을 해주면 다른 모양의 버튼이 생성된다.
rb1.pack()

rb2 = tk.Radiobutton(root , text = "Option 2" , variable = rbvar , value = "b" , 
                            indicatoron = 0 , command = Action2)

rb2.pack()

tk.mainloop()


import tkinter as tk
root = tk.Tk()

def func1():
    label.config(text = "Button 1")

def func2():
    label.config(text = "Button 2")

sel = tk.IntVar() # tk.객체에 IntVar이라는 함수를 만들어서 생성 
sel.set(1)  # set 두가지의 선택지가 있으면 1번째를 먼저 선택해라는 명령 

label = tk.Label(root ,text = "Select Button")
label.pack()

rb1 = tk.Radiobutton(root , text = "Button 1" , variable = sel , value = 1 , command = func1)
rb1.pack()

rb2 = tk.Radiobutton(root , text = "Button 2" , variable = sel , value = 2 , command = func2)
rb2.pack()
                        # variable의 넘버가 다르기때문에 바로전 코드와 같은 버튼상자가 나오지 않는다.
root.mainloop()

# 라디오 버튼 만들기 프로그램 
import tkinter as tk
root = tk.Tk()

label = tk.Label(root , text = "Educoding")
label.pack()

def func():
    print(sel.get()) # key point 어떻게 sel에 지정해놓은 IntVar의 값을 불러올것인지를 고민하고 get이라는 함수가 존재함으로 
                     # 지정한 값을 불러온다는 것을 찾아보았어야 한다.
def func1():
    label.config(text = "Button 1")

def func2():        # 총 4개의 함수를 작성을 해서 각각의 변수들에게 성립이 될 수 있도록 한다.
    label.config(text = "Button 2")

def func3():
    label.config(text = "Button 3")

sel = tk.IntVar(root , 0) # tk.객체에 IntVar이라는 함수를 만들어서 생성 
                          # 아직까지 이해가 조금 모자란 부분 tk.InVar

'''value는 각각의 Rideobutton을 구분하기 위한 ID라고 생각하면 되고 variable은 같은 그룹이며 sel의 인터프리터고 생각을 하면 된다.'''
rb1 = tk.Radiobutton(root , text = "Choice 1" , variable = sel , value = 1 , command = func1)
rb1.pack()          

rb2 = tk.Radiobutton(root , text = "Choice 2" , variable = sel , value = 2 , command = func2)
rb2.pack()

rb3 = tk.Radiobutton(root , text = "Choice 3" , variable = sel , value = 3 , command = func3)
rb3.pack()

button = tk.Button(root , text = "print choice" , command = func)
button.pack()

root.mainloop()

# 라디오 버튼 만들기 프로그램 
import tkinter as tk
root = tk.Tk()

label = tk.Label(root , text = "Educoding")
label.pack()

def func1():
    label.config(text = "Button 1")

def func2():        # 총 4개의 함수를 작성을 해서 각각의 변수들에게 성립이 될 수 있도록 한다.
    label.config(text = "Button 2")

def func3():
    label.config(text = "Button 3")

sel = tk.IntVar(root , 0) # tk.객체에 IntVar이라는 함수를 만들어서 생성 
                          # 아직까지 이해가 조금 모자란 부분 tk.InVar

'''value는 각각의 Rideobutton을 구분하기 위한 ID라고 생각하면 되고 variable은 같은 그룹이며 sel의 인터프리터고 생각을 하면 된다.'''
rb1 = tk.Radiobutton(root , text = "Choice 1" , variable = sel , value = 1 , command = func1)
rb1.pack()          

rb2 = tk.Radiobutton(root , text = "Choice 2" , variable = sel , value = 2 , command = func2)
rb2.pack()

rb3 = tk.Radiobutton(root , text = "Choice 3" , variable = sel , value = 3 , command = func3)
rb3.pack()

button = tk.Button(root , text = "print choice" , command = lambda : print(sel.get()))
button.pack()

root.mainloop()

# 슬라이더 만들기 드래그 창 만들기 인것 같다.
import tkinter as tk
root = tk.Tk()

val = tk.IntVar()

val.set(0)

def func(scl):
    label.config(text = "Value = %d" % int(scl))
    
label = tk.Label(root , text = "Value = %d" % val.get())
label.pack()
                                    # orient 옵션은 가로로 출력할것인지 세로로 할것인지 결정 정해주는 역할 "h"는 수평 즉 가로임
s= tk.Scale(root ,label = "Scale" , orient = "h" , from_ = 0 , to = 100,
            showvalue = False , variable = val , command = func )
s.pack()
root.mainloop()

'''텍스트 박스 만들기'''
import tkinter as tk

root = tk.Tk()

# 함수생성 / 이벤트가 발생을 했을때 label의 속성을 e.get으로 변경을 해준다.
def func(ev):
    label.config(text = e.get())

# 기본적인 label생성 
label = tk.Label(root , text = "Input Text")
label.pack()

# Entry는 박스를 만들어 놓고 박스를 배치만 한다.
e = tk.Entry(root)
e.pack()

# Return은 bind로 읽고 함수를 실행한다. 함수는 e의 값을 text에 업로드 하라고 했기때문에 입력한 텍스트가 업로드된다.
e.bind("<Return>" , func)
root.mainloop()


import tkinter as tk
root = tk.Tk()

def func():
    label.config(text = e.get())

label = tk.Label(root , text = "Input Text")
label.pack()

e = tk.Entry(root)
e.pack()
# e.bind("<Return>" , func)

'''뭔가 새로운것을 배울려면 상승세에 있는것을 배워야 한다.'''

button = tk.Button(root , text = "Push" , command = func)
button.pack()

tk.mainloop()


'''Text box 계산기 만들기'''

import tkinter as tk

root = tk.Tk()

result = tk.IntVar()        #IntVar은 Rideobutton을 하나의 그룹으로 묶어서 관리를 해주는 함수이다. ex) 
result.set(1)               #result 즉 IntVar이 관리하는 라디오의 개수가 여러개이면 사용자의 변경사항이 없다면 첫번째 박스를 선택을 해라라는 의미 
number = result.get()       # number변수에 result.get을 하면 IntVar이 관리하는 그룹내에서 선택된 하나의 객체의 value번호를 불러오고 그 value번호를 number 변수에 입력을 시켜준다.

def calcu():        # 함수 생성 
    a = int(Text_box1.get())    # 값을 받아올 변수를 생성  .get함수 이용
    b = int(Text_box2.get())    # 값을 받아올 변수를 생성  .get함수 이용
    total = 0                   # 결과를 담을 변수도 생성 

    if number == 1:             # number 라는 변수의 값에 맞춰서 각각의 조건을 실행 
        total = a + b
    elif number == 2:
        total =  a - b
    elif number == 3:
        total = a * b
    elif number == 4:
        if b == 0:
            label.config(text = "0으로 나눌수 없습니다.")
            return
        else:
            result = a / b
    Finalresult = "%.2f"%total  # 결과가 소숫점이나 필요없는 숫자들로 구성되어 있을 수 있으므로 다른 변수에 0.2f(소수점 2번째 까지만 출력) 저장을 해줌 
    label.config(text = Finalresult)    # 결과를 label에 업로드 

Text_box1 = tk.Entry(root)      # 빈 텍스트 박스 생성 
Text_box1.pack()

Text_box2 = tk.Entry(root)      # 빈 텍스트 박스 생성 
Text_box2.pack()

'''지속해서 말하고 있지만 variable변수는 각각의 객체를 하나의 그룹으로 묶어주는것이다.'''
'''객체내에 value는 각 그룹으로 묶여있는 객체를 구별할 수 있게 ID를 주는것이라고 생각을 하면 된다.'''
# rb1 = tk.Radiobutton(root , text = "Button +" , variable = result , value = 1)    # Ridio박스를 생성하기 위해 하나씩 정성스럽게 작성한 코드
# rb1.pack()                                                                        # IntStr 함수를 사용해 그룹으로 묶고 조건문의 조건을 형성시키기 위해 작성하기도 한 코드 
# rb2 = tk.Radiobutton(root , text = "Button -" , variable = result , value = 2)    # 내가 생각할 때는 하단의 for문 보다 개수가 적다면 이렇게 작성을 해주는 것이 가독성이 횔씬 좋은것 같다.
# rb2.pack()                                                                        # 한눈에 알아보기 쉽고 구별이 좋을 것 같다는 판단이다.
# rb3 = tk.Radiobutton(root , text = "Button *" , variable = result , value = 3)
# rb3.pack()
# rb4 = tk.Radiobutton(root , text = "Button /" , variable = result , value = 4)
# rb4.pack()
radios = []                                                                         # Ridio박스를 간단하게 반복문으로 생성하게 하는 코드
Operator = ["+" , "-" , "*" , "/"]                                                  # 연산의 기호를 나타낼 리스트를 생성하고 문자열로 연산자를 입력 
for i in range(4):                                                                  # 연산자가 4개이므로 반복문도 총 4번 실행 
    radio_ = tk.Radiobutton(root ,                                                  # radio라는 변수를 생성하고 입력할 텍스트 후미에 연산를 입력해주고 
                            text = "Button %s"%Operator[i],                         # result의 그룹으로 묶어준다. 각 객체를 구별하기 위해 value를 입력해주고 숫자를 지정해준다.
                            variable= result , value = i+1)
    radios.append(radio_)                                                           # 미리 생성해놓은 빈 리스트에 생성한 Rideo Box를 입력해준다.
    radios[i].pack()                                                                # 입력된 리스트를 각각 pack해준다.


button = tk.Button(root , text = "Result" , command = calcu)                        # 입력받은 문자열의 숫자와 Rideo Box의 value넘버로 조건문을 실행하고 매개변수들을 입력해준다.
button.pack()                                                                       

label = tk.Label(root , text = "결과 표시창") # 계산기 창 맨 하단 부분에 label을 출력         # 결과 표시창이라는 label을 하단에 pack하고 결과를 출력한다.
label.pack() 

root.mainloop()

import tkinter as tk

window = tk.Tk()
window.title("Educoding&IT")
window.geometry("320x400+100+100")
window.resizable(False , False)

b1 = tk.Button(window , text = "(50 , 50)")
b2 = tk.Button(window , text = "(50 , 100)")
b3 = tk.Button(window , text = "(100 , 150)")
b4 = tk.Button(window , text = "(0 , 200)")
b5 = tk.Button(window , text = "(0 , 300)")
b6 = tk.Button(window , text = "(0 , 300)")

b1.place(x = 50 , y = 50)
b2.place(x = 50 , y = 100 , width = 50 , height = 50)
b3.place(x = 100 , y = 150 , bordormode = "inside")
b4.place(x = 0 , y = 200 , relwidth = 0.5)
b5.place(x = 0 , y = 300 , relx = 0.5)
b6.place(x = 0 , y = 300 , relx = 0.5 , anchor = "s")

window.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("간편 계산기")
root.geometry("320x400+100+100")
root.resizable(False , False)

label = tk.Label(text = "입력")

b1 = tk.Button(root , text = "1")
b2 = tk.Button(root , text = "2")    
b3 = tk.Button(root , text = "3")    
ba = tk.Button(root , text = "+")    
b4 = tk.Button(root , text = "4")  
b5 = tk.Button(root , text = "5")    
b6 = tk.Button(root , text = "6")    
bb = tk.Button(root , text = "-")    
b7 = tk.Button(root , text = "7")    
b8 = tk.Button(root , text = "8")    
b9 = tk.Button(root , text = "9")    
b10 = tk.Button(root , text = "C")    
b11 = tk.Button(root , text = "0")    
b12 = tk.Button(root , text = "=")    


b1.place(x = 30 , y = 50 , width = 50 , height = 50)
b2.place(x = 100 , y = 50 , width = 50 , height = 50)
b3.place(x = 170 , y = 50 , width = 50 , height = 50)
b4.place(x = 30 , y = 120 , width = 50 , height = 50)
b5.place(x = 100 , y = 120 , width = 50 , height = 50)
b6.place(x = 170 , y = 120 , width = 50 , height = 50)
b7.place(x = 30 , y = 190 , width = 50 , height = 50)
b8.place(x = 100 , y = 190 , width = 50 , height = 50)
b9.place(x = 170 , y = 190 , width = 50 , height = 50)
b10.place(x = 30 , y = 260 , width = 50 , height = 50)
b11.place(x = 100 , y = 260 , width = 50 , height = 50)
b12.place(x = 170 , y = 260 , width = 50 , height = 50)

root.mainloop()

'''Google에서 가져온 계산기 만들기 프로그램의 소스코드이다.'''
'''확실히 생각한데로 코드는 상당히 길지만 배우지 않은 grid함수와 whidh , hight 를 이용해서 좀 더 깔끔하고 체계적이게 작성을 했다.'''
'''코드 리뷰를 해보고 익숙해진 다음 나의 스타일대로 change를 해보자'''
import tkinter as tk    # tk 모듈 import 
 
root = tk.Tk()  # 기존의 방식과 동일하게 부모 윈도우의 변수는 root로 설정 
root.title("Tkinter Calculator")    # title함수를 사용해서 계산기의 이름을 Tkineter Calculator 라고 설정 

'''geometry의 대한 설명은 다음과 같다.'''
'''w = 창의 너비 , h = 창의 높이 '''
'''+-x = 창의 가로 방향 위치 , + 값은 화면 왼쪽 끝에서의 거리 , - 값은 화면 오른쪽 끝에서의 거리를 의미'''
'''+-y = 창이 세로방향 위치 , + 값은 화면 왼쪽 끝에서의 거리 , - 값은 화면 오른쪽 끝에서의 거리를 의미한다.'''
'''실험 결과 후미에 -+ 는 윈도우가 나타날때 위치를 설정해주는것 같다.(정확하다고 자신할 수 있다.)'''
root.geometry("350x200")            # geometry함수를 사용해서 윈도우의 width , height를 설정 

'''한참을 고민했던 Frame함수에 대한 고민은 그저 단순히 텍스트가 삽입되는 박스를 만들어 주는것이었고 후미에 Width , Height는 박스의 크기를 설정해 주는것이었다.'''
upper_frame = tk.Frame(root, width=400, height=70)
upper_frame.pack(pady=40)
 
down_frame = tk.Frame(root, width=400, height=100)
'''padx , pady 함수는 button 박스를 입력한 크기만큼 만들어 주는함수 위에 width , heigth는 박스자체의 크기이고 내부에 padx , pady는 텍스트가 입력되는 창의 크기이다.'''
down_frame.pack(padx=10, pady=10)
entry = tk.Entry(upper_frame, width=20, font=("Courier",18), borderwidth=5) # Entry는 단순히 텍스트가 입력되는 박스를 만들어 주는것이고 font는 폰트이다.
'''borderwidth는 생성되는 박스나 윈도우에 테두리를 생성해주는 함수이다. (생각만큼 주요한것은 아니었으나 디자인에 상당히 신경을 쓴다면 신경을 써야할것 같다.)'''
entry.pack()
entry.insert(0,"") # insert는 텍스트 삽입에 도움을 주는 함수이고 0은 처음이라는 뜻이다.(아마 좌측 끝) "" 따옴표내에 아무런 문자가 없으므로 박스는 커서가 좌측끝부터 시작되고 빈 박스가 생성된다.
 
def button_clicked(number):
    current = entry.get()       # get함수는 앞에 붙은 객체에 입력되어 있는 값을 가져온다는 함수이다.
    entry.delete(0, tk.END)     # delete 함수는 예상했다시피 삭제를 해주는 함수이고 후미에 END라는 함수는 전체를 삭제하라는 내용을 가진 함수이다.
    entry.insert(0, str(current) + str(number))  
 
def button_clear():
    entry.delete(0, tk.END) # clear도 영문뜻과 마찬가지로 작성되어 있는 텍스트들을 전부 삭제해준다.
 
def button_add():
    first_number = entry.get()  
    global f_num        # 다른 함수에서도 값을 변경할 수 있게 f_num을 전역변수로 지정을 해준다
    global math         # 상단과 마찬가지로 전역변수로 지정 
    math = 'addition'   # 변수 값 입력 
    f_num = int(first_number)   # 변수 값 입력 int함수를 사용해서 type를 정수로 변형해서 저장한다. 변수이름이나 int로 변형해준것으로 보아 연산을 해 줄 첫번째 숫자를 입력받을 변수로 보인다.
                                # 첫번쨰 숫자를 누르고 연산기호를 누르면 입력되어있던 텍스트가 사라지는데 사라지는것이 아니라 f_num변수에 저장되고 최종으로 연산을 할 때 사용된다.
    entry.delete(0, tk.END)     # 입력하는 box가 하나이므로 첫번째 값을 입력받고 정수에 저장 후 2번째 정술를 받기위해 entry를 clear해주는것이다.
 
'''첫번째 함수에서 math의 값만 달라지고 나머지는 모두 같다.'''
def button_sub():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    entry.delete(0, tk.END)
'''마찬가지'''
def button_mul():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    entry.delete(0, tk.END)
'''마찬가지'''
def button_div():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    entry.delete(0, tk.END)
''' "=" 기호를 클릭했을때 생기는 이벤트를 위한 함수로서 첫번째 정수는 f_num에 저정되어 있고 "="을 클릭하기전에 입력되어 있던 텍스트정수를 second_number로 입력하여'''
'''최종적으로 math를 통해 if조건문을 통과시키고 연산을 실행해주고 난 후 텍스트박스의 값을 clear해준다음 연산 결과를 entry에 insert해준다.'''
def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
# 조건문으로 이제 어떤 연산을 할지 할당을 해주고 조건문에 할당되는 연산의 값을 도출한다.
# math의 값에 따라서 어떤 연산을 할 지 결정을 해준다.
    if math == 'addition':
        entry.insert(0,f_num + int(second_number))
 
    if math == 'subtraction':
        entry.insert(0,f_num - int(second_number))
 
    if math == 'multiplication':
        entry.insert(0,f_num * int(second_number))
 
    if math == 'division':
        entry.insert(0,f_num / int(second_number))
 
'''변수옆에 작성되어 있다시피 버튼의 텍스트를 나타내준다.'''
'''후미에 코드를 보면 눈치를 채겠지만 lambda 함수를 이용해서 지정된 함수를 호출하고 매개변수를 ()안에 작성을 해주었다.'''
'''아래에 코드들은 계산기의 버튼을 botton으로 작성해주었다.'''
btn7 = tk.Button(down_frame,text='7', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(7)) # <= 7이 매개변수 아래에 ()안에 들어있는 값들도 모두 매겨변수이다.
btn7.grid(column=0, row=0, padx=5, pady=5)
btn8 = tk.Button(down_frame,text='8', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(8))
btn8.grid(column=1, row=0, padx=5, pady=5)
btn9 = tk.Button(down_frame,text='9', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(9))
btn9.grid(column=2, row=0, padx=5, pady=5)
 
btn4 = tk.Button(down_frame,text='4', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(4))
btn4.grid(column=0, row=1, padx=5, pady=5)
btn5 = tk.Button(down_frame,text='5', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(5))
btn5.grid(column=1, row=1, padx=5, pady=5)
btn6 = tk.Button(down_frame,text='6', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(6))
btn6.grid(column=2, row=1, padx=5, pady=5)
 
btn1 = tk.Button(down_frame,text='1', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(1))
btn1.grid(column=0, row=2, padx=5, pady=5)
btn2 = tk.Button(down_frame,text='2', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(2))
btn2.grid(column=1, row=2, padx=5, pady=5)
btn3 = tk.Button(down_frame,text='3', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(3))
btn3.grid(column=2, row=2, padx=5, pady=5)
 
btn_pm = tk.Button(down_frame,text='+/-', padx=5, pady=10, font=("Courier",15),command=lambda: button_clicked('-'))
btn_pm.grid(column=0, row=3, padx=5, pady=5)
btn0 = tk.Button(down_frame,text='0', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked(0))
btn0.grid(column=1, row=3, padx=5, pady=5)
btn_p = tk.Button(down_frame,text='.', padx=15, pady=10, font=("Courier",15),command=lambda: button_clicked('.'))
btn_p.grid(column=2, row=3, padx=5, pady=5)
 
btn_mul = tk.Button(down_frame,text='X', padx=15, pady=10, font=("Courier",15),command=button_mul, bg='orange')
btn_mul.grid(column=3, row=0, padx=5, pady=5)
btn_sub = tk.Button(down_frame,text='-', padx=15, pady=10, font=("Courier",15),command=button_sub, bg='orange')
btn_sub.grid(column=3, row=1, padx=5, pady=5)
btn_add = tk.Button(down_frame, text='+', padx=15, pady=10, font=("Courier",15),command=button_add, bg='orange')
btn_add.grid(column=3, row=2, padx=5, pady=5)
btn_div = tk.Button(down_frame, text='/', padx=15, pady=10, font=("Courier",15),command=button_div, bg='orange')
btn_div.grid(column=3, row=3, padx=5, pady=5)
 
btn_c = tk.Button(down_frame, text='C', padx=15, pady=10, font=("Courier",15),command=button_clear, bg='orange')
btn_c.grid(column=2, row=4, padx=5, pady=5)
 
btn_res = tk.Button(down_frame, text='=', padx=15, pady=10, font=("Courier",15),command=button_equal, bg='orange')
btn_res.grid(column=3, row=4, padx=5, pady=5)
 
btn3 = tk.Button(root,text='9')
 
root.mainloop()