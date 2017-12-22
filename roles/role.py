class Role():
    def __init__(self):
        self.abilities = [] #abiltiies the current instance does have
        self.potentialabilities = [] #abilities that the class may someday have
        self.maxabil = 5 #maximum amount of abilities this dude can have
    def remove_abil(self, abil):
        self.abilities.remove(abil)
    def add_abil(self, abil):
        self.abilities.append(abil)
    def can_add_abil(self):
        if len(self.abilities) >= 4:
            return True
        else:
            return False