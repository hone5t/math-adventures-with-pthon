#!/usr/bin/env python

from turtle import forward, shape, right

def draw_rect_based_on(sh, size, turn):
    right(turn)
    shape(sh)
    for i in range(4):
        forward(size)
        # changed this to 90 instead of 270 to match the chart in the book
        # using left seems so natural to me :)
        right(90)
    
if __name__ == "__main__":
    for i in range(60):
        size = i + 5
        draw_rect_based_on('turtle', size, 5)
    input("please press anything to finish")