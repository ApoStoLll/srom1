from number import Number
from mapper import Mapper
from lab import mulOneDigit, shiftDigitsToHigh, compare, insert

def mulLong(num1, num2, ext): #bin
    if len(num1) > len(num2):
        print(num1, num2)
        num1, num2 = num2, num1
        print(num1, num2)
    num3 = []
    num2.reverse()
    for i in range(len(num2)):
        temp = mulOneDigit(num1, num2[i], ext)
        temp = shiftDigitsToHigh(temp, i)
        num3 = addBig(temp, num3)
    return num3

def divLong(num1, num2):
    k = len(num2)
    r = num1
    q = []
    #print(type(num2))
    while compare(r, num2):
        t = len(r)
        c = shiftDigitsToHigh(num2, t-k)
        r = addBig(r, c)
        q = insert(q, t-k)
        while(len(r) != 0):
            if r[0] == 0:
                del r[0]
            else:
                break
    return q, r

def addBig(num1, num2):
    if len(num1) < len(num2):
        print(num1, num2)
        num1, num2 = num2, num1
        print(num1, num2)
    res = []
    for i in range(len(num1)):
        temp = 0
        if len(num2) > i:
            temp = num2[i]
        res.append((num1[i] + temp) % 2)
    return res

def sqrBig(num1, pol):
    for i in range(len(num1) - 1):
        num1.insert(i*2 + 1, 0)
    num2 = divLong(num1.copy(), pol)[1]
    return num2

def add(num1Str, num2Str):
    num1 = Mapper.mapStringToBin(num1Str)
    num2 = Mapper.mapStringToBin(num2Str)
    res = []
    for i in range(len(num1)):
        res.append((num1[i] + num2[i]) % 2)
    resStr = Mapper.mapBinToString(res)
    return resStr

def mul(num1Str, num2Str, polynom, m):
    num1 = Mapper.mapStringToBin(num1Str)
    num2 = Mapper.mapStringToBin(num2Str)
    pol = Mapper.mapStringToBin(polynom)
    num3 = mulLong(num1, num2, 2)
    num4 = divLong(num3, pol)[1]
    print(num4)
    while(len(num4) > m):
        del num4[0]
    numStr = Mapper.mapBinToString(num4)
    return numStr

def trace(num1Str, pol):
    num1 = Mapper.mapStringToBin(num1Str)
    pol = Mapper.mapStringToBin(pol)
    m = len(num1)
    trace = [0]
    for i in range(0, m):
        trace = addBig(trace.copy(), num1.copy())
        num1 = sqrBig(num1.copy(), pol)
    resStr = Mapper.mapBinToString(trace)
    return resStr # STR


def main():
    m = 163
    poli = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    #checkMul(poli, m)
    checkTrace(poli)

def checkAdd():
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num2 = "10000000000000000000000000100000000100000000001000000000100000000010001000000000100000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    res = add(num1, num2)
    print(res)

def checkMul(poli, m):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num2 = "10000000000000000000000000100000000100000000001000000000100000000010001000000000100000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    res = mul(num1, num2, poli, m)
    print(res)

def checkTrace(poli):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    res = trace(num1, poli)
    print(res)

if __name__ == "__main__":
    main()