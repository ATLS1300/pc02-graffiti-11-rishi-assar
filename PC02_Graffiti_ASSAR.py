#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

Turtle() # creating a turtle to draw!
up() #picks up pen (stop drawing)
goto(-125,-350) # goes to x,y coordinate
down() #drops pen (start drawing)
color("red")
write("amazon", font=("Arial", 70, "normal"))
up()
width(3)
goto(0,0)
down()
forward(80)
left(100)
forward(230)
left(80)
forward(150)
left(100)
forward(230)
left(80)
forward(75)
home()
up()
goto(105,-85)
down()
color([0,250,0])
width(10)
right(15)
forward(400)
up()
goto(10,-75)
down()
color("orange")
fillcolor("purple") 
begin_fill()
width(3)
left(95)
forward(50)
left(100)
forward(50)
left(130)
forward(62)
end_fill()
up()
goto(-15,112)
down()
color("blue")
dot(10)
up()

home()