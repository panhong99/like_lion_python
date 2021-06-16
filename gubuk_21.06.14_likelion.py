# '''turtle모듈로 학습'''
# import turtle as t
# t.shape("turtle") # shape안에 다른 단어를 넣으면 다른 문양이 나온다.

# '''pixel = 이미지를 이루는 가장 최소의 단위
# 픽셀 수치가 높을 수록 화면을 더 조밀하게(자세하게) 구성할 수 있다.'''

# t.pencolor("BLUE")
# t.fillcolor("RED")
# t.begin_fill()
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.end_fill()

# '''완료'''
# ''' for문을 이용하여 오각형 만들기 '''
# '''input을 활용하여 다각형 그리기'''

# n = 5
# for i in range(n):
#    t.forward(100)
#    t.right((360/n)*2)
#    t.forward(100)
# t.left(360/n)
    
# t.forward(100)
# t.right(72)
# t.speed("fastest")
    

    
# t.pencolor("#dcdcdc") 
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# t.up()
# t.goto(200,0)
# t.down()

# t.pencolor("#ff0000")
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90 + 90)

# t.up()
# t.goto(300 , - 200)
# t.down()

# t.pencolor("#0000ff")
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90 + 90)

# t.up()
# t.goto(100 ,-300)
# t.down()
# t.pensize(5)
# t.pencolor("#00ff00")
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# #삼각형 만들기
# t.penup()
# t.goto(-200 , -50)
# t.pendown()
# t.circle(40 , steps = 3)

# '''사각형 만들기'''
# t.penup()
# t.goto(-100 , -50)
# t.pendown()
# t.circle(40 , steps = 4)

# #오각형 만들기
# t.penup()
# t.goto(0 , 50)
# t.pendown()
# t.circle(40 , steps = 5)

# #육각형 만들기
# t.penup()
# t.goto(100 , -50)
# t.pendown()
# t.circle(40 , steps = 6)

# # 원 만들기
# t.penup()
# t.goto(200 , -50)
# t.pendown()
# t.circle(40)

# '''========================================turtlr 게임===================================='''
# import turtle 
# import math
# import random

# t1, t2, t3 = [None] * 3
# t1x , t1y ,t2x , t2y ,t3x , t3y = [0] * 6
# swidht , sheight = 300 , 300

# if __name__ == "__main":
#    turtle.title("거북이 만나기")
#    turtle.setup(widht = swidht + 50 , height = sheight + 50)
#    turtle.screensize(swidht,sheight)

#    t1 = turtle.Turtle('turtle'); t1.color('red'); t1.speed(10); t1.penup()
#    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.speed(10); t2.penup()
#    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.speed(10); t3.penup()

#    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)

# while True:
#    angle = random.randrange(0, 360)
#    dist = random.randrange(1 , 50)
#    t1.left(angle); t1.forward(dist)
#    angle = random.randrange(0, 360)
#    dist = random.randrange(1 , 50)
#    t2.left(angle); t1.forward(dist)
#    angle = random.randrange(0, 360)
#    dist = random.randrange(1 , 50)
#    t3.left(angle); t1.forward(dist)
   
#    t1x = t1.xcor(); t1y = t1.ycor()
#    t1x = t1.xcor(); t1y = t1.ycor()
#    t1x = t1.xcor(); t1y = t1.ycor()

#    if not((-swidht / 2 <= t1x and t1x <= swidht / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2)):
#       t1.goto(-100 , -100)
#    if not((-swidht / 2 <= t1x and t1x <= swidht / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2)):
#       t2.goto(0 , 0)
#    if not((-swidht / 2 <= t1x and t1x <= swidht / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2)):
#       t3.goto(100 , 100)

#    if math.sqrt(((t1x - t2x) * (t1x - t2x)  )) + ((t1y - t2y) * (t1y - t2y)) <= 20 :
#       t1.stamp(); t2.stamp()
#    elif math.sqrt(((t1x - t3x) * (t1x - t3x)  )) + ((t1y - t3y) * (t1y - t3y)) <= 20 :
#       t1.stamp(); t3.stamp()
#    elif math.sqrt(((t2x - t3x) * (t2x - t3x)  )) + ((t2y - t3y) * (t2y - t2y)) <= 20 :
#       t2.stamp(); t3.stamp()
# '''========================================================================================================'''

