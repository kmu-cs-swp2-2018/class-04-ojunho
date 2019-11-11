from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())  # word class 의 메소드 randFromDB를 사용하여 랜덤 단어를 하나 설정해주고 Guess class의 인자로 넣어준다. guess라는 Guess객체를 만들어준다.

    finished = False
    hangman = Hangman() #hangman이라는 Hangman객체를 만들어준다.
    maxTries = hangman.getLife() #최대 목숨을 maxTries라는 변수에 할당한다.







##
    while guess.currentStatus_Tries < maxTries:    #guess.numTries를 추가해준다...... ## 실제로 해주어야함.

        display = hangman.get(maxTries - guess.currentStatus_Tries)  #최대기회 - 현재 시도수 를 빼서 display객체에 넣어준다. 즉 남은 기회.

        print(display)

##
        guess.display()    #현재까지 맞춘 글자 상태, 실패한 횟수 정보를 출력 ......## 실제로 만들어야함.


        guessedChar = input('Select a letter: ')

        if len(guessedChar) != 1:
            print('One character at a time!')
            continue

        if guessedChar in guess.guessedChars:  # guessedChars에 이 문자가 들어있으면 이미 했다구 하구 다시 받는다.
            print('You already guessed \"' + guessedChar + '\"')
            continue



        finished = guess.guess(guessedChar)  #비밀 단어 안에 있으면 그 위치를 기록( 현재까지 맞춘 글자 상태) 비밀 단어 안에 없으면 실패 횟수 증가. 모든 글자를 다 맞추었으면 트루 아니면 폴스를 리턴.

        if finished == True:  # 모든 글자를 다 맞추었으니 while loop 을 끝내줌.
            break







    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()