import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)

class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
    def initUI(self):

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        name = QLabel('Name:')
        self.nameline = QLineEdit()
        age = QLabel('Age:')
        self.ageline = QLineEdit()
        score = QLabel('Score:')
        self.scoreline = QLineEdit()
        hbox1list = [name,self.nameline,age,self.ageline,score,self.scoreline]
        for i in hbox1list:
            hbox1.addWidget(i)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        amount = QLabel('Amout:')
        key = QLabel('Key:')
        self.amountline = QLineEdit()
        self.keycombo = QComboBox()
        self.keycombo.addItems(['Age','Name','Score'])
        hbox2list = [amount,self.amountline,key,self.keycombo]
        hbox2.addStretch(1)
        for i in hbox2list:
            hbox2.addWidget(i)
        vbox.addLayout(hbox2)

        self.addkey = QPushButton('Add')
        self.delkey = QPushButton('Del')
        self.findkey = QPushButton('Find')
        self.inckey = QPushButton('Inc')
        self.showkey = QPushButton('Show')
        hbox3list = [self.addkey, self.delkey, self.findkey, self.inckey, self.showkey]
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        for i in hbox3list:
            hbox3.addWidget(i)
        vbox.addLayout(hbox3)

        hbox4 = QHBoxLayout()
        result = QLabel('Result:')
        self.errortext = QLabel('')
        hbox4.addWidget(result)
        hbox4.addStretch(1)
        hbox4.addWidget(self.errortext)
        vbox.addLayout(hbox4)

        self.addkey.clicked.connect(self.addkey_clicked)
        self.showkey.clicked.connect(self.showkey_clicked)
        self.delkey.clicked.connect(self.delkey_clicked)
        self.findkey.clicked.connect(self.findkey_clicked)
        self.inckey.clicked.connect(self.inckey_clicked)

        hbox5 = QHBoxLayout()
        self.text = QTextEdit()
        hbox5.addWidget(self.text)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()
        return

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  []
            db = []
            while True:
                try:
                    data = pickle.load(fH)
                except EOFError:
                    break
                db.append(data)
        except:
            pass
        else:
            pass
        for line in db:
            dat = line.strip()
            person = dat.split(",")
            record = {}
            for attr in person:
                kv = attr.split(":")
                record[kv[0]] = kv[1]
            self.scoredb += [record]
        fH.close()
        return self.scoredb


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        for p in self.scoredb:
            pinfo = []
            for attr in p:
                pinfo += [attr + ":" + p[attr]]
            line = ','.join(pinfo)
            pickle.dump(line + '\n', fH)
        fH.close()

    def addkey_clicked(self):
        try:
            int(self.ageline.text())
            int(self.scoreline.text())
            if self.nameline.text() != '':
                record = {'Age':self.ageline.text() ,'Name': self.nameline.text(), 'Score': self.scoreline.text()}
                self.scoredb += [record]
                self.showkey_clicked()
                self.errortext.clear()
            else:
                self.errortext.setText('Please enter a name to add')
        except ValueError:
            self.errortext.setText('Please enter your age and score as an integer')

    def delkey_clicked(self):
        n = 0
        for i in self.scoredb[:]:
            if self.nameline.text() == i['Name']:
                self.scoredb.remove(i)
                n += 1
        if n == 0:
            self.errortext.setText("Can't found name to delete")
        else:
            self.errortext.clear()
            self.showkey_clicked()

    def findkey_clicked(self):
        n = 0
        findnames = ''
        for p in self.scoredb[:]:
            if self.nameline.text() == p['Name']:
                for attr in sorted(p):
                    findnames += (attr + "=" + p[attr] + '       ')
                findnames += ('\n')
                n +=1
        if n == 0:
            self.errortext.setText("Can't found name")
        else:
            self.errortext.clear()
            self.text.setText(findnames)

    def inckey_clicked(self):
        n = 0
        try:
            for i in self.scoredb:
                if i['Name'] == self.nameline.text():
                    i['Score'] = str(int(i['Score']) + int(self.amountline.text()))
                    n += 1
            if n == 0:
                self.errortext.setText("Can't found name to increase")
            else:
                self.errortext.clear()
                self.showkey_clicked()
        except ValueError:
            self.errortext.setText('Enter the amount as integer')

    def showkey_clicked(self):
        returntext = ''
        for p in sorted(self.scoredb, key=lambda person: person[self.keycombo.currentText()]):
            for attr in sorted(p):
                returntext += (attr + "=" + p[attr]+'       ')
            returntext += ('\n')
        self.text.setText(returntext)
        self.errortext.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())