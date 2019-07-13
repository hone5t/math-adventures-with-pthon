#!/usr/bin/env python

from turtle import forward, shape, right

def draw_rect_based_on(sh, size):
    shape(sh)
    for i in range(4):
        forward(size)
        right(270)
    
if __name__ == "__main__":
    draw_rect_based_on('turtle', 100)
    input("please press enter to end:")