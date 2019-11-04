from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result


def romanToDec(numStr):


    if numStr.isdigit() is True:
        print(int(numStr))
        print("a")
        return "Put in the Roman alphabet"



    try:
        n_ = numStr[:] #객체를 복사해옴.

        n = numStr

        romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        result = 0
        for value, letters in romans:
            #while letters in n:
            #자꾸 이상하케 나왔움.

            while n.find(letters) == 0:
                result += value
                if len(letters) == 2:
                    n = n[2:]
                else:
                    n = n[1:]



        if decToRoman(result) != n_:
            return "Put the right content in"

        result = str(result)
        return result

    except:
        return "Error!"
