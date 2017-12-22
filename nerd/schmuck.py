from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical as to_categorical

model = Sequential()
model.add(Dense(5,input_dim=100,kernel_initializer="random_normal"))
print(model)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(5, size=(1000, 1))

one_hot_labels = to_categorical(labels, num_classes=5)

model.fit(data, one_hot_labels, epochs=12, batch_size=32)