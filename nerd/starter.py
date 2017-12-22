from keras.models import Sequential
from keras.layers import Dense
import csv
import numpy
# fix random seed for reproducibility
numpy.random.seed(5)

dataset = numpy.loadtxt("pima.csv", delimiter=",")

#print(dataset)
# split into input and output variables
X = dataset[:,0:8]
Y = dataset[:,8]

model= Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=150, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print(scores)