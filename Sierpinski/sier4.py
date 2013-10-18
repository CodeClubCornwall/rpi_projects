from turtle import *
from math import sqrt

# Draw several dots towards the line
#
# New command:
#   dot(size)

penup()

point = [ 100, 100 ]

for i in range(10):
    angle = towards(point[0], point[1])
    print("Angle to point is " + str(angle) + " degrees")

    print("Turning towards that point ...")

    setheading(angle)

    x, y = position()
    print("Current x = " + str(x))
    print("Current y = " + str(y))

    distance = sqrt( (point[0] - x)**2 + (point[1] -y)**2 )

    print("Distance from turtle to point: " + str(distance))

    print("Drawing line of half that distance ...")

    forward(distance/2)

    dot(5)
