import os
import re
from threading import Thread

import cv2
import jamspell
import numpy as np
import math
import operator
import test
import proc as p
from matplotlib import pyplot as plt
from autocorrect import Speller

corrector = Speller(lang='ru')


class SrcThread(Thread):
    def __init__(self, image):
        """Инициализация потока"""
        Thread.__init__(self)
        self.image = image

    def run(self):
        image_src = "checks/" + self.image
        image = cv2.imread(image_src)

        def resize(image):
            try:
                scale_percent = 20
                width = int(image.shape[1] * scale_percent / 100)
                height = int(image.shape[0] * scale_percent / 100)
                dim = (width, height)
                image1 = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
                return image1, dim
            except:
                return image, dim

        def morf(image):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
            edged = cv2.Canny(gray, 10, 255)
            blur = cv2.GaussianBlur(gray, (21, 21), 0)
            a_thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            ret3, a_thresh = cv2.threshold(a_thresh, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            kernel = np.ones((5, 5), np.uint8)
            a_thresh = cv2.erode(a_thresh, kernel, iterations=1)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 150))  # 50, 50
            closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
            return image, gray, edged, closed, thresh, a_thresh

        def processImage(image):
            print("Start processing image...")
            cnts, hier = cv2.findContours(morf(image)[3].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            total = 0
            li = {}
            i = 0
            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.0025 * peri, False)
                rect = cv2.minAreaRect(approx)  # пытаемся вписать прямоугольник
                area = int(rect[1][0] * rect[1][1])  # вычисление площади
                li.update({i: area})
                i = i + 1
                ki = sorted(li.items(), key=operator.itemgetter(1))
                # cv2.drawContours(a_thresh, [c], 0, (0, 0, 255), 10)
            c = cnts[ki[-1][0]]
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.0025 * peri, False)
            rect = cv2.minAreaRect(approx)  # пытаемся вписать прямоугольник
            box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат
            cv2.drawContours(image, [box], 0, (0, 0, 255), 10)  # рисуем прямоугольник
            morf(image)[-1]
            image = a_thresh
            # center = (int(rect[0][0]), int(rect[0][1]))
            # вычисление координат двух векторов, являющихся сторонам прямоугольника
            edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
            edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))
            # выясняем какой вектор больше
            usedEdge = edge1
            if cv2.norm(edge2) > cv2.norm(edge1):
                usedEdge = edge2
            reference = (1, 0)  # горизонтальный вектор, задающий горизонт
            # вычисляем угол между самой длинной стороной прямоугольника и горизонтом
            angle = 180.0 / math.pi * math.acos((reference[0] * usedEdge[0] + reference[1] * usedEdge[1]) / (cv2.norm(reference) * cv2.norm(usedEdge)))
            # cv2.drawContours(image, cnts, 0, (50, 0, 255), 5)
            # выводим в кадр величину угла наклона
            (h, w) = image.shape[:2]
            center_pic = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center_pic, 90 - angle, 1.0)
            image = cv2.warpAffine(image, M, (w, h))
            yy = int(box[2][1])
            yw = int(box[0][1])
            ww = int(box[1][0])
            wy = int(box[3][0])
            cut = image[yy:yw, ww:wy]
            k = str(re.sub("checks/", "", image_src))
            '''cv2.imshow(k, resize(cut)[0])
            cv2.waitKey(0)
            cv2.destroyAllWindows()'''

            # cv2.imshow("2", edged)
            # cv2.imshow("3", threshold_image)
            print("Processing complete!")

            return cut

        image, gray, edged, closed, thresh, a_thresh = morf(image)
        # processImage(image)
        test.create_threads(processImage(image), image_src)
        #test.teser(processImage(gray, edged, closed))

def create_threads():
    files = os.listdir("checks/")
    for i in range(len(files)):
        my_thread = SrcThread(files[i])
        my_thread.start()


if __name__ == "__main__":
    create_threads()
