import cv2
import numpy as np
from lib import *
import time


def task_3_bgr_to_hsv():
    print('[TAKS 3: BGR TO HSV] <Starting testing>')
    img1 = cv2.imread('images/img.jpg')
    img2 = cv2.imread('images/img.jpg')
    print('[Opening images...]')
    start_time = time.time()
    cv2.imshow('my ', bgr_to_hsv(img1))
    print(f'my time = {(time.time() - start_time)} seconds')
    start_time = time.time()
    cv2.imshow('openCV ', cv2.cvtColor(img2, cv2.COLOR_BGR2HSV))
    print(f'opencv time = {(time.time() - start_time)} seconds')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[TASK 3] <Successfully has ended>')


def task_3_hsv_to_bgr():
    print('[TAKS 3: HSV TO BGR] <Starting testing>')
    img1 = cv2.imread('images/img.jpg')
    img2 = cv2.imread('images/img.jpg')
    img1_hsv = bgr_to_hsv(img1)
    print('[Opening images...]')
    img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    start_time = time.time()
    cv2.imshow('my ', hsv_to_bgr(img1_hsv))
    print(f'my time = {(time.time() - start_time)} seconds')
    start_time = time.time()
    cv2.imshow('openCV ', cv2.cvtColor(img2_hsv, cv2.COLOR_HSV2BGR))
    print(f'opencv time = {(time.time() - start_time)} seconds')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[TASK 3] <Successfully has ended>')


def task_1_immse():
    print('[TAKS 1: IMMSE] <Starting testing>')
    img1 = cv2.imread('images/etg.jpg')
    img2 = cv2.imread('images/etgNoise.jpg')
    mse = immse(img1, img2)
    print('\tmse = ' + str(mse))
    try:
        coincidence = (255 ** 2 - mse) / (255 ** 2) * 100
    except ZeroDivisionError:
        coincidence = 0
    print('\tCoincidence = ' + str(coincidence) + ' %')
    print('[TASK 1] <Successfully has ended>')


def task_3_brightness_bgr():
    print('[TAKS 3: BRIGHTNESS BGR] <Starting testing>')
    img = cv2.imread('images/etg.jpg')
    print('[Opening image...]')
    cv2.imshow('my ', brightness_inc_bgr(img, 150))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[TASK 3] <Successfully has ended>')


def task_2_average_of_rgb():
    print('[TAKS 2: AVERAGE OF RGB] <Starting testing>')
    img1 = cv2.imread('images/etg.jpg')
    img2 = cv2.imread('images/etg.jpg')
    print('[Opening images...]')
    cv2.imshow('my ', average_of_rgb(img1))
    cv2.imshow('opencv ', cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[TASK 2] <Successfully has ended>')


def main():
    menu()


def menu():
    print(
        """
        0. Exit.
        1. Task 1. MMSE
        2. Task 2. Average of RGB
        3. Task 3. BGR to HVS
        4. Task 3. HSV to BGR
        5. Task 3. Brightness increment BGR
        6. Task 3. Brightness increment HSV
        7. Task 3. IMMSE comp in time
        """
    )

    while True:
        input_symbol = int(input('Task >>> '))
        if input_symbol == 0:
            break
        if input_symbol == 1:
            task_1_immse()
        elif input_symbol == 2:
            task_2_average_of_rgb()
        elif input_symbol == 3:
            task_3_bgr_to_hsv()
        elif input_symbol == 4:
            task_3_hsv_to_bgr()
        elif input_symbol == 5:
            task_3_brightness_bgr()
        elif input_symbol == 6:
            pass
        elif input_symbol == 7:
            pass


if __name__ == '__main__':
    main()
