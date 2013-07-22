from turtle import *
pen1 = Pen()
pen2 = Pen()
# Define the function
def polygon(pen, sides, length):
    pen1.fd(length)
    pen1.right(360 / sides)
# Call the function
polygon(pen1, 5, 75)
polygon(pen2, 4, 100)
