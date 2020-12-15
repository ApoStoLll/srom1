from number import Number
from mapper import Mapper
from lab import *

def gcd(num1, num2): #bin
    #print(num1, num2)
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
    if len(x) != 2 * len(n):
        #print("ez")
        return div(x,n)[1]
    q = killDigits(x, len(n) - 1)
    q = mul(q, m, 2).numBig
    q = killDigits(x, len(n) + 1)
    r = sub(x.copy(), mul(q.copy(), n.copy(), 2).numBig, 2).numBig
    print("r : ", r, "n :  ", n)
    while compare(r, n):
        r = sub(r, n, 2).numBig
    return r


def killDigits(x, k):
    if x == None:
        return x
    for i in range(0, k):
        del x[-i+1]
    return x

def addMod(num1, num2, modBin, beta):
    num4 = add(num1, num2, 2)
    num4Bin = Mapper.mapDecToBin(num4.numDec)
    m = 2 ** len(num4Bin)
    mBin = Mapper.mapDecToBin(m)
    m = div(mBin, modBin)[0]
    num5 = barret(num4Bin, modBin, m)
    return num5 #Bin

def subMod(num1, num2, modBin, beta):
    num4 = sub(num1, num2, 2)
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
    m = 2 ** (len(n))
    mBin = Mapper.mapDecToBin(m)
    m = div(mBin, n)[0]
    b.reverse()
    for i in range(0, len(b)):
        if b[i] == 1:
            c = barret(mul(c.copy(), a.copy(), 2).numBig, n, m)
        a = barret(mul(a.copy(), a.copy(), 2).numBig, n, m)
    return c

def mainLab2():
    # beta = 1024
    # number1 = Number(beta, "1EAFD68DCE7A944D4B0967302")
    # number2 = Number(beta, "00ABD8E74A99A18BCF231B05D")
    # mod = Number(beta, "78")

    # num1Bin = Mapper.mapDecToBin(number2.numDec)
    # num2Bin = Mapper.mapDecToBin(number1.numDec)
    # modBin = Mapper.mapDecToBin(mod.numDec)

    # res = barret(num2Bin, num1Bin, modBin)

    # resDec = Mapper.mapBinToDec(res)
    # resNum = Number(beta, resDec, "dec")
    # print(resNum.hex)
    #checkAdd()
    #checkGcd()
    #checkLcm()
    #checkSub()
    #checkMul()
    #checkPow()
    #test1()
    test2()



def checkGcd():
    beta = 2 ** 64
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    res = gcd(num1Bin, num2Bin)
    print(res.hex)

def checkLcm():
    beta = 2 ** 64
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    res = lcm(num1Bin, num2Bin)
    print(res.hex)

def checkAdd():
    beta = 1024
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    mod = Number(beta, "247A")
    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    modBin = Mapper.mapDecToBin(mod.numDec)
    res = addMod(num1Bin, num2Bin, modBin, 2)
    #print(res)
    resDec = Mapper.mapBinToDec(res)
    resNum = Number(beta, resDec, "dec")
    print(resNum.hex)

def checkSub():
    beta = 1024
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    mod = Number(beta, "247A")
    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    modBin = Mapper.mapDecToBin(mod.numDec)
    res = subMod(num2Bin, num1Bin, modBin, 2)
    #print(res)
    resDec = Mapper.mapBinToDec(res)
    resNum = Number(beta, resDec, "dec")
    print(resNum.hex)

def checkMul():
    beta = 1024
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    mod = Number(beta, "247A")
    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    modBin = Mapper.mapDecToBin(mod.numDec)
    res = mulMod(num2Bin, num1Bin, modBin, 2)
    #print(res)
    resDec = Mapper.mapBinToDec(res)
    resNum = Number(beta, resDec, "dec")
    print(resNum.hex)

def checkPow():
    beta = 1024
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    mod = Number(beta, "247A")
    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    modBin = Mapper.mapDecToBin(mod.numDec)
    res = gorner(num2Bin, num1Bin, modBin)
    #print(res)
    resDec = Mapper.mapBinToDec(res)
    resNum = Number(beta, resDec, "dec")
    print(resNum.hex)

def test1(): # distr
    beta = 1024
    number1 = Number(beta, "1EAEDD395588036066915AF60F3F84502967BD8617DC")
    number2 = Number(beta, "1253FBED85830A10694A33E1C0DF38E62C8F6B2575B1")
    number3 = Number(beta, "1253FBEF85830A10694A33E1C0DF38E62C8F6B2575B1")
    mod = Number(beta, "247A")

    num1Bin = Mapper.mapDecToBin(number1.numDec)
    num2Bin = Mapper.mapDecToBin(number2.numDec)
    num3Bin = Mapper.mapDecToBin(number3.numDec)
    modBin = Mapper.mapDecToBin(mod.numDec)

    num12sum = addMod(num1Bin, num2Bin, modBin, 2)
    num12sum3 = mulMod(num12sum, num3Bin, modBin, 2)
    num123 = mulMod(num3Bin, num12sum, modBin, 2)

    num13 = mulMod(num1Bin, num3Bin, modBin, 2)
    num23 = mulMod(num2Bin, num3Bin, modBin, 2)
    num123sum = addMod(num13, num23, modBin, 2)

    if num12sum3 == num123 and num123 == num123sum:
        print("Norm")
    else:
        print("ta za sho")


def test2(): #na = n + n + n + ...
    beta = 1024
    number1 = Number(beta, "1E")
    number2 = Number(beta, "12")
    mod = Number(beta, "A")

    num1Bin = Mapper.mapDecToBin(number1.numDec)
    num2Bin = Mapper.mapDecToBin(number2.numDec)
    modBin = Mapper.mapDecToBin(mod.numDec)

    numNa = mulMod(num1Bin, num2Bin, modBin, 2)
    
    numbin = []
    for i in range(number1.numDec):
        numbin = addMod(numbin, num2Bin, modBin, 2)
    
    if numbin == numNa:
        print("Norm")
    else:
        print("ta za sho")

if __name__ == "__main__":
    mainLab2()