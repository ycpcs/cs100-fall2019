# Import turtle graphics library
import turtle
from math import *

# Function to draw a square about the current position
#    First argument is turtle to draw with
#    Second argument is size of square sides
def drawSquareFromCenter(tur,size):
    halfsize = size/2
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

def drawRow(t,squareSize,numSquares):
	# TODO: ADD CODE TO DRAW A ROW OF SQUARES
	pass;
	
def main():
    # Create turtle named bob
    bob = turtle.Turtle()
    # Uncomment the following line to speed up the turtle
    #bob.speed(1000)

    # Get user input
    size = int(input('Enter size for the squares: '))
    height = int(input('Enter the height of the pyramid: '))

	# TODO: ADD CODE TO DRAW THE PYRAMID

    # Press any key to exit
    input()

main()