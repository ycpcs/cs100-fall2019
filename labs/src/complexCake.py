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

def moveBetweenSquares(t1,size1,size2):
	# THIS CODE IS NOT CORRECT
	# TODO: ADD CODE TO MOVE BETWEEN SQUARE CENTERS
	t1.forward(size1)
	
def drawLayerCake(t2,size):
	# THIS CODE IS NOT CORRECT
	# TODO: ADD CODE TO DRAW A LAYER CAKE WITH THE 
	#       TOP SQUARE SIDE LENGTH OF size
	#       USING THE moveBetweenSquares() FUNCTION
	drawSquareFromCenter(t2,size)

def main():
    # Create turtle named bob
    bob = turtle.Turtle()
    # Uncomment the following line to speed up the turtle
    #bob.speed(1000)

    # Get user input
    size = int(input('Enter size for the top square: '))

	# THIS CODE IS NOT CORRECT
	# TODO: ADD CODE TO DRAW THE GIVEN FIGURE
	#       USING THE drawLayerCake() FUNCTION
	drawLayerCake(bob,size)

    # Press any key to exit
    input()

main()