class Investment():
    def __init__(self, risk, value, growth):
        self.risk=risk
        self.value=value
        self.growth=growth
        self.quantity=1
        
def calcAvgRisk(arr):
    t=0
    l=0
    for a in arr:
        l=l+1
        t=t+a.risk
    return(t/l)

def calcGrowth(arr, time):
    t=0
    for a in arr:
        z=a.value*a.growth*a.quantity*time
        t=t+z
    return(t)

house = Investment(.5,1000,1.05)
#stock = Investment()
bond = Investment(.25,1000,1.025)

port = [house,bond]

def calcMoney(port):
    m=0
    for p in port:
        amoney= p.value*p.growth*(1-p.risk)*p.quantity
        m=m+amoney 