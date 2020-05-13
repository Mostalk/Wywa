import pytesseract
from pytesseract import Output
import re
import sys
from PyQt5 import QtWidgets
import recognition


class Main(QtWidgets.QMainWindow, recognition.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


    def create_threads(image, src):
        f = open("log/recognition.txt", "a")
        psm = 6
        f.write("====================" + src + "====================\n")
        #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        d = pytesseract.image_to_string(image, lang='rus+ukr', output_type=Output.STRING, config="--psm " + str(psm))
        Main.setupUi.textBrowser.setText("Hi")
        f.write(d)
        f.close()


def main(image, src):
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
