from vpython import *  # library
from time import *
# use variables instead of constant
# edgeBall = 20
eb = .75
mRadius = .75
# wallThickness = .1
wt = .1
# roomWidth, roomHeight, roomDepth = 10
# rw, rh, rd = 150, 30, 50
# rw, rh, rd = 1, 3, 5
rw, rh, rd = 15, 10, 5  # isse kya hua ki agar tujhe room ki height change karna hai to tu ab ek hi jagaha se kar sakta pura coe nahi dekhna padega
#  isme ek or parameter hai "size" - length width or height ka kam ek me
floor = box(pos=vector(0, -rh/2, 0), color=color.yellow, size=vector(rw, wt, rd))
ceiling = box(pos=vector(0, rh/2, 0), color=color.yellow, size=vector(rw, wt, rd))
backWall = box(pos=vector(0, 0, -rd/2), color=color.yellow, size=vector(rw, rh, wt))
rightWall = box(pos=vector(-rw/2, 0, 0), color=color.yellow, size=vector(wt, rh, rd))
leftWall = box(pos=vector(rw/2, 0, 0), color=color.yellow, size=vector(wt, rh, rd))
ball = sphere(color=color.red, radius=mRadius)
# variable for animating the ball
deltaX = .1
xPos = 0
while True:
    # instead of sleep use vpython command - rate
    rate(100)
    # xpos k badate raho har pal deltax se
    xPos = xPos+deltaX
    # jabh ball wall ko takarae tabh usse dusari direction e bejhdo
    if xPos+eb > rw/2 or xPos-eb < -rw/2:
        deltaX = deltaX*(-1)
    # position set kardo ball ki
    ball.pos = vector(xPos, 0, 0)