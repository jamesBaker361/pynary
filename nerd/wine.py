from keras.models import Sequential
from keras.layers import Dense
import csv
import numpy
# fix random seed for reproducibility
numpy.random.seed(3)

dataset = numpy.loadtxt("winered.csv", delimiter=";")

X = dataset[:,0:11]
Y = dataset[:,11]
print(Y)

model= Sequential()
model.add(Dense(12, input_dim=11, activation='relu'))
model.add(Dense(1, kernel_initializer='truncated_normal',bias_initializer='zeros'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=150, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))