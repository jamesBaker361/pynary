class NotNumber(Exception):
    def __init__(self, thing):
        self.thing=thing
    def __str__(self):
        return self.thing+" requires a number input"
    
def check(name, input):
    if type(input) == type(0):
        return True
    else:
        raise NotNumber(name)
        return False