import sys
from PyQt5 import QtWidgets
import calcAttach

app = QtWidgets.QApplication(sys.argv)
calculator_win = QtWidgets.QMainWindow()
calculator_ui = calcAttach.calcAttach(calculator_win)
app.exec_()