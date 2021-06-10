# '''슬라이스를 하고 요소 개수를 할당하지 않아도 알아서 할당됨
# 할당한 요소의 개수가 적으면 그만큼 리스트의 요소도 줄어듬'''
# a = [0,10,20,30,40,50,60,70,80,90]
# a[2:5] = ['a']
# print(a)

# '''증가폭을 설정해주고 슬라이스도 가능'''
# a[2:8:2] = ["a" , "b" , "c"]
# print(a)

# '''인덱스의 폭이 많아도 대치가 가능'''
# a[2:5] = ["a" , "b" , "c" , "d" , "e"]
# print(a)

# '''읽기 전용인 리스트를 제외하고 튜플 , range , 문자열은 삭제 및 변경이 불가하다.'''
# b = (0,10,20,30,40,50,60,70,80,90)
# b[2:5] = ['a' , 'b' , 'c' , 'd' , 'e']
# print(b)
 
# r = range(10)
# r[2:5] = range(0,3)
# print(r)

# a = [0,10,20,30,40,50,60,70,80,90]
# del a[2:5]
# print(a)

# '''del함수를 이용해 시퀀스 자료내의 요소들을 삭제할 수도 있다.'''
# del a[2:8:2]
# print(a)

# '''슬라이싱 응용 문제'''
# year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
# population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
# print(year[-3:])
# print(population[-3:])

# ''' index라는것은 시퀸스 요소들의 컴퓨팅넘버이다. '''
# '''  0    1     2    3 ...'''
# n = -32 , 75 , 97 , -10 , 9 , 32 , 4 , -15 , 0 , 76 , 14 , 2 
# print(n[1::2])

# '''elelment들의 개수가 -5를 벗어날경우 빈 시퀸스 자료로 출력해준다. ex) [] , ()'''
# a = input().split(":")
# print(tuple(a[:-5]))

# a = input("첫번째 줄 : ")
# b = input("두번째 줄 : ")
# a1 = (a[::2])
# b1 = (b[1::2])
# print(a1 + b1)

# '''딕셔너리 = 연관된 값을 묶어서 저장하는 용도로 사용'''
# '''딕셔너리 형태는 key : value형태로 사용한다.'''
# '''key는 변경할수 없는 타입이어야 하고 , value는 변경가능하다.'''
# '''딕셔너리는 특정 주제에 대한 연관된 값을 저장할 때 사용한다.'''
# Fruits = {"사과" : 1000 , "바나나" : 700 , "오렌지" : 1500 , "파인애플" : 2000}

# '''dic형태에 key가 중복되면 후미에 있는 key를 출력하고 선두의 값은 사라진다.'''
# lux = {"health" : 490 ,"mana" : 334 , "melee" : 550 , "armor" : 18.72}

# '''정수형의 key는 문자열 뿐만 아니라 정수 , 실수 , 불 형태도 사용가능함'''
# '''값에는 리스트 , 딕셔너리 등을 포함해 모든 자료형을 사용할 수 있음'''
# '''key에는 리스트나 딕셔너리를 사용할 수 없음'''
# x = {100:"hundred" , False : 0 , 3.5 : [3.5 , 3.5]}

# '''딕셔너리를 만드는 방법 4가지'''
# lux1 = dict(health = 490 , mana = 334 , melee = 550 , armor = 18.72)
# lux2 = dict(zip(["health" , "mana" , "melee" , "armor"] , [490 , 334 , 550 , 18.72]))
# lux3 = dict([("health" , 490) , ("mana" , 334) , ("melee" , 550) , ("armor" , 18.72)])
# lux4 = dict({"health" : 490 , "mana" : 334 , "melee" : 550 , "armor" : 18.72})

# '''딕셔너리에 접근할 때는 변수이름[key] <= 이런식으로 입력한다.'''

# Fruits = {"사과" : 1000 , "바나나" : 700 , "오렌지" : 1500 , "파인애플" : 2000}
# Fname = input("과일이름을 입력하세요 : ")
# print("선택한" , Fname ,"의 가격은" , Fruits[Fname] , "원 입니다.")

# '''딕셔너리의 value값은 아래 예시처럼 변경이 가능하다.'''
# lux1["health"] = 2037
# lux1["mana"] = 1184
# print(lux1)

# '''딕셔너리 이용'''
# Fruits = {"사과" : 1000 , "바나나" : 700 , "오렌지" : 1500 , "파인애플" : 2000}
# print("변경전 딕셔너리는" , Fruits , "입니다.")
# apple = int(input("변경된 사과 가격을 입력하세요 : "))
# Fruits["사과"] = apple
# print("변경된 딕셔너리는" , Fruits , "입니다.")

# '''딕셔너리에 추가와 오류 살펴보기'''
# lux = {"health" : 490 ,"mana" : 334 , "melee" : 550 , "armor" : 18.72}
# lux["mana_regen"] = 3.28 # <= 딕셔너리에 key:value를 추가하는 방법
# print(lux) 
# print(lux["attakc_speed"]) # <= 존재하지 않는 key를 요청하면 "keyError"이 난다.
# print("health" in lux) # <= in 연산자를 사용해 딕셔너리 내부의 값을 확인할 수 있다.
# print("attck_speed" not in lux)
# print(len(lux)) # <= len함수로 딕셔너리 내의 key의 개수를 알 수 있다.

# '''딕셔너리 연습문제'''
# Fruits = {"사과" : 0 , "바나나" : 0 , "오렌지" : 0 , "파인애플" : 0}
# apple , banana , orange , painapple = map(int , input("과일 가격입니다. : ").split(":"))
# Fruits["사과"] = apple
# Fruits["바나나"] = banana
# Fruits["오렌지"] = orange
# Fruits["파인애플"] = painapple
# print("가격이 책정된 과일들의 값은" , Fruits , "입니다.")

# keys = input("key를 입력해주세요.").split(":")
# value = input("value를 입력해주세요.").split(":")
# lux = dict(zip(keys , value))
# print(lux['health'])
# print("완성된 딕셔너리는" , lux , "입니다.")

# ''' 조건문 '''
# '''if문의 들여쓰기는 강제적이다.'''
# '''Flow chart(순서도)를 짜보는 연습을 하는게 좋다.(프로젝트 할 때 아주 유용하게 사용된다.)'''
# '''맨 처음 시작되는 첫줄을 메인 시퀀스라고 명칭한다.'''
# x = int(input(""))
# if x >= 10:
#     print("10이상입니다.")
#     if x == 15:
#         print("15입니다.")
#     if x == 20:
#         print("20입니다.")

# x = 8
# if x != 10:
#     print("ok")

# '''나의 풀이'''
# product = int(input("제품 가격입니다. : "))
# coupon = int(input("쿠폰 입니다. : "))
# if product:
#     print(product - int(coupon))

# '''강사님 풀이'''
# strMoney = input("값입력")
# strCpn = input("쿠폰입력")
# if strCpn == "Cash3000":
#     print(int(strMoney) - 3000)
# if strCpn == "Cash5000":
#     print(int(strMoney) - 5000)

# Number = int(input("숫자입니다. : "))
# if Number % 2 == 0:
#     print("짝수입니다.")
# if Number % 2 != 0:
#     print("홀수입니다.")

# Number = int(input("숫자입니다."))
# if Number >= 10:
#     print("10보다 크거나 같습니다.")
# else:
#     print("10보다 작습니다.")

# One = int(input(""))
# if One == 10:
#     print("10입니다.")
# else:
#     print("10이 아닙니다.")

# ''' bool '''
# if True:
#     print("참")
# else:
#     print("거짓")
# if False:
#     print("참")
# else:
#     print("거짓")
# if None:
#     print("참")
# else:
#     print("거짓") #None은 거짓 

# ''' 정수형 '''
# if 0:
#     print("참")
# else:
#     print("거짓")
# if 1:
#     print("참")
# else:
#     print("거짓")
# if 0x1F: #16진수
#     print("참")
# else:
#     print("거짓")
# if 0b1000: #2진수
#     print("참")
# else:
#     print("거짓")
# if 13.5: #실수
#     print("참")
# else:
#     print("거짓") 

# ''' 문자열 '''
# if "Hello":
#     print("참")
# else:
#     print("거짓")
# if '':
#     print("참")
# else:
#     print("거짓")

# x = 10
# y = 10
# if x == 10 and y == 20:
#     print("참")
# else:
#     print("거짓")

# x = 15
# if x > 0:
#     if x < 20:
#         print("20보다 작은 양수입니다.")

# if x > 0 and x < 20:
#     print("20보다 작은 양수입니다.")

# if 0 < x < 20:
#     print("20보다 작은 양수입니다.")

# Test = 75
# coding = True

# if Test > 80 and coding:
#     print("합격")
# else:
#     print("불합격")

# Kor_Test = 75
# Eng_Test = 75
# if Kor_Test >= 90 and Eng_Test >= 70:
#     print("합격")
# else:
#     print("불합격")

# '''내가 짠 코드'''
# Kor , Eng , Mat , Sci = map(int , input("시험 점수입니다. : ").split(":"))
# sum = Kor + Eng + Mat + Sci
# avr = sum / 4
# if 0 <= Kor <= 100  or 0 <=  Eng <= 100 or 0 <= Mat <= 100 or 0 <= Sci <= 100:
#     print("잘못된 점수입니다.")
# elif avr > 80:
#     print("합격")
# else:
#     print("불합격")

# x = 30
# if x == 10:
#     print("10입니다.")
# elif x == 20:
#     print("20입니다.")
# else:
#     print("10도 20도 아닙니다.")

# '''elif 활용'''
# print("음료수 자판기 입니다.")
# drink = input("음료를 골라주세요 : ")
# if drink == "콜라":
#     print("콜라")
# elif drink == "사이다":
#     print("사이다")
# elif drink == "환타":
#     print("환타")
# else:
#     print("제공되지 않는 메뉴")

# '''elif 문제 활용'''
# Student = int(input("학생인가요 ? :"))
# Class = dict(zip([1 , 2 ,3] , ["초등학생" , "중학생" , "고등학생"]))
# Say = "학생이며"
# if Student == 1:
#     print(Say , Class[Student], "입니다.")
# elif Student == 2:
#     print(Say , Class[Student] , "입니다.")
# elif Student == 3:
#     print(Say , Class[Student] , "입니다.")
# else:
#     print("학생이 아닙니다.")

# Mart = int(input("금액을 입력해 주세요. :"))
# drink = input("음료를 입력해 주세요. :")
# subject = dict(zip(["콜라","사이다","환타"] , [600 , 700 , 800]))
# if drink == "콜라":
#     Money2 = Mart - subject[drink]
#     print("잔돈은" , Money2 , "입니다.")
# elif drink == "사이다":
#     Money2 = Mart - subject[drink]
#     print("잔돈은" , Money2 , "입니다.")
# elif drink == "환타":
#     Money2 = Mart - subject[drink]
#     print("잔돈은" , Money2 , "입니다.")


# Number = int(input("숫자를 넣어주세요 : "))
# if 11 <= Number <= 20:
#     print("11 ~ 20")
# elif 21 <= Number <= 30:
#     print("21 ~ 30")
# else:
#     print("아무것도 해당되지 않음")  

# price = int(input("제품의 가격을 입력시켜 주세요 : "))
# coupon = input("쿠폰을 입력시켜 주세요 : ")
# if coupon == "Cash3000":
#     print(price - 3000)
# elif coupon == "Cash5000":
#     print(price - 5000)


# Kor , Eng , Mat , Sci = map(int , input("과목의 점수입니다. : ").split(":"))
# if (0 <= Kor <= 100 and 0 <= Eng <= 100 and 0 <= Mat <= 100 and 0 <= Sci <= 100):
#     result = Kor + Eng + Mat + Sci / 4
#     if result >= 80:
#         print("합격입니다.")
#     else:
#         print("불합격 입니다.")
# else:
#     print("잘못된 점수 입력입니다.")

# student = int(input("학생인가요? : "))
# Number = dict(zip([1,2,3] , ["초등" , "중등" , "고등"]))
# say = "학생이며"
# if student == 1:
#     print(say + Number[student] , "입니다.")
# elif student == 2:
#     print(say + Number[student] , "입니다.")
# elif student == 3:
#     print(say + Number[student] , "입니다.")
# else:
#     print("학생이 아닙니다.")

