import csv
data=[]
from keras.preprocessing.text import one_hot

import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier

s=open('splitmfesto.txt','r').read()

g=one_hot(s,10000)

for x in range(0,len(g)-51):
    line=[]
    for y in range(0,49):
        print(x+y)
        line.append(g[x+y])
    data.append(line)

with open('commie.csv','r+')as f:
    j=csv.writer(f)
    for row in data:
        j.writerow(row)
"""def baseline_model():
    # create model
    model = Sequential()
    model.add(Embedding(10000, 4, input_length=69))
    
    return model

estimator = KerasClassifier(build_fn=baseline_model, epochs=80, batch_size=200, verbose=1)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))"""