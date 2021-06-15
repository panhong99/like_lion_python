# '''python은 쉽지만 알아야 할 것들이 굉장히 많다.'''
# '''프로그램은 익숙해지는것 반복해서 작성해보는것이 가장 좋은 방법이다.'''

# name_list = ["matthew" , "mark" , "luke" , "john" , "paul" , "peter"]
# x = 0
# total = 0
# while x < len(name_list): # 리스트 요소의 개수보다 작은동안 반복
#     x += 1                  
#     if  "h" in name_list[x-1]:      # 리스트의 객체중 h가 있다면 해당된 변수에 1을 +
#         total += 1
#     elif "m"  in name_list[x-1]:    # 위와 같은 개념 
#         total += 1
#     else:
#         print("해당사항이 없습니다.")    # 해당사항이 없다면 없다고 출력
    
# print(total)

# count = 0
# for name in name_list:              # 리스트를 name이라는 변수에 저장
#     for n in name:                  # n이라는 변수에 name의 내용 저장
#         if n == "m" or  n == "h":   # n변수내에 요소들중 m , h 가 있다면
#             count += 1              # count 변수에 +1
#             break                   # if문이 성립이 되면 강제 종료를 시키고 for문 다시 반복

# print(count)

# '''리스트를 돌아 if문에 해당이 된다면 원하는 문자열 출력'''
# marks = [90 , 25 , 67 , 45 , 80]
# x = 0
# for i in marks:                     
#     x += 1
#     if i < 60:
#         continue
#     print(x , "번 학생 합격입니다.")

# '''인덱스 에러가 나서 생각해보니 x증가값과 리스트의 인덱스 값이 맞지 않았다.'''
# '''while문을 사용할때는 인덱스 -1을 사용할수도 있다는 것을 생각하자'''
# while x < len(marks):    
#     x += 1 
#     if marks[x-1] < 60:    
#         continue
#     print(x , "번 학생 합격입니다.")
    
# '''메소드를 사용하지 않고 리스트를 반대로 뒤집는 프로그래밍'''
# arr = [1,4,2,3]
# left , right = 0 , len(arr) -1          # 변수들을 각각 0과 arr리스트에 -1을 한 값을 저장
# while left < len(arr) // 2:             # 변수가 리스트요소들의 개수 / 2 를 한 값보다 작은동안 반복
#     arr[left] , arr[right] = arr[right] , arr[left]     # 1번 변수의 내용과 2번 변수의 내용을 서로 change
#     left += 1                                           # left가 0이었으므로 중간 객체의 순서를 바꿔주기 위하여 + 1을 해줌
#     right -= 1                                          # right의 내용은 3이었으므로 -1을 해주어 중간객체의 인덱스에 성립될수 있게 -1
# print("변환된 arr은" , arr , "입니다.")

# '''구구단'''
# x = int(input("숫자 입력 : "))

# '''한줄당 모든 구구단의 * 1을 한 라인을 출력 (총 9 줄 출력)'''
# for i in range(1,10):                                   
#     for j in range(2,x):
#         print(i,"*",j,"=",i*j , sep="" , end="\t") # end함수를 사용해줌으로 각 요소들마다 Tap만큼 간격두기 
#     print()                                        # 줄바꿈

# i = 1
# j = 2 
# while i < 10:
#     while j < 10:
#         print(j , "x" , i , "=" , j * i , sep="" , end="\t")
#         j += 1
#     i += 1 # 단수  
#     j = 2  # 단 
#     print()    

# '''표를 받은 리스트와 후보 번호를 담은 리스트가 있고 표를 가장 많이 받은 후보자의 이름과 투표수를 출력하는 프로그램'''
# votes = [2,5,3,4,1,5,1,5,5,3]
# candidates = ["" , "전정국" , "김남준" , "박지민" , "정호석" , "김태형"]
# i = 0
# bin_list = [0] * 6          # 후보 수만큼 빈 리스트 생성
# while i < len(votes):       
#     i += 1
#     bin_list[votes[i-1]] = bin_list[votes[i-1]] + 1         # 임의로 생성한 리스트에 투표리스트의 번호에 상응하여 빈 리스트의 인덱스에 + 1 을 해줌 ex)votes의 0번이 2라면 빈 리스트의 2번째에 해당하는 리스트에 + 1 
    
# print(candidates[max(bin_list)] ,"후보가 총 " , max(bin_list), "표를 얻어 당선되었습니다.") # 빈 리스트에 가장많이 + 된 인덱스 넘버와 그 번호와 일치되는 후보자의 이름과 투표수를 출력


# '''입력받은 수까지 숫자를 출력하고 마지막 숫자를 한칸씩 앞으로 보내는 프로그램'''
# x = int(input("숫자를 입력해주세요 : "))
# i = 0
# while i < x:
#     j = 0
#     while j < x:
#         print((i + j) % x + 1 , end="  ") # i + j 를 하고 입력받은 값으로 나누어 주고 그 값에 + 1을 해줌 ex) i = 2 , j = 1 , x = 7 (2 + 1) % 7 + 1 ==  4  
#         j += 1
#     print()
#     i += 1

# '''짝수의 제곱은 + , 홀수의 제곱은 - 를 해서 sum함수에 담고 출력하는 프로그램'''
# i = 0
# sum = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         sum += i ** 2
#     elif i % 2 != 0:
#         sum -= i ** 2
# print(sum)

# x = int(input("숫자를 입력해주세요 : "))
# for i in range(2 , x):
#     for j in range(2 , i+1):
#         if i == j and i % j == 0:
#             total = 0
#             total += j
#         elif i != j and i % j ==  0:
#             None
#     print(total , "소수입니다.")


# indata = int(input("찾을 범위를 입력하세요 : "))
# i = 2

# line = 0
# while i <= indata:              # i가 indata보다 작은동안 반복
#     j = 2                       # j = 2
#     while j <= i:               # j가 i 보다 작거나 같은동안 반복
#         if i % j == 0:          # i % j 를 나눈 나머지가 0일때
#             break               # 강제 종료
#         j += 1                  # if문에 성립이 되지 않으면 j += 1
#     if i == j:                  # i 와 j 같다면 
#         print(i , end=" ")      # i를 출력
#         line += 1               # 
#         if line == 7:           # line이 7과 같다면 
#             line = 0            # line을 0을 초기화 후 
#             print()             # 줄바꿈
#     i += 1                      

# '''==================================================================='''
# '''변수 정리 
# source = "영어로 지역이름 담을 리스트"
# i = "문제 통과를 체크하는 변수"

# 구조 
# 1.while문 = "문제가 통과될때마다 + 1을 하는 구조로 해서 5문제를 맞추면 게임 종료"
# 2.if 문 = "if문 안에 input함수를 추가하고 문제와 사용자의 입력값이 같다면 i변수에 + 를 해주고  \n 그렇지 않다면 다시 입력하세요를 출력"
# 3.import time 과 import random 을 이용해서 문제를 무작위로 출력하고 , 5문제를 푸는 동안의 시간을 계산하고 
# 모든 문제 풀이가 완료되면 화면에 사용 시간을 출력
# 4.
# 5.

# 검증 리스트 
# 게임을 3번 정도 간단하게 실행을 시켜보고 에러가 날 수 있는 행위(오타 입력 등)을 시행한 후 
# 이상이 없다면 완료'''

# '''==================================================================='''
# '''스몰 프로젝트 , 타자 게임'''
# print("=========================================================================")
# import random 
# import time 

# Source = ["Seoul" , "Busan" , "Daejeon" , "Dague" , "Inchen" , "Gangwon" , "Gwangju" , "Jeju" , "Newyork" , "LA" , "Boston" , "Texas" , "Hawai"
# , "Osaka" , "Tokyo" , "Hukusima" , "Saporo" , "Laos" , "Korea" , "Japan" , "USA"]
# chance = 0
# Fail = 0
# Problem_1 = random.choice(Source)

# Game_Start = input("게임을 시작하시겠습니까? : ")
# print("게임을 시작합니다.")
# Start = time.time()    

# while chance  <= 5:
#     print(Problem_1)
#     solution = input("화면에 보이는 영단어를 대소문자를 구별해서 정확하게 입력해주세요!! : ")
#     if Problem_1 == solution:
#         print("GOOD!!!!!")
#         Problem_1
#         chance += 1
#         Problem_1 = random.choice(Source)
#     else:
#         print("ERROR!!!!")    
#         Fail += 1 
#     if chance == 5:
#         End = time.time()
#         print("축하합니다 통과하셨어요!!!")
#         print("소요된 시간은" , int(End - Start), " 초 입니다.")
#         break
#     if Fail == 4:
#         print("기회가 한 번 남았어요!!")
#     if Fail == 5:
#         print("조금 더 연습하고 도전하세요.....")
#         break
# print("=============================================================================")


# '''
# 1. 변수
# drink = 음료의 종류와 각 음료의 금액을 dict로 작성 
# money = input함수로 금액입력
# choice = 원하는 음료의 번호선택
# return_money = 음료가격과 입력한 금액의 차이 

# 2. 구조 
# 1. if문 =   입력값과 선택값을 비교 후 계산에 따른 값 출력 , 선택확인을 하는 문구 포함 
# 2. while문 = 금액이 부족하거나 거스름돈이 부족할때의 상황을 고려하여 작성 
# 3. 

# 3.검증
# 1. 음료보다 작은값을 입력 후 에러 메세지가 출력되는지 확인 
# 2. 거스름돈이 부족할 시 에러 메세지가 출력되는지 확인 
# 3. 거스름을 지급할때 정확하게 작동되고 안내문구와 함께 출력되는지 확인 
# 4 .금액을 추가로 입력했을때 추가 입력금액이 정확하게 누적되는지 확인 
# '''


# while True:
#     print("자판기 입니다.")
#     money = int(input("금액을 입력해주세요 : "))
#     choice = int(input("음료를 선택해주세요 : "))
#     if choice == 0:
#         print("구매해주셔서 감사합니다.")
#         break
#     drink = dict(zip([1,2,3,4,5] , ["사이다" , "콜라" , "생수" , "주스" , "커피"]))
#     price = dict(zip(["사이다" , "콜라" , "생수" , "주스" , "커피"] , [1200 , 1100 , 700 , 1500 , 1300]))
#     return_money = money - price[drink[choice]]
#     local_money = return_money + money
#     만원 = 0
#     오천원 = 0  
#     천원 = 0
#     오백원  = 0
#     백원 = 0
#     if drink[choice]: 
#         print("선택하신 음료는" , drink[choice] , "이고 상품의 금액은" , price[drink[choice]], "입니다." )
#         if price[drink[choice]] > money:
#             print("돈이 부족합니다. 돈을 더 넣어주세요.")
#             break
#         else:
#             print("잔돈은" , return_money , "입니다.")
#             if return_money > 10000:
#                 만원 += int(return_money / 10000)
#                 return_money -= 만원 * 10000
#                 오천원 += int(return_money / 5000)
#                 return_money -= 오천원 * 5000
#                 천원 += int(return_money / 1000)
#                 return_money -= 천원 * 1000
#                 오백원 += int(return_money/500)
#                 return_money -= 오백원 * 500
#                 백원 += int(return_money/100)
#             elif return_money < 10000:
#                 오천원 += int(return_money / 5000)
#                 return_money -= 오천원 * 5000
#                 천원 += int(return_money / 1000)
#                 return_money -= 천원 * 1000
#                 오백원 += int(return_money/500)
#                 return_money -= 오백원 * 500
#                 백원 += int(return_money/100)        
#             print("만원", 만원 ,"장" , "오천원" , 오천원 ,"장" , "천원" , 천원 , "장" , "오백원" , 오백원 , "장" , "백원" , 백원, "장")
#     if choice == 0:
#         print("구매해주셔서 감사합니다.")
#         break

