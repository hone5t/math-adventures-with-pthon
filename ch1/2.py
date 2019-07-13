#!/usr/bin/env python

from turtle import forward, shape, right
from time import sleep

def draw_rect_based_on(sh, size, turn):
    right(turn)
    shape(sh)
    for i in range(4):
        forward(size)
        right(270)
    
if __name__ == "__main__":
    for i in range(60):
        draw_rect_based_on('turtle', 100, 5)
    input("please press anything to finish")