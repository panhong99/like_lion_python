# #input 함수를 이용해 사용자의 이름을 받는 경우와 수의합을 표현했다.

# name = input("이름을 입력하세요 : ")
# print(name ,"씨 안녕하세요?")
# print("파이썬에 오신걸 환영합니다.")
# number = int(input("숫자를 입력하세요 : "))
# number2 = int(input("숫자를 입력하세요 : "))
# print(number , "과" ,number2 , "의 합은" , number + number2 ,"입니다.")

# place = input("경기장은 어디입니까? :")
# win = input("이긴팀은 어디입니까? :")
# Lose = input("진 팀은 어디입니까? :")
# player = input("우수 선수는 누구입니까? :")
# score = input("스코어는 몇대몇입니까? : :")
# print("오늘" , place , "에서 야구 경기가 열렸습니다.")
# print(win , "과" , Lose ,"는 치열한 공방전을 펼쳤습니다.")
# print(player , "이 맹활약을 하였습니다.")
# print("결국" , win , "이" , Lose , "를" ,score , " 로 이겼습니다.") 
# print("===============================")


# print(ord("A"))
# print(ord("a"))
# print(ord("1"))

# print(chr(45))
# print(chr(97))
# print(chr(75))

# #split함수에서 /를 사용해주면 /를 기준으로 앞 뒤로 수를 편하게 구분할수 있다.
# s1 , s2 = input("두 수를 입력하세요 : ").split("/")
# i1 = int(s1)
# i2 = int(s2)
# print("두 수의 합은 :" , i1 + i2)

# t1 , t2 , t3 = input("시간을 입력 하세요 : ").split(":")
# print("시 : " , t1)
# print("분 : " , t2)
# print("초 : " , t3)


# num1 , num2 = input("두 개의 숫자를 입력하세요. : ").split("/")
# print("두 수의 합은 " , int(num1) + int(num2) , "입니다.")

# num1 , num2 , num3 , num4 , num5 = map(int, input("5개의 값입력 : ").split("/"))
# print("합은 " , num1 + num2 + num3 + num4 + num5)

# 국어 , 영어 , 과학 , 수학 = map(int , input("시험점수 평균입니다. : ").split(":"))
# print("각 과목의 점수는" , 국어 , 영어 , 수학 , 과학 , "이며 평균은 " , int((국어 + 수학 + 영어 + 과학)/4), "입니다." )

# #print의 sep= 구문은 print의 내장함수로서 밑의 예시처럼 사용하면 된다.
# print(1,2,3, sep = ",")
# print(4,5,6, sep = ",")
# print("Hello" , "Python" , sep = "")
# print(1920 , 1080 , sep = "x")

# #\n 은 줄바꿈문자이다.
# print(1,2,3, sep = "\n")

# #sep 연습문제
# kor , eng ,sic , mat = map(int , input("시험평균 : ").split(":"))
# sum1 = kor + eng + sic + mat 
# aver = sum1/4
# print(kor, eng ,sic , mat , sep="+")
# print("총합은" ,int(sum1),"입니다.") 

# # print 의 end= 함수는 줄바꿈을 무효화시켜주는 효과를 가지고 있다.
# print(1 , end="/")
# print(2 , end="/")
# print(3)


# # 한 문장안에 sep , end를 같이 사용할수도 있다.
# year = 2019 
# month = 1 
# day = 31
# hour = 10 
# minute = 33
# second = 57
# print(year , month , day , sep = "/" , end=" " )
# print(hour , minute , second , sep=":")

# ap_pay = 150
# gual_pay = 30
# apple , gual = map(int , input("사과와 귤의 갯수입니다. : ").split(":"))
# print("사과의 개수 : " , apple)
# print("귤의 개수 : " , gual)
# apple_pay = apple * ap_pay
# gual_pay = gual * gual_pay
# sum = apple_pay + gual_pay
# print("총 가격은" , sum , "원")


# # input 함수를 이용해 사용자의 이름을 받는 경우와 수의합을 표현했다.
# #타인이 짠 코드를 보고 이해하는것이 실력향상에 상당히 도움이 된다.

# name = input("이름을 입력하세요 : ")
# print(name ,"씨 안녕하세요?")
# print("파이썬에 오신걸 환영합니다.")
# number = int(input("숫자를 입력하세요 : "))
# number2 = int(input("숫자를 입력하세요 : "))
# print(number , "과" ,number2 , "의 합은" , number + number2 ,"입니다.")

# place = input("경기장은 어디입니까? :")
# win = input("이긴팀은 어디입니까? :")
# Lose = input("진 팀은 어디입니까? :")
# player = input("우수 선수는 누구입니까? :")
# score = input("스코어는 몇대몇입니까? : :")
# print("오늘" , place , "에서 야구 경기가 열렸습니다.")
# print(win , "과" , Lose ,"는 치열한 공방전을 펼쳤습니다.")
# print(player , "이 맹활약을 하였습니다.")
# print("결국" , win , "이" , Lose , "를" ,score , " 로 이겼습니다.") 
# print("===============================")


# print(ord("A"))
# print(ord("a"))
# print(ord("1"))

# print(chr(45))
# print(chr(97))
# print(chr(75))

# # split함수에서 /를 사용해주면 /를 기준으로 앞 뒤로 수를 편하게 구분할수 있다.
# s1 , s2 = input("두 수를 입력하세요 : ").split("/")
# i1 = int(s1)
# i2 = int(s2)
# print("두 수의 합은 :" , i1 + i2)

# t1 , t2 , t3 = input("시간을 입력 하세요 : ").split(":")
# print("시 : " , t1)
# print("분 : " , t2)
# print("초 : " , t3)


# num1 , num2 = input("두 개의 숫자를 입력하세요. : ").split("/")
# print("두 수의 합은 " , int(num1) + int(num2) , "입니다.")

# num1 , num2 , num3 , num4 , num5 = map(int, input("5개의 값입력 : ").split("/"))
# print("합은 " , num1 + num2 + num3 + num4 + num5)

# 국어 , 영어 , 과학 , 수학 = map(int , input("시험점수 평균입니다. : ").split(":"))
# print("각 과목의 점수는" , 국어 , 영어 , 수학 , 과학 , "이며 평균은 " , int((국어 + 수학 + 영어 + 과학)/4), "입니다." )

# # print의 sep= 구문은 print의 내장함수로서 밑의 예시처럼 사용하면 된다.
# print(1,2,3, sep = ", ")
# print(4,5,6, sep = ",")
# print("Hello" , "Python" , sep = "")
# print(1920 , 1080 , sep = "x")

# # \n 은 줄바꿈문자이다.
# print(1,2,3, sep = "\n")

# # sep 연습문제
# kor , eng ,sic , mat = map(int , input("시험평균 : ").split(":"))
# sum1 = kor + eng + sic + mat 
# aver = sum1/4
# print(kor, eng ,sic , mat , sep="+")
# print("총합은" ,int(sum1),"입니다.") 

# # print 의 end= 함수는 줄바꿈을 무효화시켜주는 효과를 가지고 있다.
# print(1 , end="/")
# print(2 , end="/")
# print(3)

# '''
# 한 문장안에 sep , end를 같이 사용할수도 있다.
# year = 2019 
# month = 1 
# day = 31
# hour = 10 
# minute = 33
# second = 57
# print(year , month , day , sep = "/" , end=" " )
# print(hour , minute , second , sep=":")

# ap_pay = 150
# gual_pay = 30
# apple , gual = map(int , input("사과와 귤의 갯수입니다. : ").split(":"))
# print("사과의 개수 : " , apple)
# print("귤의 개수 : " , gual)
# apple_pay = apple * ap_pay
# gual_pay = gual * gual_pay
# sum = apple_pay + gual_pay
# print("총 가격은" , sum , "원")
# '''

# print(10 == 10)
# print(10 != 5)
# print("python" == "python")
# print("Python" == "python")
# print("Python" != "python")

# print(10 > 20)
# print(10 < 20)
# print(10 <= 10)
# print(10 >= 10)

# print(1 == 1.0)
# print(1 is 1.0)
# print(1 is not 1.0)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# #not > and > or 순으로 판단 
# #프로그램을 짤때는 꼭!!! 괄호를 정확하게 작성해 주어야 한다. 

# print(10 == 10 ) and (10 != 5)
# print(10 > 5) or (10 < 3)
# print(not(10 > 5))
# print(not(1 is 1.0))

# print(bool(1))
# print(bool(0))
# print(bool(1.5))
# print(bool("False"))
# print(bool(""))
# print(bool(" "))
