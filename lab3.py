from number import Number
from mapper import Mapper

def add(num1Str, num2Str):
    num1 = Mapper.mapStringToBin(num1Str)
    num2 = Mapper.mapStringToBin(num2Str)
    res = []
    for i in range(len(num1)):
        res.append((num1[i] + num2[i]) % 2)
    resStr = Mapper.mapBinToString(res)
    return resStr




def main():
    m = 163
    poli = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    checkAdd()

def checkAdd():
    num1 = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000100000000000000000000000000000000000000011001001"
    num2 = "10000000000000000000000000100000000100000000001000000000100000000010001000000000100000000000000000000000000000000000000000000000000000000000000000000000000011001001"
    res = add(num1, num2)
    print(res)

if __name__ == "__main__":
    main()