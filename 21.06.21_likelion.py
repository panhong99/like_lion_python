def add(a , b):     # <= 더하기 
    return a + b    

def sub(a , b):     # <= 빼기
    return a - b    

def mul(a , b):     # <= 곱하기
    return a * b    

def div(a , b):     # <= 나누기(몫)
    return a / b    

def div2(a , b):    # <= 나누기(나머지)
    return a % b

print("============================")
print("1.더하기","\n","2.뺴기" ,"\n","3.곱하기" ,"\n","4.나누기" ,"\n","5.나머지" ,"\n","6.나가기")
print("============================")

while True:             # <= 강제 종료문이 나올때까지 반복
    send = int(input("원하는 연산자를 입력하세요. : "))     # <= 사용자 입력으로 원하는 연산입력받기 
    if send == 6:                                    # <= 사용자의 입력이 6과 같으면 반복문 종료 
        print("계산기를 종료합니다.")
        break
    first = int(input("첫번째 숫자를 입력하세요. : "))     # <= 정수입력 1
    second = int(input("두번째 숫자를 입력하세요. : "))    # <= 정수입력 2
    # calcu라는 딕셔너리 변수를 만들고 key와 value 생성 
    calcu = dict(zip([1,2,3,4,5] , [add(first,second),sub(first,second),mul(first,second),div(first,second),div2(first,second)]))   
    if calcu[send]:                                 # <= calcu라는 딕셔너리에 send한 key가 존재한다면 하위 프로그램 실행 
        print(calcu[send])
    else:                                           # <= 맞지 않으면 잘못되었다고 출력
        print("잘못입력하셨습니다. 다시 입력해 주세요.")

'''함수를 여러개 사용하지 않고 한개의 함수로 간단하게 작성하기'''
def sum(a , b , c):
    if c == 1:
        return  a + b 
    elif c == 2:
        return  a - b 
    elif c == 3:
        return  a * b 
    elif c == 4:
        return  a / b 
    elif c == 5:
        return  a % b 

print("============================")
print("1.더하기","\n","2.뺴기" ,"\n","3.곱하기" ,"\n","4.나누기" ,"\n","5.나머지" ,"\n","6.나가기")
print("=====================")

while True:             # <= 강제 종료문이 나올때까지 반복
    send = int(input("원하는 연산자를 입력하세요. : "))     # <= 사용자 입력으로 원하는 연산입력받기 
    if send == 6:                                    # <= 사용자의 입력이 6과 같으면 반복문 종료 
        print("계산기를 종료합니다.")
        break
    first = int(input("첫번째 숫자를 입력하세요. : "))     # <= 정수입력 1
    second = int(input("두번째 숫자를 입력하세요. : "))    # <= 정수입력 2
    if send == 1:                                 # <= calcu라는 딕셔너리에 send한 key가 존재한다면 하위 프로그램 실행 
        result = sum(first , second , send)
        print(result)
    elif send == 2:                                 # <= calcu라는 딕셔너리에 send한 key가 존재한다면 하위 프로그램 실행 
        result = sum(first , second, send)
        print(result)
    elif send == 3:                                 # <= calcu라는 딕셔너리에 send한 key가 존재한다면 하위 프로그램 실행 
        result = sum(first , second, send)
        print(result)
    elif send == 4:                                 # <= calcu라는 딕셔너리에 send한 key가 존재한다면 하위 프로그램 실행 
        result = sum(first , second, send)
        print(result)
    elif send == 5:                                 # <= calcu라는 딕셔너리에 send한 key가 존재한다면 하위 프로그램 실행 
        result = sum(first , second, send)
        print(result)
    elif send == 6:                                 # <= send가 6리아면 종료 문구를 출력하고 반복문 종료
        print("계산기를 종료합니다.")
        break
    else:                                           # <= 맞지 않으면 잘못되었다고 출력
        print("잘못입력하셨습니다. 다시 입력해 주세요.")

print("=================사칙연산 게임입니다.=====================")
import random                                       # 기본적으로 랜덤 모듈사용

def make_question():                                # 함수 생성
    number_A = random.randrange(1 , 10)             # 사칙연산 문제를 내기위한 랜덤숫자 출력
    number_B = random.randrange(1 , 10)             # 사칙연산 문제를 내기위한 랜덤숫자 출력 2   
    num = ["+" , "-" , "*"]                         # num이라는 연산자가 담긴 리스트 생성 
    calcu = random.choice(num)                      # calcu라는 변수를 만들고 그 변수안에 random.choice 함수에 num리스트를 입력하고 리스트 객체를 무작위로 1개 출력
    sum = str(number_A) + calcu + str(number_B)     # sum 변수를 생성해서 문제를 생성하고 저장 
    return sum                                      # 함수의 호출 시 return값을 sum변수로 지정 

i = 0
ok = 0
no = 0
while i < 5:                                        # 5문제를 출력을 할것이므로 i 가 5보다 작은 동안 반복 
    x = make_question()                             # x변수를 생성해서 make_question 함수 출력
    print(x)                                        # 사용자에게 문제를 시각화 해야 하므로 print()
    total = int(input("정답을 맞춰주세요. :"))           # total 변수를 생성해서 사용자가 문제를 보고 답을 입력받게 input함수를 이용  
    if (eval(x) == total):                          # 
        print("0")
        ok += 1
    else:
        print("x")
        no += 1
    i += 1

print("총" , i , "문제 중" , ok , "문제 맞췄습니다.")
print("==========================================================")

Student = {}

while True:
    print("1.인적사항 등록" , "2.학생 검색" , "3.학생 수정")
    print("4.학생 삭제" , "5.전체학생 보기" , "6.프로그램 종료")
    choice = int(input("원하는 번호를 입력하세요. : "))
    if choice == 1:
        key = int(input("학번을 입력하세요. : "))
        val1 = input("이름을 입력하세요. :")
        val2 = input("학점을 입력하세요 : ")
        print("등록이 완료되었습니다.")
        Student[key] = val1 , val2  
        print(Student)
        print()
        while True:
            print("1.인적사항 등록" , "2.학생 검색" , "3.학생 수정")
            print("4.학생 삭제" , "5.전체학생 보기" , "6.프로그램 종료")
            print("=======권장사항!!!!======= ")
            print(Student)
            print("위의 내용에 있는 학번들은 이미 등록이 된 학번이므로 정보를 입력하실때 중복되지 않게 주의해주세요." , "\n" ,"중복된 학번으로 입력할 시 타인에게 피해를 줄 수 있습니다.")
            print("========================")
            choice = int(input("원하는 번호를 입력하세요. : "))
            if choice == 1:
                key = int(input("학번을 입력하세요. : "))
                val1 = input("이름을 입력하세요. :")
                val2 = input("학점을 입력하세요 : ")
                print("등록이 완료되었습니다.")
                Student[key] = val1 , val2  
                print(Student)
                print()
            elif choice == 2:
                find = int(input("학번을 입력하세요. : "))
                print(Student[find])
                print("입력하신 학번과 일치하는 정보입니다.")
                print()
            elif choice == 3:
                remake = int(input("학번을 입력해주세요. :"))
                new_value1 = input("수정할 이름을 입력하세요. :")
                new_value2 = input("수정할 학점을 입력하세요 : ")
                Student[remake] = new_value1 , new_value2
                print(Student)
                print("등록이 완료되었습니다.")
                print()
            elif choice == 4:
                delete = int(input("학번을 입력하세요. : "))
                del Student[delete]
                print("정상적으로 삭제가 되었습니다.")
                print()
            elif choice == 5:
                print(Student)
                print()
            elif choice == 6:
                print("종료합니다.")
            break
    break
            
'''lambda 표현식 사용하기'''
def plus_ten(x):
    return x + 10
print(plus_ten(1))

'''람다표현식은 이름이 없는 함수이다. 익명 함수라고도 칭한다.'''
plus_ten = lambda x : x + 10 #<= 이런식으로 간단하게 정리를 해서 표현할 수 있다.
print(plus_ten(1))

print((lambda x : x + 10)(1)) # <= 매개변수를 후미에 ()안에 입력해줘도 함수로서 작동이 된다.

y = 10
print((lambda x : x + y )(1))

def plus_ten(x):
    return x + 10
print(list(map(plus_ten , [1,2,3])))

print(list(map(lambda x : x + 10 , [1,2,3])))

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x : str(x) if x % 3 == 0 else x , a)))

# 식 if 조건식 else 식2 형식 
# if만 사용하면 에러가 난다.

print(list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 10 , a)))

'''상단의 lambda 표현식을 def로 표현'''
a = [1,2,3,4,5,6,7,8,9,10]

def fun(x):
    for x in a:
        if x == 1:
            print(str(x) , end=" ")
        elif x == 2:
            print(float(x), end=" ")
        else:
            print(x + 10 , end=" ")
fun(a)

a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x , y : x * y , a , b)))

plus_ten = lambda x : x + 10
print(lambda x : x + 10)
print(plus_ten)

data = plus_ten(1)
print(data)

a1 = lambda x : x + 10
print(a1(1))

a2 =(lambda x : x + 10)(1)
print(a2)

y = 10
a_10 = lambda x : y + 10
print(a_10(10))

a = [1,2,3,4]
b = [2,4,6,8]
a_l = list(map(lambda x , y : x * y , a ,b))
print("a_l=" , a_l )

'''filter함수는 반복가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, 
filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져옴 '''

def f(x):
    return x > 5 and x < 10 # <= filter 함수는 해당 조건식이 True인것만 출력
a = [8,3,2,10,15,7,1,9,0,11]
print(list(filter(f , a)))

print(list(filter(lambda x : x > 5 and x < 10 , a))) # 위에 def를 사용한식을 lambda 형태로 변환시켜서 작성
# 가장 후미에 있는 a가 매개변수로 들어감 

def f(x , y):
    return x + y

a = [1,2,3,4,5]
from functools import reduce 
print(reduce(f ,a)) # <= 내 생각대로 풀이를 하면 최초 시작은 f = 0 , a = 1 이 되고
# 둘을 더해준 값이 f로 최신화되고 a 또한 다음객체로 넘어가 a의 요소가 다 할때까지 반복을 해주는 것이다.
# reduce 함수는 함수나 반복가능한 객체를 매개변수로 넘긴다. 
# 맞지 않는 매개변수를 넣으면 에러가 난다.
# 위에 결과가 15인 이유는 a 리스트에 모든 객체를 2개씩 더해주는것이다.

from functools import reduce
print(reduce(lambda x , y : x + y , a))

'''지역변수와 지역변수'''
x = 10
def foo():
    print(x)

foo()
print(x)

def foo():
    x = 10
    print(x)

foo()
print(x) # <= 전에는 지역변수 였지만 현재는 x가 함수안에 즉 지역변수가 되었으므로
         # 전역변수를 찾고자 print를 해도 찾을 수가없다.

'''전역변수는 10 이고 지역변수는 20이다.'''
x = 10
def foo():
    x = 20
    print(x)

'''그러므로 foo를 출력하면 같은 x라도 20 , 10 이렇게 각각 출력이 되는것이다.'''
foo() 
print(x)

'''후에 코드가 길어지면 전역변수 앞에는 g-라고 전역변수라고 표현해주는게 좋다.
하지만 애초에 전역과 지역은 변수의 이름을 다르게 하는것이 가장 좋다.
가독성 있게 짠 것이 거의 100% 좋은 코드라고 할 수 있다. 물론 짧게 작성하는것도 
좋지만 가독성 있게 코드를 작성하는것이 진정 좋은 코드라고 말할 수 있다.'''



x = 10
def foo():
    global x  # <= 이렇게 global이라는 코드를 작성을 해주면 상단에 있는 x값을 불러온다는 말과 같다.
    print(x)

foo()         # <= 그러므로 출력을 해도 foo() , print(x)는 같은 값이 나온다.
print(x)

def foo():
    global x  # <= 이렇게 global이라는 코드를 작성을 해주면 지역변수가 아니라 전역변수가 된다.
    x = 20
    print(x)

foo()         # <= 그러므로 출력을 해도 foo() , print(x)는 같은 값이 나온다.
print(x)

def print_hello():
    hello = "Hello, world!"
    def print_message():
        print(hello)
    print_message()

print_hello()

'''함수내에서 지역변수를 만들면 그 지역변수는 그 함수에만 사용가능한 지역변수이다.'''
def A():
    x = 10
    def B():
        nonlocal x #현재 함수의 바깥쪽에 있는 지역변수 사용 
        x = 20     #A의 지역 변수 x에 20 할당

    B()
    print(x)       #A의 지역변수 x 출력

A()

