import numpy
import pandas
import csv
import string
from keras.models import Sequential
from keras.layers import Dense, Reshape, Flatten
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

seed = 7
numpy.random.seed(seed)

chars='abcdefghijklmnopqrstuv/-wxyz.;() ,0123456789' #41 different characters

dicks=np_utils.to_categorical([10,3,5])

print(dicks)

def getshittwo(q,file):
    data=numpy.zeros(shape=(q, 98,len(chars))) #(119649, 98, )
    data.flags.writeable=True
    y=numpy.zeros(shape=(q,len(chars)))
    y.flags.writeable=True
    r=open(file)
    reader=csv.reader(r)
    startrow=0
    for row in reader:
        startrow+=1
        startrow2=0
        if(startrow-1<q):
            for r in row:
                startrow2+=1
                lorax=string.find(chars,r)
                if(startrow2-1<98):
                    data[startrow-1][startrow2-1]=lorax
                else:
                    y[startrow-1]=lorax
    jnp=np_utils.to_categorical(y,len(chars))
    for d in data:
        d.flags.writeable=True
        d=np_utils.to_categorical(d,len(chars))
        print(d[0])
        print('yeeeeet')
    return(data,jnp)

'''g,j=getshittwo(50,'capital.csv')
print(g)
print(g[0])
print(g[0][0])
print(g[0][0][0])
'''

#print(type(dummy[0]))
def getshit(q,file,start=0):
    data=numpy.ndarray(shape=(q, 98, len(chars))) #(119649, 98, len(chars))
    y=numpy.ndarray(shape=(q, len(chars)))
    r=open(file)
    reader=csv.reader(r)
    startrow=0
    for row in reader:
        if(start<startrow):
            continue
        startrow+=1
        startrow2=0
        blankrow=numpy.ndarray(shape=(98,len(chars)))
        for r in row:
            startrow2+=1
            blank=numpy.zeros(len(chars))
            blank[string.find(chars,r)]=1
            if(startrow2==99):
                if(startrow-1<q):
                    y[startrow-1]=blank
            else:
                blankrow[startrow2-1]=blank
        if(startrow-1<q):
            data[startrow-1]=blankrow
    return(data,y)
g,j=getshit(50000,'commie_three.csv')
#data,y=getshit(119649,'commie_three.csv')
#data,y=getshit(100,'capital.csv')
def lettertovec(r):
    #r is a character string
    #returns a len(chars) dimensional vector
    blank=numpy.zeros(len(chars))
    blank[string.find(chars,r)]=1
    
def vectoletter(j):
    #j is the len(chars)-d vector
    #returns the corresponding character
    print(j)
    for c in range(0,len(j)):
        if(numpy.float64(j[c])==numpy.float64(1)):
            bitch=c
            return(chars[bitch])

model=Sequential()
model.add(Dense(40,input_shape=(98,len(chars)),use_bias=True,activation='relu'))
model.add(Flatten())
model.add(Dense(len(chars),activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
model.fit(g, j, batch_size=248, epochs=3, verbose=1)
h,k=getshit(50000,'commie_three.csv',start=60000)
score=model.evaluate(h,k,batch_size=64)
print(type(score))
for s in score:
    print(s)

text=" "
for m in model.predict(h):
    for r in range(0,len(m)):
        if(m[r]==max(m)):
            print(r)
            text=text+(chars[r])
print(text)
