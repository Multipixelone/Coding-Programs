from turtle import *
import random

def polygon(pen, sides, length):
    """ makes a [sides] sided polygon polygon each side is [length] long """
    for i in range(sides):
        pen.forward(length)
        pen.right( 360.0 / sides  )
        
                         
pen1 = Pen()



for i in range(180):
    pen1.speed("fastest")
    pen1.right(2)
    pen1.forward(125)
    pen1.back(125)
    pen1.color(random.random(),
               random.random(),
               random.random())
   
    

