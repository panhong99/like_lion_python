import numpy 
import tensorflow as tf 
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import reuters
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Embedding , LSTM
from tensorflow.keras.callbacks import ModelCheckpoint , EarlyStopping

# seed값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(seed)

(X_train , Y_train) , (X_test , Y_test) = reuters.load_data(num_words = 1000 , test_split = 0.2)

# 데이터 확인하기
# 데이터를 print해보면 이미 시퀀스화 되어있는 모습을 볼 수가 있는데
# 이유는 이미 케라스에서 단어에 대한 전처리를 다 완료 해놓았기 때문이다.
category = numpy.max(Y_train) + 1
print(category , "카테고리")
print(len(X_train) , "학습용 뉴스 기사")
print(len(X_test) , "테스트용 뉴스 기사")
print(X_train[0])

# get_word_index함수를 사용해서 각 단어들과 인덱스를 확인할 수 있음
# 단어의 빈도스가 높을수록 인덱스 번호가 낮음
# 인덱스 번호가 높을수록 해당 문장에서 빈도수가 낮다라고 판단할수 있음
word_to_index = reuters.get_word_index()
print(word_to_index)

# 딕셔너리 생성
index_to_word = {}
# word_to_index = 단어들의 인덱스번호와 단어들이 입력되어 있음 
# key = 단어 , value = 인덱스 번호
for key , value in word_to_index.items():
    # key = 단어 , index_to_word의 value들을 이제는 숫자가 아니라
    # 단어들로 변경시켜줌
    index_to_word[value] = key

# 공백이나 특수문자 없이 출력
# index_to_word = 딕셔너리 형태 
# X_train은 숫자로 되어있으므로 자동적으로 key가 입력이 되어 
# value(단어)들이 공백없이 출력이됨
print("".join([index_to_word[X] for X in X_train[0]]))


# pad_sequence함수는 배열의 길이를 맞춰주는 함수 maxlen = 100이므로
# 한 배열의 길이는 100
# X_train의 단어들을 요소로 삼아서 100개를 가져옴
# 빈도수가 높은 순서대로 100개가 채워짐 
# 인덱스번호가 99번까지가 채워지는것임
x_train = sequence.pad_sequences(X_train , maxlen = 100)
x_test = sequence.pad_sequences(X_test , maxlen = 100)

# padding = 길이를 똑같이 맞춰주는 작업
# pad_sequence가 패딩을 해주는 함수임


# 데이터 전처리
y_train = to_categorical(Y_train)
y_test = to_categorical(Y_test)


# 모델 설정
model = Sequential()
# Embedding층 
# 총 사용하는 단어가 1000개 
# 각각의 단어마다 임베딩 크기를 100개!!
model.add(Embedding(1000 ,100))
# RNN에서 자주사용하는 LSTM을 이용
# 앞전에 사용한 레이어의 영향을 받는부분에 대해서
# 전체에 영향을 다 받는것이 아니라 부분적으로 영향을 받게 해준다.
model.add(LSTM(100 , activation = "tanh"))
model.add(Dense(46 , activation = "softmax"))
# 기울기 손실 때문에 RNN에서는 활성화 함수를 하이퍼블릭 탄젠트를 사용
model.compile(loss = "categorical_crossentropy" , optimizer = "adam" , metrics = ["accuracy"])

es = EarlyStopping(monitor = "val_loss" , patience = 4 , mode = min , verbose = 1)
mc = ModelCheckpoint("best_model.h5" , monitor = "val_acc" , mode = "max" , verbose = 1 , save_best_only = True)

history = model.fit(x_train , y_train , batch_size = 100 , epochs = 20 , validation_data = (x_test , y_test) , callbacks = [es , mc])

print("\nAccuracy : %.4f" %(model.evaluate(x_test , y_test)[1]))

y_vloss = history.history["val_loss"]
y_loss = history.history["loss"]

import matplotlib.pyplot as plt

x_len = numpy.arange(len(y_loss))
plt.plot(x_len , y_vloss , marker = "." , c = "red" , label = "Testset_loss") 
plt.plot(x_len , y_loss , marker = "." , c = "blue" , label = "Trainset_loss") 
plt.legend(loc = "upper right")
plt.grid()
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()

import matplotlib.pyplot as plt
print("뉴스 기사의 최대 길이 : {}".format(max(len(l) for l in X_train)))
print("뉴스 기사의 최대 길이 : {}".format(sum(map(len , X_train)) / len(X_train)))

plt.hist([len(s) for s in X_train] , bins = 50)
plt.xlabel("length of samples")
plt.ylabel("number of samples")
plt.show()

