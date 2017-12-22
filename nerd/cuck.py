import math
import numpy

def sigmoid(x):
    return(1/(1+math.exp(x)))

def sigmoidDrv(x):
    return(sigmoid(x)*(1-sigmoid(x)))

def randVal():
    return(numpy.random.normal(0,.01))

def arrayRand(w):
    for index,x in numpy.ndenumerate(w):
        w[index]=randVal()

def arrayClear(w):
    for index,x in numpy.ndenumerate(w):
        w[index]=None
        
w=numpy.ndarray(shape=(3,4,4)) #w[l,j,i]
b=numpy.ndarray(shape=(2,4)) #b[l,i]
n=numpy.ndarray(shape=(4)) #i dont remeber waht this is
a=numpy.ndarray(shape=(3,4)) #a[l,i]
z=numpy.ndarray(shape=(3,4)) #z[l,i]
e=numpy.ndarray(shape=(3,4)) #e[l,i]

arrayRand(w)
arrayRand(b)
arrayClear(a)
arrayClear(z)
arrayClear(e)

d=[.01,.02,.03,.04]
yi=[1,0,0,0]

def getActiv(l,i,x=d,f=sigmoid,z=z,a=a,layer=3,imax=4,w=w):
    #print(a)
    if a[l,i] == a[l,i]:
        return(a[l,i])
    if l == 0:
        #print("a neuron "+ str(i)+" in layer "+str(l))
        #print(x[i])
        return(x[i])
    else: 
        q=b[l-2,i];
        for h in range(imax):
            q=q+(w[l-1,h,i]*getActiv(l-1,h,x=x))
        #print("a neuron "+ str(i)+" in layer "+str(l))
        #print(f(q))
        return(f(q))

#def getError(l,i,x=d,y=1,f=sigmoid)
def getZ(l,i,x=d,f=sigmoid,z=z,a=a,imax=4,w=w):
    #print(z)
    if z[l,i] == z[l,i]:
        return(z[l,i])
    if l == 0:
        #print("z neuron "+ str(i)+" in layer "+str(l))
        #print(x[i])
        return(x[i])
    else: 
        q=b[l-2,i];
        for h in range(imax):
            q=q+(w[l,h,i]*getActiv(l-1,h,x=x))
        #print("z neuron "+ str(i)+" in layer "+str(l))
        #print(q)
        return(q)

def fillZ(z=z,getZ=getZ):
    for index,x in numpy.ndenumerate(z):
        #print(index)
        z[index]=getZ(index[0],index[1])
        #index[0] = l (goes from 0 to 2)
        #index[1] = i (goes from 0 to 3)
        
def fillActiv(a=a,getActiv=getActiv):
    for index,x in numpy.ndenumerate(a):
        a[index]=getActiv(index[0],index[1])
        
def getErr(l,i,x=d,y=yi,layers=3,e=e,fDrv=sigmoidDrv,imax=4):
    if e[l,i] == e[l,i]:
        return(e[l,i])
    else:
        if l ==layers-1:
            return(.5)
            return(-1*(y[i]-getActiv(l,i,x=x))*fDrv(getZ(l,i,x=x)))
        else:
            c=numpy.float64(0.0)
            for g in range(imax):
                c=c+(w[l,g,i]*numpy.float64(getErr(l+1,g)))
            return(c*(fDrv(getZ(l,i))))

def fillErr(e=e,getErr=getErr):
    for index,x in numpy.ndenumerate(e):
        e[index]=getErr(index[0],index[1])

fillZ()
print(e)
fillActiv()
fillErr()
print(e)