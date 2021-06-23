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
    if (eval(x) == total):                          # eval함수는 문자열로 형성이 된 연산식의 값을 출력해주는 함수이다. 그러므로 사용자의 정답이 입력되는 total함수와 eval의 값이 일치할시 if문의 조건에 성립된다.
        print("0")
        ok += 1
    else:                                           # 정답이면 ok 오답이면 no를 해주어 5문제동안 정답의 수와 오답의 수를 측정한다.
        print("x")
        no += 1
    i += 1

print("총" , i , "문제 중" , ok , "문제 맞췄습니다.")     # 반복문이 종료되고 출력된 문제의 수와 그 중 답을 맞힌 횟수를 출력한다.
print("==========================================================")
# 학생들의 학번과 학점을 기록하는 프로그램 
Student = {}

while True:                                                 # 무한루프 생성              
    print("1.인적사항 등록" , "2.학생 검색" , "3.학생 수정")        # 총 6개의 목록을 형성하고 print 한다.
    print("4.학생 삭제" , "5.전체학생 보기" , "6.프로그램 종료")
    choice = int(input("원하는 번호를 입력하세요. : "))           # input으로 이용자가 원하는 목록을 선택하게 한다.
    if choice == 1:                                         # 조건문의 시작부분 사용자가 원하는 목록을 선택한 후 각각의 맞춰서 동작을 진행한다.
        key = int(input("학번을 입력하세요. : "))               # 1번에 해당하는 조건은 새롭게 정보를 등록하는 것이므로 새로운 학번과 이름 학점을 입력한다. (구분은 고유번호인 학번으로 구분한다.)       
        val1 = input("이름을 입력하세요. :")                    
        val2 = input("학점을 입력하세요 : ")
        print("등록이 완료되었습니다.")
        Student[key] = val1 , val2                          # 새로이 등록이 되었으므로 생성해놓은 dict에 새로운 key와 value를 저장해준다.
        print(Student)
        print()
        while True: 
            print("1.인적사항 등록" , "2.학생 검색" , "3.학생 수정")
            print("4.학생 삭제" , "5.전체학생 보기" , "6.프로그램 종료")
# 권장사항은 지금까지 등록이 되어있는 정보들을 출력을 해주면서 해당 고유학번과 중복되지 않게 사용자에게 고지를 한다.
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
            elif choice == 2:                           # 2번 조건은 dict내에 일치하는 학번을 입력을 하면 해당 학번에 일치하는 정보를 출력해준다.
                find = int(input("학번을 입력하세요. : "))
                print(Student[find])                    # 이 때 입력받는 input문은 find라는 변수이다. Student의 객체내에 find로 입력받은 정수의 학번을 key로 입력받아 value를 출력한다.
                print("입력하신 학번과 일치하는 정보입니다.")
                print()                                 # 이용자가 정보를 편하게 볼 수 있게 줄바꿈을 해준다.
            elif choice == 3:
                remake = int(input("학번을 입력해주세요. :"))       # 3번 조건은 저장된 내용의 수정으로 역시 일치되는 학번을 input으로 입력을 받는다.
                new_value1 = input("수정할 이름을 입력하세요. :")    # 해당 학번과 일치하는 정보를 받고 새로이 변경할 value를 입력한다.(이름)
                new_value2 = input("수정할 학점을 입력하세요 : ")    # 위의 설명고 같고 새로이 변경할 value를 입력한다.(학점)
                Student[remake] = new_value1 , new_value2      # value를 입력받고 새로운 정보를 업데이트 해준다.
                print(Student)                                 # 정보를 입력받고 변경사항을 출력해준다.
                print("등록이 완료되었습니다.")
                print()
            elif choice == 4:                           # 4번 조건은 저장해놓은 정보를 삭제하는 것이다.
                delete = int(input("학번을 입력하세요. : "))        # delete라는 변수로 input내용을 입력받는다.(일치하는 학번입력)
                del Student[delete]                     # del 함수로 Student 딕셔너리안에 있는 일치되는 key 와 값을 삭제해준다.
                print("정상적으로 삭제가 되었습니다.")          # 동작을 보여주고 완료가 되었다고 안내문자를 출력한다.
                print()
            elif choice == 5:                           # 5번 조건은 현재 저장되어 있는 모든 dict의 정보를 한 번에 출력을 해준다.
                print(Student)
                print()
            elif choice == 6:                           # 6번 조건은 프로그램 종료이다.
                print("종료합니다.")
            break
    break
# 코드 리뷰 : dict를 이용하면 생각보다 고민하지 않고 편안하게 작성을 할 수가 있었다. dict를 좀 더 사용한다면 더 코드를 줄일수는 있겠지만 가독성을 위해 현재 나의 수준으로는 
# 가장 깔끔하고 가독성있게 작성을 한 것 같다. 아무래도 dict를 활용한 코드작성은 익숙하고 편한것 같다.
'''========================================================================================================================================'''
'''lambda 표현식 사용하기'''
def plus_ten(x):
    return x + 10
print(plus_ten(1))

'''람다표현식은 이름이 없는 함수이다. 익명 함수라고도 칭한다.'''
plus_ten = lambda x : x + 10 #<= 이런식으로 간단하게 정리를 해서 표현할 수 있다.
print(plus_ten(1))

print((lambda x : x + 10)(1)) # <= 매개변수를 후미에 ()안에 입력해줘도 함수로서 작동이 된다.

y = 10
print((lambda x : x + y )(1))       # y를 전역변수로 10으로 지정해주었고 후미에 (1)이 x의 매개변수가 되어 출력값은 11이 나온다.

def plus_ten(x):                    # 매개변수에 10을 *해주는 함수이다.
    return x + 10
print(list(map(plus_ten , [1,2,3])))    # 리스트로 1,2,3을 각각 매개변수로 지정해주었다.

print(list(map(lambda x : x + 10 , [1,2,3])))   # 위의 코드를 lambda 함수를 이용해 조금 더 간결하게 작성을 하였다.

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x : str(x) if x % 3 == 0 else x , a)))    # 리스트는 if문은 if문 선두에 있는 변수가 if문의 내용이고 후미에 else문은 else문의 우측에 있는 내용이 else의 내용이 된다.

# 식 if 조건식 else 식2 형식 
# if만 사용하면 에러가 난다.

print(list(map(lambda x : str(x) if x == 1 else float(x) if x == 2 else x + 10 , a)))

'''상단의 lambda 표현식을 def로 표현'''
a = [1,2,3,4,5,6,7,8,9,10]

def fun(x):                             # 함수를 생성해서 if조건문을 함수의 조건으로 지정을 해주었다.
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
print(list(map(lambda x , y : x * y , a , b)))  # x , y 를 인수로 지정하고 a , b 각각의 리스트를 x , y에 매개변수로 지정을 해주었다.

plus_ten = lambda x : x + 10                    # lambda 함수 자체로 결괏값이 나오는것이 아니다. map함수가 언팩킹을 해주지 않으면 내용이 출력되지 않는 것과 같은 개념이다.
print(lambda x : x + 10)
print(plus_ten)

data = plus_ten(1)                              # data로 lambda 함수를 불러내고 매개변수를 후미에 (1)로 지정을 해주었다.
print(data)

a1 = lambda x : x + 10                          # 상단과 같다.
print(a1(1))

a2 =(lambda x : x + 10)(1)
print(a2)

y = 10
a_10 = lambda x : y + 10                        # 이 부분에서 의문점은 y 는 10으로 지정해주었지만 매개변수를 10으로 내용을 입력하면 되는것을 굳이 +10을 해주었나라는 의문이 들었고
print(a_10(10))                                 # 답변을 듣고 나서는 (10)을 해준이유는 lambda함수의 작동을 위해 10을 넣어준것이라고 이해를 했다.

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

from functools import reduce                # 상단에 작성을 해준것과 같이 a를 매개변수로 입력을 해주고 초기에 값은 x = 0 , y = 1이라고 생각을 하고 
print(reduce(lambda x , y : x + y , a))     # a의 리스트의 값이 차려대로 입력이 되면서 x <= y의 방향대로 최신화가 된다고 생각을 하면 된다. 답은 15이다.

'''전역변수와 지역변수'''
# 전역변수는 함수의 외각에 위치하는것이고 지역변수는 함수내에 위치한 변수이다.
x = 10                                      
def foo():              # 전역 변수를 사용했으므로 x를 출력해도 10이 출력된다.
    print(x)

foo()
print(x)

def foo():              # 지역변수로 설정이 되어있으므로 외각에서 x를 출력하고자 하면 에러를 출력한다.
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

def print_hello():              # 이중 함수를 작성한 부분인데 첫 함수에서는 변수를 지정을 해주고 2번째 함수에서는 변수를 출력을 해준다. 
    hello = "Hello, world!"     # 그리고서 2번째 함수를 출력해주었고 
    def print_message():
        print(hello)
    print_message()

print_hello()                   # 첫번째 함수를 불러내도 2번째 함수가 1번째 함수에 내장되어있기 때문에 "Hello world"가 정상적으로 출력이 된다.

'''함수내에서 지역변수를 만들면 그 지역변수는 그 함수에만 사용가능한 지역변수이다.'''
def A():
    x = 10
    def B():
        nonlocal x #현재 함수의 바깥쪽에 있는 지역변수 사용 
        x = 20     #A의 지역 변수 x에 20 할당

    B()
    print(x)       #A의 지역변수 x 출력

A()

