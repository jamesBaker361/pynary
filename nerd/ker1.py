from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

data=numpy.loadtxt('data.csv',delimiter=',')
X = data[:,0:8]
Y = data[:,8]
print(Y)

model=Sequential()

model.add(Dense(12, input_dim=8,activation='relu'))
model.add(Dense(8,activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X,Y,epochs=35,batch_size=10)

scores = model.evaluate(X, Y)
print("model.metrics_names[1] ",model.metrics_names[1])
print("scores[1]*100", scores[1]*100)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

pred = model.predict(X)
print(pred)