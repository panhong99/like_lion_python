import turtle 
import math
import random

t1, t2, t3 = [None] * 3
t1x , t1y ,t2x , t2y ,t3x , t3y = [0] * 6
swidht , sheight = 300 , 300

if __name__ == "__main":
   turtle.title("거북이 만나기")
   turtle.setup(widht = swidht + 50 , height = sheight + 50)
   turtle.screensize(swidht,sheight)

   t1 = turtle.Turtle('turtle'); t1.color('red'); t1.speed(10); t1.penup()
   t2 = turtle.Turtle('turtle'); t2.color('green'); t2.speed(10); t2.penup()
   t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.speed(10); t3.penup()

   t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)

while True:
   angle = random.randrange(0, 360)
   dist = random.randrange(1 , 50)
   t1.left(angle); t1.forward(dist)
   angle = random.randrange(0, 360)
   dist = random.randrange(1 , 50)
   t2.left(angle); t1.forward(dist)
   angle = random.randrange(0, 360)
   dist = random.randrange(1 , 50)
   t3.left(angle); t1.forward(dist)
   
   t1x = t1.xcor(); t1y = t1.ycor()
   t1x = t1.xcor(); t1y = t1.ycor()
   t1x = t1.xcor(); t1y = t1.ycor()

   if not((-swidht / 2 <= t1x and t1x <= swidht / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2)):
      t1.goto(-100 , -100)
   if not((-swidht / 2 <= t1x and t1x <= swidht / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2)):
      t2.goto(0 , 0)
   if not((-swidht / 2 <= t1x and t1x <= swidht / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2)):
      t3.goto(100 , 100)

   if math.sqrt(((t1x - t2x) * (t1x - t2x)  )) + ((t1y - t2y) * (t1y - t2y)) <= 20 :
      t1.stamp(); t2.stamp()
   elif math.sqrt(((t1x - t3x) * (t1x - t3x)  )) + ((t1y - t3y) * (t1y - t3y)) <= 20 :
      t1.stamp(); t3.stamp()
   elif math.sqrt(((t2x - t3x) * (t2x - t3x)  )) + ((t2y - t3y) * (t2y - t2y)) <= 20 :
      t2.stamp(); t3.stamp()
