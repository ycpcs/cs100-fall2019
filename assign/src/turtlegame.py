# CS100 - Assign3 Fall 2019
# Import turtle graphics library
import turtle

# Import math functions
from math import *

# draw a rectangle at upper-left corner (x1, y1) with the specified fill color
# rectangle passes in a 4-tuple of consisting of (x1, y1, x2, y2)
#  size is determined by upper-left (x1, y1) and lower-right (x2, y2) corners
# rectangle dimensions:
#   width:  x2 - x1
#   height: y2 - y1
def drawRectangleAtPosition(turtle, rectangle, fill):

    # save current position and orientation
    (x,y) = turtle.position()
    heading = turtle.heading()

    # get upper-left and lower-right corners of rectangle
    (x1, y1, x2, y2) = rectangle

    # calc width and height from upper-left and lower-right corners
    width  = abs(x2 - x1)
    height = abs(y2 - y1)

    # position turtle to upper-left corner
    turtle.penup()
    turtle.setposition(x1, y1)
    turtle.setheading(0)
    if fill != "none":
        turtle.color(fill)
        turtle.begin_fill()
    else:
        turtle.color("black")
    turtle.pendown()

    # draw rectangle
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

    # return turtle to original position and orientation
    turtle.penup()
    turtle.end_fill()
    turtle.setposition(x, y)
    turtle.setheading(heading)
    turtle.color("black")


# draw a circle centered at (x1, y1) with the specified radius and color
# circle passes in a 3-tuple of consisting of (x1, y1, radius)
# (x1, y1) is the center of the circle
# radius is the radius of the circle
def drawCircleAtPosition(turtle, circle, fill):

    # save current position and orientation
    (x,y) = turtle.position()
    heading = turtle.heading()

    # get center and radius of circle
    (x1, y1, radius) = circle

    # position turtle to center of circle
    turtle.penup()
    turtle.setposition(x1, y1-radius)
    turtle.setheading(0)

    # set fill color
    if fill != "none":
        turtle.color(fill)
        turtle.begin_fill()
    else:
        turtle.color("black")
    turtle.pendown()

    # draw circle
    turtle.circle(radius)

    # return turtle to original position and orientation
    turtle.penup()
    turtle.end_fill()
    turtle.setposition(x, y)
    turtle.setheading(heading)
    turtle.color("black")

# detects collision of the turtle with the inside of the given boundary
# a collision occurs if the turtle attempts to leave the inside of the boundary
# boundary is a 4-tuple of (x1, y1, x2, y2)
# (x1, y1) is the upper-left corner
# (x2, y2) is the lower-right corner
# returns True if a collision is detected, and False otherwise
def detectCollisionWithBoundary(turtle, boundary):

    # get current position
    (x,y) = turtle.position()

    # get boundary dimensions
    (x1, y1, x2, y2) = boundary

# TODO 1: implement the code for the following comment
    # boundary is centered around origin
    # turtle must stay inside boundary
    # left edge is at x1, right edge is at x2
    # top edge is at y1, bottom edge is at y2




    return False

# detects collision of the turtle with the outside of the given rectangle
# rectangle is a 4-tuple of (x1, y1, x2, y2)
# (x1, y1) is the upper-left corner
# (x2, y2) is the lower-right corner
# returns True if a collision is detected, and False otherwise
def detectCollisionWithRectangle(turtle, rectangle):

    # get current position
    (x,y) = turtle.position()

    # get the corners of the rectangle
    (x1, y1, x2, y2) = rectangle

# TODO 2: implement the code for the following comment
    #  if x is right of left edge and left of right edge,
    # and y is below top edge and above bottom edge
    # then turtle has collided with rectangle



    return False

# detect collision of turtle with the outside of the given circle
# circle is a 3-tuple of (x1, x2, radius)
# (x1, x2) is the center of the circle
# radius is the radius of the circle
# returns True if a collision is detected, and False otherwise
def detectCollisionWithCircle(turtle, circle):

    # get current position
    (x, y) = turtle.position()

    # get center and radius of circle
    (x1, y1, radius) = circle

# TODO 3: implement the code for the following comment
    # if turtle is within a radius distance of the center of the circle
    # then the turtle has collided with the circle
    # Pythagorean theorem for distance between turtle and center of circle



    return False

# get new heading from user
# the user can select from various mnemonic choices, e.g., east, up, left, etc...
# the use can also specify how far to turn from the current orientation
# + values are CCW, - values are CW
# the user is prompted for values until a valid values is entered
# a try/except block is used to get the integer degrees
def getNewHeading(turtle):

    # initialize loop variable to False
    # haveReading is set to True when the user enters a valid heading
    haveHeading = False

    # keep trying until user enters valid choice
    while (not haveHeading):

        # reset flag for valid input
        haveHeading = True

        # get current heading
        heading = turtle.heading()

        # print menu of choices
        print("Heading choices:")
        print("   e  - east")
        print("   ne - northeast")
        print("   n  - north")
        print("   nw - northwest")
        print("   w  - west")
        print("   sw - southwest")
        print("   s  - south")
        print("   se - southeast")
        print("   u  - up")
        print("   d  - down")
        print("   l  - left")
        print("   r  - right")
        print("   f  - forward")
        print("   b  - backward")
        print("   ### - degrees to turn (+ CCW, - CW")

        # get choice from user
        choice = input("Enter new heading: ")

        # convert choice to lower-case
        choice = choice.lower()

        # East: set heading to 0
        if choice == "e":
            heading = 0
        # Northeast: set heading to 45
        elif choice == "ne":
            heading = 45
        # North or Up, set heading to 90
        elif choice == "n" or choice == "u":
            heading = 90
        # Northwest: set heading to 135
        elif choice == "nw":
            heading = 135
        # West: set heading to 180
        elif choice == "w":
            heading = 180
        # Southwest: set heading to 225
        elif choice == "sw":
            heading = 225
# TODO 4: add code for the following comments
# TODO 4: look at the above menu for headings and test for the applicable value(s)
        # South or Down, set heading to 270



        #  Southeast: set heading to 315




        # Left: add 90 to current heading (turn 90 degrees CCW)




        # Right: subtract 90 from current heading (turn 90 degrees CW)




        # Forward: maintain current heading




        # Backward: subtract 180 from current heading




        # otherwise: must be degrees to turn from current heading, add to current heading
        # (+) is CCW turn
        # (-) is CW turn
        else:
            # try to convert choice to an integer
            try:
                heading += int(choice)
            # failed to convert, must be invalid input
            # stay in while loop
            except:
                print("Invalid choice, try again")
                haveHeading = False

        # user entered valid heading, return new heading
        if haveHeading:
            return heading

# Creates an external rectangular boundary as a game board, and places some obstacles
# inside the boundary on the game board
# The user enters the maximum length for each move, and then is prompted for a new heading
# at the end of each move.
# The user is allowed to have 4 collisions with the boundary and the obstacles while moving
# around the game board.
def main():
    # create turtle
    bob = turtle.Turtle()

    # set speed to FAST
    bob.speed(0)

    # set size of game field
    width  = 800
    height = 600

    # set boundary rectangle upper-left and lower-right corners
    boundary = (-width/2, height/2, width/2, -height/2)

    # specify upper-left and lower-right corners for rectangular obstacles
    rectangle1 = ( 250, 200,  350, -200)
    rectangle2 = (-350, 200, -250, -200)

    # specify center and radius for circular obstacles
    circle1 = ( 10,  190, 75)
    circle2 = ( 10, -190, 75)
    circle3 = (-115,  10, 75)
    circle4 = ( 115,  10, 75)

    # draw boundary lines, with no fill
    drawRectangleAtPosition(bob, boundary, "none")

    # draw rectangular obstacles in red
    drawRectangleAtPosition(bob,  rectangle1, "red")
    drawRectangleAtPosition(bob,  rectangle2, "red")

    # draw circular obstacles in red
    drawCircleAtPosition(bob, circle1, "red")
    drawCircleAtPosition(bob, circle2, "red")
    drawCircleAtPosition(bob, circle3, "red")
    drawCircleAtPosition(bob, circle4, "red")

    # initialize maximum length of each move
    maxMove = 0

# TODO 5: surround the prompt below with a loop that validates the user input
    # get maxMove distance from user
    # validate maximum move value to be within the range 20 to 200 pixels inclusive
    # keep prompting until the user enters a valid value

    # prompt user for value
    maxMove = int(input("Enter maximum distance to travel between moves (20-200 pixels): "))




    # set max allowed collisions
    maxCollisions = 4

    # initialize # of collisions detected
    collisions = 0

    # set collision flag for no collision detected
    collision = False

    # set initial heading to East
    bob.setheading(0)

    # initialize distance traveled for current move
    distance  = 0

    # this loop runs the program as long as the user
    # has not exceeded the allowed number of collisions
    while collisions <= maxCollisions:

        # this loop handles movement for the current heading
        # if not at end of current move and no collision detected
        # it moves the turtle by one pixel and then checks for collisions
        # and the end of the current move
        while (distance < maxMove) and (not collision):
            # attempt to move forward, 1 pixel at a time
            # leave a trail where turtle has been
            bob.pendown()
            bob.forward(1)
            bob.penup()

            # check for collision with boundary
            collision = detectCollisionWithBoundary(bob, boundary)

            # if no collision, check for collision with circle1
            if not collision:
                collision = detectCollisionWithCircle(bob, circle1)

            # if no collision, check for collision with circle2
            if not collision:
                collision = detectCollisionWithCircle(bob, circle2)

# TODO 6: add collision detection for circle3 and circle4

            # if no collision, check for collision with rectangle1
            if not collision:
                collision = detectCollisionWithRectangle(bob, rectangle1)

# TODO 7: add collision detection for rectangle2




# TODO 8: add the code specified by the following comment
            #  if no collision, increment distance traveled for this move


# TODO 9: add the code that detects the end of the current move
# TODO 9: prompts the user for the next heading (which is included)
# TODO 9: retrieves the new heading
# TODO 9: resets the distance for the next move
        # if reached end of current move





# TODO 10: add the elif condition that checks if a collision was detected
# TODO 10:    count the collisions
# TODO 10:    check for too many collisions and tell the user if that has occurred
# TODO 10:    if a collision has occurred (but maxCollisions was not exceeded)
# TODO 10:       move the turtle away from the obstacle it collided with by 1 pixel
# TODO 10:       prompt the user for a new heading (already provided)
# TODO 10:       get the new heading from the user
        # otherwise, turtle must have collided with an obstacle







    input("Press any key to exit")

main()

