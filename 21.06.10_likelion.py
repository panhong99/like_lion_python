# '''기본적으로 input이 받아들이는 tyep는 str이다.
# but input().split()을 하면 list 타입이 되는데 이유는 
# split은 여러개의 객체가 나오기 때문에 그 객체들을 묶어서 리스트 형태가 되는것이다.'''

# '''if 조건문 활용문제'''
# card = 9000
# age = int(input("나이를 입력해주세요 : "))
# if 7 <= age <= 12:
#     print("잔액은" , card - 650 , "원 입니다.")
# elif 13 <= age <= 18:
#     print("잔액은" , card - 1050, "원 입니다.")
# elif 19 <= age:
#     print("잔액은" , card - 1250, "원 입니다.")
# else:
#     print("잔액은" , card , "입니다.")
 
# '''================쪽지 시험================='''

# ''' 1 '''
# print("홀 , 짝 판단기")
# x = int(input("숫자 입력 : "))
# if x % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# ''' 2 '''
# x = int(input("숫자를 입력해주세요 : "))
# a = x + 20
# if a < 255:
#     print(a)
# else: 
#     print(255)

# ''' 3 ''' 
# x = int(input("숫자를 입력해주세요 : "))
# a = x - 20
# if a < 0:
#     print(0)
# else:
#     print(x , a)

# ''' 4 '''
# x = int(input("숫자를 입력해주세요 : "))
# a = x - 20
# if a < 0:
#     result = 0
# elif a > 255:
#     result = 255
# else:
#     result = a
# print(result)

# ''' 5 '''
# hour = input("시간을 입력해주세요 : ")
# second = input("시간을 입력해주세요 : ")
# if second == "00":
#     print(hour,":",second,"\n","정각입니다.")
# elif second != "00":
#     print(hour,":",second,"\n","정각이 아닙니다.")

# '''슬라이스를 활용한 풀이법'''
# data = input("입력값 : ")
# if data[3:] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

# ''' 6 '''
# age = (input("나이를 입력해주세요 : "))
# if len(str(age)) == 2 or len(str(age)) == 4:
#     print("잘못된 나이 입니다.")
# elif int(age[:2]) > 19:
#     print("성년입니다.")
# elif 10 <= int(age[:2]) <= 18:
#     print("청소년입니다.")

# ''' 7 '''
# fruit = ["사과" , "포도" , "홍시"]
# fruit2 = input("좋아하는 과일은? : ")
# if fruit2 in fruit:
#     print("정답입니다.")
# else:
#     print("땡")
 
# ''' 8 '''
# warning = ["Microsoft" , "Google" , "Naver" , "Kakao" , "SAMSUNG" , "LG"]
# invester = input("투자 종목 : ")
# if invester in warning:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# ''' 9 '''
# fruits = dict(zip(["봄" , "여름" , "가을"] , ["딸기" , "토마토" , "사과"]))
# like_fruits = input("제가 제일 좋아하는 계절은 : ")
# if like_fruits in fruits:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# ''' 10 '''
# fruits = dict(zip(["봄" , "여름" , "가을"] , ["딸기" , "토마토" , "사과"]))
# like_fruits = input("제가 제일 좋아하는 과일은 : ")
# if like_fruits in fruits.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# ''' 11 '''
# drink = dict(zip([1, 2, 3] , [700 , 600 , 800]))
# money = int(input("돈을 넣어주세요 : "))
# if money > 10000:
#     print("금액 입력 초과입니다.")
# else:
#     order = int(input("음료 선택 : "))
#     if money < drink[order]:
#         print("금액이 부족합니다.")
#     elif order == 1 or order == 2 or order == 3:
#         fee = money - drink[order]
#         print("잔액은" , fee , "원 입니다.")

# ''' 12 '''
# print("계산기 입니다.")
# x = int(input("숫자를 입력해주세요 : "))
# y = int(input("숫자를 입력해주세요 : "))
# sum = input("연산자를 선택해주세요. : " )
# if sum == "+":
#     print(x + y)
# elif sum == "-":
#     print(x - y)
# elif sum == "*":
#     print(x * y)
# if sum == "/":
#     if  y != 0:
#         print(x / y)
#     else:
#         print("질못된 연산자 입니다.")

# ''' 딕셔너리를 이용한 계산기 만들기 '''
# print("계산기 입니다.")
# x = int(input("숫자를 입력해주세요 : "))
# y = int(input("숫자를 입력해주세요 : "))
# choice = int(input("어떤 계산을 하실거죠 ? : "))
# if choice == 4 and y == 0:
#     print("잘못된 입력 정보")
# else: 
#     num = dict(zip([1 ,2 ,3 ,4] , [x + y  , x - y , x * y , x / y]))
#     if num[choice]:
#         print(num[choice])    

# ''' 13 '''
# apple = 150
# gyul = 30
# apple_1 , gyul_1 = map(int , input("사과와 귤을 몇 개 구매하실거죠? : ").split(":"))
# result = apple * apple_1
# result2 = gyul * gyul_1
# sum = result + result2
# if apple_1 >= 10:
#     apple_price  = result/10
#     print(sum - apple_price)
# else:
#     print(result + result2)

# ''' 14 '''
# apple = 150
# gyul = 30
# apple1 , gyul1 = map(int , input("몇개씩 구매하실거죠 ? : ").split(":"))
# result = apple * apple1
# result2 = gyul * gyul1
# sum = result + result2
# if apple1 > 5 and gyul1 > 3:
#     print(sum - sum/30)
# else:
#     print(sum)

# ''' 15 '''
# year = int(input("올해가 몇년도 인가요? : "))
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print("윤년입니다.")
# else:
#     print("평년입니다.")

# '''============================================================='''
# '''반복문 for'''
# for i in range(5 , 12):
#     print("Hello world" , i)

# for i in range(0,9,2):
#     print("Hello world" , i)

# for i in range(10,0,-1):
#     print("Hello world" , i)

# ''' reversed 함수는 요소들을 거꾸로 출력시켜준다.'''
# for i in reversed(range(10)):
#     print("Hello world" , i)

# '''for 과 if 문을 이용한 활용방식'''
# x = int(input("시작 숫자를 입력하세요 : "))
# y = int(input("끝 숫자를 말해주세요 : "))
# z = int(input("간격은요?? : "))
# if z < 0:
#     y -= 1
# else:
#     y += 1 
# for i in range(x , y , z):
#     print("Hello world" , i) 

# '''리스트 사용가능'''            
# a = [10,20,30,40,50]
# for i in a:
#     print(i)

# '''튜플'''
# fruits = ("apple" , "orange" , "grape")
# for fruit in fruits:
#     print(fruit) 

# for letter in reversed("python"):
#     print(letter , end=" ")

# x = [49 , -17 , 25 , 102 , 8 , 62 , 21]
# for i in x:
#     print(i * 10 , end=" ")    

# x = int(input("숫자 입력 : "))
# for i in range(1,10):
#     print(x,"*",i,"=",x*i)

# sum = 0
# x = int(input("숫자 입력 : "))
# for i in range(0,x+1):
#     sum += i
# print(sum)    

