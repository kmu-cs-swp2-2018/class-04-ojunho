import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    #생성자 메소드.
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    #UI 생성자 메소드.
    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        #QLables
        lblname = QLabel('Name: ')
        lblage = QLabel('Age: ')
        lblscore = QLabel('Score: ')
        lblamount = QLabel('Amount: ')
        lblkey = QLabel('Key: ')
        lblresult = QLabel('Result: ')

        #QTextEdit
        self.txtResult = QTextEdit()

        #QlineEdit
        self.NameLe = QLineEdit()
        self.AgeLe = QLineEdit()
        self.ScoreLe = QLineEdit()
        self.AmountLe = QLineEdit()

        #QComboBox
        self.cbo = QComboBox()
        self.cbo.addItems(["Name", "Age", "Score"])

        #QPushButton
        addbutton = QPushButton("Add")
        delbutton = QPushButton("Del")
        findbutton = QPushButton("Find")
        incbutton = QPushButton("Inc")
        showbutton = QPushButton("Show")

        #각각의 Button들을 기능을 수행하는 메소드와 연결시켜준다.
        addbutton.clicked.connect(self.Click_addbutton)
        delbutton.clicked.connect(self.Click_delbutton)
        findbutton.clicked.connect(self.Click_findbutton)
        incbutton.clicked.connect(self.Click_incbutton)
        showbutton.clicked.connect(self.Click_showbutton)

        #hbox 레이아웃 만들기.
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()

        #hbox2,3을 오른쪽 끝으로 밀어주기.
        #hbox2, 3만 오른쪽 끝으로 밀어주면 될 것 같아서 두개만 진행하였다.
        hbox2.addStretch(1)
        hbox3.addStretch(1)

        #vbox 레이아웃 만들기.
        vbox = QVBoxLayout()

        #vbox에 hbox전부 집어넣기.
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        #각각의 hbox에 widget들 넣어주기.
        #hbox1
        hbox1.addWidget(lblname)
        hbox1.addWidget(self.NameLe)
        hbox1.addWidget(lblage)
        hbox1.addWidget(self.AgeLe)
        hbox1.addWidget(lblscore)
        hbox1.addWidget(self.ScoreLe)

        #hbox2
        hbox2.addWidget(lblamount)
        hbox2.addWidget(self.AmountLe)
        hbox2.addWidget(lblkey)
        hbox2.addWidget(self.cbo)

        #hbox3
        hbox3.addWidget(addbutton)
        hbox3.addWidget(delbutton)
        hbox3.addWidget(findbutton)
        hbox3.addWidget(incbutton)
        hbox3.addWidget(showbutton)

        #hbox4
        hbox4.addWidget(lblresult)

        #hbox5
        hbox5.addWidget(self.txtResult)

        self.setLayout(vbox)
        self.show()

    #esc키를 입력했을 때 창이 꺼지도록 만들기.
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

    #add button을 클릭했을 때
    def Click_addbutton(self):
        #chart는 사전이다. scoredb라는 리스트에 사전들을 넣어준다.
        #애초에 값을 받을 때 인티져로 해주어야 나중에 나오는 doScoreDB메소드에서 그리고 몇몇의 메소드에서 key값으로 정렬을 할 때 좋다.
        #예외 처리를 통해서 LineEdit에 정해진 대로 수행하지 않으면 "입력창을 확인해 주세요" 라는 말을 결과 창에 보여주게 된다.
        try:
            chart = {"Name": self.NameLe.text(), "Age": int(self.AgeLe.text()), "Score": int(self.ScoreLe.text())}
            self.scoredb += [chart]
            self.doScoreDB()
            self.clearLE()
        except ValueError:
            self.txtResult.setText("Name, Age, Score 입력 창을 확인해주세요.")


    #del button을 클릭했을 때.
    def Click_delbutton(self):
        #처음에는 기존의 리스트에서 삭제하는 방식으로 하려고 했으나.
        #remove를 하는 과정에서 오류가 계속 생겨서 새로운 리스트에 추가하는 방식으로 바꾸었다.
        newlist = []

        for i in self.scoredb:
            if i["Name"] != self.NameLe.text():
                newlist.append(i)
        self.scoredb = newlist

        self.doScoreDB()
        self.clearLE()



    def Click_findbutton(self):
        temp_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.cbo.currentText()]):
            if p["Name"] == self.NameLe.text():
                for attr in sorted(p):
                    temp_str += str(attr) + "=" + str(p[attr]) + '\t'
                temp_str += '\n'

        self.txtResult.setText(temp_str)
        #Find Button을 누른 후에 LineEdit에 있는 내용이 안 사라졌으면 좋겠다.
	#그래서 LineEdit청소 안해줬음.



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


    def Click_showbutton(self):
        self.doScoreDB()
        # 정렬 값에 따라서 보여준 후에 LineEdit에 있는 내용을 없애 주는게 좋겠음.
        self.clearLE()


    def clearLE(self):
        self.NameLe.setText("")
        self.AgeLe.setText("")
        self.ScoreLe.setText("")
        self.AmountLe.setText("")


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.doScoreDB()




    def doScoreDB(self):
        temp_str = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.cbo.currentText()]):
            for attr in sorted(p):
                temp_str += (str(attr) + "=" + str(p[attr])) + "\t"
            temp_str += "\n"
        self.txtResult.setText(temp_str)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
