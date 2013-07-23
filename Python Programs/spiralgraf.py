# PaulGame2.py

#inport
import random
from turtle import *

#make funson
def polygon(pen, sides, length):
    """ makes a [sides] sided polygon each side is [length]"""
    for i in range(sides):
        pen.fd(length)
        pen.right( 360.0 /sides )

        
        
    

# pens
pen1 = Pen()
pen2 = Pen()
pen3 = Pen()
pen1.speed("fastest")
pen2.speed("fastest")
pen3.speed("fastest")

#patern
for i in range(180):
    pen1.color(random.random(),
           random.random(),
           random.random())
    
    polygon(pen1, 3, 200)
    pen1.right(2)
    
    
    
