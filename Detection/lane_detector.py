import cv2
import numpy as np
from matplotlib import pyplot as plt
import detection

import numpy as np
from matplotlib import pyplot as plt


def lanesDetection(img):
    # img = cv.imread("./img/road.jpg")
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    region_of_interest_vertices = [
        (100, height-60), ((width / 2) , (height / 1.37)-40), (width - 120, height-60)
    ]


    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    edge = cv2.Canny(gray_img, 50, 100, apertureSize=3)

    cropped_image = region_of_interest(edge, np.array([region_of_interest_vertices], np.int32))
    #cropped_image=edge
    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi / 180,
                           threshold=50, lines=np.array([]), minLineLength=10, maxLineGap=30)
    image_with_lines = draw_lines(img, lines)
    # plt.imshow(image_with_lines)
    # plt.show()
    return image_with_lines


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = (255)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

