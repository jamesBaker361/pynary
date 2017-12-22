import numpy
import pandas
import csv
import string
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

seed = 7
numpy.random.seed(seed)

chars='abcdefghijklmnopqrstuvwxyz. ,0123456789' #39 different characters

arr=[]

for x in range(0,len(chars)):
    arr.append(x)
    
dummy=np_utils.to_categorical(arr)
#print(type(dummy[0]))
data=numpy.ndarray(shape=(119649, 98, 39)) #(119649, 98, 39)
y=numpy.ndarray(shape=(119649, 39))

r=open('commie_three.csv')
reader=csv.reader(r)


startrow=0
for row in reader:
    startrow+=1
    startrow2=0
    blankrow=numpy.ndarray(shape=(98,39))
    for r in row:
        startrow2+=1
        blank=numpy.zeros(39)
        blank[string.find(chars,r)]=1
        if(startrow2==99):
            if(startrow-1<119649):
                y[startrow-1]=blank
        else:
            print('start row:')
            print(startrow)
            blankrow[startrow2-1]=blank
    if(startrow-1<119649):
        data[startrow-1]=blankrow

def lettertovec(r):
    #r is a character string
    #returns a 39 dimensional vector
    blank=numpy.zeros(39)
    blank[string.find(chars,r)]=1
    
def vectoletter(j):
    #j is the 39-d vector
    #returns the corresponding character
    print(j)
    for c in range(0,len(j)):
        if(numpy.float64(j[c])==numpy.float64(1)):
            bitch=c
            return(chars[bitch])

# define baseline model
def baseline_model():
# create model
    model = Sequential()
    model.add(Dense(98, input_dim=39, activation='relu'))
    model.add(Dense(39, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=1)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, data[0], y[0], cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))