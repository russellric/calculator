from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from calculator import Ui_MainWindow

class calcAttach(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

        self.result = 0
        self.variable = ''

        #numpad buttons
        self.n1.clicked.connect(self.n1clicked)
        self.n2.clicked.connect(self.n2clicked)
        self.n3.clicked.connect(self.n3clicked)
        self.n4.clicked.connect(self.n4clicked)
        self.n5.clicked.connect(self.n5clicked)
        self.n6.clicked.connect(self.n6clicked)
        self.n7.clicked.connect(self.n7clicked)
        self.n8.clicked.connect(self.n8clicked)
        self.n9.clicked.connect(self.n9clicked)
        self.n0.clicked.connect(self.n0clicked)
        self.des.clicked.connect(self.desclicked)

        #clear button
        self.clear.clicked.connect(self.clearclicked)

        #opperation buttons
        self.plus.clicked.connect(self.plusclicked)
        self.subtract.clicked.connect(self.subtractclicked)
        self.divide.clicked.connect(self.divideclicked)
        self.multiply.clicked.connect(self.multiplyclicked)
        self.equal.clicked.connect(self.equalclicked)


    def n1clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '1'
        self.display.setText(self.variable)

    def n2clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '2'
        self.display.setText(self.variable)
    
    def n3clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '3'
        self.display.setText(self.variable)
    
    def n4clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '4'
        self.display.setText(self.variable)
    
    def n5clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '5'
        self.display.setText(self.variable)
    
    def n6clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '6'
        self.display.setText(self.variable)

    def n7clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '7'
        self.display.setText(self.variable)

    def n8clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '8'
        self.display.setText(self.variable)

    def n9clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '9'
        self.display.setText(self.variable)

    def n0clicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        self.variable += '0'
        self.display.setText(self.variable)

    def desclicked(self):
        if 'ERROR' in self.variable:
            self.variable = self.variable.replace('ERROR', '')
        desimal = '.'
        if desimal in self.variable:
            pass
        else:
            self.variable += '.'
        self.display.setText(self.variable)

    def clearclicked(self):
        self.variable = ''
        self.display.setText(self.variable)
        
    def plusclicked(self):
        self.variable += ' + '
        self.display.setText(self.variable)

    def subtractclicked(self):
        self.variable += ' - '
        self.display.setText(self.variable)

    def divideclicked(self):
        self.variable += ' / '
        self.display.setText(self.variable)

    def multiplyclicked(self):
        self.variable += ' * '
        self.display.setText(self.variable)

    def equalclicked(self):
        try:
            answer = str(eval(self.variable))
            self.variable = answer
        except:
            self.variable = "ERROR"
        self.display.setText(self.variable)
