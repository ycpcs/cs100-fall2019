import turtle
from math import *

def drawSquareFromCenter(t,x):
    t.penup()
    t.forward(-x/2)
    t.right(90)
    t.forward(x/2)
    t.left(90)
    t.pendown( )
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.penup( )
    t.forward(x/2)
    t.left(90)
    t.forward(x/2)
    t.right(90)


def main():
    # create turtle
    bob = turtle.Turtle()

    # get user input
    size1 = int(input("Enter size for the diamonds: "))

    # TODO 0: create and initialize variables we will use
    # calc diagonal of diamonds
    diagSize1 = size1 * sqrt(2)

    # calc half diagonal of diamonds
    halfDiag1 = diagSize1 / 2

    # calc size of larger square that circumscribes diamonds
    # it is twice the diagonal of the diamonds
    size2 = diagSize1 * 2

    # TODO 1: draw larger square, centered around origin
    drawSquareFromCenter(bob, size2)

    # TODO 2: draw the horizontal diagonal of the diamonds
    # back up to left edge of large square
    bob.forward(-diagSize1)

    # draw horizontal diagonal
    bob.pendown()
    bob.forward(size2)

    # return to origin
    bob.penup()
    bob.forward(-diagSize1)

    # draw the as diamonds, centered around the origin
    # drawing diamonds in clockwise fashion (E, S, W, N)
    # TODO 3: move to the center of 1st diamond (east along diagonal)
    bob.forward(halfDiag1)

    # turn the cursor down (SE) 45 degrees to draw diamonds using square function
    bob.right(45)

    # TODO 4: draw 1st diamond (east)
    drawSquareFromCenter(bob,size1)

    # TODO 5: move to center of 2nd diamond (SW)
    bob.right(90)
    bob.forward(size1)

    # TODO 6: draw 2nd diamond (south)
    drawSquareFromCenter(bob,size1)

    # TODO 7: move to center of 3rd diamond (NW)
    bob.right(90)
    bob.forward(size1)

    # TODO 8: draw 3rd diamond (west)
    drawSquareFromCenter(bob,size1)

    # TODO 9: move to center of 4th diamond (NE)
    bob.right(90)
    bob.forward(size1)

    # TODO 10: draw 4th diamond (north)
    drawSquareFromCenter(bob,size1)

    # TODO 11: return cursor to origin (S)
    bob.right(135)
    bob.forward(halfDiag1)
    bob.left(90)

    # wait for user input before exiting
    input("Press any key to exit")

main()