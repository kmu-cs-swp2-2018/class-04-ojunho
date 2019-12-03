#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from hangman import Hangman
from guess import Guess
from word import Word

#필요한 메서드들을 기능별로 나누어 구현.
class HangmanGame(QWidget):

    #UI및 필요한 것들 초기화.
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database        
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

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

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.hangman = Hangman()
        #길이를 해주었다.
        self.guess = Guess(self.word.randFromDB(40))
        self.gameOver = False

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())
        self.currentWord.setText(self.guess.displayCurrent())
        self.guessedChars.setText(self.guess.displayGuessed())
        self.message.clear()


    def guessClicked(self):
        guessedChar = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            # 메시지 출력하고 - message.setText() - 리턴
            self.message.setText("The game is over!")
            return -1

        # 입력의 길이가 1 인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if len(guessedChar) != 1:
            self.message.setText("Please enter only one character!")
            return 1
        
        # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
        if guessedChar in self.guess.guessedChars:
            self.message.setText("already used \"" + guessedChar + "\"")
            return 1

        if not 'a' <= guessedChar <= 'z':
            self.message.setText("Please enter lowercase English only")
            return

        #사용자에게 입력받은 문자를 소문자로 바꿔주었음.
        success = self.guess.guess(guessedChar.lower())
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

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

        if e.key() == Qt.Key_Return:
            self.guessClicked()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())

