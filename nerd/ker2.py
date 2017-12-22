

import numpy
import pandas
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

dataframe=pandas.read_csv("iris.csv",header=None)
dataset=dataframe.values
print(dataframe)

X = dataset[:,0:4].astype(float)
Y = dataset[:,4]

encoder = LabelEncoder()
encoder.fit(Y)
print(encoder)
encoded_Y = encoder.transform(Y)
print(encoded_Y)

dummy_y = np_utils.to_categorical(encoded_Y)
print(dummy_y)

def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(4, input_dim=4, kernel_initializer='normal', activation='relu'))
    model.add(Dense(3, kernel_initializer='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

c=baseline_model().fit(X,dummy_y)

estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=1)
print(estimator)

kfold = KFold(n_splits=10, shuffle=True, random_state=seed)

results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

model.predict([1,.5,.5,.5])

