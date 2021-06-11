# # '''밑에는 디버깅을 할 수 있는 모듈이다.'''
# # import pdb 
# # pdb.set_trace()
# # '''=================================='''

# # total = 0
# # number = int(input("숫자를 입력하세요 : "))
# # for i in range(number + 1):
# #     total += i
# #     print(total)

# # x = [49 , -17 , 25 , 102 , 8 , 62 , 21]
# # for i in x:
# #     print(i * 10 , end=" ") 

# # x = int(input("숫자를 입력해주세요 : "))
# # for i in range(1,10):
# #     print(x , "*" , i ,"=" , x * i)

# # sum = 0
# # x = int(input("숫자를 입력해주세요 : "))
# # for i in range(0 , x + 1):
# #     sum += i
# # print(sum)

# # stone = [20.5 , 13.4 , 6.9 ,16.3 , 9.7 , 24.3 , 18.2 , 5.7 , 11.4 , 8.3]
# # sum = 0
# # for i in stone:
# #     print("돌의 무게를 나타내세요! : " , i)
# #     sum += i 
# # result = sum / len(stone)
# # print("모든돌의 평균 무게는",int(result), "입니다.")

# # '''======================================'''
# # ''' while 문 '''
# # '''while문은 조건이 True이면 계속해서 실행을 하고 False라면 그 즉시 프로그램을 종료시킨다.'''
# # i = 0
# # while i < 10:
# #     print(i+1 , end="  ")
# #     i += 1

# # for i in range(10):
# #     print(i+1 , end="  ")

# # '''================== 내가 제일 어려워했던 줄바꿈 구문 ======================'''
# # '''-50 부터 1 까지 출력하고 5개씩 줄바꿈 하는 프로그램을 작성하시요.'''
# # i = -50
# # sum = 1
# # while i <= 1:
# #     if sum % 5 == 0:            # sum을 5로 나누었을때 나머지가 0이라면 
# #         print(i , end = "\t")   # 출력을 하고 
# #         print()                 # 줄바꿈
# #     else:                       # 아니라면
# #         print(i , end = " \t")  # 그대로 출력
# #     i += 1                      
# #     sum += 1
# # '''==================================================================='''

# # x = int(input("숫자 입력 : "))
# # sum = 0
# # while 0 < x:
# #     sum += x
# #     x -= 1
# # print(sum)

# # x = int(input("숫자 입력 : "))
# # i = 1
# # while i < 10 :
# #     print(x , "*" , i , "=" , x * i) 
# #     i += 1
# # '''========================= 내가 쓴 풀이 =============================='''
# # marks = [90 , 25 , 67 , 45 , 80]
# # i = 0
# # while i < len(marks):
# #     for x in marks:
# #         i += 1
# #         if x > 60:
# #             print(i ,"번 학생은 합격입니다.")
# #         else:
# #             print(i ,"번 학생은 불합격입니다.")
# # '''=================================================================='''

# # '''while문을 이용하여 학생들의 합격여부를 확인하는 프로그램을 만드시오.'''

# # '''========= 강사님 풀이 ======='''
# # marks = [90 , 25 , 67 , 45 , 80]
# # i = 0
# # while i < 5:
# #     if marks[i] >= 60:
# #         print(i , "번 학생은 합격입니다.")
# #     else:
# #         print(i , "번 학생은 불합격입니다.")
# #     i += 1
# # '''=========================='''

# # marks = [90 , 25 , 67 , 45 , 80]
# # i = 0
# # while i < 5:
# #     if marks[i] >= 60:
# #         print(i , "번 학생은 합격입니다.")
# #     else:
# #         None
# #     i += 1

# # '''문제 주어진 리스트의 평균을 구하는 프로그램을 while문을 이용하여 작성하시요.'''
# # '''내 풀이법'''
# # Kor = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# # sum = 0
# # x = 0
# # while x < 1: 
# #     for i in Kor:
# #         sum += i
# #         result = sum / len(Kor)
# #     x += 1
# #     print(result)

# # ''' 강사님 풀이법'''
# # total = 0
# # i = 0
# # while i < len(Kor):
# #     total += Kor[i]
# #     i += 1
# # avr = total / len(Kor)
# # print(avr)

# # '''문제 while문을 이용해서 2의 20제곱을 구하는 프로그램을 작성하시요'''
# # '''나의 풀이'''
# # x = int(input("숫자 입력 : "))
# # i = 0 
# # while i < 20:
# #     i += 1 
# #     sum = 0
# #     sum += x ** i

# # print(x , "의 20제곱은 " , sum , "입니다.")

# # '''강사님 풀이'''
# # n = 1 
# # result = 0

# # while n < 20:
# #     result *= 2
# #     n +=1 

# # print("2의 20제곱은" , result , "입니다.")

# # num = int(input("숫자 입력 : ")) # 숫자 입력
# # data = []  # 빈 데이터
# # while True: # while문 시작
# #     a_data = int(num / 2) # num입력숫자의 2로 나눈 몫을 저장 
# #     b_data = int(num % 2) # num입력숫자의 2로 나눈 나머지를 저장
# #     data.insert(0, b_data) # 빈 데이터의 0번째에 b_data를 저장
# #     if a_data != 0: # num / 2가 0 이 아니면 
# #         num = a_data # num 변수에 a_data를 입력
# #     else:
# #         break #0이 맞다면 while문 탈출
# # print(data) # data를 출력
# # for i in data:  # i에 data를 담고
# #     print(i , end=" ") # i를출력

# '''묘듈은 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것
# 모듈안에는 함수 , 클래스 , 혹은 변수들이 정의 될 수 있다.'''

# import random 

# '''반복동작 실행문제'''
# i = 0
# while i < 10:
#     print(random.randint(1,6))
#     i += 1

# '''문제 1'''
# i = 0  # 변수 설정
# number = [0,0,0,0,0,0] # 6개의 빈 리스트를 지정
# while i < 10: # i가 10보다 작을때까지 반복
#     rad = random.randint(1,6) #rad라는 변수를 지정해서 랜덤수 출력
#     print(rad)    #rad 출력
#     number[rad-1] = number[rad-1] + 1 
#     i += 1
# print(number)

# i = 0
# while i != 3:     # i 가 3과 같지않으면 무한 반복
#     number = random.randint(1,6)  # number이란 변수지정후 1에서 6까지 랜덤수 출력
#     i = number # i에 number의 값을 입력
#     print(i)

# '''숫자를 맞춰야 끝나는 문제'''
# z = 0
# y = random.randint(1,10) 
# while y != z:
#     x = input("숫자를 입력해주세요. : ")
#     z = int(x)
#     if z == y:
#         print("정답입니다.")
#     elif z > y:
#         print("너무 큽니다.")
#     elif z < y:
#         print("너무 작습니다.")


# '''두개의 조건을 성립했을때 실행되는 while문'''
# i = 2 
# j = 5
# while i <= 32 or j >= 1:
#     print(i ,j) 
#     i *= 2    # i가 32보다 작은 동안 i * 2 반복
#     j -= 1    # j가 1보다 큰 동안 j - 1 반복

# i = 0
# while True: #무한루프  
#     print(i)  #i를 출력
#     i += 1    # 반복문 활성화되는 동안 i에 +1
#     if i == 100:  # i가 100과 같아진다면 
#         break     #브레이크

# '''1부터 100까지의 합을 더하는 프로그램'''
# i = 0
# total = 0
# while True: # 무한루프
#     i += 1  # i 에 1을 +
#     total += i # total 에 i 를 +
#     print(i) # i 를 출력
#     if i == 100: # 만약 i 가 100과 같다면 
#         break # 브레이크
# print(total) 

# ''' for문에 break사용예시 '''
# for i in range(10000):
#     print(i)
#     if i == 100:
#         break

# sum = 0
# for i in range(100000):
#     sum += i 
#     if i == 100:
#         break
# print(sum)

# '''continue 함수'''
# '''continue조건이 성립이 되면 밑의 구문은 실행하지 않고 다시 초기값으로 프로그램을 실행시킨다.
#    continue문과 성립되지 않을시 밑의 구문 실행'''
# for i in range(100): # 0부터 99까지를 생성
#     if i % 2 == 0:   # 2로 나누었을때 나머지가 0이라면 (짝수)
#         continue     # 프로그램을 다시 실행 
#     print(i)         # 

# i = 0
# while i < 100: # 100보다 작은동안
#     i += 1     # 1씩 +
#     if i % 2 == 0:  # 2로 나누었을때 나머지가 0이라면 (짝수라면)
#         continue    # 처음부터 다시 실행
#     print(i)        # if문이 성립하지 않으면 i를 출력 (홀수)

# count = int(input("반복 횟수 입력 : ")) # 사용자가 반복 횟수 지정
# for i in range(100000): # range함수로 100000숫자를 생성
#     print(i)    # i 를 출력
#     if i == count:      # 만약 count와 값이 같다면 
#         break           # 프로그램 강제종료 = break

# i = 0
# while True:     #무한루프
#     if i % 10 != 3: #10으로 나누었을때 나머지가 3아 아니라면
#         i += 1      # 1을 더해주고
#         continue    # 프로그램 다시시작
#     if i > 73:      # 73보다 크면 
#         break       # 강제 종료
#     print(i , end="  ") # i를 출력 , 각각에 공간을 띄워서
#     i += 1          


# start , stop = map(int , input("숫자를 입력해주세요 : ").split(":"))
# i = start
# while True:
#     if i % 10 == 3:
#         i += 1
#         continue
#     if i > stop:
#         break
#     print(i , end=" ")
#     i += 1 