from number import Number
from mapper import Mapper
from lab import mulOneDigit, shiftDigitsToHigh, compare, insert

def mulLong(num1, num2, ext): #bin
    if len(num1) > len(num2):
        #print(num1, num2)
        num1, num2 = num2, num1
        #print(num1, num2)
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

def sqrBig(num1, pol):
    for i in range(len(num1) - 1):
        num1.insert(i*2 + 1, 0)
    num2 = divLong(num1.copy(), pol)[1]
    return num2

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

def mul(num1Str, num2Str, polynom, m):
    num1 = Mapper.mapStringToBin(num1Str)
    num2 = Mapper.mapStringToBin(num2Str)
    pol = Mapper.mapStringToBin(polynom)
    num3 = mulLong(num1, num2, 2)
    num4 = divLong(num3, pol)[1]
    #print(num4)
    while(len(num4) > m):
        del num4[0]
    numStr = Mapper.mapBinToString(num4)
    return numStr

def trace(num1Str, pol, m):
    num1 = Mapper.mapStringToBin(num1Str)
    pol = Mapper.mapStringToBin(pol)
    trace = [0]
    for i in range(0, m):
        trace = addBig(trace.copy(), num1.copy())
        num1 = sqrBig(num1.copy(), pol.copy())
    resStr = Mapper.mapBinToString(trace)
    return resStr # STR

def power(num1Str, nStr, pol):
    num1 = Mapper.mapStringToBin(num1Str)
    powe = Mapper.mapStringToBin(nStr)
    pol = Mapper.mapStringToBin(pol)
    num2 = [1]
    powe.reverse()
    for i in range(len(powe)):
        if powe[i] == 1:
            num2 = mulLong(num2.copy(), num1.copy(), 2)
            num2 = divLong(num2.copy(), pol)[1]
        num1 = sqrBig(num1.copy(), pol)
        num1 = divLong(num1.copy(), pol)[1]
    num3 = Mapper.mapBinToString(num2)
    return num3

def inv(num1Str, pol, m):
    num1 = Mapper.mapStringToBin(num1Str)
    n = (2 ** m) - 2
    nBin = Mapper.mapDecToBin(n)
    nStr = Mapper.mapBinToString(nBin)
    return power(num1Str, nStr, pol)

def test1(pol, m): #(a+b)c
    num1 = "10000000000000000000000000000000000000000010000000000000000000010000000000000000000000000000000000000000010000000000100000000000000000100000000000000000000011001001"
    num2 = "10000000000000001000000000000000000000000000000010000000000010000000000000000000000000000000000000000000010000000000100000000001000000000000000000000000000011001001"
    num3 = "10000000010000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000010000000000100000000000000000000000000000000100000011001001"
    a = Mapper.mapStringToBin(num1)
    b = Mapper.mapStringToBin(num2)
    c = Mapper.mapStringToBin(num3)
    
    aSumb = addBig(a.copy(), b.copy())
    #print("aSumb", Mapper.mapBinToString(aSumb))
    abc = mul(Mapper.mapBinToString(aSumb), num3, pol, m)
    #print("abc", abc)
    ac = mul(num1, num3, pol, m)
    #print("ac", ac)
    bc = mul(num2, num3, pol, m)
    #print("bc", bc)
    abc2 = add(ac, bc)
    #print("abc2", abc2)
    if abc == abc2:
        print("Norm")
    else:
        print("((")

def test2(pol, m):
    num1 = "10000000000000000000000000000000000000000010000000000000000000010000000000000000000000000000000000000000010000000000100000000000000000100000000000000000000011001001"
    n = 2 ** m - 1
    nBin = Mapper.mapDecToBin(n)
    nStr = Mapper.mapBinToString(nBin)
    powe = power(num1, nStr, pol)
    if powe == "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011001000":
        print("Norm")
    else:
        print("((")



def main():
    m = 163
    poli = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    if "11111000010000110000000000001100000010000001000010001000100000010010100000000010000011100000000010100010100001000011011100100000010110010010110111010111011101000101000001001" == "11111000010000110000000000001100000010000001000010001000100000010010100000000010000011100000000010100010100001000011011100100000010110010010110111010111011101000101000001001":
        print("ok")
    else:
        print("gg")
    #checkSqr(poli)
    #checkAdd()
    #checkMul(poli, m)
    #checkTrace(poli, m)
    #checkPower(poli)
    #checkInv(poli, m)
    #test1(poli, m)
    #test2(poli, m)

def checkAdd():
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num2 = "10000000000000000000000000100000000100000000001000000000100000000010001000000000100000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    res = add(num1, num2)
    if res == "" or res is None:
        print(0)
    print(res)

def checkMul(poli, m):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num2 = "10000000000000000000000000100000000100000000001000000000100000000010001000000000100000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    res = mul(num1, num2, poli, m)
    if res == "" or res is None:
        print(0)
    print(res)

def checkTrace(poli, m):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    res = trace(num1, poli, m)
    if res == "" or res is None:
        print(0)
    print(res)

def checkSqr(pol):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num = Mapper.mapStringToBin(num1)
    p = Mapper.mapStringToBin(pol)
    res = sqrBig(num, p)
    if res == "" or res is None:
        print(0)
    print(Mapper.mapBinToString(res))

def checkPower(pol):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    n = "111111111111111111011111111111111111111111101111111111111111111111111111111111111111111111111110"
    res = power(num1, n, pol)
    if res == "" or res is None:
        print(0)
    print(res)

def checkInv(pol, m):
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    res = inv(num1, pol, m)
    if res == "" or res is None:
        print(0)
    print(res)

if __name__ == "__main__":
    main()