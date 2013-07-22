from turtle import *
import random

def polygon(pen, sides, length):
    """ makes a [sides] sided polygon polygon each side is [length] long """
    for i in range(sides):
        pen.forward(length)
        pen.right( 360.0 / sides  )

                         
pen1 = Pen()
pen2 = Pen()


for i in range(1000):
    polygon(pen1, 5,100)
    pen1.speed("fastest")
    pen1.right(10)
    pen1.color("purple")

    polygon(pen2, 5,100)
    pen2.speed("fastest")
    pen2.right(1)
    pen2.color(random.random(),
        random.random(),
        random.random())
                   
    polygon(pen2, 5,100)
    pen2.speed("fastest")
    pen2.right(1)
    pen2.color("blue")
