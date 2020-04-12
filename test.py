import re
import cv2
import numpy as np
import pytesseract

import main
import proc as p
import jamspell
from pytesseract import Output
from matplotlib import pyplot as plt
from threading import Thread
import re

from main import corrector


class MyThread(Thread):
    def __init__(self, name, image, image_src):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.image = image
        self.src = image_src

    def run(self):
        def processing(text):
            summ = ["СУМА", "СУМ", "СУММА", "СЕМА"]
            for sum in summ:
                if sum in text['text']:
                    su = open("log/sum.txt", 'a')
                    ii = 1
                    while text['text'][sum.index(sum) + ii] == "":
                        ii = ii + 1
                        print(sum.index(sum) + ii)
                    su.write(text['text'][sum.index(sum) + ii])
                    su.close()

        def teser(image):
            dd = []
            # print("Recognition...")
            psm = self.name
            # print("Mode: " + psm + " start")
            f.write("====================" + re.sub("checks/", "", self.src) + "====================\n")
            print("====================" + re.sub("checks/", "", self.src) + "====================\n")
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            modes = ['get_grayscale', 'remove_noise', 'thresholding', 'dilate', 'erode', 'opening', 'canny']
            # print("--------" + "CLEAR" +"-------- " + str(psm) + " --------")
            d = pytesseract.image_to_data(image, lang='rus+ukr', output_type=Output.STRING, config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            cv2.drawContours(image, (d['width'], d['height']), 0, (0, 0, 255), 10)
            cv2.imshow(self.src, main.resize(image)[0])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            # f.write("--------" + "CLEAR" + "--------\n")
            # dd = d.split(" ")
            print(d)
            for word in d['text']:
                try:
                    # d = corrector(word)
                    None
                except:
                    continue
            for text in d['text']:
                if not text == "":
                    f.write(str(d['text']))
            f.write("----------------\n")
            '''# print("--------" + modes[0] + "-------- " + str(psm) + " --------")
            gray = p.get_grayscale(image)
            d = pytesseract.image_to_string(gray, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[0] + "--------\n")
            f.write(d)
            f.write("----------------\n")
            # print("--------" + modes[1] + "-------- " + str(psm) + " --------")
            noice = p.remove_noise(gray)
            d = pytesseract.image_to_string(noice, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[1] + "--------\n")
            f.write(d)
            f.write("----------------\n")
            # print("--------" + modes[2] + "-------- " + str(psm) + " --------")
            thresh = p.thresholding(gray)
            d = pytesseract.image_to_string(thresh, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[2] + "--------\n")
            f.write(d)
            f.write("----------------\n")
            # print("--------" + modes[3] + "-------- " + str(psm) + " --------")
            dilate = p.dilate(gray)
            d = pytesseract.image_to_string(dilate, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[3] + "--------\n")
            f.write(d)
            f.write("----------------\n")
            # print("--------" + modes[4] + "-------- " + str(psm) + " --------")
            erode = p.erode(gray)
            d = pytesseract.image_to_string(erode, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[4] + "--------\n")
            f.write(d)
            f.write("----------------\n")
            # print("--------" + modes[5] + "-------- " + str(psm) + " --------")
            opening = p.opening(gray)
            d = pytesseract.image_to_string(opening, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[5] + "--------\n")
            f.write(d)
            f.write("----------------\n")
            # print("--------" + modes[6] + "-------- " + str(psm) + " --------")
            canny = p.canny(gray)
            d = pytesseract.image_to_string(canny, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[6] + "--------\n")
            f.write(d)'''

            print("Mode: " + psm + " end!")
            return d

        f = open("log/recognition.txt", "a")
        teser(self.image)
        f.close()

    """  #n_boxes = len(d['text'])
    
    linex = 0
    #for i in range(n_boxes):
    #    line = []
        # condition to only pick boxes with a confidence > 60%
#            if int(d['conf'][i]) > 10:
#                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#               line.append(d['text'][i])
#           #print(line)
    #b, g, r = cv2.split(image)
    #rgb_img = cv2.merge([r, g, b])
    #plt.figure(figsize=(5, 5))
    scale_percent = 100  # Процент от изначального размера
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    numb = range(1,1000)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("test" + str(numb),image)
    #plt.title('Пример')
    #plt.show()"""


def create_threads(image, image_src):
    name = 6
    my_thread = MyThread(name, image, image_src)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
