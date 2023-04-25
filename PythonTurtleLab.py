# Turtle Lab #4
# 4/3/2022
# Anthony Al-khafaji
# Turtle goes on Vacation using modular programing

import turtle
import time
#import math
# Module to Reset Turtle
def ResetTurtle():
    time.sleep(3)
    turtle.reset()
    turtle.shape("classic")
# Module for Hiking
def MountainHike(color, size):
    # shape the turtle
    turtle.shape("turtle")
    # turtle color/ design
    turtle.color("green")
    turtle.pencolor(color)
    turtle.pensize(size)
    for i in range (0,4,1):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.forward(50)
    turtle.pencolor(0, 0, 0)
    # display 
    turtle.write("Hurray! I made it to the top!", align="right", font=("Arial", 16, "bold"))
    # reset
    ResetTurtle()
# Module for swimming
def GoingSwiming(color, size):
    turtle.penup()
    # Module Location
    turtle.goto(-165,60)
    turtle.pendown()
    # color/design
    turtle.color("turquoise")
    turtle.pencolor("green")
    turtle.pensize(size)
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(270)
    turtle.shape("turtle")
    turtle.color("orange")
    turtle.pencolor(color)
    turtle.circle(125)
    turtle.pencolor("blue")
    turtle.left(90)
    turtle.forward(100)
    turtle.pencolor(0, 0, 0)
    # display
    turtle.write("Yeah! I'm Swimming!", align="right", font=("Arial", 16, "bold"))
    # reset
    ResetTurtle()
# Module for sleeping turtle
def TurtleBedtime():
    #location
    turtle.penup()
    turtle.goto(250,-250)
    turtle.pendown()
    # color/design
    turtle.pencolor("brown")
    turtle.color("green")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.shape("turtle")
    for i in range(4):
        turtle.forward(75)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(37)
    turtle.left(90)
    turtle.forward(50)
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(15)
        turtle.left(90)
    turtle.right(90)
    for i in range(4):
        turtle.forward(15)
        turtle.left(90)
    turtle.end_fill()
    turtle.shape("turtle")
    turtle.fillcolor("green")
    turtle.pencolor("black")
    turtle.left(90)
    # display
    turtle.write("Good night!" , align="right", font=("Arial", 16, "bold"))
    # reset
    ResetTurtle()
# Module to fead the turtle
def TurtleEating():
    # food colors
    colors = ["blue", "orange", "green", "pink"]
    x = int() # added x & y 
    y = int()
    x = -180
    y = -180
    turtle.penup()
    # location / design
    turtle.goto(x , y)# was -180 both
    turtle.pendown()
    for i in range(0, len(colors), 1):
        turtle.pencolor(colors[i])
        turtle.fillcolor(colors[i])
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        x = x + 10 # added x & y 
        y = y + 10
        turtle.goto(x,y)# added by prof
    turtle.penup()
    turtle.left(180)
    turtle.forward(40)
    turtle.right(180)
    turtle.goto(x , y)# added
    turtle.pendown()
    turtle.shape("turtle")
    turtle.pencolor("white")
    for i in range(0, len(colors), 1):
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(35)# (30)
        turtle.end_fill()
        x = x - 15 # added x & y 
        y = y - 15
        turtle.goto(x,y)
        time.sleep(2)
    turtle.pencolor("black")
    turtle.fillcolor("green")
    # display
    turtle.write("What a great meal!", align="right", font=("Arial", 16, "bold"))
    # reset
    ResetTurtle()
# Main Module
def main():
    turtle.setup(800,600)
    MountainHike("blue", 3)
    GoingSwiming("green", 2)
    TurtleEating()
    TurtleBedtime()
    turtle.done()
# Call Main
main()

