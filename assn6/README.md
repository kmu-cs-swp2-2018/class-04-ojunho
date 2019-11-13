# assn6 보고서

## Guess 생성자.

    def __init__(self, word):


        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = ""
        self.currentStatus_Current = "_"*len(self.secretWord)
        self.currentStatus_Tries = self.numTries #정수타입.

word method 에서 만든 Word 객체 word를 인자로 받아와서 secretWord에 저장해준다.
이미 사용한 글자를 담는 배열 guessedChars를 초기화해준다.
시도한 횟수 (정수)를 담는 numTries 라는 변수를 초기 값 0 으로 초기화 해준다.

현재까지의 상태를 보여주는 문장을  String 객체 currentStatus로 해주려고 하였으나.
currentStatus_Current, currentStatus_Tries의 두가지 정보를 더한 currentStatus를 만들어주려고 하였으나.
결국엔 각각 표시하도록하여서 currentStatus 를 사용할 일이 없어졌다.

currentStatus_Current는 실제 "Current: " 뒤에 현재까지 맞춘 글자는 알파벳으로, 아닌 글자는 "_"로 표기하여 나타내기 위해서 만든 String 객체이고 "_" 곱하기 단어의 길이만큼 해주어서 리셋해준다.

currentStatus_Tries는 전에 생성한 numTries를 받아오는 변수인데 굳이 이 할당은 해주지 않았어도 되었다.
오히려 할당해 줌으로써 문제가 발생하였다.
(currentStatus_Tries를 증가시키면서 프로그램을 돌렸는데, game클래스에서는 numTries로 가져왔기 때문에 Hangman클래스에서 Hangman그림을 그릴 때 목숨이 줄 때 그림이 점차 머리가 그려져야 하는데, 계속 인덱스 0의 그림(단두대만 그려지는 그림) 만 출력이 되는 문제가 발생하였다.)


## Guess display method.

    def display(self): # currentStatus 사용?

        print("Current : ", self.currentStatus_Current)
        print("Tries : ", self.currentStatus_Tries)
        print("Used : ", self.guessedChars)

ex)
Current : _pp_e
Tries : 0
Used : [p,e]

처럼 출력되도록 메소드를 만들어 주었다.


## Guess guess method


    def guess(self, character):
        self.guessedChars.append(character)
        if not character in self.secretWord:
            self.currentStatus_Tries += 1

        else:
            while character in self.secretWord:
                idx = self.secretWord.find(character)

                #while loop을 돌면서 계속 character을 지워주기 위해서.
                self.secretWord = self.secretWord.replace(character,"_",1)

                #slicing을 통해서 표시될 문장을 고쳐준다.
                self.currentStatus_Current = self.currentStatus_Current[:idx] + character + self.currentStatus_Current[idx + 1:]


                # self.currentStatus_Current = self.currentStatus_Current.replace()
                # self.currentStatus_Current[idx] = character



        if not "_" in self.currentStatus_Current:
            return True
        else:
            return False

guess method의 인자로 character를 받아오는데 character는 사용자가 입력한 글자이다.

우선 character는 이제 사용한 단어이기 때문에  guessedChars에 넣어준다.

조건문 if else를 크게 두개 돌게 된다.
처음의 조건문은 사용자가 입력한 글자가 맞춰야하는 비밀단어에 들어있는지의 여부에 따라서 명령을 실행한다.
만약에 비밀단어에 글자가 없으면 시도 수만 한번 증가시켜준다.
하지만 비밀단어에 글자가 있다면 이 비밀단어에 사용자가 입력한 단어 character가 있을 때 동안 while loop을 돌면서 비밀단어에서 character를 찾아서 다른 문자로 바꿔주면서 표시할 문장도 업데이트 해준다.

idx라는 변수에 character의 인덱스를 저장해준다. 그리고 비밀단어에서 왼쪽부터 character를 찾아서 하나만 "_"로 replace해준다.
또 String slicing을 통해서 currentStatus_Current를 고쳐준다(업데이트 해준다). 
처음에는 replace method를 사용할 때 self.secretWord.replace(character,"_") 라고만 해주고 뒤에 1을 적지 않았는데 그렇게 되면 character를 전부 _로 바꿔준다. 하나씩만 대체해 주어야 while loop 안에서 계속 지워줄 수 있다.(하나 씩 지워주는 이유는 find는 index를 하나씩밖에 못찾기 때문이다)

두번째 조건문은 현재까지 맞춘 상황을 나타낸 문자열의 "_"가 없으면, 즉 모든 글자를 맞추었을 때 True를 리턴하고, 아니라면 False를 리턴한다.



## 개선할 점.(개선한 점)

앞서 말했지만 이미 설정한 변수를 또 다른 변수에 설정하여 guess메소드에서 틀렸을 때 다시 할당한 변수의 값을 증가시켜주었지만, 객체의 값은 변화한 것이 아니기 때문에 game메소드 에서는 변하지 않은 값을 인자로 다시 Hangman메소드에서 그림을 가져왔었기 때문에 그 부분을 수정해주었다.



문자를 표시할 때 전부 "_"로 해주었더니 몇글자이지 보이지 않았다. 그래서 다른문자로의 변형, 띄어쓰기 추가, 혹은 글자수를 알려주기 등을 통해서 해결할 수 있을 것이다.

일단 글자수를 알려주는 방향으로 해결 하였지만, 추후 더 완벽한 방법을 추구할 것이다.


단어 맞추기에 실패했을 때 단어를 알려주지 않고 끝내서 상당히 test를 하면서 상당히 궁금증을 자아냈다. 실패했을 때 사용자에게 정답을 알려주도록 코드를 고칠 수 있을 것이다.

현재 guess method의 while문의 find와 slicing을 사용하기 때문에 시간복잡도가 높다. 자료형 구조를 잘 사용하여 들어온 character가 들어간 인덱스를 전부 저장하는 방법, join method를 사용하여 시간복잡도를 줄일 수 있을 것이다.

사용한 글자를 나타내는 리스트를 정렬을 해서 보여줄 까도 했지만, 정렬을 하지 않을 경우에 본인의 의식의 흐름이 보이기 때문에 굳이 정렬해 주지는 않았다.

많이 쓰이는 단어를 보여주는 방향, 그리고 문제를 푸는 사람에게 힌트를 제공하는 방향, 그리고 한글입력 혹은 숫자 입력의 오류를 처리하는 방향으로 수정을 할 수 있을 것이다.









