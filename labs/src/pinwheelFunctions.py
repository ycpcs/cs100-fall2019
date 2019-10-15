# Import turtle graphics library
import turtle

# Import math functions
from math import *

# Function to draw a square about the current position
def drawSquareFromCenter(t,size):
    halfsize = size/2
    t.penup()
    t.forward(-halfsize)
    t.right(90)
    t.forward(halfsize)
    t.left(90)
    t.pendown()
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.penup()
    t.forward(halfsize)
    t.left(90)
    t.forward(halfsize)
    t.right(90)

# TODO: Right turn movement function
def moveToCenterRightTurn():
    # DELETE THIS LINE
    pass;

# TODO: Diagonal movement function
def moveToCenterDiagonal():
    # DELETE THIS LINE
    pass;

# TODO: Complete program to call functions
#       to draw pinwheel
def main():
    # Create turtle
    bob = turtle.Turtle()

    # Get user input
    size1 = int(input('Enter size for first square: '))

    # Draw first square
    drawSquareFromCenter(bob,size1)

    # Press any key to exit
    input()

main()