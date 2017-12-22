import numpy
import pandas
import csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

h=open('splitmfesto.txt').read()

chars='abcdefghijklmnopqrstuvwxyz. ,0123456789'

arr=[]

for x in range(0,len(chars)):
    arr.append(x)

dummy=np_utils.to_categorical(arr)

data=[]

com=open('commie_three.csv','r+')
writer=csv.writer(com)

for y in range(0, len(h)-100):
    row=[]
    for j in range(0,99):
        row.append(h[j+y])
    data.append(row)
    writer.writerow(row)
    

'''
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(50, input_dim=39, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model'''