import re
import cv2
import numpy as np
import pytesseract
import proc as p
from pytesseract import Output
from matplotlib import pyplot as plt
from threading import Thread


class MyThread(Thread):
    def __init__(self, name, image, image_src):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.image = image
        self.src = image_src

    def run(self):
        def teser(image):
            # print("Recognition...")
            psm = self.name
            print("Mode: " + psm + " start")
            f = open("log/" + self.src + " - " + psm, "a")
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            modes = ['get_grayscale', 'remove_noise', 'thresholding', 'dilate', 'erode', 'opening', 'canny']
            # print("--------" + "CLEAR" +"-------- " + str(psm) + " --------")
            d = pytesseract.image_to_string(image, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            f.write("--------" + "CLEAR" + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[0] + "-------- " + str(psm) + " --------")
            gray = p.get_grayscale(image)
            d = pytesseract.image_to_string(gray, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[0] + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[1] + "-------- " + str(psm) + " --------")
            noice = p.remove_noise(gray)
            d = pytesseract.image_to_string(noice, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[1] + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[2] + "-------- " + str(psm) + " --------")
            thresh = p.thresholding(gray)
            d = pytesseract.image_to_string(thresh, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[2] + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[3] + "-------- " + str(psm) + " --------")
            dilate = p.dilate(gray)
            d = pytesseract.image_to_string(dilate, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[3] + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[4] + "-------- " + str(psm) + " --------")
            erode = p.erode(gray)
            d = pytesseract.image_to_string(erode, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[4] + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[5] + "-------- " + str(psm) + " --------")
            opening = p.opening(gray)
            d = pytesseract.image_to_string(opening, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[5] + "-------- ")
            f.write(d)
            f.write("----------------")
            # print("--------" + modes[6] + "-------- " + str(psm) + " --------")
            canny = p.canny(gray)
            d = pytesseract.image_to_string(canny, lang='rus+ukr', config="--psm " + str(
                psm))  # d = pytesseract.image_to_data(image, lang='rus', output_type=Output.DICT, config="--psm" + psm")
            # print(d)
            f.write("--------" + modes[6] + "-------- ")
            f.write(d)
            f.write("----------------")
            f.close()
            print("Mode: " + psm + " end!")

        teser(self.image)

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
    for i in [0, 2, 3, 5, 10, 11]:
        name = i + 1
        my_thread = MyThread(name, image, image_src)
        my_thread.start()


if __name__ == "__main__":
    create_threads()
