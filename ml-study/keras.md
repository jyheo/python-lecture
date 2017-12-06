layout: true
.top-line[]

---
class: center, middle

# Keras

---
## Keras 란?
* Keras는 Theano 또는 TensorFlow 또는 CNTK 위에서 동작하는 딥러닝 라이브러리
* convolutional, recurrent networks 모두 지원하고 둘을 결합한 형태도 지원
* Keras는 최대한 쉽고 빠르게 딥러닝 모델을 만들 수 있음
* GPU와 CPU에서 모두 동작함
* MIT 라이선스
* https://keras.io/

---
## 설치
* Theano나 TensorFlow를 먼저 설치해야 함
* 여기에서는 TensorFlow-CPU를 기준으로
	- TensorFlow 설치: https://www.tensorflow.org/install/
	- $ pip install --upgrade tensorflow
* Keras 설치
	- $ pip install keras
* 버전 확인
	-$ python -c "import keras; print(keras.__version__)"
	- Using TensorFlow backend.
	- 2.1.1

---
## 딥러닝 모델 in Keras
* 모델 정의: 시퀀스 생성과 레이어 추가
* 모델 컴파일: loss 함수와 optimizer 지정
* 모델 훈련(fit): 데이터를 이용하여 모델 훈련
* 모델 적용(prediction): 모델에 새 데이터를 입력시켜 예측 결과 출력

---
## 모델 정의
* 레이어(Dense)의 시퀀스(Sequential)
* 입력 레이어(input_dim)
* 레이어의 수는? 연결 방법은? 휴리스틱, trial and error를 통해,
* fully-connected 일 경우 레이어는 Dense 클래스 사용
* Dense 클래스 생성시
	- 첫번 째 인자는 뉴런(노드)의 수
	- init: 웨이트 값 초기화 방법, 디폴트는 uniform(0과 0.05 사이의 값), 다른 것으로 normal(가우시안) 있음
	- activation: 액티베이션 함수, relu, sigmoid 등 사용

```python
# create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

---
## 모델 컴파일
* loss 함수 - 웨이트들을 계산하기 위해
	- binary_crossentropy: logarithmic loss, 바이너리 분류에 사용
	- mean_squared_error, categorical_crossentropy
* optimizer
	- adam: grdient descent 알고리즘
	- sgd: stochastic gradient descent
* metrics
	- accuracy: 정확도

```python
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

---
## 모델 훈련(Fit)
* fit()
* epochs: 반복 횟수
* batch_size: batch_size 샘플 수마다 gradient descent 업데이트 수행(디폴트는 32)

```python
# Fit the model
model.fit(X, Y, epochs=150, batch_size=32)
```

---
## 확인

```python
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

---
## 예측

```python
# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
print(rounded)
```

---
## 실행 결과

```c
768/768 [==============================] - 3s 3ms/step - loss: 10.2464 - acc: 0.3490
Epoch 2/15
768/768 [==============================] - 0s 93us/step - loss: 8.3416 - acc: 0.3516
Epoch 3/15
768/768 [==============================] - 0s 93us/step - loss: 2.4441 - acc: 0.4531

...

Epoch 13/15
768/768 [==============================] - 0s 97us/step - loss: 0.6700 - acc: 0.6224
Epoch 14/15
768/768 [==============================] - 0s 94us/step - loss: 0.6648 - acc: 0.6380
Epoch 15/15
768/768 [==============================] - 0s 102us/step - loss: 0.6599 - acc: 0.6341
768/768 [==============================] - 0s 61us/step

acc: 79.04%
[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,

...

 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
```


---
## 전체 코드


