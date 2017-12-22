import csv

data=[]

t=open('commie.csv')
reader=csv.reader(t)

for row in reader:
    for r in row:
        data.append(int(r))
        
print(len(data))

for d in data:
    if(d==9999):
        print('1 found!!!')