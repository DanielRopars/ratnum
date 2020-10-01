class rat:
    num=0
    den=0
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.ratnum = self.num/self.den
    def __float__(self):
        return self.ratnum
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self, other):
        addednum = (self.num*other.den)+(other.num*self.den)
        addedden = (self.den*other.den)
        return rat(addednum,addedden)
    def __sub__(self,other):
        subnum = (self.num*other.den)-(other.num*self.den)
        subden = (self.den*other.den)
        return rat(subnum,subden)
    def __mul__(self,other):
        mulnum = self.num*other.num
        mulden = self.den*other.den
        return rat(mulnum,mulden)
    def __truediv__(self,other):
        divnum = self.num*other.den
        divden = self.den*other.num
        return rat(divnum,divden)
half = rat(1,2)
quart = rat(1,4)
def grat():
    one = rat(1,1)
    gratnum = rat(1,1)
    for i in range(1,100):
        gratnum = one + rat(one.ratnum,gratnum.ratnum)
    return str(float(gratnum))
def prat():
    one = rat(1,1)
    two = rat(2,1)
    three = rat(3,1)
    six = rat(6,1)
    pratnum = rat(6,1)
    for i in range(1,100000):
        square = (three*three)
        pratnum = six + rat(square.ratnum,pratnum.ratnum)
        three = three + two
    threeprat = 3 + (1/pratnum.ratnum)
    return str(threeprat)
print(prat())
