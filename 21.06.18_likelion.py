import copy 
a = [10,20,30]
b = copy.deepcopy(a) # <= 2차원 리스트를 복사하고 엘리먼트를 단독으로 변경하고 싶을때는 
b[0][0] = 500        # <= copy모듈을 사용해서 deepcopy를 사용해서 엘리먼트들을 바꿔준다.
print(a)
print(b)

'''2차원 리스트 만들기를 응용한 3차원 리스트 만들기'''
lien = 0
a = [[[0 for a in range(3)] for b in range(4)] for c in range(2)]
print(a)

s = "Hello, world!".replace("world" , "python") # <= 문자열 메서드인 replace함수는 지정한 문자열을 변경할 문자열로 교체해준다.
print(s)
 
s = "Hello, world!" # <= 만약 바꿀 문자열이 존재하지 않는다면 그대로 출력한다.
s = s.replace("world" , "python")
print(s)

table = str.maketrans("aeiou" , "12345") # <= 문자열 안에 문자를 다른 문자로 바꿈 
print("apple".translate(table))          # <= 바꿈 당할 문잘르 지정하고 그것에 해당이 된다면 바꿔줄 문자로 바꿔줌

print("apple pear grape pineapple oraange".split()) # <= map함수에서 자주 이용하는 split함수이다.
print("apple,pear,grape,pineapple,oraange".split(","))

'''join함수는 각 문자열을 구분할떄 사용자가 원하는 부호를 넣어 구분짓게 해준다.'''
print("/".join(["apple" , "pear" , "grape"  , "pineapple" , "oraange"]))

print("python".upper()) #<= 대문자 전환함수
print("PYTHON".lower()) #<= 소문자 전환함수

print("       python      ".lstrip()) # <= 좌측 공백 삭제
print("       python      ".rstrip()) # <= 우측 공백 삭제 
print("       python      ".strip()) # <= 양측 공백 삭제  

print(",   python.".lstrip(",.")) # <= 좌측 , 삭제
print(",python    .".rstrip(".")) # <= 우측 . 삭제 
print(",python.".strip(",.")) # <= 양측 ,. 삭제  

print("python".ljust(10)) # <= 문자열의 칸을 10칸으로 정해서 좌측정렬을 하고 남는공간을 공백으로 채움
print("python".rjust(10)) # <= 우측정렬 후 남는칸을 공백으로 채움 
print("python".center(10)) # <= 가운데 정렬 후 남는칸을 양측에 공백으로 채움

print("python".rjust(10).upper()) # <= 여러개의 메서드들을 사용한다고 해서 메서드 체이닝이라고 명칭한다.

print("3.5".zfill(6)) #<= 전체문자열을 지정해주고 문자열을 출력하고 남은 칸은 0으로 채워준다.

print("apple pineapple".find("pl")) # <= 특정문자열을 찾아 해당 문자열의 인덱스번호를 가르쳐줌 
print("apple pineapple".find("xy")) # <= 해당하는 문자열이 없을경우 -1 을 출력
# 해당 문자가 여러개가 있을경우 가장 선두에 있는 문자의 인덱스를 알려줌

print("apple pineapple".rfind("pl")) # <= rfind함수를 사용하면 find와 동작은 같으나 인덱스 뒤에서 부터 문자열을 찾아줌
print("apple pineapple".rfind("xy")) # <= 해당하는 문자열이 없을경우 -1 을 출력

print("apple pineapple".index("pl"))    # <= find와 같은 동작 
print("apple pineapple".rindex("pl"))   # <= rfind와 같은 동작
# find함수는 찾을 문자가 없다면 -1을 반환하지만 rindex는 에러를 출력한다.

print("apple pineapple".count("pl")) # <= 특정문자가 해당문자열에서 몇번이나 등장하는지 알려줌

apple = "apple pineapple apple pineapple"
find = apple.find("pl")
print(find)
newfind = find + 2
apple = apple[newfind:]
find1 = apple.find("pl")
find1 = newfind + find1
print(find1)

apple = "apple pineapple apple pineapple"
find = apple.find("pl")
i = 0
a = 0
while apple[a:] != -1:
    if apple[find + 1] == "l":
        print(find)
        a += find + 2
        apple = apple[a:]
        find = apple.find("pl")
        find += a
        
    apple = "apple pineapple apple pineapple"     
    num = "pl"
    cnt = apple.find(num)
    print(cnt)
    while apple[cnt+2:].find(num) != -1:
        cnt = apple[cnt+2:].find(num) + cnt + 2
        print(cnt)


apple = "apple pineapple apple pineapple"

i = 0
while i < len(apple):
    if apple[i] == "p" and apple[i+1] == "l":
        print(i)
    else:
        None
    i += 1

a = "I am %s" % "James"
print(a)

name = "maria"
a = "I am %s" %name
print(a)

a = "I am %d years old" % 20
print(a)

a = "%.2f" % 2.3
print(a)

a = "%10s" % "python"
print(a)

a = "%-10s" % "python"
print(a)

a = "Today is %d %s" % (3, "April")
print(a)

a = "Hello , {0} ".format("world")
print(a)

a = "Hello , {0} , {2} , {1}".format("python" , "script" , 3.6)
print(a)

a = "{0} , {1}".format("a"*3 , "b"*3)
print(a)

a = "Hello , {} {} {} ".format("python" , "script" , 3.6) 
print(a)

a = "Hello {language}  {version}".format(language="python" , version=3.6)
print(a)

language = "python"
version = 3.6
a = f"Hello , {language} {version}"
print(a)

a = "{0:<10}".format("python") # <= 좌측 정렬
print(a)

a = "{0:>10}".format("python") # <= 우측 정렬
print(a)

a = "{:>10}".format("python")
print(a)

a = "{0:<10} {2:>10}{1:>10}".format("python" , "abc" , 123)
print(a)

a = "%03d" % 1
print(a)

a = "{0:03d}".format(35)
print(a)

a = "%08.2f" %3.6
print(a)

a = "{0:08.2f}".format(150.37)
print(a)

a = "{0:0<10}".format(15)
print(a)

a = "{0:0>10}".format(15)
print(a)

a = "{0:0>10.2f}".format(15)
print(a)

a = "{0: >10}".format(15)
print(a)

a = "{0:>10}".format(15)
print(a)

a = "{0:x>10}".format(15)
print(a)

path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-32\\data.txt'
a = path.split("\\")
filename = a[-1]
print(filename)

ward = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
a = ward.split(" ")
x = 0
for i in a:
    if i == "the":
        x += 1
        print(i)
print(x)

print(ward.replace("," , " ").replace("." , " ").split(" ").count("the"))
b = ",".join(a)
print(b.count("the"))

'''========================= 함수 ========================================'''
def hello():
    print("Hello world")

for i in range(10):
    hello()

def add(a , b): # <= 함수에서 값을 받으려면 ()안에 변수 이름을 지정해주면 됨
    print(a + b)# <= 이 변수들의 이름을 "매개변수" 라고 부름 
 
add(10,20)

def add(a , b):
    return a + b # <= return값을 사용하면 함수 바깥으로 반환할 수 있고 , 함수에서 나온 값을 변수에 저장할 수 있다.

x = add(10,20)   # <= return값이 x라는 변수에 들어간다.
print(x)
print(add(10,20)) # <= 굳이 변수에 값을 지정하지 않아도 print로도 인수를 입력해주면 return값을 츨력가능하다.

def mul(a , b ,c): # <= 매개변수를 3개를 입력받음
    return a * b * c # <= return값은 3개의 매개변수를 * 해준 값

x = mul(1,2,3)      # <= mul함수에 할당되는 인수 3개를 지정 하고 x라는 변수에 return값을 저장
print(x)            # <= return값이 저장된 x변수를 출력

def add_sub(a , b): # <= 값을 여러개도 반환가능
    return a + b , a - b  # <= return값에 연산을 2개 넣어놓고 그 구분을 ,(콤마)로 구분해주면 됨

x , y = add_sub(10,20) # <=변수 x , y에 각각 함수의 값을 지정 
print(x) #<= 30
print(y) #<= -10

z = add_sub(10,20) # <= 2개의 return값을 하나의 변수에 할당이 가능하다.
print(z)           # <= print로 출력을 하면 tuple형태로 값을 반환해준다.
print(type(z))


x , y = map(int , input("정수 입력 : ").split(":")) # <= x , 라는 변수에 사용자의 입력을 받아서 2개의 정수 할당

def math(a , b):    #<= math라는 함수를 작성하고 매개변수를 2개를 할당받는다.
    return a + b , a - b , a * b , a / b # <= return값은 2개의 매개변수를 사칙연산을 계산한 값이다.

x = math(x , y)     # <= x라는 변수를 만들고 함수를 호출하고 인수를 지정해주고 return값을 x변수에다 저장한다.
print("+ = %d , -= %d , *= %d , /= %d" %x) # x변수에는 값이 튜플형식으로 4개가 들어있으므로 각각의 문자열 서식을 이용하여 출력을 해준다.

def mul(a , b):
    c = a * b
    return c

def add(a, b): # <= 보기와 같은 함수와 같이 함수내에서 함수를 호출하는것도 가능하다.
    c = a + b  
    print(c)
    d = mul(a,b)
    print(d)

x = 10
y = 20
add(x , y)

x = 10
y = 3

def sum(a , b):
    c = int(a / b)
    print(c)
    d = a % b
    print(d)

a, b = sum(x , y)
print("몫" , a , "나머지" , b)


def get_quotient_remainder(x,y):
    return a // b , a % b

quotient , remainder = get_quotient_remainder(x,y)
print("몫" , quotient , "나머지" , remainder)

Number_a , Number_b = map(int , input("정수 입력 : ").split(":"))

def calcu(a , b):
    return a + b , a - b , a * b , a // b

add , sub , mul , div = calcu(Number_a , Number_b)

print(f"덧셈 {add} , 뺄셈 {sub} , 곱하기 {mul} , 나누기 {div}")

def add(a , b):
    return a + b    

def sub(a , b):
    return a - b    

def mul(a , b):
    return a * b    

def div(a , b):
    return a / b    

def div2(a , b):
    return a % b

print("============================")
print("1.더하기","\n","2.뺴기" ,"\n","3.곱하기" ,"\n","4.나누기" ,"\n","5.나머지" ,"\n","6.나가기")
print("============================")

while True:
    send = int(input("원하는 연산자를 입력하세요. : "))
    if send == 6:
        print("계산기를 종료합니다.")
        break
    first = int(input("첫번째 숫자를 입력하세요. : "))
    second = int(input("두번째 숫자를 입력하세요. : "))
    calcu = dict(zip([1,2,3,4,5] , [add(first,second),sub(first,second),mul(first,second),div(first,second),div2(first,second)]))    
    if calcu[send]:
        print(calcu[send])
    else:
        print("잘못입력하셨습니다. 다시 입력해 주세요.")
