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

    ('roman -> dec' , calcFunctions.romanToDec),

]

functionList = [i[0] for i in functionMap]
functionMethods = {i[0]: i[1] for i in functionMap}

