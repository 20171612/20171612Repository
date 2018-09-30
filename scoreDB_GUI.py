import pickle
import sys
from PyQt5.QtWidgets import *


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
        hbox1.addWidget(name)
        hbox1.addWidget(self.nameline)
        hbox1.addWidget(age)
        hbox1.addWidget(self.ageline)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreline)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        amount = QLabel('Amout:')
        key = QLabel('Key:')
        self.amountline = QLineEdit()
        self.keycombo = QComboBox()
        self.keycombo.addItems(['Age','Name','Score'])
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountline)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keycombo)
        vbox.addLayout(hbox2)

        self.addkey = QPushButton('Add')
        self.delkey = QPushButton('Del')
        self.findkey = QPushButton('Find')
        self.inckey = QPushButton('Inc')
        self.showkey = QPushButton('Show')
        keylist = [self.addkey, self.delkey, self.findkey, self.inckey, self.showkey]
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        for i in keylist:
            hbox3.addWidget(i)
        vbox.addLayout(hbox3)

        hbox4 = QHBoxLayout()
        result = QLabel('Result:')
        hbox4.addWidget(result)
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
            fH = open(self.dbfilename, 'r')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  []
        except:
            pass
        else:
            pass
        for line in fH:
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
        fH = open(self.dbfilename, 'w')
        for p in self.scoredb:
            pinfo = []
            for attr in p:
                pinfo += [attr + ":" + p[attr]]
            line = ','.join(pinfo)
            fH.write(line + '\n')
        fH.close()
        return

    def addkey_clicked(self):
        record = {'Age':self.ageline.text() ,'Name': self.nameline.text(), 'Score': self.scoreline.text()}
        self.scoredb += [record]

    def delkey_clicked(self):
        for i in self.scoredb[:]:
            if self.nameline.text() == i['Name']:
                self.scoredb.remove(i)
        return

    def findkey_clicked(self):
        findnames = ''
        for p in self.scoredb[:]:
            if self.nameline.text() == p['Name']:
                for attr in sorted(p):
                    findnames += (attr + "=" + p[attr] + '       ')
                findnames += ('\n')
        self.text.setText(findnames)
        return

    def inckey_clicked(self):
        for i in self.scoredb:
            if i['Name'] == self.nameline.text():
                i['Score'] = str(int(i['Score']) + int(self.amountline.text()))
        return

    def showkey_clicked(self):
        returntext = ''
        for p in sorted(self.scoredb, key=lambda person: person[self.keycombo.currentText()]):
            for attr in sorted(p):
                returntext += (attr + "=" + p[attr]+'       ')
            returntext += ('\n')
        self.text.setText(returntext)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    ex.readScoreDB()
    sys.exit(app.exec_())
