# vpython ki madat se ham 3d animation, image or video bhi bana sakte
from vpython import *  # library
from time import *
# abhi bas dekhege ki ball ke characteristics kaise change kar sakte or alag  alag shape
# sphere
# parameter - color, pos, radius, or bhi hai abhi  nahi batae
ball = sphere(color=color.red, pos=vector(0,-3,0))  # creating a sphere
# sleep(5) # ball bana ke ruk thodi deer
# ball.color = color.blue  # phir uska characteristics change karde
# sleep(5) # vapis ruk
# ball.color = color.green  # uska dusara characteristics change kardo

# box(cube, cuboid)
# parameter - pos(vector chahiye isme) - helo to set position of object, color, length, width, height, or bhi hai
#                      x, y, z
wall = box(pos=vector(0, -5, 0), color=color.yellow, length=10, width=10, height=.2)
ceiling = box(pos=vector(0, 5, 0), color=color.yellow, length=10, width=10, height=.2)
backWall = box(pos=vector(0, 0, -5), color=color.yellow, length=10, width=.2, height=10)
rightWall = box(pos=vector(-5, 0, 0), color=color.yellow, length=.2, width=10, height=10)
leftWall = box(pos=vector(5, 0, 0), color=color.yellow, length=.2, width=10, height=10)

# cylinder
# parmeter sabme bhhot sare hai abhi nahi bataya
# myCylinder = cylinder(color=color.orange, length=6, radius=1)  # radius ki jagaha width or height bhi de sakta
# myCylinder = cylinder(color=color.orange, length=2, width=6, height=1)
while True:
    pass  # just do nothing jo uper likha hai use conti karte raho