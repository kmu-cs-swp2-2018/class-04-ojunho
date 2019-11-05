# calculator 3

## keypad.py

    functionMap = [
        ('factorial (!)' , calcFunctions.factorial),

        ('-> binary' , calcFunctions.decToBin),

        ('binary -> dec' , calcFunctions.binToDec),

        ('-> roman' , calcFunctions.decToRoman),

        ('roman -> dec' , calcFunctions.romanToDec),

    ]

keypad.py 의 코드는 숫자키, 연산자키, 상수, 함수의 내용을 모아 놓은 파일이다.
이전에는 romanToDec이라는 함수가 없었기 때문에 새로 추가할 romanToDec을 추가 확장 하기 위해서 추가해준다.

## 함수 기능 수행 부분


### 이전의 코드 

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

### 이후의 코드

    romans = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]


    romans_list = [x[1] for x in romans]


    def romanToDec(numStr):

        splitList = list(numStr)
        for i in splitList:
            if not i in romans_list:
                return "Put in the right Roman alphabet"
                break

        # if numStr.isdig:
        #     print(int(numStr))
        #     print("a")
        #     return "Put in the Roman alphabet

        else:
    
            Copy_n = numStr[:] #객체를 복사해옴.
 
            n = numStr



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



            if decToRoman(result) != Copy_n:
                return "Put the right content in"

            result = str(result)
            return result


## 개선한 점

numStr을 복사해온 객체의 이름을 기존에 있는 변수 이름인 n과 너무 비슷하게 n_으로 한 것이 아쉽다는 지적을 받아 Copy_n으로 변경해 주었다.

함수 구현 부분의 메인 코드를 try, except로 예외처리를 해주었는데 사실 파이썬에서 에러라고 할만한 큰 에러는 없을 것 같아서 그 부분을 삭제 해 주었다.

romans를 기존에 두번 썼던 것을 맨 위에 한번 써서 코드의 반복을 줄였다.
또한 올바른 로마숫자가 들어갔는지를 확인하기 위한 예외 처리를 할 때 isdigit을 사용하여 10진수로 나타날 수 있는 숫자인지만 판별하고, 10진수로 표현되는 수이면 에러 문구를 반환하도록 해주었다. 하지만 이는 실제 오류와 동치하지 않기 때문에 romans의 letters들만 가져온 romans_list를 만든 후에 주어진 문자열을 처음부터 읽어들이면서 letters에 없는 문자로 구성되어 있으면 바로 오류를 리턴하도록 변경하였다.



## 개선해야 할 점

내가 짠 코드는 find와 String slicing을 사용하기 때문에 굉장히 시간 복잡도가 높다고 한다. find를 사용하지 않고 문자열의 처음 인덱스를 확인해 주는 조건으로, String slicing 대신에 indexing을 사용하여 시간복잡도를 줄일 수 있다고 한다.

또한 XIIII와 같이 올바른 표현이 아닌 숫자가 들어왔을 때의 예외 처리 부분은 본인이 전에 짰던 코드를 사용해서 검사하기 때문에 전의 코드에 의존성이 생기기 때문에 아쉬운 부분이 있다. 
