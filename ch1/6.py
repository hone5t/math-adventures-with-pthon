#!/usr/bin/env python

from turtle import forward, shape, right
def start_spacial(sh, size, turn):
    right(turn)
    draw_rect_based_on(sh, size)

def draw_rect_based_on(sh, size):
    shape(sh)
    for i in range(5):
        forward(size)
        right(144)

if __name__ == "__main__":
    for i in range(60):
        size = i*5+ 5
        start_spacial('triangle', size, 5)
    input("please press anything to finish")