# assn2.py GUI 보고서.

## def initUI(self):

class 가 생성 되면 생성자 메소드에서 연결되는 UI생성자라고 볼 수 있다.
QLabels, QTextEdit(결과 출력창), QLineEdit(내용 입력창), QComboBox(정렬기준), QPushButton(기능 수행 버튼들) 객체를 만들어준다.

만들어진 각각의 버튼들을 button.clicked.connect(self.(method_name))을 통해서 기능을 수행하는 메소드와 연결시켜준다.

hbox레이아웃과 vbox레이아웃을 만들어서 vbox 에 hbox를 전부 넣어준 후, hbox에 전에 만들어준 (QLables 등등) widget들을 넣어준다.

## def doScoreDB(self):
각각의 다른 메소드에서 결국에는 마지막에 같은 메소드를 호출하는 생각.

버튼을 눌렀을 때 수행하는 작업들이 공통적으로 수행하는 기능을 몰아서 doScoreDB 메소드를 만든 후에, 각각의 버튼 수행 메소드에서 doScoreDB메소드로 연결될 수 있도록 해준다.

### 이전의 코드
    def doScoreDB(self):
        self.txtResult.clear()
        temp_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.cbo.currentText()]):
            for attr in sorted(p):
                temp_str += (str(attr) + "=" + str(p[attr])) + "\t"
            temp_str += "\n"
        self.txtResult.append(temp_str)

### 새로운 코드
    def doScoreDB(self):
	temp_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.cbo.currentText()]):
            for attr in sorted(p):
                temp_str += (str(attr) + "=" + str(p[attr])) + "\t"
            temp_str += "\n"
        self.txtResult.setText(temp_str)

#### 기능 
scoredb안의 내용을 QComboBox의 값을 기준으로 정렬한 것을 일정한 형식을 갖춘 문자열로 더해가며 마지막
결과 창에 반환한다.

#### 변화점.

기존의 코드에서는 doScoreDB를 수행할 때 처음에 결과창을 비워주고 정렬을 통해 원하는 형식의 문자열을 얻은 다음에 현재 비어있는 결과창에 내용을 더해주는 형식이었다.

새로운 코드에서는 처음에 결과창을 따로 비워주지 않고, 정렬을 통해 원하는 형식의 문자열을 얻은 다음에 결과창의 내용을 그 문자열로 바로 설정해준다.

바꾼이유:
	결과창을 한번 비워주고 거기에 내용을 추가하는것 -> 결과창의 내용을 새로 설정해 주는것
	이기 때문에 처음에 결과창을 한 번 더 비워주는 수고를 덜어준다.

## def Click_addbutton(self):

### 최종 메소드

    def Click_addbutton(self):
	try:
            chart = {"Name": self.NameLe.text(), "Age": int(self.AgeLe.text()), "Score": int(self.ScoreLe.text())}
            self.scoredb += [chart]
            self.doScoreDB()
            self.clearLE()
        except ValueError:
            self.txtResult.setText("Name, Age, Score 입력 창을 확인해주세요.")

#### 기능

addbutton을 눌렀을 때 내용 입력 창에 있는 세가지 내용을 scoredb에 추가하고 그 결과를 결과 창에 보여준다.
chart 라는 사전에 키와 밸류 값으로 내용 입력창에 있는 내용을 가져와서 scoredb에 추가하고, (doScoreDB를 통해) QCombo값을 기준으로 정렬하고 정해진 형식의 문자열로 결과창에 반환한다. 그리고 내용입력창(LineEdit)의 내용은 지워준다.

#### 고난과 역경

처음 코드를 짤 때 chart = {"Name": self.NameLe.text(), "Age": (self.AgeLe.text()), "Score": (self.ScoreLe.text())} 와 같이 짜게 되었는데, doScoreDB를 통해서 정렬을 하고 결과를 보여줄 때 정렬 기준 값이 age혹은, score인 경우에는 정렬이 이상하게 되었다.
예를 들어서 Lee 12 100, Oh 4 120 인 경우에 age값을 기준으로 정렬을 하려고 QCombo의 값을 age로 해주고 정렬을 했다.
원하는 결과 값인 Oh 4 120, Lee 12 100이 아닌 Lee 12 100, Oh 4 120이 결과로 나오게 되었다. 여러 다른 케이스를 실행해보고 검토해본 결과 age값이 정수형 숫자로 되어있고, 숫자로 정렬된것이 아니었다. age값이 문자열로 되어있었고, 그에따라 '4'가 '12'보다 크다고 인식하여서 원하는 정렬값이 나오지 않는 것이었다.
그래서 addbutton을 통해서 db에 값을 넣어줄 때 int로 넣어주기만 하면 후에도 계속 int로 사용이 가능하기 때문에  age, score은 int형으로 값을 받아 넣어주었다.

#### 예외처리

강제 종료되는 순간:
	add button에서 필수적인 세가지 값 name age score에 오류가 있을 때 강제종료 된다.
(세개중에 하나라도 입력을 안했을 때, 세개를 다 입력하더라고 age, score에 숫자가 아닌 것이 들어왔을 때)

ValueError이길래 예외처리를 통해서 결과창에 내용입력창을 확인해달라는 문구를 보여주도록 만들었다.


## def Click_delbutton(self):

    def Click_delbutton(self):
	newlist = []

        for i in self.scoredb:
            if i["Name"] != self.NameLe.text():
                newlist.append(i)
        self.scoredb = newlist

        self.doScoreDB()
        self.clearLE()

처음 코드를 짤 때 remove()를 통해서 기존의 리스트에서 삭제하는 방식으로 하려고 하였다.
하지만 remove를 하는 과정에서 반복문을 도는 도중에 삭제가 되어 맞지 않는 바람에 하나만 삭제되었다.
그래서 새로운 리스트에 추가하는 방식을 통해서 구현하였다.

## def Click_findbutton(self):

    def Click_findbutton(self):
        temp_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.cbo.currentText()]):
            if p["Name"] == self.NameLe.text():
                for attr in sorted(p):
                    temp_str += str(attr) + "=" + str(p[attr]) + '\t'
                temp_str += '\n'

        self.txtResult.setText(temp_str)	
 
doScoreDB에서 사용된 알고리즘과 비슷한 알고리즘이다. name LineEdit에 있는 내용과 같으면 원하는 형태의 스트링으로 저장하여 출력해주는 기능을 한다.

find 버튼을 누른 뒤에는 LineEdit에 있는 내용이 사라지지 않게하여 사용자로 하여금 무엇을 찾고있는지 까먹지 않도록 도움을 주고 싶어서 self.clearLE()를 해주지 않았다.

이 메소드도 마찬가지로 처음에는 clear(), append()를 통해 결과창을 보여줬지만 setText()를 통해서 코드와 알고리즘을 간결하게 바꿨다.

## def Click_incbutton(self):

    def Click_incbutton(self):
        try:

            for i in self.scoredb:
                if i["Name"] == self.NameLe.text():
                    i["Score"] = (int(i["Score"]) + int(self.AmountLe.text()))
            self.doScoreDB()
            #Inc 버튼을 누른 후에는 LineEdit에 있는 내용이 안 사라졌으면 좋겠다.
	    #그래서 LineEdit청소 안해줬음.
        except ValueError:
            self.txtResult.setText("Amount 입력창에 숫자 값을 넣었는지 확인해 주세요.")

name LineEdit에 써져 있는 내용과 db에 있는사람이 같으면 amount만큼 모두 증가시켜 준다.
scoredb를 전부 돌면서 조건문을 통해서 LineEdit에 써있는 내용과 같으면 amount만큼 증가시켜준 후에 doScoreDB를 통해서 정렬과 출력을 해준다.

#### clearLE()

inc button도 사용자가 전에 입력했던 내용을 알 수 있도록 clearLE()는 해주지 않았다.

#### 예외처리

amount 입력창에 아무것도 입력하지 않았을 때, 문자를 입력했을 때
모두 ValueError이기 때문에 ValueError처리에서 amount 입력창에 숫자로된 값을 제대로 넣었는지 확인해달라는 문구를 출력하도록 만들었다.

## def Click_showbutton(self):


    def Click_showbutton(self):
        self.doScoreDB()
        # 정렬 값에 따라서 보여준 후에 LineEdit에 있는 내용을 없애 주는게 좋겠음.
        self.clearLE()

#### 기능
QComboBox에 있는 정렬값을 기준으로 정렬하고 출력해준다.
하지만 doScoreDB()에서 전부 해주는 기능이므로 self.doScoreDB를 통해서 메소드를 호출해준다.

#### clearLE()
입력창은 깔끔하게 정리해주는 것이 좋을 것 같아서 self.clearLE()를 해준다.

## def Click_clearLE(self):

    def clearLE(self):
        self.NameLe.setText("")
        self.AgeLe.setText("")
        self.ScoreLe.setText("")
        self.AmountLe.setText("")

#### 기능
Line Edit에 있는 모든내용을 지워준다.


# 바뀐점.

## esc키를 눌렀을 대 창이 꺼지도록 만들기.

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()
#### 기능
키보드의 esc키를 눌렀을 때 열려져있는 GUI창이 닫히도록 한다.

## clear(), append(tmp) -> setText(tmp)

doScoreDB 메소드 혹은 Click_findbutton 메소드에서 결과창의 내용을 바꿔주기 위해서 clear()을 처음에 해주고 마지막에 append(tmp)를 함으로써 수행했던 것을 setText(tmp)를 통해서 조금이나마 더 간결한 코드 조금 더 간결한 알고리즘으로 바꿔 주었다.

## 예외처리.

버튼들을 눌렀을 때 의도치 않은 오류로 인해서 강제로 창이 종료되는 경우가 있다. 
-추가버튼:
	1. 필수 입력 세개중에 하나라도 입력을 안했을 때
	2. 세개를 다 입력해도 age, score에 숫자가 아닌 것이 들어갔을 때

-증가버튼
	1. amount에 아무것도 입력하지 않았을 때, amount에 문자를 입력했을 때

try except를 통해서 
ValueError가 발생하면 결과창에 다음과 같이 출력한다.
-추가버튼
	-> Name, Age, Score 입력 창을 확인해주세요.

-증가버튼
	-> Amount 입력창에 숫자 값을 넣었는지 확인해주세요.

## clearLE()

clearLE() (내용 입력창의 내용을 다 지워주는 메소드) 를  find, inc, show 버튼 메소드에서 사용할지 말지의 여부를 생각하여 clearLE() 메소드를 추가, 혹은 추가하지 않았다.
