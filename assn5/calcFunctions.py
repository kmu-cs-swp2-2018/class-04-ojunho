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


    if numStr.isdigit():
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


                # 멍청했다.

                # if len(letters) == 2:
                #     n = n[2:]
                # else:
                #     n = n[1:]

                n = n[len(letters):]



        if decToRoman(result) != n_:
            return "Put the right content in"

        result = str(result)
        return result

    except:
        return "Error!"

#######################################
def romanToDec(romanStr):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(0, len(romanStr)):
        #     if i not in list(romans.keys()):
        #         return "변환 불가능한 로마문자열입니다."
        # 첫번째 문자 또는
        # 왼쪽(1칸앞)의문자보다 작거 같다면 -> 뺄수없다 -> 그럼 더함.
        if i == 0 or romans[romanStr[i]] <= romans[romanStr[i - 1]]:
            result += romans[romanStr[i]]
        else:
            # 왼쪽(1칸앞)의문자보다 크다면 빼야되는데, 2번빼는 이유는 이전 루프에서 더 했기 때문이다.
            result += romans[romanStr[i]] - 2 * romans[romanStr[i - 1]]
    return result
