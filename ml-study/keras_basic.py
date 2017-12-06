from keras.models import Sequential
from keras.layers import Dense
from keras.utils import plot_model
import numpy as np

# fix random seed for reproducibility
np.random.seed(8)

# 1. load pima indians dataset
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]


# 2. create model
## 8 - 12 - 8 - 1
model = Sequential()
model.add(Dense(units=12, input_dim=8, activation='relu'))
model.add(Dense(units=8, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

plot_model(model, to_file='model.png', show_shapes=True)


# 3. Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. Fit the model
model.fit(X, Y, epochs=150)

# 5. evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# 5-2 calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [int(round(x[0])) for x in predictions]
print(rounded)
