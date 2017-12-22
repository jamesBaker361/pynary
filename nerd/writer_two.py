from twi import chars
import string

t=string.lower(open('splitmfesto.txt','r').read())

k=""

for c in t:
    if (string.find(chars,c)!=-1):
        k=k+c
print(k)

f=open('mfesto.txt','r+')
#print(t)
'''
tok.fit_on_texts(t)

data=[]

for x in range(0,len(t)-101):
    line=[]
    for y in range(0,99):
        #print(t[x+y])
        line.append(t[x+y])
    data.append(line)'''