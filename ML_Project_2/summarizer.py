from PyQt5 import QtCore, QtGui, QtWidgets

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 1271, 381))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 540, 1271, 231))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 410, 461, 101))
        self.pushButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Generate Summary"))

        self.pushButton.clicked.connect(self.generateSummary)

    def generateSummary(self):
        text = self.textEdit.toPlainText()
        words = word_tokenize(text)
        sentences = sent_tokenize(text)
        sWords = set(stopwords.words("english"))
        w_net = WordNetLemmatizer()

        freq_dist = dict()

        for word in words:
            word = word.lower()

            if word in sWords:
                continue

            word = w_net.lemmatize(word, pos='v')

            if word in freq_dist:
                freq_dist[word] += 1
            else:
                freq_dist[word] = 1

        sent_dist = dict()

        for sentence in sentences:
            for word, freq in freq_dist.items():
                if word in sentence:
                    if sentence in sent_dist:
                        print("Word =>", word)
                        print("Sentence =>", sentence)
                        sent_dist[sentence] += freq
                    else:
                        print("Word =>", word)
                        print("Sentence =>", sentence)
                        sent_dist[sentence] = freq

        avg = int(sum(sent_dist.values()) / len(sent_dist))
        summary = ""
        for sentence in sentences:
            if sent_dist[sentence] > avg * 1.1:
                #         print(sentence)
                summary += " " + sentence

        self.textEdit_2.setText(summary)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

