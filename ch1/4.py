#!/usr/bin/env python

from turtle import forward, shape, right

def draw_poli_based_on(sh, size):
    shape(sh)
    for i in range(6):
        forward(size)
        # i draw poli stroking the pen down with triangle i usually go up
        right(60)
    
    
if __name__ == "__main__":
    draw_poli_based_on('triangle', 100)
    input("please press enter to end:")