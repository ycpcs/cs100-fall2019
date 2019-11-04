# CS100 Assignment 2 - Fall 2019
# Import turtle graphics library
import turtle

# Import math functions
from math import *

# draw a square centered at the current cursor position
# TODO 1: convert drawSquareFromCenter() to use a loop to draw the 4 sides of the square
def drawSquareFromCenter(turtle,x):
    turtle.penup()
    turtle.forward(-x / 2)
    turtle.right(90)
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.penup()
    turtle.forward(x / 2)
    turtle.left(90)
    turtle.forward(x / 2)
    turtle.right(90)

# right turn movement function to move from corner to center of square
def moveToCenterRightAngle(turtle, size):
    turtle.penup()
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size/2)
    turtle.right(90)

# diagonal movement function between centers of 2 squares
def moveToCenterDiagonal(turtle, sizeSrc, sizeDest):
    turtle.penup()
    dx = (sizeDest - sizeSrc) / 2
    dy = (sizeSrc + sizeDest) / 2
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dx, dy))
    turtle.left(angle)
    turtle.forward(dist)
    turtle.right(angle)

# equilateral triangle function
# TODO 2: convert drawEquiTriangle() to use a loop to draw the 3 sides of the triangle
def drawEquiTriangle(turtle, size):
    turtle.pendown()
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.penup()

# right triangle function
def drawRightTriangle(turtle, base, height):
    hyp = sqrt(base**2 + height**2)
    angle = degrees(atan2(base, height))
    turtle.pendown()
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(180 - angle)
    turtle.forward(hyp)
    turtle.left(90 + angle)
    turtle.penup()

# isoosceles triangle function
def drawIsoTriangle(turtle, base, height):
    side = sqrt((base/2)**2 + height**2)
    angle = degrees(atan2(height, base/2))
    turtle.pendown()
    turtle.forward(base)
    turtle.left(180 - angle)
    turtle.forward(side)
    turtle.left(angle * 2)
    turtle.forward(side)
    turtle.left(180 - angle)
    turtle.penup()

# TODO 3: implement drawRegHexagon(turtle, size) so that it calls
# TODO 3: drawEquiTriangle() within a loop to draw a regular hexagon with triangles
# TODO 3: make sure to return the cursor to its original location and orientation
def drawRegHexagon(turtle, size):
    drawEquiTriangle(turtle, size)


# TODO 4: implement a function that uses a loop to generate a hexagon using
# TODO 4: incrementally increasing equilateral triangles
# TODO 4: use the loop counter to calculate the sizes of the sides of the hexagon so that each
# TODO 4: side is size/5 pixels bigger than the previous side
# TODO 4: the last triangle drawn will be twice the size of the first triangle drawn
# TODO 4: make sure to return the cursor to its original location and orientation
def drawPinwheelHexagon(turtle, size):
    drawEquiTriangle(turtle, size)

# TODO 5: implement a function that draws a 4-pointed star, using the following functions:
# TODO 5:    drawSquareFromCenter() and drawIsoTriangle()
# TODO 5: after drawing the center square, use a loop to draw the 4 points of the star around the square
# TODO 5: the name of the function should be drawStar(), and it should accept the following 3 parameters:
# TODO 5:   turtle: the turtle object that will do the drawing
# TODO 5:   size: the size of the center square (also the base of the isosceles triangles)
# TODO 5:   height: the height of the isosceles triangles that make up the points of the star
# TODO 5: make sure to return the cursor to its original location and orientation


def main():
    # create turtle
    bob = turtle.Turtle()

    # get user input
    size   = int(input('Enter size for EquiTriangles, base of IsoTriangles, and square in star: '))
    height = int(input('Enter height for IsoTriangles (points of star): '))
    radius = int(input("Enter radius of star constellation; "))
    stars  = int(input("Enter number of stars in constellation: "))

    # draw equilateral triangle
    drawEquiTriangle(bob, size)

    # wait for user
    input("Press any key to draw isosceles triangle")
    bob.clear()

    # draw isosceles triangle
    drawIsoTriangle(bob, size, height)

    # wait for user
    input("Press any key to draw regular hexagon")
    bob.clear()

    # draw regular hexagon
    drawRegHexagon(bob, size)

    # wait for user
    input("Press any key to draw pinwheel hexagon")
    bob.clear()

    # draw pinwheel hexagon using equilateral triangles
    drawPinwheelHexagon(bob, size)

    # wait for user
    input("Press any key to draw the central star")
    bob.clear()

    # TODO 6: call the function to draw 4-pointed star at center
    # TODO 6: size specifies the size of the square and the base of the iso triangles
    # TODO 6: height specifies the height of the iso triangles (points of the stars)




    # wait for user
    input("Press any key to draw the constellation of stars")

    # TODO 7: use a loop to draw a constellation of stars around the central star
    # TODO 7:    radius specifies the distance from the origin to the center of each star
    # TODO 7:    stars specifies the # of stars to draw around the central star
    # TODO 7: make sure that the stars are evenly spaced around the central star
    # TODO 7: make sure to return the cursor to its original location and orientation



    # Press any key to exit
    input("Press any key to exit")

main()