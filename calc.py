from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.kalkulator()

    def init_ui(self):
        self.setWindowTitle('Kalkulator')
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)



        self.show()
    def kalkulator(self):

        alles=""
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addStretch(1)

        lista = [['AC', '±', '%', '÷'], ['7', '8', '9', '×'], ['4', '5',
                         '6', '-'], ['1', '2', '3', '+'],[ '0', '.', '=']
        ]
        results = QLineEdit()
        results.setMinimumSize(300,65)
        results.setMaximumSize(300,65)
        vbox.addWidget(results)
        for pos in lista:
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.setSpacing(0)



            for name in pos:
                if name == "0":

                    button = QPushButton(name)
                    button.setMinimumSize(150,60)
                    button.setMaximumSize(150,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)

                    button.clicked.connect(lambda:self.handleInput(0,results,alles))

                if name == "1":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(1,results, alles))
                if name == "2":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(2,results, alles))
                if name == "3":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(3,results, alles))
                if name == "4":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(4,results, alles))
                if name == "5":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(5,results, alles))
                if name == "6":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(6,results, alles))
                if name == "7":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(7,results, alles))
                if name == "8":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(8,results, alles))
                if name == "9":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(9,results, alles))
                if name == "AC":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("AC",results, alles))
                if name == "±":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("±",results, alles))
                if name == "%":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("%",results, alles))
                if name == "=":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(196, 194, 194)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("=",results, alles))
                if name == "÷":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(196,194,194)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("/",results, alles))
                if name == ".":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(241, 241, 241)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput(".",results, alles))
                if name == "+":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(196,194,194)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("+",results, alles))
                if name == "-":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(196,194,194)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("-",results, alles))
                if name == "×":

                    button = QPushButton(name)
                    button.setMinimumSize(75,60)
                    button.setMaximumSize(75,60)
                    button.setStyleSheet("background-color: rgb(196,194,194)");
                    hbox.addWidget(button)
                    button.clicked.connect(lambda: self.handleInput("*",results, alles))






            vbox.addLayout(hbox)
        print(vbox)
        vbox.setContentsMargins(0,0,0,0)
        self.setLayout(vbox)
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Kalkulator')
        self.move(300, 150)
        self.show()

    def handleInput(self, v, res,all):
        if v == "=":
            new = eval(res.text())
            res.setText(str(new))
        elif v =="AC":
            res.setText("")
        else:
            current_value = res.text()

            new = current_value + str(v)
            res.setText(new)
            print("clicked = ", v)

        return all

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = calculator()
    sys.exit(app.exec_())

