import cv2
import numpy as np
from lib import *


def task_3_bgr_to_hsv():
    print('[TAKS 3: BGR TO HSV] <Starting testing>')
    img1 = cv2.imread('images/img.jpg')
    img2 = cv2.imread('images/img.jpg')
    print('[Opening images...]')
    cv2.imshow('my ', bgr_to_hsv(img1))
    cv2.imshow('openCV ', cv2.cvtColor(img2, cv2.COLOR_BGR2HSV))
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
    cv2.imshow('my ', hsv_to_bgr(img1_hsv))
    cv2.imshow('openCV ', cv2.cvtColor(img2_hsv, cv2.COLOR_HSV2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[TASK 3] <Successfully has ended>')
