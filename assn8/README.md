# assn8 Hangman3

## 과제1-1 : HangmanGame 클래스 구현의 완성
HangmanGame.guessClicked() 메소드의 구현 완성.

    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            # 메시지 출력하고 - message.setText() - 리턴
            self.message.setText("The game is over!")
            return 1
            pass

        # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if len(guessedChar) != 1:
            self.message.setText("Please enter only one character!")
            return 1
        
        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if guessedChar in self.guess.guessedChars:
            self.message.setText("already used \"" + guessedChar + "\"")
            return 1


        success = self.guess.guess(guessedChar)
        if success == False:
            # 남아 있는 목숨을 1 만큼 감소
            self.hangman.decreaseLife()

            # 메시지 출력
            self.message.setText("Incorrect")
            pass


        # hangmanWindow 에 현재 hangman 상태 그림을 출력
        # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
        # guessedChars 에 지금까지 이용한 글자들의 집합을 출력
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())


        if self.guess.finished():
            # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로
            self.message.setText("Success!")
            self.gameOver = True

            pass

        elif self.hangman.getRemainingLives() == 0:
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로
            self.message.setText("Fail! " + self.guess.secretWord)
            self.gameOver = True
            pass

if self.gameOver == True:
만약 게임이 끝난 상태에서 guess버튼을 누른다면. self.message.setText("The game is over!")를 해주어서 텍스트를 보여주고, return 값이 중요하지 않기 대문에 1을 리턴해준다.

입력의 길이가 1인지를 판단하고, 아닌경우에는 메시지를 출력한다, 리턴.
if len(guessedChar) != 1:
    self.message.setText("please enter only one charact")
    return 1
입력받은 문자의 길이가 1이 아닌경우에는 위와 같이 message.setText()를 해주고, return 1을 해주어서 메소드를 끝낸다.

이미 사용한 글자인지를 판단하고, 아닌경우 메시지를 출력한다. 리턴.
if guessedChar in self.guess.guessedChars:
    self.message.setText("already used \"" + guessedChar + "\"")
    return 1
사용자가 적은 글자가 이미 사용된 글자를 담고있는 집합에 있다면 다음과 같이 메시지만 하고 리턴하여 메소드를 종료한다.

위와같이 걸러낸 다음에 사용자가 입력한 문자로 본격적으로 guess를 한다. 

guess메소드를 사용하여 이 문자가 없으면 self.hangman.decreaseLife()를 사용해서 목숨을 1 감소시키고, 틀렸다는 메시지도 출력한다.

그리고 나서 
        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
를 해줌으로써 행맨 상태그림을 출력, 맞추어진 단어 상태를 출력, 이용한 글자들의 집합을 출력한다.

        if self.guess.finished():
            # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로
            self.message.setText("Success!")
            self.gameOver = True
그리고나서 self.guess.finished()를 사용하여 이 게임이 성공적으로 끝났으면 message를 "Success!"로 설정해주고,
gameover를 True로 바꿔준다.

        elif self.hangman.getRemainingLives() == 0:
            # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로
            self.message.setText("Fail! " + self.guess.secretWord)
            self.gameOver = True
            pass
그게아니라 목숨이 다 닳아서 실패했으면 message를 Fail과 정답을 알려주고, gameover를 True로 해준다.


## 과제1-2 : def keyPressEvent(self, e):

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

        if e.key() == Qt.Key_Return:
            self.guessClicked()
과제를 만들면서 esc키가 눌리면 창이 꺼지고, 엔터키를 누르면 guess버튼이 눌리게 하고 싶어서 이렇게 해주었다.


## 과제2: word class 기능의 확장. 일정 길이 이상의 단어만!

    def randFromDB(self, i):
        # r = random.randrange(self.count)
        # while len(self.words[r]) <
        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) <= i:
                break

        return self.words[r]
word class의 def randFromDB(self, i):
에서 인자로 i를 한개 더 주고 i(정수)보다 길이가 작은 문자열이 나올 때까지 무한반복문을 돌면서 랜덤으로 문자를 뽑는다.

    def startGame(self):
        self.hangman = Hangman()
        #길이를 해주었다.
        self.guess = Guess(self.word.randFromDB(10))
        self.gameOver = False

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()
그리고 나서 game class의 def startGame(self)에서 처음 Guess객체를 만들 때에도 인자로 10을 넣어주었다.

## 과제3: 버그의 제거. 길이가 긴 단어가 선택되면 전체가 보이지 않는 버그.(사용한 문자의 칸도 다보이지 않을 수 있음)

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        #setFixedWidth(500)을 해주었고, 그에 따라서 밑에 있는 lineEdit도 길어졌다.
        self.currentWord.setFixedWidth(500)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

HangmanGame class의 생성자 부분에서 QLineEdit()을 설정해주는 단계이다. 이 단계에서 self.currentWord.setFixedWidth(500)을 해주면 이 객체(QLineEdit())가 차지하는 공간도 커지고 전체 창의 크기도 커진다. 그에 따라서 밑의 길이도 커지게 되어 보이지 않는 버그는 줄어들었을 것이다.


# 코드리뷰 이후.
처음 짠 코드의 안타까운 점이 많았다.
1. 숫자, 영어가아닌 알파벳, 소문자가 아닌 대문자의 처리가 되지 않음.
2. word class의 무한반복문에 빠지지 않는 방법을 고안하지 못함.
3. 과제 2에서 word class를 수정할 때에 '최대한 (인자) 보다 작은 단어를 선택하도록' 으로 잘못 이해하고 코드를 짰음.


1. 숫자, 영어가아닌 알파벳, 소문자가 아닌 대문자의 처리가 되지 않음.
        if not 'a' <= guessedChar <= 'z':
            self.message.setText("Please enter lowercase English only")
            return
숫자와, 영어가 아닌 알파벳에 대한 처리를 해주었다. 'a' 'z'를 사용함으로써 소문자에 대한 처리도 되었다.
그리고
        #사용자에게 입력받은 문자를 소문자로 바꿔주었음.
        success = self.guess.guess(guessedChar.lower())
정상적으로 guess method를 사용할 때에 소문자로 바꿔주었다.

2. word class의 무한반복문에 빠지지 않는 방법을 고안하지 못함.
        maxLen = len(max(self.words, key = len))

        if i > maxLen:
            i = maxLen
randFromDB(self, i) 메소드인데, 인자로 입력받은 값이 너무 커서 무한 반복문에 빠지지 않도록, 단어의 최대 길이보다 입력받은 인자가 클 경우에는 i를 maxLen으로 설정해준 다음에 로직을 진행한다.

3. 과제 2에서 word class를 수정할 때에 '최대한 (인자) 보다 작은 단어를 선택하도록' 으로 잘못 이해하고 코드를 짰음.
그래서
        while True:
            r = random.randrange(self.count)
            if len(self.words[r]) >= i:
                break
로직을 수행할 때의 부등호 방향을 반대로 해주었다.





