import csv

c=0
d=[]

def avg(r,index):
    x=0
    s=0
    for row in r:
        s=s+1
        x=x+float(row[index])
    return(x/s)

with open('statstwo.csv') as csvfile:
    r = csv.reader(csvfile) #avg labor freedom is 59.4033149171 avg gdp per capita PPP is 14725
    #print(avg(r,1))
    for row in r:
        print(c)
        c=c+1     
        print(row)
        lbf='above'
        gpc='above'
        if(float(row[1])<59.4):
            lbf='below'
        if(int(row[2].translate(None,'$,'))<10112):
            gpc='below'
        d.append([row[0],float(row[1].strip('$')),int(row[2].translate(None,'$,')),lbf,gpc])
    print(d)
with open('statsfinaltwo.csv','wb') as csvfile:
    writer=csv.writer(csvfile)
    for drow in d:
        writer.writerow(drow)