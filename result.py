import sys
from PyQt5 import QtWidgets
import recognition


class Main(QtWidgets.QMainWindow, recognition.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
