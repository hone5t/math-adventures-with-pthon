#!/usr/bin/env python

from turtle import forward, shape, right

def draw_tri_based_on(sh, size):
    shape(sh)
    for i in range(3):
        forward(size)
        right(240)
    
    # for fun lets have it exactly like the book
    forward(size*2)
    
if __name__ == "__main__":
    draw_tri_based_on('triangle', 100)
    input("please press enter to end:")