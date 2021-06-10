'''
# 실력 확인 연습문제

# 1번
hour , min , sec = map(int,input("시간을 입력하세요. : ").split(":"))
print("시 :" , hour)
print("분 :" , min)
print("초 :" , sec)

#2번
국어 , 영어 , 수학 , 과학 = map(int , input("점수 평균 계산기 : ").split(":"))
sum = 국어 + 영어 + 수학 + 과학
avr = sum / 4 
print("점수 평균은" , float(avr), "입니다.")

#3번
국어 , 영어 , 수학 , 과학 = map(int , input("점수 평균 계산기 : ").split(":"))
sum = 국어 + 영어 + 수학 + 과학
avr = sum / 4 
print(국어 , 영어 , 수학 , 과학 , sep="+")
print("총 합은" , sum , "입니다.")

#4번
year = 2019
month = 1
day = 31
hour = 10
minute = 33
second = 57
print("실행 결과 1:")
print(year , month , day , sep="/" , end=" ")
print(hour , minute , second , sep=":")
'''

#and 연산자는 양측 값이 모두 성립해야 True 한쪽만 성립시 False
print(True and "python") #"python"
print("python" and True) #True
print("python" and False) #False

#and 연산은 선두값이 True이면 후미값으로 판단을 하여 결과는 후미값으로 아웃풋을 내준다.
print(False and "python") #선두가 False 당연히 False
print(0 and "python") #선두가 0 결과 = 0

#or 연산자는 비교대상 중 하나라도 True라면 True 
print(True or "python") #True
print("python" or True) #"python"
print("Fasle" or "python") #False 
print(0 or False) #False 

korean = 92
english = 47
mathematice = 86
science = 81
print(korean >= 50 and english >= 50 and mathematice >= 50 and science >= 50)

kor , eng , mat , sci = map(int , input("").split(":"))
print(kor >= 90 and eng > 80 and mat > 85 and sci >= 80)

# 문자열 
print('hello python')
hello = "Hello python"
print(hello)

hello = '''Hello , world!
안녕하세요.
python입니다.'''
print(hello)

s = "Python isn't difficult"
s1 = 'He said "python is easy"'
print(s)
print(s1)

single_quote = ''' "안녕하세요."
'파이썬' 입니다. '''
double_quote = """"Hello"
'python'"""
double_quote2 = """Hello , 'python'"""
print(single_quote)
print(double_quote)
print(double_quote2)

s = '''"Python is a programing language that lets you work quikckly
and 
intergrate systems morer effecitvely"'''
print(s)

# list 자료형 
a = [38 , 21 , 53 , 62 , 19]
print(a)

person = ["David" , 49 , 173.3 , True]
print(person)

a = []
print(a)
b = list()
print(b)

a = list(range(10))
print(a)

b = list(range(5,12))
print(b)

c = list(range(-4 , 10 , 2))
print(c)

d = list(range(10,0,-1))
print(d)

# 프로그래밍 오류를 잡을 수 있어야 하고 디버깅을 잘 할줄 알아야 한다.

print(list(range(0 , 11)))
print(list(range(0 , 13 , 2)))
print(list(range(13 , 2 , -2)))
print(list(range(-8 , 10 , 2)))
print(list(range(-100 , 101 , 50)))

# 튜플
a = (38 , 21 , 53, 62 , 18)
print(type(a))

'''type함수를 이용하는 습관을 들이는게 후에 좋다.'''

person = ("james" , 17 , 175.3, True)
print(person)

'''요소가 1개인 튜플은 ()안에 하나의 값 입력 후 콤마 기입'''
a = (38,)
b = (38)
print(type(a)) #turple
print(type(b)) #int

a = tuple(range(1,11, 2))
print(a)

'''tuple와 list는 서로 형변환 가능'''
a = (1,2,3)
print(list(a))

''' list , tuple의 문자열'''
a = list("Hello")
print(a)

b = tuple("Hello")
print(b)

'''리스트와 튜플의 변수의 개수는 엘리먼트의 개수와 같아야 매치가 된다.'''
a , b ,c = [1,2,3]
print(a,b,c)

d, e ,f = (4,5,6)
print(d,e,f)

''' 리스트 언팩킹 = 리스트와 튜플의 요소를 여러개의 변수에 할당하는것'''
x = [1,2,3]
a , b ,c = x 
print(a,b,c)

y = (4,5,6)
d , e, f = y
print(d,e,f)


a = input().split()
x, y = a
print(x,y)

''' 리스트와 튜플의 패킹은 변수에 리스트와 튜플을 할당하는것''' 
a = list(range(5 , -10 , -2))
print(a)

''' tuple 사용 응용 '''
a , b , c = map(int , input("숫자를 입력해주세요 : ").split(":"))
x = tuple(range(a , b , c))
print(x)

''' 시퀀스 자료형 = 리스트 , 튜플 , range ,문자열의 공통점 : 연속적인 데이터를 처리한다.
특징 : 공통 동작과 기능을 제공 
객체 : 시퀀스 자료형으로 만든 객체 
요소(element) : 시퀀스 객체에 들어있는 각 값'''

'''특정 값이 있는지 확인하는 방법은 연산자를 활용하면 된다.'''
a = [10,20,30,40,50,60,70,80,90]
print(30 in a)
print(100 in a)
print(100 not in a)
print(30 not in a)

print(43 not in (38 , 76 , 43 ,62 , 19))
print(1 not in range(10))
print("P" not in "Hello, Python")

a = list(range(1, 20 , 2))
print(a)
print(13 not in a)
print(4  not in a)
print(12 not in a)

'''시퀀스 객체 연결하기'''
a = [0, 10, 20, 30]
b = [9, 8 , 7 , 6]
print(a + b)

'''리스트와 튜플을 하나의 형태로 맞추고 더해줄수도 있다.'''
a = [1, 2, 3]
b = (4 ,5)
print(a + list(b))

a = ['사과' , '배' , '귤' , '오렌지'] 
b = ['토마토' , '바나나' , '수박' , '딸기']
c = a + b 
print("사과"  not in c)

'''range는 리스트 또는 튜플로 언팩킹 후 연결이 가능'''
print(list(range(0,10)) + list(range(10,20)))

'''문자열도 연산자로 연결가능'''
a = "Hello," + "world"
print(a)

'''시퀀스 연산자를 특정 횟수만큼 할 수 있는것은 * 연산자를 사용'''
a = [0,10,20,30] * 3
print(a)

print(list(range(0 , 5, 2))* 3)
print("Hello" * 3) 

'''len함수를 사용하여 시퀀스 객체내에 element개수를 구할수 있다. '''
a = [0 , 10, 20, 30, 40, 50, 60, 70, 80 ,90]
b = (0,10,20)
print(len(b))

fru1 = ["사과" , "배" , "귤" , "오렌지"]
fru2 = ["토마토" , "바나나" , "수박"]
print(len(fru1 + fru2))

print(len(range(0, 10 , 2)))
hello = "Hello, world!"
print(len(hello))

'''시퀀스 객체의 시작은 항상 0부터 , index사용하기'''
a = (38 , 21 , 53 , 62 , 19)
print(a[5])
print(a[1])
print(a[2])
print(a[-1])
print(a[-5])

'''index는 앞에서는 0부터 시작 뒤에서는 -1부터 시작한다. '''
a = range(0, 10 , 2)
print(a[2])

hello = "Hello, world!"
print(hello[-5])

a = list(range(1, 21 , 2))
print(a)
print(a[2])

a = list(range(0, 101 , 2))
print(a[-3])

a = [0,1,2,3,4,5,6,7,8,9]
print(len(a) -1)

a = (0) * 5
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
print(a[0])

'''시퀀스의 자료형중에서 튜플 , range , 문자열은 읽기전용이다. <= 변경은 list형만 가능하다.'''
hello = "Hello, world!"
hello[0] = "A"
del hello[2]
print(hello)

'''시퀀스 객체 인덱스 삭제 = del'''
a = [38, 21, 53 , 62 , 19]
del a[2]
print(a)

r = range(0,10,2)
del r[2]
print(r)

'''슬라이스 최고중요!!'''
a = [0,10,20,30,40,50,60,70,80,90]
print(a[2:-1]) # <= 새로운 객체를 만든것은 아니고 a에서 끄집어낸것이다.
print(a[2:8:3]) #<= 슬라이싱의 증가폭을 지정할수 있지만 슬라이스 범위를 벗어나는것은 불가능하다.
print(a[:7]) #<= 시작점을 지정해주지 않으면 리스트의 첫번째 인덱스부터 시작
print(a[7:]) # <= 위와 마찬가지인 개념 리스트의 마지막까지 출력
print(a[:]) #<= 전체 출력
print(a[:7:2]) # <= 시작을 지정해주지 않고 증가폭 사용시 첫번째 인덱스부터 시작
print(a[7::2]) # <= 위와 같은 개념 처음과 증가폭만 지정
print(a[::2]) # <= 리스트 전체를 불러오고 증가폭만큼 출력
'''a[:] == a[::] = 결과가 같음 '''

'''튜플도 슬라이싱 가능!! 작동명령은 리스트의 슬라이싱과 동일'''
a = (0,10,20,30,40,50,60,70,80,90)
print(a[4:7])
print(a[4:])
print(a[:7:2])

'''range 같은 경우는 리스트와 튜플처럼 슬라이싱이 되는것이 아니라 지정된 범위의 숫자를 생성한다.'''
r = range(10)
print(list(r))
print(r[4:7])
print(r[4:])
print((r[:7:2]) #<= 결과를 보고싶다면 list 나 tuple로 언팩킹 후 print!

# 문자열도 슬라이싱이 가능.

hello  = 'Hello, world!'
print(hello[2:9])
print(hello[2:])
print(hello[:9:2]) 

'''시퀸스 객체는 슬라이스로 범위를 지정하여 여러 요소의 값을 할당할 수 있다.'''
a = [0,10,20,30,40,50,60,70,80,90]
a[2:5] = ["a" , "b" , "c"]
print(a)  
'''범위를 지정해서 요소를 할당했을 경우에는 원래 있던 리스트가 변경되며 새 리스트는 생성되지 않음
그 말인 즉슨 a가 새롭게 정의가 되었다는 이야기'''



