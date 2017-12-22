useList = []
class User:
    def __init__(self, nameinp, ageinp):
        self.name = nameinp
        self.age = ageinp
        self.isUser = True
        useList.append(self)
    def printshit(self):
        print("printed shit")
        print(dir())
        print(type(dir()[0]))
uno = User("a","b")
def func():
    n = raw_input("whats your name? ")
    a = raw_input("waht's your age? ")
    u = User(n, a)
    u.printshit()
def makeuser():
    n = raw_input("whats your name? ")
    a = raw_input("waht's your age? ")
    u = User(n, a)
    return u
def getUsers():
    tres = User("a","b")
    ayyy = []
    for w in dir():
        print(w)
    print(dir())
def test():
    makeuser()
    getUsers()
test()
def addtest(num):
    return num + 1
def testobject(ob):
    ob["proppy"]=ob["proppy"]+1
def testUser(use):
    use.name="successful"
def testvar(vari):
    vari = User("a","s")
if __name__ == "__main__":
    import sys
    print("main main main")