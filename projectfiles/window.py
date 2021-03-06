from PyQt5 import QtCore, QtGui, QtWidgets

def wr_setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(800, 623)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")


    self.startButton = QtWidgets.QPushButton(self.centralwidget)
    self.startButton.setGeometry(QtCore.QRect(600, 70, 121, 41))
    self.startButton.setObjectName("startButton")

    self.funkcja = QtWidgets.QPlainTextEdit(self.centralwidget)
    self.funkcja.setGeometry(QtCore.QRect(80, 70, 341, 31))
    self.funkcja.setPlainText("x1^2+x2^2")
    self.funkcja.setObjectName("funkcja")



    self.wynik = QtWidgets.QPlainTextEdit(self.centralwidget)
    self.wynik.setGeometry(QtCore.QRect(470, 390, 291, 192))
    self.wynik.setObjectName("wynik")

#estetyka
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(40, 70, 61, 31))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setObjectName("label")

    self.label_2 = QtWidgets.QLabel(self.centralwidget)
    self.label_2.setGeometry(QtCore.QRect(340, 0, 171, 41))
    font = QtGui.QFont()
    font.setFamily("MS Serif")
    font.setPointSize(17)
    font.setBold(True)
    font.setWeight(75)
    self.label_2.setFont(font)
    self.label_2.setObjectName("label_2")
    self.line = QtWidgets.QFrame(self.centralwidget)
    self.line.setGeometry(QtCore.QRect(-3, 120, 841, 20))
    self.line.setFrameShape(QtWidgets.QFrame.HLine)
    self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line.setObjectName("line")
    self.label_3 = QtWidgets.QLabel(self.centralwidget)
    self.label_3.setGeometry(QtCore.QRect(20, 140, 351, 20))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.label_3.setFont(font)
    self.label_3.setObjectName("label_3")
    self.line_2 = QtWidgets.QFrame(self.centralwidget)
    self.line_2.setGeometry(QtCore.QRect(410, 130, 16, 451))
    self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
    self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.line_2.setObjectName("line_2")
#ogranieczenia - pola do wpisania
    self.ogr1 = QtWidgets.QTextEdit(self.centralwidget)
    self.ogr1.setGeometry(QtCore.QRect(100, 190, 291, 31))
    self.ogr1.setPlainText("4-x1-x2")
    self.ogr1.setObjectName("ogr1")
    self.ogr2 = QtWidgets.QTextEdit(self.centralwidget)
    self.ogr2.setGeometry(QtCore.QRect(100, 230, 291, 31))

    self.ogr2.setObjectName("ogr2")
    self.ogr3 = QtWidgets.QTextEdit(self.centralwidget)
    self.ogr3.setGeometry(QtCore.QRect(100, 270, 291, 31))

    self.ogr3.setObjectName("ogr3")
    self.ogr4 = QtWidgets.QTextEdit(self.centralwidget)
    self.ogr4.setGeometry(QtCore.QRect(100, 310, 291, 31))

    self.ogr4.setObjectName("ogr4")
    self.ogr5 = QtWidgets.QTextEdit(self.centralwidget)
    self.ogr5.setGeometry(QtCore.QRect(100, 350, 291, 31))

    self.ogr5.setObjectName("ogr5")
#Napisy
    self.Ograniczenie1 = QtWidgets.QLabel(self.centralwidget)
    self.Ograniczenie1.setGeometry(QtCore.QRect(10, 190, 91, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.Ograniczenie1.setFont(font)
    self.Ograniczenie1.setObjectName("Ograniczenie1")
    self.Ograniczenie2 = QtWidgets.QLabel(self.centralwidget)
    self.Ograniczenie2.setGeometry(QtCore.QRect(10, 230, 91, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.Ograniczenie2.setFont(font)
    self.Ograniczenie2.setObjectName("Ograniczenie2")
    self.Ograniczenie3 = QtWidgets.QLabel(self.centralwidget)
    self.Ograniczenie3.setGeometry(QtCore.QRect(10, 270, 91, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.Ograniczenie3.setFont(font)
    self.Ograniczenie3.setObjectName("Ograniczenie3")
    self.Ograniczenie4 = QtWidgets.QLabel(self.centralwidget)
    self.Ograniczenie4.setGeometry(QtCore.QRect(10, 310, 91, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.Ograniczenie4.setFont(font)
    self.Ograniczenie4.setObjectName("Ograniczenie4")
    self.Ograniczenie5 = QtWidgets.QLabel(self.centralwidget)
    self.Ograniczenie5.setGeometry(QtCore.QRect(10, 350, 91, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.Ograniczenie5.setFont(font)
    self.Ograniczenie5.setObjectName("Ograniczenie5")
#napis wspolczynnikk
    self.wspolczynnikprzyblizen = QtWidgets.QLabel(self.centralwidget)
    self.wspolczynnikprzyblizen.setGeometry(QtCore.QRect(10, 390, 161, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.wspolczynnikprzyblizen.setFont(font)
    self.wspolczynnikprzyblizen.setObjectName("wspolczynnikprzyblizen")
#pole na r0
    self.r0 = QtWidgets.QTextEdit(self.centralwidget)
    self.r0.setGeometry(QtCore.QRect(170, 390, 221, 31))
    self.r0.setPlainText("1")
    self.r0.setObjectName("r0")
#napis punkt startowy
    self.label_10 = QtWidgets.QLabel(self.centralwidget)
    self.label_10.setGeometry(QtCore.QRect(460, 140, 191, 20))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.label_10.setFont(font)
    self.label_10.setObjectName("label_10")
#NAPISY x1,x2,x3,x4,x5
    self.x1 = QtWidgets.QLabel(self.centralwidget)
    self.x1.setGeometry(QtCore.QRect(440, 190, 21, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.x1.setFont(font)
    self.x1.setObjectName("x1")
    self.x2 = QtWidgets.QLabel(self.centralwidget)
    self.x2.setGeometry(QtCore.QRect(440, 230, 21, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.x2.setFont(font)
    self.x2.setObjectName("x2")
    self.x3 = QtWidgets.QLabel(self.centralwidget)
    self.x3.setGeometry(QtCore.QRect(440, 270, 21, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.x3.setFont(font)
    self.x3.setObjectName("x3")
    self.x4 = QtWidgets.QLabel(self.centralwidget)
    self.x4.setGeometry(QtCore.QRect(440, 310, 21, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.x4.setFont(font)
    self.x4.setObjectName("x4")
    self.x5 = QtWidgets.QLabel(self.centralwidget)
    self.x5.setGeometry(QtCore.QRect(440, 350, 21, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.x5.setFont(font)
    self.x5.setObjectName("x5")
#POLA NA PUNKTY STARTOWE
    self.x1i = QtWidgets.QTextEdit(self.centralwidget)
    self.x1i.setGeometry(QtCore.QRect(470, 190, 291, 31))
    self.x1i.setPlainText("3")
    self.x1i.setObjectName("x1i")
    self.x2i = QtWidgets.QTextEdit(self.centralwidget)
    self.x2i.setGeometry(QtCore.QRect(470, 230, 291, 31))
    self.x2i.setPlainText("3")
    self.x2i.setObjectName("x2i")
    self.x3i = QtWidgets.QTextEdit(self.centralwidget)
    self.x3i.setGeometry(QtCore.QRect(470, 270, 291, 31))
    self.x3i.setPlainText("3")
    self.x3i.setObjectName("x3i")
    self.x4i = QtWidgets.QTextEdit(self.centralwidget)
    self.x4i.setGeometry(QtCore.QRect(470, 310, 291, 31))
    self.x4i.setPlainText("3")
    self.x4i.setObjectName("x4i")
    self.x5i = QtWidgets.QTextEdit(self.centralwidget)
    self.x5i.setGeometry(QtCore.QRect(470, 350, 291, 31))
    self.x5i.setPlainText("3")
    self.x5i.setObjectName("x5i")
#NAPIS LICZBA ITERACJI
    self.liczbaiteracji = QtWidgets.QLabel(self.centralwidget)
    self.liczbaiteracji.setGeometry(QtCore.QRect(10, 430, 101, 21))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.liczbaiteracji.setFont(font)
    self.liczbaiteracji.setObjectName("liczbaiteracji")
#POLE NA L
    self.L = QtWidgets.QTextEdit(self.centralwidget)
    self.L.setGeometry(QtCore.QRect(110, 430, 281, 31))
    self.L.setPlainText("1000")
    self.L.setObjectName("L")
#NAPIS e1
    self.epsilon1 = QtWidgets.QLabel(self.centralwidget)
    self.epsilon1.setGeometry(QtCore.QRect(10, 470, 31, 21))
    font = QtGui.QFont()
    font.setPointSize(11)
    font.setBold(True)
    font.setWeight(75)
    self.epsilon1.setFont(font)
    self.epsilon1.setObjectName("epsilon1")
#POLE NA e1
    self.e1 = QtWidgets.QTextEdit(self.centralwidget)
    self.e1.setGeometry(QtCore.QRect(50, 470, 341, 31))
    self.e1.setPlainText("1e-11")
    self.e1.setObjectName("e1")
#NAPIS e2
    self.epsilon2 = QtWidgets.QLabel(self.centralwidget)
    self.epsilon2.setGeometry(QtCore.QRect(10, 510, 41, 21))
    font = QtGui.QFont()
    font.setPointSize(11)
    font.setBold(True)
    font.setWeight(75)
    self.epsilon2.setFont(font)
    self.epsilon2.setObjectName("epsilon2")
#POLE NA e2
    self.e2 = QtWidgets.QTextEdit(self.centralwidget)
    self.e2.setGeometry(QtCore.QRect(50, 510, 341, 31))
    self.e2.setPlainText("1e-11")
    self.e2.setObjectName("e2")
#NAPIS e3
    self.epsilon3 = QtWidgets.QLabel(self.centralwidget)
    self.epsilon3.setGeometry(QtCore.QRect(10, 550, 41, 21))
    font = QtGui.QFont()
    font.setPointSize(11)
    font.setBold(True)
    font.setWeight(75)
    self.epsilon3.setFont(font)
    self.epsilon3.setObjectName("liczbaiteracji_4")
#POLE NA e3
    self.e3 = QtWidgets.QTextEdit(self.centralwidget)
    self.e3.setGeometry(QtCore.QRect(50, 550, 341, 31))
    self.e3.setPlainText("1e-11")
    self.e3.setObjectName("e3")
#MENU
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 21))
    self.menubar.setObjectName("menubar")
    MainWindow.setMenuBar(self.menubar)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)

    wr_retranslateUi(self, MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

def wr_retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Metoda Carrolla"))
    self.startButton.setText(_translate("MainWindow", "Uruchom Program"))
    self.label.setText(_translate("MainWindow", "F(x):"))
    self.label_2.setText(_translate("MainWindow", "Metoda Carolla"))
    self.label_3.setText(_translate("MainWindow", "Funkcje ograniczaj??ce zakres szukania minimum"))
    self.Ograniczenie1.setText(_translate("MainWindow", "Ograniczenie 1:"))
    self.Ograniczenie2.setText(_translate("MainWindow", "Ograniczenie 2:"))
    self.Ograniczenie3.setText(_translate("MainWindow", "Ograniczenie 3:"))
    self.Ograniczenie4.setText(_translate("MainWindow", "Ograniczenie 4:"))
    self.Ograniczenie5.setText(_translate("MainWindow", "Ograniczenie 5:"))
    self.wspolczynnikprzyblizen.setText(_translate("MainWindow", "Wsp????czynnik przybli??e?? r0:"))
    self.label_10.setText(_translate("MainWindow", "Punkt startowy algorytmu"))
    self.x1.setText(_translate("MainWindow", "x1:"))
    self.x2.setText(_translate("MainWindow", "x2:"))
    self.x3.setText(_translate("MainWindow", "x3:"))
    self.x4.setText(_translate("MainWindow", "x4:"))
    self.x5.setText(_translate("MainWindow", "x5:"))
    self.liczbaiteracji.setText(_translate("MainWindow", "Liczba iteracji L:"))
    self.epsilon1.setText(_translate("MainWindow", "<html><head/><body><p>&epsilon;1:</p><br/></body></html>"))
    self.epsilon2.setText(_translate("MainWindow", "<html><head/><body><p>&epsilon;2:</p><br/></body></html>"))
    self.epsilon3.setText(_translate("MainWindow", "<html><head/><body><p>&epsilon;3:</p><br/></body></html>"))
    self.wynik.setPlainText(_translate("MainWindow","Wynik:"))
