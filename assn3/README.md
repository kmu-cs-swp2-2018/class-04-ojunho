# assn3 Calculator Assignment1

## 처음 짤 때 추가한 코드.


### 고치기 전
class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(35)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]
        self.digitButton[0] = Button('0', self.buttonClicked)
        self.digitButton[1] = Button('1', self.buttonClicked)
        self.digitButton[2] = Button('2', self.buttonClicked)
        self.digitButton[3] = Button('3', self.buttonClicked)
        self.digitButton[4] = Button('4', self.buttonClicked)
        self.digitButton[5] = Button('5', self.buttonClicked)
        self.digitButton[6] = Button('6', self.buttonClicked)
        self.digitButton[7] = Button('7', self.buttonClicked)
        self.digitButton[8] = Button('8', self.buttonClicked)
        self.digitButton[9] = Button('9', self.buttonClicked)

 위와 같았던 코드를 아래와 같이  for loop을 통해서 버튼을 생성하였다.


### 고친 후
    class Calculator(QWidget):
        def __init__(self, parent=None):
            self.digitButton = [x for x in range(0, 10)]
        
            for i in range(10):
	        self.digitButton[i] = Button(str(i), self.buttonClicked)



### 고치기 전
    def __init__(self, parent=None):
   	numLayout.addWidget(self.digitButton[0], 3, 0)
    	numLayout.addWidget(self.digitButton[1], 2, 0)
    	numLayout.addWidget(self.digitButton[2], 2, 1)
    	numLayout.addWidget(self.digitButton[3], 2, 2)
    	numLayout.addWidget(self.digitButton[4], 1, 0)
    	numLayout.addWidget(self.digitButton[5], 1, 1)
    	numLayout.addWidget(self.digitButton[6], 1, 2)
    	numLayout.addWidget(self.digitButton[7], 0, 0)
    	numLayout.addWidget(self.digitButton[8], 0, 1)
    	numLayout.addWidget(self.digitButton[9], 0, 2)

### 고치고 난 후
    def __init__(self. parent=None):
    	for i in range(1, 10):
		numLayout.addWidget(self.digitButton[i], (10 - (i + 1)) // 3, (i - 1)%3)

행과 열을 설정하여 3으로 나눴을 때의 몫과 나머지를 활용하여 숫자의 배열을 완성해준다.






## 코드리뷰 이후

### 예외처리.
	def buttonClicked(self):

		#a, b에 Error message를 미리 몰아서 할당해 줌으로써 나중에 오타로 인해 생기는 불상사를 방지할 수 있도록 한다.
        	a = "you can't divide it into zero"
        	b = "Write down the formula correctly"

        	button = self.sender()
        	key = button.text()

        	# 어떠한 키를 누르던 결과 창의 내용이 에러 메세지 a, b이면 결과 창을 비우고 시작한다.
        	if self.display.text() == a or self.display.text() == b:
            	self.display.setText("")

        	# "="를 누르면 일단 계산을 하도록 노력하고, 에러 두가지가 나타날 경우에 각각의 경우에 따른 에러 메시지를 결과창에 표시하도록 설계해준다.
        	if key == '=':
            	    try:
                	result = str(eval(self.display.text()))
                	self.display.setText(result)

           	    # 0으로 나눈 경우
           	    except ZeroDivisionError:
               	         self.display.setText(a)

           	    # 계산이 안되는 식을 써놓고 "="을 누른경우. 문법오류.
            	    except SyntaxError:
                	self.display.setText(b)

        	elif key == 'C':
            		self.display.setText("")
        	else:
            		self.display.setText(self.display.text() + key)


계산을 할 때 0으로 나누거나, 계산이 안되는 식을 계산하려고 할 때 각각 ZeroDivisionError, SyntaxError가 나타났다. 예외처리를 통해서 결과창에 문구를 통해 표시하도록 하였다. 

표시할 에러 메시지를 변수에 할당해 줌으로써 재사용할 때 예상치못한 오타로 인해서 불상사를 겪지 않도록 해준다. 메시지의 일부분이 바뀌어도 그 메시지만 바꿔주면 다른 곳에서는 처리해줄 필요가 없다.

또한 에러 메시지를 표시한 후에 지워주지 않으면 그 후에 숫자, 혹은 연산이 이어서 표시되기 때문에 buttonClicked 메소드에서 결과창이 에러메시지이면 지우고 시작하도록 해준다.

또한 예외처리 이후 곤란한 상황 (의도한대로 코드가 진행되는 것이 아니라, 왜 에러 메시지 이후에 숫자나 연산자를 입력해도 아무런 일이 일어나지 않는지 모르는 상황)이 발생하지 않기 위해서 결과 표시창의 길이 제한을 늘려주었다.

제한이 적으면 에러메시지 이후에 숫자가 이어서 적어지지 않는다. 만약 그대로 왜 그런지도 모르고 코딩을 이어서 한다면 안되기 때문에 길이의 제한을 늘려놓는다.


### 코드의 의도가 보이도록 직관적으로 코드를 짰는가.

row column과 같이 변수의 이름을 잘 설정함으로써 직관적으로 보이도록할 수 있다.

#### 처음 고친 코드.

    def __init__(self. parent=None):
        for i in range(1, 10):
            numLayout.addWidget(self.digitButton[i], (10 - (i + 1)) // 3, (i - 1)%3)

#### 다시 고친 코드.

    def __init__(self. parent=None):
        for i in range(1, 10):
            row = (10 - (i + 1))//3
	    column = (i - 1)%3
	    numLayout.addWidget(self.digitButton[i], row, column)


### Esc키를 누르면 창이 꺼지도록 해주었다.
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
             self.close()



### 추후에 더 개선하고 싶은 점.

실제 계산기는 한 번 계산을 한 이후에 연산식이 이어서 들어오면 전의 결과에 이어서 계산을 하고,
숫자가 들어오면 아예 새로운 계산을 시작하도록 한다.

현재 본인이 만든 계산기는 연산식이 들어오면 계산을 이어서 하긴하지만, 숫자를 넣었을 때는 전의 결과 뒤에 숫자가 이어진다.
Ex) 전의 계산결과 : 43    입력한 숫자: 3
원하는 전개: 3    실제 전개: 433

처럼 된다. 이 점을 실제 계산기 처럼 수행할 수 있도록 개선하려고 한다.

