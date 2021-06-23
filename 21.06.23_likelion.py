# '''유저와 주고받는 것을 GUI라고 한다.'''
# # Grapic user interface

# import tkinter as tk

# root = tk.Tk()    # 부모 객체 인스턴스 생성 

# Swich = False       # Swich라는 전역변수를 생성하고 False라고 지정을 해줌
# print(type(Swich))
# def func():     # 버튼처리 함수 생성 
#     global Swich    # 전역변수를 사용하겠다고 global함수로 처리 
#     if Swich:       # Swich가 True 일때
#         label.config(text = "apple")   # 이벤트가 생성이 되면 apple 변경 
#         Swich = False                  # Swich의 값을 False로 변경 
#     else:  
#         label.config(text = "orange")   # 이벤트가 생성이 되면 orange로 변경 
#         Swich = True                    # Swich의 값을 True로 변경 

# # config는 label의 속성을 변경할때 사용하는 함수 
# label = tk.Label(root , text = "Push Button")   #label생성 후 텍스트는 Push Button이라고 입력 
# label.pack()    # label을 tk.Tk로 생성을 해놓은 부모객체에 팩킹 

# button = tk.Button(root , text = "Push" , command = func)   # Push라는 텍스트가 입력되어 있는 Button 생성 
# button.pack()   # Button을 부모객체에 팩킹 

# root.mainloop() # root를 지속적으로 표시


# import tkinter as tk

# root = tk.Tk()

# # 두개의 함수를 작성 
# def func():     # 특정 이벤트 발생 시 text를 Pushed로 변경 
#     label.config(text = "Pushed")

# def func_event(ev): # 특정 이벤트 발생 시 text를 Leave으로 변경 
#     label.config(text = "Leave")

# def func_event2(ev): # 특정 이벤트 발생 시 text를 Enter 로 변경 
#     label.config(text = "Enter")

# label = tk.Label(root ,text = "Push Button")    # 라벨 생성 
# label.pack()

# button = tk.Button(root , text = "Push!" , command = func)  # Button 클릭 이벤트 발생을 체크하는 함수 이벤트가 생기면 func함수를 실행 
# button.pack()

# # bind는 button에 여러가지 이벤트를 처리해주는 역할을 한다. 지금은 Leave라는 이벤트가 발생이 되면 func_event함수를 실행시킨다.
# button.bind("<Leave>" , func_event)  # Leave함수는 마우스 커서가 위젯밖으로 나갔을 때 발생하는 이벤트이다.
# button.bind("<Enter>" , func_event2) # Enter함수는 마우스 커서가 위젯안으로 들어왔을때 발생하는 이벤트이다.

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()

# def func():
#     label.config(text = "Pushed")

# def func_event_click(ev):
#     disp = str(ev.x) + "/" + str(ev.y) # ev는 x , y의 좌표를 알고있는 함수이므로 이벤트가 발생했을시 x , y의 좌표를 str로 변경해주고 text를 각 x , y의 좌표로 변경해준다.
#     label.config(text = disp)

# label = tk.Label(root , text = "P B") # 기본 label의 text
# label.pack()
# button = tk.Button(root , text = "Push" , command = func)
# button.pack()

# button.bind("<Button-1>" , func_event_click) # Button-1은 왼쪽 마우스이고 왼쪽 마우스가 클릭이 되었을때 발생하는 이벤트이다.

# root.mainloop()

# def Action1():
#     lbl.config(text = "Option 1")
# def Action2():
#     lbl.config(text = "Option 2")

# root = tk.Tk()
# # underline 이라는것은 텍스트에 3번째 문자 밑에 밑줄을 쳐주겠다는 뜻이다.
# lbl = tk.Label(root ,text = "EduCoding" , underline = 3)
# lbl.pack()

# # Radiobutton은 체크박스와 같다고 생각하면된다. 중복체크는 불가하지만 남 , 여 ,/ 나이대 선택 등등을 할때 사용한다. 
# rbvar = ""
# rb1 = tk.Radiobutton(root , text = "Option 1" , variable = rbvar , value = "a" ,
#                             indicatoron = 0 , command = Action1)
#                             # idicatoron 은 0이 아니라 다른 번호를 작성을 해주면 다른 모양의 버튼이 생성된다.
# rb1.pack()

# rb2 = tk.Radiobutton(root , text = "Option 2" , variable = rbvar , value = "b" , 
#                             indicatoron = 0 , command = Action2)

# rb2.pack()

# tk.mainloop()


# import tkinter as tk
# root = tk.Tk()

# def func1():
#     label.config(text = "Button 1")

# def func2():
#     label.config(text = "Button 2")

# sel = tk.IntVar() # tk.객체에 IntVar이라는 함수를 만들어서 생성 
# sel.set(1)  # set 두가지의 선택지가 있으면 1번째를 먼저 선택해라는 명령 

# label = tk.Label(root ,text = "Select Button")
# label.pack()

# rb1 = tk.Radiobutton(root , text = "Button 1" , variable = sel , value = 1 , command = func1)
# rb1.pack()

# rb2 = tk.Radiobutton(root , text = "Button 2" , variable = sel , value = 2 , command = func2)
# rb2.pack()
#                         # variable의 넘버가 다르기때문에 바로전 코드와 같은 버튼상자가 나오지 않는다.
# root.mainloop()

# # 라디오 버튼 만들기 프로그램 
# import tkinter as tk
# root = tk.Tk()

# label = tk.Label(root , text = "Educoding")
# label.pack()

# def func():
#     print(sel.get()) # key point 어떻게 sel에 지정해놓은 IntVar의 값을 불러올것인지를 고민하고 get이라는 함수가 존재함으로 
#                      # 지정한 값을 불러온다는 것을 찾아보았어야 한다.
# def func1():
#     label.config(text = "Button 1")

# def func2():        # 총 4개의 함수를 작성을 해서 각각의 변수들에게 성립이 될 수 있도록 한다.
#     label.config(text = "Button 2")

# def func3():
#     label.config(text = "Button 3")

# sel = tk.IntVar(root , 0) # tk.객체에 IntVar이라는 함수를 만들어서 생성 
#                           # 아직까지 이해가 조금 모자란 부분 tk.InVar

# '''value는 각각의 Rideobutton을 구분하기 위한 ID라고 생각하면 되고 variable은 같은 그룹이며 sel의 인터프리터고 생각을 하면 된다.'''
# rb1 = tk.Radiobutton(root , text = "Choice 1" , variable = sel , value = 1 , command = func1)
# rb1.pack()          

# rb2 = tk.Radiobutton(root , text = "Choice 2" , variable = sel , value = 2 , command = func2)
# rb2.pack()

# rb3 = tk.Radiobutton(root , text = "Choice 3" , variable = sel , value = 3 , command = func3)
# rb3.pack()

# button = tk.Button(root , text = "print choice" , command = func)
# button.pack()

# root.mainloop()

# # 라디오 버튼 만들기 프로그램 
# import tkinter as tk
# root = tk.Tk()

# label = tk.Label(root , text = "Educoding")
# label.pack()

# def func1():
#     label.config(text = "Button 1")

# def func2():        # 총 4개의 함수를 작성을 해서 각각의 변수들에게 성립이 될 수 있도록 한다.
#     label.config(text = "Button 2")

# def func3():
#     label.config(text = "Button 3")

# sel = tk.IntVar(root , 0) # tk.객체에 IntVar이라는 함수를 만들어서 생성 
#                           # 아직까지 이해가 조금 모자란 부분 tk.InVar

# '''value는 각각의 Rideobutton을 구분하기 위한 ID라고 생각하면 되고 variable은 같은 그룹이며 sel의 인터프리터고 생각을 하면 된다.'''
# rb1 = tk.Radiobutton(root , text = "Choice 1" , variable = sel , value = 1 , command = func1)
# rb1.pack()          

# rb2 = tk.Radiobutton(root , text = "Choice 2" , variable = sel , value = 2 , command = func2)
# rb2.pack()

# rb3 = tk.Radiobutton(root , text = "Choice 3" , variable = sel , value = 3 , command = func3)
# rb3.pack()

# button = tk.Button(root , text = "print choice" , command = lambda : print(sel.get()))
# button.pack()

# root.mainloop()

# # 슬라이더 만들기 드래그 창 만들기 인것 같다.
# import tkinter as tk
# root = tk.Tk()

# val = tk.IntVar()

# val.set(0)

# def func(scl):
#     label.config(text = "Value = %d" % int(scl))
    
# label = tk.Label(root , text = "Value = %d" % val.get())
# label.pack()
#                                     # orient 옵션은 가로로 출력할것인지 세로로 할것인지 결정 정해주는 역할 "h"는 수평 즉 가로임
# s= tk.Scale(root ,label = "Scale" , orient = "h" , from_ = 0 , to = 100,
#             showvalue = False , variable = val , command = func )
# s.pack()
# root.mainloop()

# '''텍스트 박스 만들기'''
# import tkinter as tk

# root = tk.Tk()

# # 함수생성 / 이벤트가 발생을 했을때 label의 속성을 e.get으로 변경을 해준다.
# def func(ev):
#     label.config(text = e.get())

# # 기본적인 label생성 
# label = tk.Label(root , text = "Input Text")
# label.pack()

# # Entry는 박스를 만들어 놓고 박스를 배치만 한다.
# e = tk.Entry(root)
# e.pack()

# # Return은 bind로 읽고 함수를 실행한다. 함수는 e의 값을 text에 업로드 하라고 했기때문에 입력한 텍스트가 업로드된다.
# e.bind("<Return>" , func)
# root.mainloop()


# import tkinter as tk
# root = tk.Tk()

# def func():
#     label.config(text = e.get())

# label = tk.Label(root , text = "Input Text")
# label.pack()

# e = tk.Entry(root)
# e.pack()
# # e.bind("<Return>" , func)

# '''뭔가 새로운것을 배울려면 상승세에 있는것을 배워야 한다.'''

# button = tk.Button(root , text = "Push" , command = func)
# button.pack()

# tk.mainloop()


# '''Text box 계산기 만들기'''

# import tkinter as tk

# root = tk.Tk()

# result = tk.IntVar()        #IntVar은 Rideobutton을 하나의 그룹으로 묶어서 관리를 해주는 함수이다. ex) 
# result.set(1)               #result 즉 IntVar이 관리하는 라디오의 개수가 여러개이면 사용자의 변경사항이 없다면 첫번째 박스를 선택을 해라라는 의미 
# number = result.get()       # number변수에 result.get을 하면 IntVar이 관리하는 그룹내에서 선택된 하나의 객체의 value번호를 불러오고 그 value번호를 number 변수에 입력을 시켜준다.

# def calcu():        # 함수 생성 
#     a = int(Text_box1.get())    # 값을 받아올 변수를 생성  .get함수 이용
#     b = int(Text_box2.get())    # 값을 받아올 변수를 생성  .get함수 이용
#     total = 0                   # 결과를 담을 변수도 생성 

#     if number == 1:             # number 라는 변수의 값에 맞춰서 각각의 조건을 실행 
#         total = a + b
#     elif number == 2:
#         total =  a - b
#     elif number == 3:
#         total = a * b
#     elif number == 4:
#         if b == 0:
#             label.config(text = "0으로 나눌수 없습니다.")
#             return
#         else:
#             result = a / b
#     Finalresult = "%.2f"%total  # 결과가 소숫점이나 필요없는 숫자들로 구성되어 있을 수 있으므로 다른 변수에 0.2f(소수점 2번째 까지만 출력) 저장을 해줌 
#     label.config(text = Finalresult)    # 결과를 label에 업로드 

# Text_box1 = tk.Entry(root)
# Text_box1.pack()

# Text_box2 = tk.Entry(root)
# Text_box2.pack()

# '''지속해서 말하고 있지만 variable변수는 각각의 객체를 하나의 그룹으로 묶어주는것이다.'''
# '''객체내에 value는 각 그룹으로 묶여있는 객체를 구별할 수 있게 ID를 주는것이라고 생각을 하면 된다.'''
# # rb1 = tk.Radiobutton(root , text = "Button +" , variable = result , value = 1)
# # rb1.pack()
# # rb2 = tk.Radiobutton(root , text = "Button -" , variable = result , value = 2)
# # rb2.pack()
# # rb3 = tk.Radiobutton(root , text = "Button *" , variable = result , value = 3)
# # rb3.pack()
# # rb4 = tk.Radiobutton(root , text = "Button /" , variable = result , value = 4)
# # rb4.pack()
# radios = []
# Operator = ["+" , "-" , "*" , "/"]
# for i in range(4):
#     radio_ = tk.Radiobutton(root ,
#                             text = "Button %s"%Operator[i],
#                             variable= result , value = i+1)
#     radios.append(radio_)
#     radios[i].pack()


# button = tk.Button(root , text = "Result" , command = calcu)
# button.pack()

# label = tk.Label(root , text = "결과 표시창") # 계산기 창 맨 하단 부분에 label을 출력
# label.pack() 

# root.mainloop()

# '''RadioButton을 밑과 같은 식으로 줄여줄 수 있다.'''
# radios = []
# Operator = ["+" , "-" , "*" , "/"]
# for i in range(4):
#     radio_ = tk.Radiobutton(root ,
#                             text = "Button %s"%Operator[i],
#                             variable= result , value = i)
#     radios.append(radio_)
#     radios[i].pack()

# import tkinter as tk

# window = tk.Tk()
# window.title("Educoding&IT")
# window.geometry("320x400+100+100")
# window.resizable(False , False)

# b1 = tk.Button(window , text = "(50 , 50)")
# b2 = tk.Button(window , text = "(50 , 100)")
# b3 = tk.Button(window , text = "(100 , 150)")
# b4 = tk.Button(window , text = "(0 , 200)")
# b5 = tk.Button(window , text = "(0 , 300)")
# b6 = tk.Button(window , text = "(0 , 300)")

# b1.place(x = 50 , y = 50)
# b2.place(x = 50 , y = 100 , width = 50 , height = 50)
# b3.place(x = 100 , y = 150 , bordormode = "inside")
# b4.place(x = 0 , y = 200 , relwidth = 0.5)
# b5.place(x = 0 , y = 300 , relx = 0.5)
# b6.place(x = 0 , y = 300 , relx = 0.5 , anchor = "s")

# window.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("간편 계산기")
root.geometry("320x400+100+100")
root.resizable(False , False)

label = tk.Label(text = "입력")

b1 = tk.Button(root , text = "1")
b2 = tk.Button(root , text = "2")    
b3 = tk.Button(root , text = "3")    
b4 = tk.Button(root , text = "4")    
b5 = tk.Button(root , text = "5")    
b6 = tk.Button(root , text = "6")    
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