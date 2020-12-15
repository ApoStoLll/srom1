from number import Number
from mapper import Mapper
from lab import *

def gcd(num1, num2): #bin
    print(num1, num2)
    if not compare(num1, num2):
        num1, num2 = num2.copy(), num1.copy()
        # a = num1.copy()
        # num1 = num2.copy()
        # num2 = a

    d = [1]
    while num1[-1] == 0 and num2[-1] == 0:
        
        num1 = div(num1, [1,0])[0]
        num2 = div(num2, [1,0])[0]
        #print(num1, num2)
        d = Mapper.mapDecToBin(mul(d, [1,0], 2).numDec)
    while num1[-1] == 0:
        num1 = div(num1, [1,0])[0]
        if num1[0] == None:
            num1.append(0)
    while num2 != [0]:
        while num2[-1] == 0:
            num2 = div(num2, [1,0])[0]
            if num2[0] == None:
                num2.append(0)
        if compare(num1, num2):
            a = num1.copy()
            num1 = num2.copy()
            num2 =  Mapper.mapDecToBin(sub(a, num2, 2).numDec)
        else:
            num2 = Mapper.mapDecToBin(sub(num2, num1, 2).numDec)
        if len(num2) == 0:
            num2.append(0)
    d = mul(d, num1, 2)
    return d #Number

def lcm(num1, num2): #bin
    if not compare(num1, num2):
        x = num1.copy()
        num1 = num2.copy()
        num2 = x
    gcdNum = gcd(num1.copy(), num2.copy())
    num1 = div(num1, Mapper.mapDecToBin(gcdNum.numDec))[0]
    num3 = mul(num2, num1, 2)
    return num3 #Number

def barret(x, n, m):
    q = killDigits(x.copy(), len(n) - 1)
    q = mul(q, m, 2).numBig
    q = killDigits(x.copy(), len(n) + 1)
    r = sub(x.copy(), mul(q.copy(), n.copy(), 2), 2).numBig
    return div(x,n)[1]

def killDigits(x, k):
    if x != None:
        return x
    for i in range(0, k):
        del x[-i+1]
    return x

def addMod(num1, num2, modBin, beta):
    num4 = add(num1, num2, beta)
    num4Bin = Mapper.mapDecToBin(num4.numDec)
    m = 2 ** len(num4Bin)
    mBin = Mapper.mapDecToBin(m)
    m = div(mBin, modBin)[0]
    num5 = barret(num4Bin, modBin, m)
    return num5 #Bin

def subMod(num1, num2, modBin, beta):
    num4 = sub(num1, num2, beta)
    num4Bin = Mapper.mapDecToBin(num4.numDec)
    m = 2 ** len(num4Bin)
    mBin = Mapper.mapDecToBin(m)
    m = div(mBin, modBin)[0]
    num5 = barret(num4Bin, modBin, m)
    return num5 #Bin

def mulMod(num1, num2, modBin, beta):
    num4 = mul(num1, num2, beta)
    num4Bin = Mapper.mapDecToBin(num4.numDec)
    m = 2 ** len(num4Bin)
    mBin = Mapper.mapDecToBin(m)
    m = div(mBin, modBin)[0]
    num5 = barret(num4Bin, modBin, m)
    return num5 #Bin

def gorner(a, b, n):
    c = [1]
    m = 2 ** (len(n) * 2)
    mBin = Mapper.mapDecToBin(m)
    m = div(mBin, n)[0]
    b.reverse()
    for i in range(0, len(b)):
        if b[i] == 1:
            c = barret(mul(c.copy(), a.copy(), 2).numBig, n, m)
        a = barret(mul(a.copy(), a.copy(), 2).numBig, n, m)
    return c

def mainLab2():
    beta = 32
    number1 = Number(beta, "12")
    number2 = Number(beta, "16")

    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    mainBinLab2(num1Bin, num2Bin)

def mainBinLab2(number1, number2):
    res = gcd(number1, number2)
    print(res.numDec)

if __name__ == "__main__":
    mainLab2()