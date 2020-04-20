import pytesseract
from pytesseract import Output
from threading import Thread
import re


class MyThread(Thread):
    def __init__(self, name, image, image_src):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.image = image
        self.src = image_src

    def run(self):
        def teser(image):
            psm = self.name
            f.write("====================" + re.sub("checks/", "", self.src) + "====================\n")
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            d = pytesseract.image_to_data(image, lang='rus+ukr', output_type=Output.STRING, config="--psm " + str(psm))
            return d
        f = open("log/recognition.txt", "a")
        teser(self.image)
        f.close()


def create_threads(image, image_src):
    name = 6
    my_thread = MyThread(name, image, image_src)
    my_thread.start()


if __name__ == "__main__":
    create_threads()
