from number import Number
from mapper import Mapper
from lab import *

def gcd(num1, num2):
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
    return d


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