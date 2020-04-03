import cv2
import numpy as np


def viewImage(image):
    cv2.imshow("1", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread("checks/check.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(gray, 150, 255, 0)
edged = cv2.Canny(gray, 10, 255)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cnts, hier = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total = 0
for c in cnts:
    # аппроксимируем (сглаживаем) контур
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.0001 * peri, True)
    rect = cv2.minAreaRect(approx)  # пытаемся вписать прямоугольник
    box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
    box = np.int0(box)  # округление координат
    # cv2.drawContours(edged, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник
    area = int(rect[1][0] * rect[1][1])  # вычисление площади
    if area > 3000000:
        cv2.drawContours(image, [box], 0, (50, 0, 255), 5)
        total += 1
print(total)
scale_percent = 20  # Процент от изначального размера
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
print(dim)

edged = cv2.resize(closed, dim, interpolation=cv2.INTER_AREA)
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
threshold_image = cv2.resize(threshold_image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("1", image)
cv2.imshow("2", edged)
cv2.imshow("3", threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
