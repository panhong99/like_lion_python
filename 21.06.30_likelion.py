import numpy as np

# 아래와 같이 리스트를 사용하면 파이썬과 같이 type이 리스트일것 같지만

# numpy를 사용했기 때문에 type는 numpy.ndarray이다.
# np는 numpy의 함수이다. 사용은 np.함수 이런식으로 사용한다.
ar = np.array([0,1,2,3,4,5,6,7,8,9])
print(ar)
ar

# 설명 :

# 단순히 ar을 print하면 리스트만 출력이 되어 type이 리스트라고 착각할수가 있다.

# 하지만 아래에 출력에서 보여지듯 ar을 출력하면 numpy.array로 감싸져 있는

# 리스트의 형태를 확인할 수 있다.

# (tensorflow를 사용할때 type에서 어려움이 많이 있기 때문에 type를 수시로 확인해주는 습관이 필요하다.)

my_list = [0,1,2,3,4,5,6,7,8,9]
ar1 = np.array(my_list )
print(ar)
ar

# 설명 :

# 아래와 같이 my_list와 ar의 type는 각각 리스트와 numpy.array로

# type이 다른것을 확인할수 있다.

print(type(my_list))
print(type(ar))

data = [0,1,2,3,4,5,6,7,8,9]
data1 = list(range(10))
print(data)
print(data1)

# for 반복문을 아래와 같이 사용할 수 있다.
answer = []
for di in data:
    answer.append(2 * di)
answer

# 하지만 백터화 연산을 사용하면 다음과 같이 for반복문 없이 한 번의 연산으로 할 수 있다. 계산 속도도 반복문을 사용할때 보다 횔씬 빠르다.

x = np.array(data) # <= 리스트형태인 data를 np.array로 형태를 변경해준다.
print(x)

# np.array로 형태를 변경해줌으로서 for문을 사용하지 않고도 연산이 가능하다.
print(x * 2) 

# 백터화 연산은 논리 연산을 포함한 모든 종류의 수학 연산에 대해 적용된다.
# 선형 대수에 적용되는 벡터화 연산에 대해서는 나중에 보다 자세히 설명한다.

a = np.array([1,2,3])
b = np.array([10,20,30])

## Numpy Array의 벡터화 연산 
(2 * a) + b

### 리스트의 연산과 비교
list_a = [1,2,3]
list_b = [10,20,30]
2 * list_a + list_b

# array의 내에 인스턴스들을 인지하고 a == 2 라는 bool연산식을 작성했을때 아래와 같은 내용이 출력된다.(단순히 T

a = np.array([1,2,3])
print(a) 
print(a == 2)  # a == 2라는 연산식이 성립한 인스턴스만 True를 반환 나머지는 False

b = np.array([10,20,30])
print(b)
print(b > 10)  # 마찬가지로 b > 10 이라는 연산이 성립되는 경우만 True 출력

# a(0) , b(0) 이런식으로 두개의 변수의 인덱스를 하나로 묶어서 논리연산 하는것 또한 가능하다.

print((a == 2) & (b > 10)) # & 논리연산 
print((a == 2) | (b > 10)) # or 논리연산

c = np.array([[0,1,2] , [3,4,5]]) # 2차원 array
print(c)
c

# 2차원 배열의 행과 열의 개수는 다음처럼 구한다.

#행의 개수 2차원 요소의 개수 (바깥 array의 객체의 개수)
print(len(c))

#열의 개수 1차원 요소의 개수 (안쪽 array의 객체의 개수)
print(c[0])
print(len(c[0]))

# 2차원 array 만들기
array = np.array([[10,20,30,40] , [50,60,70,80]])
print(array)

# 3차원 array 만들기

d = np.array([[[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]],
            [[11,12,13,14],
            [15,16,17,18],
            [19,20,21,22]]])
print(d)

d1 = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

d2 = [[11,12,13,14],
     [15,16,17,18],
     [19,20,21,22]]

d = np.array([d1,d2])

print(d)

# 3차원 배열길이 , 2차원 배열길이 , 1차원 배열길이
print(len(d)  , len(d[1]) , len(d[0][0]))

# 배열의 차원 및 크기를 구하는 더 간단한 방법은 배열의 ndim속성과 shpae 속성을 이용하는 것이다.

# ndim 속성은 배열의 차원
# shape 속성은 배열의 크기를 반환한다. = (len)

a = np.array([1,2,3])
print(a)
print(a.ndim)
print(a.shape)

c = np.array([[0,1,2] , [3,4,5]])
print(c)
print(c.ndim)
print(c.shape)

# 출력결과를 확인하면 3 , [2,3,4] 가 출력이 되는데
# 3은 3차원 배열이라는 뜻이고 [2,3,4]는 4개의 객체를 갖고 있는
# array 3개가 하나의 덩어리이고 그 덩어리가 2개가 있다는 뜻임.

d = np.array([[[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]],
             [[11,12,13,14],
             [15,16,17,18],
             [19,20,21,22]]])
print(d)
print(d.ndim)
print(d.shape)

# 다차원 배열일때 원하는 인스턴스를 가져오려면 리스트에서는 [][] 형태를 사용해야 한다.
# 하지만 array에서는 ,(콤마)로 구분하여 원하는 인스턴스를 가져올 수 있다.

a = np.array([[0,1,2] , [3,4,5]])
print(a)
print(a[0,0])
print(a[0,1])

## 배열 슬라이싱 

a = np.array([[0,1,2,3],
             [4,5,6,7]])
print(a)

print(a[0 , :]) # 첫번째 행 전체
print(a[ :, 1]) # 두번째 행 전체
print(a[1 , 1:]) # 두번째 행에 두번째 열부터 끝까지
print(a[:2 , :2]) # 두번째 행까지 그리고 두번째 열까지

m = np.array([[0,1,2,3,4],
             [5,6,7,8,9],
             [10,11,12,13,14]])
print(m)
print(m[1,2])
print(m[2,2])
print(m[1 , 1:3])
print(m[:2 ,-2:])

# np.array로 정수가 담겨진 array와 bool 연산이 담겨진 array를 작성하고 a[ldx]라는 표현을 사용하게 되면 bool연산 array에서 True로 지정해진 인덱스의 위치한 "a" array의 정수가 출력이 된다.
a = np.array([0,1,2,3,4,5])
ldx = np.array([True , False , True ,False , True , False])
print(a[ldx])
print(np.array([0,1,2])[np.array([True , False , True])])

# 간단한 연산 a % 2 나머지를 출력

print(a)
print(a % 2)

# 연산이 성립하면 True , 아님 False
print(a % 2 == 0)

# 연산이 성립하는 인스턴스만 출력
print(a[a% 2 == 0])

# 위와 같이 numpy 모듈은 굳이 반복문이나 조건물을 일일이
# 작성해줄 필요없이 한줄 작성으로도 표현이 가능하다.
# ldx를 a에 대입시키면 해당되는 인덱스의 값들이 출력된다.
a = np.array([11,22,33,44,55,66,77,88,99])
ldx = np.array([0 , 2, 4, 6, 8])
print(a[ldx])

# a.array에 크기에 상관없이 해당되는 인덱스의 값을 출력

ldx = np.array([0,0,0,0,1,1,1,1,1,2,2,2,2])
print(a[ldx])

a = np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]])
print(a)

# 슬라이싱을 이용한 2차원 array 내에서 원하는 값 출력
print(a[: , [True , False , False , True]])

# 행의 순서 바꾸기
print(a[: , [2,0,1]]) # 인스턴스들의 인덱스가 변경 ex) 1,2,3 = 3 , 1, 2
print(a[[2,0,1] , :]) # 행의 위치가 변경 

# r변수에 range로 값을 저장하고
# x변수에 np.array를 이용해 array로 저장
r = range(1 , 21)
x = np.array(r)
print(x)

# 3의 배수를 찾기 , 간단하게 연산을 array연산을 이용해서 표현
print(x[x % 3 == 0])

# 4로 나누면 1이 남는수
print(x[x % 4 == 1])

# 3으로 나누어지고 4로 나누면 1이 남는수
# 간단하게 & 연산을 이용해서 표현했다.
print(x[(x % 3 == 0)&(x % 4 == 1)])

# array명령으로 배열을 만들때 자료형을 명시적으로 작용하려면 dtype 인수를 사용한다. 만약 dtype인수가 없으면 주어진 데이터를 지정할 수 있는 자료형을 스스로유추한다. 만들어진 배열의 자료형을 보려면 dtype속성을 본다.
x = np.array([1,2,3])
print(x)
print(x.dtype)

x = np.array([1.0 , 2.0 ,3.0])
print(x.dtype)

x = np.array([1,2,3.0])
print(x)
print(x.dtype)

x = np.array([1,2,3] , dtype="f") #dtype접두사를 후미에 장착
print(x.dtype)

print(x[0] + x[1])
x = np.array([1,2,3] , dtype = "U") #Unicode = 문자로표현
print(x.dtype , x)    # 하단에 출력결과를 보면 문자열로 변형된 형태를 확인가능
print(x[0] + x[1]) # 문자열

np.array([0,1,-1,0]) / np.array([1,0,0,0])
np.log(0)  # 밑수가 1인 로그함수
np.exp(-np.inf)
np.exp(1) # 지수함수의 e값과 동일 (잘으 모르겠지만....)

a = np.zeros(5)
print(a)

# (2,3)을 작성해주면 다차원 배열이 만들어 진다.
# (3개의 인스턴스를 보유한 array 2개 = 2차원 리스트)
b = np.zeros((2,3))
print(b)

# dtype인수를 후미에 명시하면 해당 자료형 원소를 가진 배열을 만든다.
c = np.zeros((5,2) , dtype = "i")
print(c)

# dtype로 형태를 문자열로 변환해주고 배열에 인스턴스로 지정해준다.
d = np.zeros(5 , dtype = "U4") # unicode 4글자
print(d)    # 4글자인 이유는 단순히 U4이기 때문 U3을 하면 3글자

d[0] = "abc"
d[1] = "abcd"
d[2] = "ABCDE"
print(d)

# 0이 아닌 1로 초기화된 배열을 생성하려면 ones명령을 사용한다.

# 4개의 객체를 가진 배열3개를 한 묶음으로 2개 출력
e = np.ones((2,3,4) , dtype = "i8")
print(e)

# e와 같은 형식으로 출력을 하지만 f형태로 출력
f = np.ones_like(e , dtype = "f")
print(f)

# e == ones인데 f1은 zeros로 지정을 해주고 형태는 e와 같은 형태로 출력
f1 = np.zeros_like(e)
print(f1)

# 배열의 크기가 커지면 배열을 초기화하는데도 시간이 걸린다. 이 시간을 단축하려면 배열을 생성만 하고 특정한 값으로 초기화를 하지 않는 empty 명령을 사용할 수 있다.

# 오버플로우 = 내가 사용하는 영역을 초과한다.

g = np.empty((4,3))
print(g)

# %%time # <= 해당 셀이 실행되는 속도를 출력해준다.
h = np.empty((10000 , 10000))

# %%time 
m = np.ones((10000,10000))
# %%
# %%time 
m = np.zeros((10000 , 10000))

# arange 명령은 numpy버전의 range명령이라고 볼 수 있다. 특정한 규칙에 따라 증가하는 수열을 만든다.
print(np.arange(10))
print(np.arange(3 ,21 , 2))
print(np.array([np.arange(-10 , 12 , 2)]))
print(np.array([np.arange(7 , -9 , -3)]))
print(np.arange(1.7 , 10.8 , 1.5))

print(np.linspace(0, 100, 5)) # 시작 , 끝(포함) , 갯수
# 출력결과를 보면 마지막 숫자를 총 5개로 나누었다.

print(np.linspace(0,10,10, endpoint = False))  #endpoint = False or True
# endpoint는 마지막수를 포함하지 않고 출력하라는 의미

print(np.linspace(0,10,10, endpoint = True)) # 0,10 포함 10개 구간으로
print(np.linspace(0,10,0))  # endpoint가 생략되면 endpoint=True(default)
print(np.linspace(1,50)) # 갯수 생략시 50개)

print(np.logspace(1,4,4)) # 10 ** 1 , 10 ** 2 , 10 ** 
print(np.linspace(0.1 , 1.0 , num = 10))


print(np.logspace(0.1 , 1.0 , num = 10)) # 10 ** 0.1 , 10 ** 0.2 이런식으로 연산을 한 값을 출력하는것이다.)
print(10 ** 0.1  , 10 ** 0.2 , 10 ** 0.3 , 10 ** 0.4 , 10 ** 0.5)
print(10**np.linspace(0.1 , 2.0 , 20))
print(np.logspace(0.1 , 2.0 , 20))
# 2차원 배열의 전치 연산은 행과 열을 바꾸는 작업 (T속성으로 구할 수 있다.) 메서드가 아닌 속성이라는 점에 유의한다.
A = np.array([[1,2,3] , [4,5,6]])
print(A , A.shape)
print(A.T) # 파이썬 함수의 zip과 같은것 같다.

a = np.arange(12)
print(a)
b = np.arange(12).reshape(3,2,2)
print(b)
# reshape를 해주면 2개의 객체를 가진 리스트 2개를 2개씩 묶어서 3개 출력
# 이때 객체의 개수와 reshape의 개수가 틀리면 에러가 발생한다.

print(b.ndim)
print(b.shape)

# 사용하는 원소의 갯수가 정해져 있다면 reshape 명령의 형태 튜플의 원소 중 하나는 -1이라는 숫자로 대체할 수 있다.
ar = a.reshape(3,-1) # -1을 매개변수로 작성해주면 에러가 나야 하지만
# -1을 자연스레 4로 대처해주어 코드가 작동이 된다.
print(ar)

print(a.reshape(3,-1).shape) # 위의 코드의 이유를 보여주고 있다.
# shape를 해주면 -1 이 4로 바뀐것을 확인할 수 있다.

b = a.reshape(2,2,-1) # 아래에서 확인할 수 있는것과 같이 
# -1을 작성해주면 b.shape의 값으로 reshape를 해준다.
print(b)
print(b.shape)

c = a.reshape(2, -1 , 2) # 마찬가지 
print(c)
print(c.shape)

print(b) # flattem은 reshape를 해서 다차원 배열로 바뀐 변수를 
# 다시 1차원 배열로 전환시켜주는 변수이다.
print(b.flatten())

print(b.ravel())  #ravel함수 또한 1차원 배열로 반환)

# 다 같은것을 표현하는 것 같아도 다 다른 표현이다.¶

x = np.arange(6)
print(len(x) , x.ndim , x.shape)

x1 = x.reshape(1,6)
print(x1 , len(x1) , x1.ndim , x1.shape)

x2 = x.reshape(6,1)
print(x2 , len(x2) , x2.ndim , x2.shape)

print(x.reshape(6,) == x.reshape(1,6))
print(x.reshape(6,) is x.reshape(1,6))
print(x.reshape(2,3) == x.reshape(3,2))

number = np.arange(11 , 31)
print(number.reshape(4,5))

number = np.arange(3.3 , -8.3 , -0.5)
print(number.reshape(6,4))

# 배열 연결
# hstack
a1 = np.ones((2,3))
print(a1)

a2 = np.zeros((2,2))
print(a2)

a3 = np.arange(10,70,10).reshape(2,3)
print(a3)

print(np.hstack([a1,a2,a3])) # 전체 2차원이므로 각 차원끼리 더하기

b1 = np.ones((2,3))
print(b1)

b2 = np.zeros((3,3))
print(b2)

print(np.vstack([b1 , b2]))

cs1 = np.array([1,2,3])
cs2 = np.array([10,20,30])
print(np.column_stack([cs1 , cs2])) # 파이썬의 zip함수 느낌 
#1차원 요소들의 2개가 합쳐지고 합쳐지는 개수만큼 2차원 요소가 

c1 = np.ones(3)
print(c1)
print(c1.shape)

c2 = np.zeros(3)
print(c2)

print(np.dstack([c1,c2])) #3차원 배열 생성하는듯

c3 = np.ones((3,4))
print(c3)

c4 = np.zeros((3,4))
print(c4)

print(np.dstack([c3,c4]))

print(np.dstack([c1,c2]).shape)

a = np.zeros((3,3))
print(a)

b = np.ones((3,2))
print(b)

c = np.arange(10 , 151 ,10 ).reshape(3 , 5)
print(c)

# hstack = 가로 , vstack = 세로 (순서대로 블록쌓기) , dstack = 두개의 배열이 있을때 같은 인덱스요소끼리 묶어서 세로로 출력 (색깔맞춰서 블록쌓기)

x1 = np.hstack([a,b])
c1 = np.vstack([x1 , c])
c2 = np.vstack([c1 , c1])
print(c2)

a = np.arange(1,101).reshape(20,5)
b = np.arange(201,401,2).reshape(20,5)

print(np.savetxt("/Users/panhong/Downloads/ThoraricSurgery.csv" , a , fmt = "%d" , delimiter = " , "))
print(np.savetxt("/Users/panhong/Downloads/ThoraricSurgery.csv" , a + b , fmt = "%d" , delimiter = " , "))

print(a)

read_a = np.loadtxt("/Users/panhong/Downloads/ThoraricSurgery.csv" , delimiter = " , " , skiprows = 1 , dtype = "int")
print(read_a)

read_b = np.loadtxt("/Users/panhong/Downloads/ThoraricSurgery.csv" , delimiter = " , " , skiprows = 1 , dtype = "int")
print(read_b)