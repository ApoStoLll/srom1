class Mapper:

    @staticmethod
    def mapCharToDec(char):
        if char == 'A':
            return 10
        elif char == 'B':
            return 11
        elif char == 'C':
            return 12
        elif char == 'D':
            return 13
        elif char == 'E':
            return 14
        elif char == 'F':
            return 15
        else:
            return int(char)

    @staticmethod
    def mapDecToChar(dec):
        if dec == 10:
            return 'A'
        elif dec == 11:
            return 'B'
        elif dec == 12:
            return 'C'
        elif dec == 13:
            return 'D'
        elif dec == 14:
            return 'E'
        elif dec == 15:
            return 'F'
        else:
            return str(dec)

    @staticmethod
    def mapDecToBin(dec):
        binary = ""
        while dec > 0:
            binary = str(dec % 2) + binary
            dec = dec // 2
        numBin = []
        for b in binary:
            numBin.append(int(b))
        return numBin

    @staticmethod
    def mapBinToDec(numBin):
        numBin.reverse()
        numDec = 0
        i = 0
        for char in numBin:
            numDec += char * int(2 ** i)
            i += 1
        return numDec

    @staticmethod
    def mapStringToBin(strNum):
        numBin = []
        for char in strNum:
            numBin.append(int(char))
        return numBin
    
    @staticmethod
    def mapBinToString(num):
        strNum = ""
        for bit in num:
            strNum += str(bit)
        return strNum


