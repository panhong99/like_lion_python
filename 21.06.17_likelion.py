a = [10,20,30,15,20,40]
print(a.count(20)) # <= count함수는 입력된 요소가 리스트내에 몇개나 존재하는지 그 개수를 알려줌

a.reverse() # <= 엘리머트들을 반대로 출력
print(a)

a.sort() # <= 리스트들을 오름차순으로 정리
print(a)

a.sort(reverse=True) # <= 리스트들을 내림차순으로 정리
print(a)

a.sort
print(a[0] , a[-1])

a.clear() # <= 리스트의 모든 엘리먼트들을 제거 
print(a)

del a[:] # <= del은 삭제요소를 지정도 가능하지만 슬라이스를 통해 전체삭제도 가능하다.
print(a)

a = [10,20,30]
a[len(a) : ] = [500] == a.append(500) # <= 시작 인덱스를 기존의 리스트이 길이부터 시작하고 리스트의 끝에서부터 시작하겠다는 뜻임
print(a)             # <= 리스트의 길이를 빈공간으로 하나 늘리고 그 공간에다 원하는값 대입
a[len(a) : ] = [500 , 600] == a.extend([500 , 600]) # <= 리스트를 입력해도 엘리먼트로 변환되서 추가됨
print(a)

a = [0] * 5
b = a # <=  a 를 b에 대입 
print(a)
print(b)
print(a is b)
b[2] = 99 # <= a 와 b 는 같으므로 선두와 같이 값을 변경해주면 a 와 b에 모두 반영됨
print(id(a)) 
print(id(b)) # <= print를 해보면 주소가 같은것을 확인가능함 

b = a.copy()
print(id(a))
print(id(b)) # <= 카피는 복사본을 만든것이므로 a와 같은 리스트를 b가 가지지만 주소를 같지않다.
print(a is b) # <= 주소가 다르기떼문에 False
print(a == b) # <= 주소는 다르지만 겉은 같기때문에 True

for i in [10,20,30,15,20,40]: # <= list에 시퀀스를 직접 만들어서 바로 대입도 가능하다.
    print(i)

a = [10,20,30,15,20,40]

for index , value in enumerate(a): # <= enumerater함수를 사용하면 해당 시퀀스 객체의 인덱스 번호와 value를 가르쳐 준다.
    print(index + 1, value)        # <= enumerater함수를 사용할때는 값을 받느 변수가 1개여도 출력이 가능하다.(tuple형태로 출력)
                                   # <= index값에 + 1을 해주면 보기 편하게 출력이 가능하다.
for index , value in enumerate(a , start = 1): # <= 앞에서 보이듯 enumerate에 start + 1을 하면 인덱스에 자연스레 + 1이 되서 출력된다.
    print(index + 1, value)  

a = [10,20,30,40,20,50,20,30,60,70,20]

for i , j in enumerate(a):
    if 20 == j:               # <= 20이 j와 같다면 조건 충족
        print(i , end=" ")    # <= if문에 성립되는 value에 해당하는 인덱스 값 출력

a = [38 , 21 , 53 , 62 ,19]
i = 0
while i < len(a):
    print(a[i])
    i += 1

max = 0
min = a[0]
for i in a:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)

a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

min(a) # <= 해당 리스트의 최솟값을 출력
max(a) # <= 해당 리스트이 최댓값을 출력

a = [10,10,10,10,10]
sum = 0
i = 0
while i < len(a):
    sum += a[i]
    i += 1
print(sum)

sum(a) # <= 해당 리스트의 모든 엘리먼트들의 합을 구해줌 

No_list = []
i = 1

while i <= 10:
    No_list.append(i)
    i += 1
print(No_list)

i = len(No_list) - 1

while i >= 0:
    if No_list[i] % 2 != 0:
        del No_list[i]
    i -= 1
print(No_list)

No_list.insert(0 , 20)  # 20 삽입
print(No_list)

No_list.remove(20)      # 20 삭제
print(No_list)

print(No_list.index(4)) # 인덱스 찾기

No_list.sort(reverse = True)
print(No_list)

a = [i for i in range(10)] # <= 결과적으로 a 의 엘리먼트들은 i 로 구성되어 진다. 
print(a)                   # <= 리스트의 엘리먼트들은 for문으로 작성하고 변수 i에 저장해준다.

b = list(i for i in range(10)) # <= 순서도는 뒤에서부터 이해하면 편리하다.
print(b)

a = [i for i in range(10) if i % 2 == 0] # <= 순서도는 ranged부터 모든 조건식이 충족되고 나서 출력이 된다고 생각하면 될거같다.
print(a)

b = [6,8,10,12,14]
b = list(i for i in range(6,15) if i % 2 == 0)
print(b)

b = [i+5  for i in range(10) if i % 2 == 1]
print(b)

gugudan = list(i * j for i in range(2,10) for j in range(1,10))
print(gugudan)

a = [1.2 , 2.5 , 3.7 , 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [10,20,30,40,50,60]
a = list(map(str , a))
print(a)

print(list(map(str , "12345")))
print(list(map(float , "12345")))
print(list(map(int , "12345")))

x = input().split()
m = map(int ,x) # <= map함수는 형변환을 간편하게 해줄수 있지만 언팩킹을 하지않는다면 소용이 없다.
a , b = m       # <=  a , b로 map의 객체를 언팩킹을 해주고 출력을 하면
print(m)        # <= 정상적으로 출력이 가능하다.
print(a,b)


'''튜플은 append같은 더해주거나 pop같은 삭제는 불가능하다.'''
'''읽어오는 것만 가능하다.'''

a = (38, 21, 53, 62, 19, 53)
print(a.index(53))
# a = (10,20,30,15,20,40)
# print(a.count(20))

for i in a:
    print(i , end=" ")
print()

i = 0
while i < len(a):
    print(a[i] ,end=" ")
    i += 1
print()

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

print(i for i in range(10) if i % 2 == 0)  # <= generator는 반복가능한 객체를 돌려주는것으로 만들어 주는것이다.

a = (1.2 , 2.5 , 3.7 , 4.6)
a = tuple(map(int , a)) # <= map으로 형변환을 시켜준 후 tuple의 객체로 만들어주는 과정
print(a)

a = (38, 21, 53, 62, 19, 53)
print(min(a)) # <= 메서드의 사용방법은 리스트와 동일하다.
print(max(a)) # <= 메서드의 사용방법은 리스트와 동일하다.
print(sum(a)) # <= 메서드의 사용방법은 리스트와 동일하다.

'''a 튜플중 길이가 5인것들만 출력'''
a = ["alpha" , "bravo" , "charlie" , "delta" , "echo" , "foxtrot" , "golf" , "hotel" , "india"]

b = tuple(i for i in a if len(i) == 5) 
print(b)    

x = int(input(":"))
y = int(input(":"))
sum = []
for i in range(x , y+1):
    if 1 <= x <= 20 and 10 <= y <= 30:
        total = 2 ** i
        sum.append(total)        
    else:
        print("data error")  

sum.pop(1)
sum.pop(-2)
print(sum)

ai_classes = {
     'class01' : [
                {'name' : '서준', 'age' : 24},
                {'name' : '하준', 'age' : 34},
                {'name' : '도윤', 'age' : 37},
                {'name' : '시윤', 'age' : 19},
                {'name' : '은우', 'age' : 31}
     ],
     'class02' : [
                  {'name' : '지호', 'age' : 34},
                  {'name' : '예준', 'age' : 19},
                  {'name' : '동원', 'age' : 21},
                  {'name' : '민정', 'age' : 22},
                  {'name' : '효주', 'age' : 24}
     ]
 }

for age in ai_classes: # <= age라는 변수에 key값을 저장 
    for i in range(len(ai_classes[age])): # <= 지정된 딕셔너리에 key에 접근을 해서 키 내부에 새로운 딕셔너리 리스트가 있으므로 그 리스트의 개수를 i에 저장
        print(i)
        if ai_classes[age][i]['age'] >= 30: #내부 딕셔너리의 i번째 리스트에 'age'라는 키의 값에 접근해서 키의 value가 30이 넘으면 출력
            print(ai_classes[age][i]['name'] , " : " , ai_classes[age][i]['age'], end=" / ")
# 출력은 if문에 해당하는 리스트의 라인에 'name'라는 키의 value와 'age'라는 키를 가진 value를 출력


'''로또 번호 구하기'''
'''나의 풀이'''
import random 
i = 0
lotto = []
while i <= 7:
    number = random.randrange(1, 51)
    lotto.append(number)
    i += 1
lotto.sort()
print(lotto)

'''정확한 풀이'''
for i in range(10):
    lotto_numbers = []
    while len(lotto_numbers) < 7:
        lotto_number = random.randint(1, 50)
        if lotto_number not in lotto_numbers:
            lotto_numbers.append(lotto_number)
    print(lotto_numbers)
    lotto_numbers.sort()
    print(lotto_numbers)

'''2차원 리스트 (아파트의 동 , 층 ,호 라는 개념으로 접근하면 좋다.)'''
'''리스트[세로인덱스][가로인덱스]'''
'''리스트[세로인덱스][가로인덱스] = 값'''
'''이중 포장되어 있는 상자를 하나씩 차례대로 뜯는다고 생각하면 좋을 것 같다.'''
a = [[10,20],[30,40],[50,60]] # <= 3단지 아파트 중에 선두부터 1단지 , 2단지 ,3단지로 접근

for i in a: 
    for j in i:
        print(j , end= " ")
    print()

for x , y in a:
    print(x , y)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] , end= " ")
    print()

i = 0
while i < len(a):
    x , y = a[i]
    print(x , y)
    i += 1

'''천천히 하면된다. 급할거 하나도 없다.'''
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=" ")
        j += 1
    print()
    i += 1

a = [[1,2,3] , [5,6,7] , [8,9,10] ,[12,13,14]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] , end=" ")
    print()

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j] , end=" ")
        j += 1
    print()  
    i += 1

for aa in a:
    for aaa in aa:
        print(aaa, end=" ")
    print()

'''빈 리스트 만들기'''
a = []

for i in range(10):
    b = []
    a.append(b)
    for j in range(2):
        b.append(0)
print(a)

a = [[0 for j in range(2)] for i in range(3)]
print(a)

a = [[0] * 2 for i in range(3)]
print(a)

x = [3,1,3,2,5]
a = [[0] * i for i in x]
print(a)

a = []
for i in x:
    b = []
    for j in range(i):
        b.append(0)
    a.append(b)
print(a)
