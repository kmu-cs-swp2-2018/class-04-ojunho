# Second Calculator 보고서

#  코드 설명

## calcFunctions.py

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
        return 'dec -> Roman'

    #functionList = {
    #    'factorial (!)' : 'factorial()',
    #    '-> binary' : 'decToBin()',
    #    'binary -> dec' : 'binToDec()',
    #    '-> roman' : 'decToRoman()',
    #}


calFunctions python 파일에는 계산기에 들어갈 functions의 기능을 수행하는 함수들이 들어있다.


## keypad2.py

    import calcFunctions


    numPadList = [
        '7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0', '.', '=',
    ]

    operatorList = [
        '*', '/',
        '+', '-',
        '(', ')',
        'C',
    ]
    
    constantMap = [
        ('pi' , "3.141592"),
  
        ('빛의 이동 속도 (m/s)' , "3E+8"),
  
        ('소리의 이동 속도 (m/s)' , "340"),
  
        ('태양과의 평균 거리 (km)' , "1.5E+8"),
    ]

    constantList = [i[0] for i in constantMap]
    constantValues = {i[0]: i[1] for i in constantMap}


    functionMap = [
        ('factorial (!)' , calcFunctions.factorial),
  
        ('-> binary' , calcFunctions.decToBin),

        ('binary -> dec' , calcFunctions.binToDec),

        ('-> roman' , calcFunctions.decToRoman),
    ]

    functionList = [i[0] for i in functionMap]
    functionMethods = {i[0]: i[1] for i in functionMap}

keypad python 파일에는 위의 calFunctions 파일을 임포트 한 후에 각각의(숫자, 계산, 상수, 함수) 버튼에 들어갈 텍스트와 실제 값, 수행내용(상수버튼과 함수버튼인 경우에)을 담는다.  실제 계산기 실행 코드인 mycalc 에서 버튼 눌렸는지를 인식하기 위해, 그리고 인식 후에 상수값을 불러오기 위해서 혹은 함수를 불러오기 위해서 이러한 작업을 해주는 것이다.


## mycalc.py

실제 계산기 실행 코드이다. 너무 길기 때문에 자세한 설명할 때 부분부분 떼어 오도록 하겠음.
위의 코드 calcFunctions.py keypad2.py를 모두 import 한다.

    from keypad2 import numPadList, operatorList, constantList, constantValues, functionList, functionMethods
    import calcFunctions

### Constant & Functions
    
    elif key == constantList[0]:
        self.display.setText(self.display.text() + '3.141592')
    elif key == constantList[1]:
        self.display.setText(self.display.text() + '3E+8')
    elif key == constantList[2]:
        self.display.setText(self.display.text() + '340')
    elif key == constantList[3]:
        self.display.setText(self.display.text() + '1.5E+8')
    elif key == functionList[0]:
        n = self.display.text()
        value = calcFunctions.factorial(n)
        self.display.setText(str(value))
    elif key == functionList[1]:
        n = self.display.text()
        value = calcFunctions.decToBin(n)
        self.display.setText(str(value))
    elif key == functionList[2]:
        n = self.display.text()
        value = calcFunctions.binToDec(n)
        self.display.setText(str(value))
    elif key == functionList[3]:
        n = self.display.text()
        value = calcFunctions.decToRoman(n)
        self.display.setText(str(value))
    else:
        self.display.setText(self.display.text() + key)

원래 초기의 코드는 이러했다. constantList에 있는 몇번째 인덱스의 버튼이 눌리면 어떻게 수행하고 ... 

하는 식으로 하나하나 조건문을 통해서 정해주었는데 이렇게 하면 사람이 코드를 치는 것이기 때문에 코드가 길다면 실수가 나올 수 밖에 없다.

#### 처음 짠 코드
    
    elif key in constantList:
        if self.display.text().isdigit():
            self.display.setText(self.display.text() + "*" + constantList[key])
        else:
            self.display.setText(self.display.text() + constantList[key])

    elif key in functionList:
        self.display.setText(functionList[key](self.display.text()))

constantList 와 functionList에 누른 키가 있으면 그 텍스트에 대치되는 상수, 혹은 함수가 나올 수 있게끔 사전형식으로 정리해서 사용을 했었다.

두번째 아이디어는 사전에(constantList, functionList에) 접근할 때 인덱스로 접근하는 방법이 있었다.

하지만 위의 두가지 방법엔 각각의 단점이 존재했다.
텍스트로 대치하여 상수와 함수를 불러오는 경우 다른나라에 코드를 수출할 때 언어별로 해줘야하는데 오타가 하나라도 존재하면 오류가 났다.
인덱스로 접근하면 이러한 문제는 해결할 수 있다 오타가 날 걱정을 하지 않아도 되기 때문이다. 하지만 상수(혹은 함수)의 순서가 바뀌거나 내용이 빠지거나 추가될 때 인덱스가 밀린다는 단점도 존재했다.

그래서 아예 constantList를 만들 때 컴퓨터가 묵묵히 제일 잘 하는 일인, 정확하고 빠른 반복문을 통해서 만들었다.
상수와 함수의 버튼에 들어갈 텍스트들만 모아놓은 list 인 constantList, functionList. 그리고 그 텍스트와 실제 상수값(혹은 함수의 내용) 을 key와 value로 담은 사전을 constantValue, functionMethods로 반복문을 통해서 만들어 주었다.(keypad2.py에)

위의 keypad2.py 코드에서 볼 수 있듯이 constantMap, functionMap이라는 튜플의 리스트를 만든다음에 이 리스트를 통해서 새로운 constantList, constantValues 그리고 functionList, functionMethods를 만들어 주는 것이다.

#### 수정한 코드

    elif key in constantList:
        if self.display.text().isdigit():
            self.display.setText(self.display.text() + "*" + constantValues[key])
        else:
            self.display.setText(self.difplay.text() + constantValues[key])
    elif key in functionList:
        self.display.setText(functionMethods[key](self.display.text()))

로 조건문의 실행 코드의 변화가 생겼다. 그리고 import문에서도 기존에 없었던 constantValues, functionMethods가 추가되었다.


### isdigit(),,,?

코드 중간에 계속 isdigit()을 사용한 조건문이 한개 더 보일 것이다.
상수 키를 눌렀을 때의 조건문 안에 이 조건문을 한개 더 넣어준 것이다.
상수 버튼을 눌렀을 때, 그 당시의 결과창의 내용이 숫자로 바뀔 수 있다면 그 내용에다가 "*" 를 해주고 그 후에 상수를 추가해주었다.
즉 "(현재 결과창에 있는 수)*(현재 누른 상수의 값)"으로 표현하여 결과창에 나타나도록 한 것이다. 

실제 우리가 수학에서 3파이라고 그냥 말하기 때문에 3을 누른 후에 곱하기를 따로 누르지 않아도 상수를 누르면 편하게 계산할 수 있도록 이 조건문을 추가해 준 것이다.

하지만 3 다음에 파이를 누르면 되지만, 순서를 반대로하여 하면 되지 않는 다는 문제를 발견하였고 아직은 여러모로 애매한 해결책인 것 같아서 더 개선해야할 것 같다.
