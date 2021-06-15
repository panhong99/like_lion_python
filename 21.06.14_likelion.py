# '''중첩 루프 사용하기'''
# '''사각형 별 출력하기'''
# for i in range(5): # 바깥쪽 루프 세로방향 5회 반복 
#     for j in range(6): # 안쪽 루프 가로방향 5회 반복
#         print("*",end= "") # j값 출력 ("*"을 range수 만큼 찍어줌 , 줄바꿈 방지)
#     print()                 # i값 출력 (내부 for문을 수행후 줄바꿈)
 
# '''별 출력하기 2번째'''
# for i in range(5):      # 바깥루프 세로방향 5번 반복
#     for j in range(5):  # 안쪽루프 가로방향 5번 반복
#         if j == i:      # j 가 i 보다 같으면
#             print("*" , end=" ")   # "*"을 출력
#         else:       
#             print(" " , end=" ")   # 다르다면 스페이스로 공백 출력
#     print()

# '''파이썬을 이용해서 간편하게 만들 수 있다.'''
# for i in range(1,6):
#     print(i * "*")

# for i in range(1,5):
#     for j in range(5 - i):
#         print(" " , end="")
#     for j in range(2 * i - 1):
#         print("*" , end="")
#     print()

# rows = 4
# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2*i -1))

# '''거꾸로 별 출력하기'''
# for i in range(5):      
#     for j in range(5):  
#         if i <= j:      
#             print("*" , end=" ")   
#         else:       
#             print(" " , end=" ")   
#     print()

# for i in range(1,5):
#     for j in range(5 - i):
#         print(" " , end="")
#     for j in range(2 * i - 1):
#         print("*" , end="")
#     print()

# '''역삼각형의 별을 출력하는 문제'''
# '''기존의 별을 출력하는 문제에서 바깥for문에 reversed 함수만 사용해주면 풀리는 문제'''
# for i in reversed(range(1,6)): # rever함수로 5 ~ 1 까지 생성
#     for j in range(5 - i):     # 5 - i 를 해주고 그 값만큼 공백 생성
#         print("=" ,end="")     
#     for j in range(2 * i - 1):  # *은 홀수로 출력 짝수를 만들어서 -1 을 해주면 홀수가 나오고 나온 수 만큼 * 출력
#         print("*" ,end="")     
#     print()
    
# '''3과 5의 공배수 처리하기'''
# for i in range(1, 101):
#     if i % (3 * 5) == 0: # 3과 5의 최송공배수가 15이므로 3*5를 하고 나머지가 0 이면 Fizzbuzz출력
#         print("FizzBuzz")
#     elif i % 5 == 0:     # 5 로 나누었을때 나머지가 0 이라면 Buzz
#         print("Buzz")
#     elif i % 3 == 0:     # 3 으로 나누었을때 나머지가 0이라면 Fizz
#         print("Fizz")    
#     else:                # 해당사항이 없다면 i를  출력
#         print(i)         

# '''코드를 최대한 간소화해서 실행시간을 줄이는것은 좋지만 
# 실무에서는 여러사람과 협업을 하게 될 때 팀에게 피해를 줄 수 있으므로 
# 프로그램을 짤때 읽기쉽고 타인이 이해하기 쉽도록 작성을 하는것이 가장 좋다.'''

# for i in range(1, 101):
#     if i % 22 == 0:
#         print("FizzBuzz")
#     elif i % 2 == 0:
#         print("Fizz")
#     elif i % 11 == 0:
#         print("Buzz")
#     else:
#         print(i)

# import turtle as t
# t.shape("turtle")

# '''완료'''
# ''' for문을 이용하여 사각형 만들기 '''
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# #삼각형 만들기
# t.penup()
# t.goto(-200 , -50)
# t.pendown()
# t.circle(40 , steps = 3)

# #사각형 만들기
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

# # 사각형 색깔 채우기
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

# '''사각형 다른 펜슬색깔로 여러개 그리기'''
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

# '''별 만들기'''
# n = 5
# for i in range(n):
#     t.forward(100)
#     t.right((360/n)*2)
#     t.forward(100)
#     t.left(360/n)


# '''1부터 10까지 줄바꿈을 하지 않고 출력하기 for , while문 사용''' 
# for i in range(1,11):
#     print(i , end=" ")

# i = 0
# while i < 10:
#     i += 1
#     print(i , end=" ")

# '''정수와 정수사이의 합 구하기'''
# '''for문 사용'''
# x = int(input("정수를 입력해주세요 : "))
# y = int(input("정수를 입력해주세요 : "))
# sum = 0
# for i in range(x , y+1):
#     sum += i
# print(x ,"부터" , y , "까지의 합은" , sum , "입니다.")

# '''while문 사용'''
# i = x
# sum = 0
# while i <= y:
#     sum += i 
#     i += 1
# print(x ,"부터" , y , "까지의 합은" , sum , "입니다.")

# '''짝수의 제곱을 구해 모두 합하는 문제'''
# '''for문 풀이'''
# x = int(input("정수를 입력해주세요 : "))
# y = int(input("정수를 입력해주세요 : "))
# total = 0
# for i in range(x , y+1):
#     if i % 2 == 0:
#         sum = 0
#         sum += i ** 2
#         total += sum
# print(total)

# '''while문 풀이'''
# i = x 
# total = 0
# while i < y:
#     i +=1 
#     if i % 2 == 0:
#         sum = 0
#         sum += i ** 2
#         total += sum 
#     print(total)

# '''리스트의 합을 받아 그 합의 평균을 구하는 문제'''
# '''for문 이용'''
# kor = [70 , 60 , 55, 75 , 95 , 90 , 80 , 80 , 85, 100]
# sum = 0
# total = 0 
# for i in kor:
#     sum += i
#     total = sum / len(kor)
# print(total)

# '''while문 이용'''
# i = 0
# sum = 0
# while i < len(kor):
#     i += 1
#     for i in kor:
#         sum += i
#         total = sum / len(kor)
#     print(total)

# '''강사님 풀이
# while문은 for문과 다르게 index에 접근을 하므로 while문 문제를 
# 풀때는 어떻게 index에 다가갈지 고민하자'''

# total = 0
# i = 0
# while i < len(kor):
#     total += kor[i]
#     i += 1
# avr = total / len(kor)
# print(avr) 

# '''1000미만의 자연수중 3과 5의 합을 구하는 문제'''
# '''for문 사용'''
# sum = 0
# for i in range(1000):
#     if i % 3 == 0:
#         sum += i
#     elif i % 5 == 0:
#         sum += i
#     else:
#         None
# print(sum)

# '''while문 사용'''
# i = 1
# sum = 0
# number = 1000
# while i < number:
#     i += 1 
#     if i % 3 == 0:
#         sum += i
#     elif i % 5 == 0:
#         sum += i
#     else:
#         None
# print(sum)

# '''리스트의 최고와 최저 점수를 제거하고 나머지 리스트들의 합과 평균을 구하는 문제'''
# scores = list(map(int , input("점수를 입력하세요 : ").split(":")))
# x = 0
# sum = 0
# while x < len(scores):
#     sorted(scores)
#     scores.remove(scores[0])
#     scores.remove(scores[-1])
#     x += 1
#     for i in scores:
#         sum += i
#         total = sum / len(scores) 
#     print(total)
#     break

# '''조건에 해당하면 각 배정된 리스트의 +1을 하는 프로그램 작성'''
# test = list(map(int, input("점수를 가르쳐 주세요. : ").split(":")))
# grade_counter = [0] * 5
# for i in test:
#     if i > 85:
#         grade_counter[0] = grade_counter[0] + 1
#     elif i > 70 and i < 84:
#         grade_counter[1] = grade_counter[1] + 1
#     elif 55 < i < 69:
#         grade_counter[2] = grade_counter[2] + 1
#     elif 40 < i < 54:
#         grade_counter[3] = grade_counter[3] + 1
#     elif 0 < i < 39:
#         grade_counter[4] = grade_counter[4] + 1
# print(grade_counter)

