# Import turtle graphics library
import turtle
from math import *


# Function to draw a square about the current position
#    First argument is turtle to draw with
#    Second argument is size of square sides
def drawSquareFromCenter(tur, size):
    halfsize = size / 2
    tur.penup()
    tur.forward(-halfsize)
    tur.right(90)
    tur.forward(halfsize)
    tur.left(90)
    tur.pendown()
    tur.forward(size)
    tur.left(90)
    tur.forward(size)
    tur.left(90)
    tur.forward(size)
    tur.left(90)
    tur.forward(size)
    tur.left(90)
    tur.penup()
    tur.forward(halfsize)
    tur.left(90)
    tur.forward(halfsize)
    tur.right(90)


def drawRow(t, squareSize, numSquares):
    # TODO: ADD CODE TO DRAW A ROW OF SQUARES
    # draw row of squares
    for i in range(numSquares):
        drawSquareFromCenter(t, squareSize)
        t.penup()
        t.forward(squareSize)

    # move back to start
    t.penup()
    t.forward(-numSquares * squareSize)


def main():
    # Create turtle named bob
    bob = turtle.Turtle()
    # Uncomment the following line to speed up the turtle
    # bob.speed(1000)

    # Get user input
    maxHeight = int(input('Enter the maximum size for the stack: '))

    stackHeight = 0
    numBlocks = 1

    # TODO: Continue to draw rows as long as
    #       total stack height is less than maxHeight
    #       AND numBlocks is greater than 0

    # TODO: Validate user input size to be positive

    numBlocks = int(input('Enter the number of blocks for the row: '))

    # TODO: if the number of blocks is positive
    #       set color to red if odd
    #       set color to green if even
    #       move to center of left square, draw row, move to top center of row, and
    #       update stackHeight


# Press any key to exit
input()

main()