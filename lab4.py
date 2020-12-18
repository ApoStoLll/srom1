from number import Number
from mapper import Mapper
from lab import mulOneDigit, shiftDigitsToHigh, compare, insert


def add(num1Str, num2Str):
    num1 = Mapper.mapStringToBin(num1Str)
    num2 = Mapper.mapStringToBin(num2Str)
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    res = []
    num1.reverse()
    num2.reverse()
    for i in range(len(num1)):
        temp = 0
        if len(num2) > i:
            temp = num2[i]
        res.append((num1[i] + temp) % 2)
    res.reverse()
    resStr = Mapper.mapBinToString(res)
    return resStr

def addBig(num1, num2):
    if len(num1) < len(num2):
        #print(num1, num2)
        num1, num2 = num2, num1
        #print(num1, num2)
    res = []
    num1.reverse()
    num2.reverse()
    for i in range(len(num1)):
        temp = 0
        if len(num2) > i:
            temp = num2[i]
        res.append((num1[i] + temp) % 2)
    res.reverse()
    return res

def sqr(num1Str):
    num1 = Mapper.mapStringToBin(num1Str)
    num1.insert(0, num1[-1])
    del num1[- 1]
    return Mapper.mapBinToString(num1) #Str

def createMatrix(num1): #!!!!!!!!!!!!!!!!!!!!!!!!!!!
    m = len(num1)
    p = 2 * m + 1
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(m):
            if ((2 ** i) + (2 ** j)) % p == 1 or ((2 ** i) - (2 ** j)) % p == 1 or (-(2 ** i) + (2 ** j)) % p == 1 or (-(2 ** i) - (2 ** j)) % p == 1:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix

def mulBig(num1, num2): #Bin
    matrix = createMatrix(num1)
    d = []
    for k in range(len(num1)):
        c = []
        for i in range(len(num1)):
            summ = 0
            for j in range(len(num1)):
                summ += num1[j] * matrix[j][i]
            c.append(summ % 2)
        summ = 0
        for i in range(len(c)):
            summ += c[i] * num2[i]
        d.append(summ % 2)
        x = num1[0]
        del num1[0]
        num1.append(x)
        y = num2[0]
        del num2[0]
        num2.append(y)
    return d

def power(num1, n): #Bin
    c = []
    for i in range(len(num1)):
        c.append(1)
    n.reverse()
    for i in range(len(n)):
        if n[i] == 1:
            c = mulBig(c.copy(), num1.copy())
        num1 = Mapper.mapStringToBin(sqr(Mapper.mapBinToString(num1.copy())))
    return c

def inv(num1Str): #!!!!!!!!!!!!!
    num1 = Mapper.mapStringToBin(num1Str)
    m = len(num1)
    n = m - 1
    nBin = Mapper.mapDecToBin(n)
    k = 1
    num2 = num1.copy()
    for i in range(len(nBin)):
        if i == 0:
            continue
        num3 = Mapper.mapStringToBin(sqr(Mapper.mapBinToString(num2.copy())))
        num3 = power(num2.copy(), Mapper.mapDecToBin(2 ** k))
        num2 = mulBig(num3.copy(), num2.copy())
        k = 2*k
        if nBin[i] == 1:
            num2 = Mapper.mapStringToBin(sqr(Mapper.mapBinToString(num2.copy())))
            num2 = mulBig(num2.copy(), num1.copy())
            k = k + 1
    num2 = Mapper.mapStringToBin(sqr(Mapper.mapBinToString(num2.copy())))
    return Mapper.mapBinToString(num2)


def trace(num1Str):
    num1 = Mapper.mapStringToBin(num1Str)
    trace = [0]
    for i in range(len(num1)):
        trace = addBig(trace.copy(), num1.copy())
        num1 = Mapper.mapStringToBin(sqr(Mapper.mapBinToString(num1)))
    return Mapper.mapBinToString(trace)

def test1():
    num1Str = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num2Str = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num3Str = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"

    a = Mapper.mapStringToBin(num1Str)
    b = Mapper.mapStringToBin(num2Str)
    c = Mapper.mapStringToBin(num3Str)
    
    aSumb = addBig(a.copy(), b.copy())
    #print("aSumb", Mapper.mapBinToString(aSumb))
    abc = mulBig(aSumb, c)
    #print("abc", abc)
    ac = mulBig(a, c)
    #print("ac", ac)
    bc = mulBig(b,c)
    #print("bc", bc)
    abc2 = add(ac, bc)
    #print("abc2", abc2)
    if abc == abc2:
        print("Norm")
    else:
        print("((")

def test2(m):
    num1Str = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    a = Mapper.mapStringToBin(num1Str)
    n = 2 ** m - 1
    nBin = Mapper.mapDecToBin(n)
    powe = power(a, nBin)
    if powe == "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011001000":
        print("Norm")
    else:
        print("((")

def main():
    m = 173
    #checkAdd()
    #checkSqr()
    #checkMul()
    #checkTrace()
    checkPower()

def checkAdd():
    num1 = "100000000000000000100000000000000000000000000000000000000000000000000000000010000000000000000001000000000000000000000000000000000001000000000000000000000000000000000000000001"
    num2 = "100000000000000000100000000000000000000000100000000000000100000000000000000010000000000000000001000000001000000000000000000100000001000000000000000000010000000000000000000001"
    res = add(num1, num2)
    if res == "" or res is None:
        print(0)
    print(res)

def checkSqr():
    num1 = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    res = sqr(num1)
    print(res)

def checkMul():
    num1 = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    num2 = "10000000000000000010000000000000000000000010000000000000010000000000000000001000000000000000000100000000100000000000000000010000000100000000000000000010000000000000000000001"
    a = Mapper.mapStringToBin(num1)
    b = Mapper.mapStringToBin(num2)
    res = mulBig(a, b)
    print(Mapper.mapBinToString(res))

def checkTrace():
    num1 = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    res = trace(num1)
    print(res)

def checkPower():
    num1 = "10000000000000000010000000000000000000000000000000000000000000000000000000001000000000000000000100000000000000000000000000000000001000000000000000000000000000000000000000001"
    num2 = "1000000000000010000000100000001000000000000000000100000000100000000000100000001000000010000000001"
    a = Mapper.mapStringToBin(num1)
    b = Mapper.mapStringToBin(num2)
    power(a, b)

if __name__ == "__main__":
    main()