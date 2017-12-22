text=";hnajchfabcdefghijklmnopqrstuvyxyzjknlksdfKLFD"
text=text.lower()
import numpy as np

chars = sorted(list(set(text)))
print("chars",chars)
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

print("indiec_char",indices_char)
print("char_indices",char_indices)

maxlen = 30
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))
print('sentences',sentences)
print("next_chars",next_chars)

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
print("X",X)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
print("y",y)
for i, sentence in enumerate(sentences):
    print("sentence",sentence)
    for t, char in enumerate(sentence):
        print("char",char)
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1
print("X",X)
print("y",y)

from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM
from keras.optimizers import RMSprop

print('Build model...')
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
print('model',model)

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
print(dir(model.outputs))
#print(model.outputs.index(0,0))

import pydot
from keras.utils import plot_model
plot_model(model, to_file='model.png',show_shapes=True)
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot

SVG(model_to_dot(model).create(prog='dot', format='svg'))