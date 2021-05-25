from classFile import *
#from gui import *
from window import *
from PyQt5 import QtCore, QtGui, QtWidgets

"""
x, iter_ = F.run(fun, [4, 4], [100 - i for i in range(101)], 100, 1e-8, g)
print(x)
F.visualise()


fun = "x1^4+x2^4-2x1^2*x2-4*x1+3"
g = ["(4-x1-x2)"]

fun = "(x1-2)^2+(x2-1)^2"
#g = ["x1^2-x2", "-2+x1+x2"]
g = ["x1^2+x2^2-2"] #g = ["x1-2x2+1", "x1^2/4+x2^2-1"]


fun = "(x1^2+x2-11)^2+(x1+x2^2-7)^2"
g = ["(x1-0.05)^2+(x2-2.5)^2-4.84", "4.84-x1^2-(x2-2.5)^2"]

F = CarrollMethod()

x, iter_, fx = F.run(fun, [-1.2, 0.4], 1, 1000, 1e-5, 1e-6, 1e-6, g)
print(x, fx, iter_)
F.visualise()
"""

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        wr_setupUi(self, MainWindow)

    def retranslateUi(self, MainWindow):
        wr_retranslateUi(self, MainWindow)

    def runfunc(self):
        self.startButton.clicked.connect(self.clicked)

    def getValues(self):
        args = []
        args.append(self.funkcja.toPlainText())#0
        args.append(self.ogr1.toPlainText())#1
        args.append(self.ogr2.toPlainText())#2
        args.append(self.ogr3.toPlainText())#3
        args.append(self.ogr4.toPlainText())#4
        args.append(self.ogr5.toPlainText())#5
        args.append(self.r0.toPlainText())#6
        args.append(self.L.toPlainText())#7
        args.append(self.x1i.toPlainText())#8
        args.append(self.x2i.toPlainText())#9
        args.append(self.x3i.toPlainText())#10
        args.append(self.x4i.toPlainText())#11
        args.append(self.x5i.toPlainText())#12
        args.append(self.e1.toPlainText())#13
        args.append(self.e2.toPlainText())#14
        args.append(self.e3.toPlainText())#15

        for i in range(6,16):
            args[i]=float(args[i])
        args[7]=int(args[7])
        return args

    def clicked(self):

        try:
            args = self.getValues()
            print(args)
            a = CarrollMethod()
            x = a.run(goalFunction=args[0],
                      x0=[args[8],args[9],args[10],args[11],args[12]],
                      r0=args[6],
                      maxIter=args[7],
                      epsilon1=args[13],
                      epsilon2=args[14],
                      epsilon3=args[15],
                      g_i=[args[1],args[2],args[3],args[4],args[5]],
                      visualiseEveryIteration=False,
                      )
            self.wynik.setPlainText(str(x))
            a.visualise()
        except Exception as E:
            print(E)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.runfunc()
    MainWindow.show()
    sys.exit(app.exec_())