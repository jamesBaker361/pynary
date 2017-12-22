import csv
import string

def texttocsv(name):
    y=string.lower(open(name+'.txt').read())
    w=open(name+'.csv','w')
    writer=csv.writer(w)
    for c in range(0,len(y)-100):
        row=[]
        for x in range(0,99):
            row.append(y[x+c])
        writer.writerow(row)