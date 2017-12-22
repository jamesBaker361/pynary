import csv
import numpy
import emoji
from keras.models import Model
from keras.layers import Input, Dense

def main():
	
	inp=numpy.ndarray(shape=(6,))
	outp=numpy.ndarray(shape=(1,))

	with open('in.csv','r') as csvfile:
		reader=csv.reader(csvfile)
		for row in reader:
			inp=numpy.append(inp,numpy.array(row))

	with open('out.csv','r') as csvfile:
		reader=csv.reader(csvfile)
		for row in reader:
			outp=numpy.append(outp,row)

	print(inp)
	print(emoji.emojize(':skull:'))
	print(outp)
if __name__ == '__main__':
	main()