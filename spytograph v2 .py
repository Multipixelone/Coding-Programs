from turtle import *
import random

def polygon(pen, sides, length):
    """ makes a [sides] sided polygon polygon each side is [length] long """
    for i in range(sides):
        pen.forward(length)
        pen.right( 360.0 / sides  )
        
                         
pen1 = Pen()
pen2 = Pen()
pen2.speed("fastest")

for i in range(1000):
    polygon(pen1, 10,30)
    pen1.speed("fastest")
    pen1.right(2)
    pen1.color(random.random(),
           random.random(),
           random.random())
    polygon(pen2, 10,60)
    pen2.right(2)
    pen2.color(random.random(),
           random.random(), 
           random.random())
    pen2.circle(70)    

