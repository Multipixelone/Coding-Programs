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
pen1.speed("fastest")
for i in range(1000000):
    pen1.color(random.random(),
           random.random(),
           random.random())
    pen1.up()
    pen1.goto(random.randrange(-240, 240),
          random.randrange(-240, 240))
    pen1.down()
    polygon(pen1,random.randrange(3, 15), 25)

    pen2.color(random.random(),
           random.random(),
           random.random())
    pen2.up()
    pen2.goto(random.randrange(-240, 240),
          random.randrange(-240, 240))
    pen2.down()
    polygon(pen2,random.randrange(3, 15), 25)
