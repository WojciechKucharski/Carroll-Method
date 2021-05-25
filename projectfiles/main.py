from classFile import *
from window import *
from PyQt5 import QtCore, QtGui, QtWidgets
from _thread import *
import time


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        wr_setupUi(self, MainWindow)
        self.startButton.clicked.connect(self.runAlgorithm)
        start_new_thread(self.updatingThread, (1,))

    def updatingThread(self, useless):
        function = ""
        constrains = ""
        while True:
            time.sleep(0.1)
            if function != self.getGoalFunction:
                try:
                    self.updatePointsAccess()
                except:
                    pass
                function = self.getGoalFunction
            if constrains != self.getConstraints:
                try:
                    self.updateConstrainsAccess()
                except Exception as e:
                    print(e)
                constrains = self.getConstraints

    def updatePointsAccess(self):
        dimension = self.functionDimension
        for i in range(1, 6):
            eval(f"self.x{i}i.setDisabled({i > dimension})")

    def updateConstrainsAccess(self):

        for j in range(5):
            for i in range(1, 6):
                if len(eval(f"self.ogr{i}.toPlainText()")) == 0 and i < 5:
                    new = eval(f"self.ogr{i+1}.toPlainText()")
                    #eval(f"self.ogr{i}.setPlainText({str(new)})")

        empty = []
        for i in range(1, 6):
            if len(eval(f"self.ogr{i}.toPlainText()")) == 0:
                eval(f"self.ogr{i}.setDisabled(False)")
                empty.append(i)
        if len(empty) > 1:
            empty = empty[1:]
            for i in empty:
                eval(f"self.ogr{i}.setDisabled(True)")

    @property
    def getStartingPoint(self):
        x = []
        for i in range(1, self.functionDimension + 1):
            try:
                xn = float(eval(f"self.x{i}i.toPlainText()"))
                x.append(xn)
            except:
                raise Exception(f"Błędna współrzędna x{i}")
        return x

    @property
    def getGoalFunction(self):
        return self.funkcja.toPlainText()

    @property
    def getConstraints(self):
        g = []
        for i in range(1, 6):
            try:
                g_i = eval(f"self.ogr{i}.toPlainText()")
                if len(g_i) == 0:
                    pass
                else:
                    g.append(g_i)
            except:
                raise Exception(f"Problem z ograniczniem g{i}")
        return g

    @property
    def getr0(self):
        try:
            r0 = float(self.r0.toPlainText())
        except:
            raise Exception("Błędna wartość r0")
        return r0

    @property
    def getMaxIterations(self):
        try:
            maxIter = int(self.L.toPlainText())
            if maxIter <= 0:
                raise Exception("Błedna liczba iteracji")
        except:
            raise Exception("Błedna liczba iteracji")

        return maxIter

    @property
    def getEpsilon(self):
        epsilon = []
        for i in range(1, 4):
            try:
                epsilon.append(float(eval(f"self.e{i}.toPlainText()")))
            except:
                raise Exception(f"Błędna wartość e{i}")
        return epsilon

    @property
    def functionDimension(self):
        function = self.getGoalFunction
        varDim = 0
        try:
            for i in range(1, 8):
                if f"x{i}" in function:
                    varDim = i
            return varDim
        except:
            raise Exception("Błędna funkcja celu")

    def runAlgorithm(self):
        self.wynik.setPlainText("Trwa liczenie...")
        try:
            a = CarrollMethod()
            X, iterations, fvalue = a.run(goalFunction=self.getGoalFunction,
                                          x0=self.getStartingPoint,
                                          r0=self.getr0,
                                          maxIter=self.getMaxIterations,
                                          epsilon1=self.getEpsilon[0],
                                          epsilon2=self.getEpsilon[1],
                                          epsilon3=self.getEpsilon[2],
                                          g_i=self.getConstraints
                                          )
            self.wynik.setPlainText(f"Najlepszy punkt x: \n{X}\nNajlepsza wartość f:{fvalue}\nIteracje:{iterations}")
            a.visualise()

        except Exception as E:
            print(E)
            self.wynik.setPlainText(str(E))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
