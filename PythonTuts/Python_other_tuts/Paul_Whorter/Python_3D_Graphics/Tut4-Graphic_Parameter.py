from vpython import *
from time import *
mRadius=2
wallThickness=1
roomWidth=15
roomDepth=12
roomHeight=8
floor=box(pos=vector(0,-roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
ceiling=box(pos=vector(0,roomHeight/2,0),size=vector(roomWidth,wallThickness,roomDepth), color=color.white)
backWall=box(pos=vector(0,0,-roomDepth/2),size=vector(roomWidth,roomHeight,wallThickness), color=color.white)
leftWall=box(pos=vector(-roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
rightWall=box(pos=vector(roomWidth/2,0,0),size=vector(wallThickness,roomHeight,roomDepth), color=color.white)
marble=sphere(radius=mRadius,color=color.red)
deltaX=.1
xPos=0
while True:
    rate(25)
    xPos=xPos+deltaX
    Xrme=xPos+mRadius
    Xlme=xPos-mRadius
    Rwe=roomWidth/2-wallThickness/2
    Lwe=-roomWidth/2+wallThickness/2
    if Xrme>=Rwe or Xlme<Lwe:
        deltaX=deltaX*(-1) 
    marble.pos=vector(xPos,0,0)