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

def task_3_brightness_hsv():
    print('[TAKS 3: BRIGHTNESS HSV] <Starting testing>')
    img = cv2.imread('images/etg.jpg')
    print('[Opening image...]')
    img = bgr_to_hsv(img)
    cv2.imshow('my ', hsv_to_bgr(brightness_inc_hsv(img, 50)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[TASK 3] <Successfully has ended>')


task_3_brightness_hsv()