import cv2 as cv
import numpy as np

class Rectangle:

    # Constructor
    def __init__(self, center_x, center_y, width, height, line_color=(0, 255, 0), name=''):
        self.pos_x = center_x
        self.pos_y = center_y
        self.width = width
        self.height = height
        self.line_color = line_color
        self.name = name

        self.top_left = (self.pos_x, self.pos_y)
        self.bottom_right = (self.pos_x + self.width, self.pos_y + self.height)
        self.top_left_ten = (self.pos_x, self.pos_y - 10)

    # Donat una imatge, pinta el rectangle sobre ella
    def printRectangle(self, haystack_img, show_name=False):
        cv.rectangle(haystack_img, self.top_left, self.bottom_right, self.line_color, -1)  # line_type
        if show_name:
            cv.putText(haystack_img, self.name, self.top_left_ten, cv.FONT_ITALIC, 0.9, self.line_color, 1)

        return haystack_img

    # Permet canviar el centre d'un rectangle
    def canviaCentre(self, center_x, center_y):
        self.pos_x = center_x - int(self.width / 2)
        self.pos_y = center_y - int(self.height / 2)
        self.top_left = (self.pos_x, self.pos_y)
        self.bottom_right = (self.pos_x + self.width, self.pos_y + self.height)
        self.top_left_ten = (self.pos_x, self.pos_y - 10)

    def printCrossHair(self, haystack_img):
        center_x, center_y = self.rectangleToPoint()
        cv.drawMarker(haystack_img, (center_x, center_y), self.line_color, 1)
        return haystack_img

    def rectangleToPoint(self):
        # Càlcul del centre del rectangle
        center_x = self.pos_x + int(self.width/2)
        center_y = self.pos_y + int(self.height/2)
        # Retornam el punt
        return center_x, center_y

    def returnInfo(self):
        return self.pos_x, self.pos_y, self.width, self.height

    def returnPoints(self):
        return np.array((self.pos_x, self.pos_y))