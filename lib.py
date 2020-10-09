import cv2
import numpy as np

# OpenCV equivalent: cv2.cvtColor(img, <name>)
def bgr_to_hsv_color(b:int=0, g:int=0, r:int=0): # b/g/r from 0 to 255
    b /= 255
    g /= 255
    r /= 255
    v = 0
    h = 0
    s = 0
    Cmax = max(b, g, r)
    Cmin = min(b, g, r)

    if Cmax == Cmin:
        Cmax -= 1

    v = Cmax

    try:
        if Cmax == r and  g >= b:
            h = 60 * (g - b) / (Cmax - Cmin) + 0
        elif Cmax == r and g < b:
            h = 60 * (g - b) / (Cmax - Cmin) + 360
        elif Cmax == g:
            h = 60 * (b - r) / (Cmax - Cmin) + 120
        elif Cmax == b:
            h = 60 * (r - g) / (Cmax - Cmin) + 240
    except ZeroDivisionError:
        h = 0

    if Cmax == 0:
        s = 0
    else:
        s = 1 - Cmin / Cmax

    return h, s, v


def bgr_to_hsv(img):
    img_width, img_height, img_channel = img.shape
    for x in range(img_width):
        for y in range(img_height):
            h, s, v = bgr_to_hsv_color(img.item(x, y, 0),
                                    img.item(x, y, 1),
                                    img.item(x, y, 2))
            img.itemset((x, y, 0), h * 255 / 360)
            img.itemset((x, y, 1), s * 255)
            img.itemset((x, y, 2), v * 255)
    return img


def hsv_to_bgr_color(h:int=0, s:int=0, v:int=0):
    Hi = (h // 60) % 6
    Vmin = (100 - s) * v / 100
    a = (v - Vmin) * (h % 60) / 60
    Vinc = Vmin + a
    Vdec = v - a
    CONSTVAR = 255 / 100

    bgr = (0, 0, 0)
    if Hi == 0: 
        bgr = (Vmin * CONSTVAR, Vinc * CONSTVAR, v * CONSTVAR)
    elif Hi == 1: 
        bgr = (Vmin * CONSTVAR, v * CONSTVAR, Vdec * CONSTVAR)
    elif Hi == 2: 
        bgr = (Vinc * CONSTVAR, v * CONSTVAR, Vmin * CONSTVAR)
    elif Hi == 3: 
        bgr = (v * CONSTVAR, Vdec * CONSTVAR, Vmin * CONSTVAR)
    elif Hi == 4: 
        bgr = (v * CONSTVAR, Vmin * CONSTVAR, Vinc * CONSTVAR)
    elif Hi == 5: 
        bgr = (Vdec * CONSTVAR, Vmin * CONSTVAR, v * CONSTVAR)

    return bgr


def hsv_to_bgr(img):
    img_width, img_height, imt_channel = img.shape
    for x in range(img_width):
        for y in range(img_height):
            h = img.item(x, y, 0) / 255 * 360
            s = img.item(x, y, 1) / 255 * 100
            v = img.item(x, y, 2) / 255 * 100
            b, g, r = hsv_to_bgr_color(h, s, v)
            img.itemset((x, y, 0), b)
            img.itemset((x, y, 1), g)
            img.itemset((x, y, 2), r)
    return img


def immse(img1, img2):
    img_width, img_height, img_channel = img1.shape
    sum = np.int64()
    for x in range(img_width):
        for y in range(img_height):
            avg1 = (np.int64(img1.item(x, y, 0)) +
                    np.int64(img1.item(x, y, 1)) +
                    np.int64(img1.item(x, y, 2))) // 3

            avg2 = (np.int64(img2.item(x, y, 0)) +
                    np.int64(img2.item(x, y, 1)) +
                    np.int64(img2.item(x, y, 2))) // 3
            sum += (avg1 - avg2) ** 2
    return sum / (img_width * img_height)


def average_of_rgb(img):
    (img_width, img_height, img_channel) = img.shape
    for x in range(img_width):
        for y in range(img_height):
            b = int(img.item(x, y, 0))
            g = int(img.item(x, y, 1))
            r = int(img.item(x, y, 2))
            avg = (b + g + r) // 3

            for i in range(3):
                img.itemset((x, y, i), avg)
    return img


def brightness_inc_bgr(img, delta):
    if delta <= 0:
        return img
    img_width, img_height, img_channel = img.shape
    for x in range(img_width):
        for y in range(img_height):
            b = img.item(x, y, 0)
            g = img.item(x, y, 1)
            r = img.item(x, y, 2)

            if b + delta <= 255:
                img.itemset((x, y, 0), b + delta)
            else:
                img.itemset((x, y, 0), 255)

            if g + delta <= 255:
                img.itemset((x, y, 1), g + delta)
            else:
                img.itemset((x, y, 1), 255)

            if r + delta <= 255:
                img.itemset((x, y, 2), r + delta)
            else:
                img.itemset((x, y, 2), 255)
    return img


def brightness_inc_hsv(img, delta:int=0):
    if delta <= 0:
        return img
    w, h, c = img.shape
    for x in range(w):
        for y in range(h):
            v = img.item(x, y, 2) / 255 * 100
            if v + delta <= 100:
                img.itemset((x, y, 2), (v + delta) * 255 / 100)
            else: 
                img.itemset((x, y, 2), 100 * 255 / 100)
    return img

