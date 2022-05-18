import math

import cv2
import numpy as np


def draw_line(frame, mask):
    """
    for i in range(mask.shape[0]):
      for j in range(len(mask[i])):
        if mask[i,j] > 0:
          frame[i,j] = [247,121,106]
      return frame

    """
    line_image = np.zeros_like(mask)

    dst = cv2.Canny(mask, 0, 255)

    # lines = cv2.HoughLines(dst, 1, np.pi / 180, 0, None, 0, 0)
    rho = 1  # Distance resolution of the accumulator in pixels.
    theta = np.pi / 180  # Angle resolution of the accumulator in radians.
    threshold = 20  # Only lines that are greater than threshold will be returned.
    minLineLength = 20  # Line segments shorter than that are rejected.
    maxLineGap = 300  # Maximum allowed gap between points on the same line to link them
    lines = cv2.HoughLinesP(dst, rho=rho, theta=theta, threshold=threshold, minLineLength=minLineLength,
                            maxLineGap=maxLineGap)

    """if lines is not None:
      for line in lines:
        x1, y1, x2, y2 = line
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 10)"""
    if lines is not None:

        for line in lines:

            for x1, y1, x2, y2 in line:
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

    return frame


def detect(frame):


    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mask = np.zeros_like(frame_gray)
    contours = np.array([[310, 300], [410, 300], [570, 470], [180, 470]])

    cv2.fillPoly(mask, pts=[contours], color=(255, 255, 255))

    masked_image = cv2.bitwise_and(frame_gray, mask)

    masked_image[(masked_image[:, :] < 115)] = 0
    masked_image[(masked_image[:, :] > 130)] = 0

    masked_image = cv2.dilate(masked_image, (6, 6))
    masked_image = cv2.dilate(masked_image, (6, 6))
    masked_image = cv2.dilate(masked_image, (8, 8))

    lines = draw_line(frame, masked_image)


    #cv2.imshow('frame', frame)
    #cv2.imshow('lines', lines)
    return lines
    # cv2.imshow('image_1',mask)
    #cv2.imshow('masked_image', masked_image)
    # cv2.imshow('frame_gray',frame_gray)

