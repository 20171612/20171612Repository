from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton, QComboBox, QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text,callback):  #callback추가
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(10):
            self.digitButton[i]=Button(str(i),self.buttonClicked)

        # . and = Buttons
        self.decButton = Button('.',self.buttonClicked)
        self.eqButton = Button('=',self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*',self.buttonClicked)
        self.divButton = Button('/',self.buttonClicked)
        self.addButton = Button('+',self.buttonClicked)
        self.subButton = Button('-',self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(',self.buttonClicked)
        self.rparButton = Button(')',self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C',self.buttonClicked)

        # special
        self.specialButton = Button('▶',self.buttonClicked)
        self.specialnum = QComboBox()
        self.specialfun = QComboBox()
        self.specialnumtext = QLabel('특수 상수')
        self.specialnumbutton = Button('입력',self.buttonClicked)
        self.specialfuntext = QLabel('특수 함수')
        self.specialfunbutton = Button('입력',self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)


        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addWidget(self.specialnumtext, 2, 0,1,1)
        mainLayout.addWidget(self.specialnumbutton, 3, 1,1,1)
        mainLayout.addWidget(self.specialnum, 3, 0, 1, 1)
        mainLayout.addWidget(self.specialfuntext, 4, 0)
        mainLayout.addWidget(self.specialfunbutton, 5, 1)  #입력버튼 위치수정
        mainLayout.addWidget(self.specialfun, 5, 0, 1, 1)


        numLayout = QGridLayout()

        for i in range(1,10):
            numLayout.addWidget(self.digitButton[i], (9-i)//3+1, (i+2)%3)
        numLayout.addWidget(self.digitButton[0], 4, 1)

        numLayout.addWidget(self.clearButton, 0, 0)
        numLayout.addWidget(self.lparButton, 0, 1)
        numLayout.addWidget(self.rparButton, 0, 2)
        numLayout.addWidget(self.divButton, 0, 3)
        numLayout.addWidget(self.decButton, 1, 3)
        numLayout.addWidget(self.mulButton, 2, 3)
        numLayout.addWidget(self.subButton, 3, 3)
        numLayout.addWidget(self.addButton, 4, 3)
        numLayout.addWidget(self.eqButton, 4, 2)
        numLayout.addWidget(self.specialButton, 4, 0)
        mainLayout.addLayout(numLayout, 1, 0)


        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")
    #버튼클릭 메서드 추
    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        try:
            if self.display.text() == ('잘못된 수식입니다'):
                self.display.clear()
            if key == '=':
                result = str(eval(self.display.text()))
                self.display.setText(result)
            elif key == 'C':
                self.display.clear()
            elif key == '▶':
                self.display.setText(self.display.text()[:-1])  #지우기버튼 메서드 구현
            elif key == '입력':
                pass    #나중에 특수상수,함수추가하기 버튼 추가하
            else:
                self.display.setText(self.display.text() + key)
        except SyntaxError:
            self.display.setText('잘못된 수식입니다')


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

