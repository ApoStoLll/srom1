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
    beta = 2 ** 64
    number1 = Number(beta, "D4D2110984907B5625309D956521BAB4157B8B1ECE04043249A3D379AC112E5B9AF44E721E148D88A942744CF56A06B92D28A0DB950FE4CED2B41A0BD38BCE7D0BE1055CF5DE38F2A588C2C9A79A75011058C320A7B661C6CE1C36C7D870758307E5D2CF07D9B6E8D529779B6B2910DD17B6766A7EFEE215A98CAC300F2827DB")
    number2 = Number(beta, "3A7EF2554E8940FA9B93B2A5E822CC7BB262F4A14159E4318CAE3ABF5AEB1022EC6D01DEFAB48B528868679D649B445A753684C13F6C3ADBAB059D635A2882090FC166EA9F0AAACD16A062149E4A0952F7FAAB14A0E9D3CB0BE9200DBD3B0342496421826919148E617AF1DB66978B1FCD28F8408506B79979CCBCC7F7E5FDE7")
    mod = Number(beta, "87D6D58D3991D536544389CEFA72FD0EBED75B2EBDC2C79BC3717793108F0952011E7E2D7040FFFB32F10BEB8ED0A485026B6860020B230128A8222B0525A6888942FB01C537800BF25D6F021D4B99D3CBD6DF9055FA22F91A6CFC4FDFC408AEF78F6418D3CE4E20EC7888B61BAE3D73C27C257CCA905DE0353C3A7CFFD9FE15")

    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    mainBinLab2(num1Bin, num2Bin)

def mainBinLab2(number1, number2):
    print("start gcd")
    res = gcd(number1, number2)
    print(res.hex)

if __name__ == "__main__":
    mainLab2()