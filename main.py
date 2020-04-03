import cv2
import numpy as np
import math

image = cv2.imread("checks/check.jpg")


def processImage(imgage):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 10, 255)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    cnts, hier = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    color_yellow = (0, 255, 255)
    total = 0
    for c in cnts:
        # аппроксимируем (сглаживаем) контур
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.0001 * peri, True)
        rect = cv2.minAreaRect(approx)  # пытаемся вписать прямоугольник
        box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        center = (int(rect[0][0]), int(rect[0][1]))
        # вычисление координат двух векторов, являющихся сторонам прямоугольника
        edge1 = np.int0((box[1][0] - box[0][0], box[1][1] - box[0][1]))
        edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

        # выясняем какой вектор больше
        usedEdge = edge1
        if cv2.norm(edge2) > cv2.norm(edge1):
            usedEdge = edge2
        reference = (1, 0)  # горизонтальный вектор, задающий горизонт
        # вычисляем угол между самой длинной стороной прямоугольника и горизонтом
        angle = 180.0 / math.pi * math.acos(
            (reference[0] * usedEdge[0] + reference[1] * usedEdge[1]) / (cv2.norm(reference) * cv2.norm(usedEdge)))
        # cv2.drawContours(edged, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        if area > 3000000:
            cv2.drawContours(image, [box], 0, (50, 0, 255), 5)
            # выводим в кадр величину угла наклона
            (h, w) = image.shape[:2]
            center_pic = (w / 2, h / 2)
            M = cv2.getRotationMatrix2D(center_pic, 90 - angle, 1.0)
            image = cv2.warpAffine(image, M, (w, h))
            total += 1
            yy = int(box[2][1])
            yw = int(box[0][1])
            ww = int(box[1][0])
            wy = int(box[3][0])
    image = image[yy:yw, ww:wy]
    scale_percent = 20  # Процент от изначального размера
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 10, 255)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    ret, threshold_image = cv2.threshold(gray, 150, 255, 0)
    edged = cv2.resize(closed, dim, interpolation=cv2.INTER_AREA)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    threshold_image = cv2.resize(threshold_image, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("1", image)
    cv2.imshow("2", edged)
    cv2.imshow("3", threshold_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
