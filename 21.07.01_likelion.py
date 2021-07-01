import numpy as np
x = [2, 4, 6, 8]
y = [81 , 93 , 91 , 97]

mx = np.mean(x) # mean함수는 np함수로서 해당되는 array의 평균을 출력해준다.
my = np.mean(y)

divisor = sum([(mx - i) ** 2 for i in x]) # 기울기 공식의 분모

# def top(x , mx , y , my):
#     d = 0 
#     for i in range(len(x)):
#         d += (x[i] - mx) * (y[i] - my)
#     return d
# dividend = top(x , mx , y , my)

dividend = sum([(x[i] - mx) * (y[i] - my) for i in range(len(x))])
dividend

print("분모" ,divisor)
print("분자" ,dividend)

a = dividend / divisor
b = my - (mx * a)

print("기울기 a = " , a)
print("y절편 b = " , b)

x = [2, 4, 6, 8]
y = [81 , 93 , 91 , 97]

x_sum = np.mean(x) # 평균구하기
y_sum = np.mean(y) 

# 분모
mother = sum([(i - x_sum) ** 2 for i in x]) # 평균에서 평균재료들을 - 한 값에 제곱의 합

#분자
sun = 0
for i in range(len(x)):
    sun += sum([(x[i] - x_sum) * (y[i] - y_sum)])
    
a = sun / mother

b = y_sum - (x_sum * a)

b

print("분자 = " , sun)
print("분모 = " , mother)
print("a = " , a)
print("b = " , b)

MaxSize = 30
Time = [1,2,3,4,5,6,7,8]
Size = [0.2 , 0.3 , 0.5 , 0.6 , 0.9 , 0.95 , 1.1 , 1.5]

tx = np.mean(Time)
sx = np.mean(Size)

mother = sum([(i - tx) ** 2 for i in Time])


sun = 0
for i in range(len(Time)):
    sun += sum([(Time[i] - tx) * (Size[i] - sx)])

sun

a = sun / mother
b = sx - (tx * a)

print("분자 = " , sun )
print("분모 = " , mother )
print("기울기 a = " , round(a ,3) )
print("y절편 = " , round(b,3) )

def size(x):
    v = a * x + b
    return MaxSize if v > MaxSize else round(v , 3)
print("15주 후의 크기 : " , size(15), "cm" )
print("25주 후의 크기 : " , size(25), "cm" )
print("77주 후의 크기 : " , size(77), "cm" )
print("5주차 예상치와 차이 : " , (0.9 - size(5)) , "cm")

x = [2, 4, 6, 8]
y = [81 , 93 , 91 , 97]

x_sum = np.mean(x) # 평균구하기
y_sum = np.mean(y) 

# 분모
mother = sum([(i - x_sum) ** 2 for i in x]) # 평균에서 평균재료들을 - 한 값에 제곱의 합

#분자
sun = 0
for i in range(len(x)):
    sun += sum([(x[i] - x_sum) * (y[i] - y_sum)])
    
a = sun / mother

b = y_sum - (x_sum * a)

b

print("분자 = " , sun)
print("분모 = " , mother)
print("a = " , a)
print("b = " , b)

ab = [3 ,76]

data = [[2,81] , [4,93] , [6,91] , [8,97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

def predict(x):
    return ab[0] * x + ab[1]

#rmse 함수
def rmse(p , a):
    return np.sqrt(((p - a) ** 2).mean())
# rmse 함수를 각 y값에 대입하여 최종 값을 구하는 함수
def rmse_val(predict_result , y):
    return rmse(np.array(predict_result) , np.array(y))
# 예측값이 들어갈 빈 리스트 
predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부한 시간 = %.f , 실제 점수 = %.f , 예측점수 = %.f"
         %(x[i] , y[i] , predict(x[i])))
    
print(predict_result)
print(y)
print("rmse 최종값 : " + str(rmse_val(predict_result , y)))

ab = [0.1756 , - 0.03392]
data = [[1,0.2] , [2,0.3] , [3,0.5] , [4,0.6] , [5,0.9] , [6,0.95] , [7 , 1.1] , [8 , 1.5]]
fish_Time = [i[0] for i in data]
fish_Size = [i[1] for i in data]

def rmse(p , a):
    return np.sqrt(((p - a) ** 2).mean())

def rmse_val(predict_result , y):
    return rmse(np.array(predict_result) , np.array(y))
 
predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("주수 = %.f , 실제 크기 = %.2f , 예측크기 = %.f"
         %(x[i] , y[i] , predict(x[i])))
    
print(predict_result)
print(y)
print("rmse 최종값 : " + str(rmse_val(predict_result , y)))
    