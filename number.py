import math
from mapper import Mapper

class Number:
    def __init__(self, beta, number, numType="hex"):
        self.beta = beta
        if numType == "hex":
            self.hex = number
            self.getDec()
            self.getBig()
        elif numType == "dec":
            self.numDec = number
            self.getBig()
            self.getHex()
        elif numType == "big":
            self.numBig = number
            self.getDecFromBig()
            self.getHex()
        else:
            print("Smth went wrong in number create")

        
        #self.mapper = Mapper()

    def getDec(self):
        num = self.hex[::-1]
        numDec = 0
        i = 0
        for char in num:
            numDec += Mapper.mapCharToDec(char) * int(pow(16, i))
            i += 1
        self.numDec = numDec

    def getHex(self):
        num = self.numDec
        numHex = ""
        while num > 0:
            numHex += Mapper.mapDecToChar(num % 16)
            num = num // 16
        self.hex = numHex[::-1]

    def getDecFromBig(self):
        num = self.numBig
        num.reverse()
        numDec = 0
        i = 0
        for n in num:
            numDec += n * int(self.beta ** i)
            i += 1
        self.numDec = int(numDec)
        self.numBig.reverse()

    def getBig(self):
        num = self.numDec
        numBig = []
        while num > 0:
            numBig.append(num % self.beta)
            num = num // self.beta
        numBig.reverse()
        self.numBig = numBig

    
