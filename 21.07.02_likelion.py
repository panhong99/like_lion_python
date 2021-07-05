import tensorflow.compat.v1 as tf

tf.compat.v1.disable_v2_behavior()

# import numpy as np

# import matplotlib.pyplot as plt
# # 경사하강법을 numpy만으로만 사용한것이 아닌 
# # tensor을 사용하여 경사하강법 코드 작성 

# # 주어진 데이터
# data = [[2,81] , [4,93] , [6,91] , [8,97]]
# # 데이터 찢기 x 값
# x_data = [x_row[0] for x_row in data]
# # 데이터 찢기 y 값
# y_data = [y_row[1] for y_row in data]

# # 기울기 a와 y 절편 b의 값을 임의로 정한다.
# # 단, 기울기의 범위는 0 ~ 10 사이이며 , y 절편은 0 ~ 100 사이에서 변하게 한다.
# a = tf.Variable(tf.random_uniform([1] , 0 , 10 , dtype = tf.float64 , seed = 0))
# b = tf.Variable(tf.random_uniform([1] , 0 , 100 , dtype = tf.float64 , seed = 0))

# # y에 대한 1차 방정식 ax + b 의 식을 세운다.
# y = a * x_data + b

# # 텐서플로 RMSE 함수
# rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))

# # 학습률 값
# learning_rate = 0.1

# # RMSE 값을 최소로 하는 값 찾기
# gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

# # 텐서플로를 이용한 학습
# with tf.Session() as sess:
#     # 변수 초기화
#     sess.run(tf.global_variables_initializer())
#     # 2001번 실행(0번째를 포함하므로)
#     for step in range(2001):
#         sess.run(gradient_decent)
#         # 100번마다 결과 출력
#         if step % 100 == 0:
#             print("Epoch: %f , RMSE = %.04f , 기울기 a = %.4f , y절편 b = %.4f" %(step , sess.run(rmse) , sess.run(a) , sess.run(b)))
            
            
data = [[100 , 20] , [150 , 24] , [300 , 36] , [400 , 47] , [130 , 22] , [240 , 32] , [350 , 47] , [200 , 42] , [100 , 21] , [110 , 21] , [190 , 30] , [120 , 25] , [130 , 18] , [270 , 38] , [225 , 28]]
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

a = tf.Variable(tf.random_uniform([1] , 0 , dtype = tf.float64 , seed = 0))
b = tf.Variable(tf.random_uniform([1] , 0 , dtype = tf.float64 , seed = 0))

# y값 구하기
y = a * x_data + b

# 제곱근 오차 구하기
rmse = tf.sqrt(tf.reduce_mean(tf.square( y - y_data)))

learning_rate = 0.001


tensor_edge = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(100001):
        sess.run(tensor_edge)
        if step % 50000 == 0:
            print("Epoch: %f , RMSE = %.04f , 기울기 a = %.4f , y절편 b = %.5f" %(step , sess.run(rmse) , sess.run(a) , sess.run(b)))
            