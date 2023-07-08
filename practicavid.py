import numpy as np
import cv2

def img_show(filename): #Функция ввывода  изображения
    cv2.namedWindow('Image')
    cv2.imshow("Image", filename)
    cv2.waitKey(1)


#Ввод значения контрастности
contrast = int(input('Введите значение контрастности (от 40 и более): '))

#Ввод степени размытия исходного изрбражения (пункт меню)
print('\n----Степень размытия----\n'
      '1. Малая\n'
      '2. Средняя\n'
      '3. Большая\n'
      '4. Без размытия')
flag = 0
while flag != 1:
    q = int(input('Введите выбранный номер: '))
    if q == 1:
        blur = (3, 3)
        flag = 1
    elif q == 2:
        blur = (7, 7)
        flag = 1
    elif q == 3:
        blur = (11, 11)
        flag = 1
    elif q == 4:
        blur = (1, 1)
        flag = 1
    else:
        print('Вы ввели неправильный номер!!!')

#Вывод цветного исходного изображения
image_color = cv2.imread('img.jpg', 255)
img_show(image_color)


img_for_blur = cv2.imread('img.jpg', 0) #Сохраняем изображение в ч/б
img = cv2.GaussianBlur(img_for_blur, blur, 0) #Используем фильтр размытия Гаусса

G_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) #Оператор Собеля по горизонтали
G_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]) #Оператор Собеля по вертикали

#Задаем количество строк и столбцов
rows = np.size(img, 0)
columns = np.size(img, 1)

#Заполняем клонированное изображение (массив) нулями
mag = np.zeros(img.shape)

#Выполнение производной по вертикали и горизонтали
for i in range(0, rows - 2):
    for j in range(0, columns - 2):
        v = sum(sum(G_x * img[i:i + 3, j:j + 3]))
        h = sum(sum(G_y * img[i:i + 3, j:j + 3]))
        mag[i+1, j+1] = np.sqrt((v * v) + (h * h)) #Результирующая матрица изображения
    img_show(mag)

#Задаем порог контрастности изображения
for i in range(0, rows):
    for j in range(0, columns):
        if mag[i, j] < contrast:
            mag[i, j] = 0
    img_show(mag)
#Вывод результирующего изображения
# img_show(mag)
#Сохраним преобразованное изображение
cv2.imwrite('img_result.jpg', mag)