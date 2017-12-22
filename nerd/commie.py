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

# fix random seed for reproducibility
seed = 3
numpy.random.seed(seed)

data= pandas.read_csv('commie.csv',header=None)
dataset = data.values

#X = dataset[:,0:48].astype(float)
#print(dataset.shape)

numbers=numpy.zeros(shape=9998,dtype=int)
#the lowest number is 1, the greatest is 9999

for x in range(1,9999):
    numbers[x-1]=x
    
encoder = LabelEncoder()
encoder.fit(numbers)
encoded_Y = encoder.transform(numbers)
print(encoded_Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(numbers)

print(dummy_y)
'''
Y = dataset[:,48]

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

# encode class values as integers
encoderx = LabelEncoder()
encoderx.fit(X)
encoded_X = encoderx.transform(X)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_x = np_utils.to_categorical(encoded_X)
'''