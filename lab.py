import math
from number import Number
from mapper import Mapper

def insert(num, pos):
    if len(num) <= pos:
        num.append(1)
        num  = shiftDigitsToHigh(num, pos)
    else:
        num.reverse()
        num[pos] = 1
        num.reverse()
    return num


def compare(num1, num2):
    if len(num1) > len(num2):
        return True
    elif len(num1) < len(num2):
        return False
    else:
        for i in range(len(num2)):
            if num1[i] > num2[i]:
                return True
            if num1[i] < num2[i]:
                return False
        return True # =


def shiftDigitsToHigh(num, count):
    newNum = num.copy()
    for i in range(count):
        newNum.append(0)
    return newNum

def mulOneDigit(num1, a, beta):
    num1.reverse()
    carry = 0
    res = []
    for i in range(len(num1)):
        temp = num1[i] * a + carry
        res.append(temp % beta)
        carry = temp // beta
    if carry != 0:
        res.append(carry)
    revers([res, num1])
    return res 
    
#Main func

def add(num1, num2, beta):
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    num3 = []
    revers([num1, num2])
    carry = 0
    for i in range(len(num1)):
        sec = 0
        if len(num2) > i:
            sec = num2[i]
        temp = num1[i] + sec + carry
        num3.append(temp % beta)
        carry = temp // beta
    if carry != 0:
        num3.append(carry)
    num3.reverse()
    #print(num3)
    number3 = Number(beta = beta, number = num3, numType="big")
    revers([num1, num2])
    return number3

def sub(num1, num2, beta):
    num3 = []
    revers([num1, num2])
    borrow = 0
    for i in range(len(num1)):
        sec = 0
        if len(num2) > i:
            sec = num2[i]
        temp = num1[i] - sec - borrow
        if temp >= 0:
            num3.append(temp)
            borrow = 0
        else:
            num3.append(temp + beta)
            borrow = 1
    num3.reverse()
    while(len(num3) != 0):
        if num3[0] == 0:
            del num3[0]
        else:
            break
    revers([num1, num2])
    number3 = Number(beta = beta, number = num3, numType="big")
    return number3

def mul(num1, num2, beta):
    if len(num2) > len(num1):
        num2, num1 = num1, num2
    num3 = []
    num2.reverse()
    for i in range(len(num2)):
        temp = mulOneDigit(num1, num2[i], beta)
        temp = shiftDigitsToHigh(temp, i)
        #print(num3)
        num3 = add(temp, num3, beta).numBig
    num2.reverse()
    return Number(beta = beta, number = num3, numType="big")

def div(num1, num2):
    k = len(num2)
    r = num1
    q = []
    while compare(r, num2):
        t = len(r)
        c = shiftDigitsToHigh(num2, t-k)
        if not compare(r,c):
            t -= 1
            c = shiftDigitsToHigh(num2, t-k)
        r = Mapper.mapDecToBin(sub(r, c, 2).numDec)
        q = insert(q, t-k)
    return q, r  

def power(num1, num2):
    num3 = [1]
    num2.reverse()
    for char in num2:
        if char == 1:
            num3 = Mapper.mapDecToBin(mul(num3, num1, 2).numDec)
        num1 = Mapper.mapDecToBin(mul(num1.copy(), num1, 2).numDec)
        #print(num1, num3)
    return num3

def testDistr(beta, num1, num2, num3): #(a+b)c
    num1sum2 = add(num1.numBig, num2.numBig, beta).numBig
    num1sum2mul3 = mul(num1sum2, num3.numBig, beta)

    num3mul1sum2 = mul(num3.numBig, num1sum2, beta)

    num1mul3 = mul(num1.numBig, num3.numBig, beta).numBig
    num2mul3 = mul(num2.numBig, num3.numBig, beta).numBig
    num123 = add(num1mul3, num2mul3, beta)
    print(num1sum2mul3.numDec, num3mul1sum2.numDec, num123.numDec)
    if num1sum2mul3.numDec == num3mul1sum2.numDec and num3mul1sum2.numDec == num123.numDec:
        print("Ok")
    else:
        print("Wrong")

def testSum(beta, num1, num2): #na = n + n + n + ... + n
    numSum = []
    for i in range(num1.numDec):
        numSum = add(numSum, num2.numBig, beta).numBig
    numNA = mul(num1.numBig, num2.numBig, beta)
    numSumNumber = Number(beta, numSum, numType="big")
    print(numNA.numDec, numSumNumber.numDec)
    if numNA.numDec == numSumNumber.numDec:
        print("Ok")
    else:
        print("Wrong")



def main():
    beta = 32
    number1 = Number(beta, "76")
    number2 = Number(beta, "345")
    number3 = Number(beta, "235CF")
    #testDistr(beta, number1, number2, number3)
    #testSum(beta, number1, number2)

    num1Bin = Mapper.mapDecToBin(number2.numDec)
    num2Bin = Mapper.mapDecToBin(number1.numDec)
    mainBin(num1Bin, num2Bin)

def mainBin(number1, number2):
    #res = div(num1 = number1, num2 = number2)
    #print(number1)
    res = power(number1, number2)
    #print(res)
    num = Number(32, Mapper.mapBinToDec(res), "dec")
    print(num.hex)
    #print(16**16)

def revers(nums):
    for num in nums:
        num.reverse()

if __name__ == "__main__":
    main()