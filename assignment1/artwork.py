# Author: Shawn Yat Sin
# ID: 261052225

import turtle
import math

def polygon(t, length, n):           # Draws a regular polygon with n sides, with each side measuring the length input.
    for i in range(n):
        t.forward(length)
        t.left(360/n)
        
def circle(t, r):                    # Draws a circle with radius r.
    circumference = 2* math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)

def eyes(t):         # Draws the eyes and mouth.
    t.penup()
    t.goto(20, 80)
    t.pendown()
    t.left(45)
    t.forward(40)
    t.fillcolor("white")    # Colors the eyes white.
    t.begin_fill()
    circle(t,30)
    t.backward(70)
    circle(t, 30)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(30)
    t.shape('circle')        # Adds black pupils.
    t.fillcolor("black")
    t.begin_fill()
    t.stamp()
    t.right(90)
    t.forward(70)
    t.left(90)
    t.stamp()
    t.end_fill()
    
def hat(t):                      # Draws a blue triangular hat.
    t.goto(0, 200)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    polygon(t, 120, 3)
    t.end_fill()
     
def body(t):                 # Draws the spine of the stickman and his feet.
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(225)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.fillcolor("brown")
    t.begin_fill()
    polygon(t, 60, 4)
    t.backward(100)
    t.left(90)
    polygon(t, 60, 4)
    t.end_fill()
    
def fingers(t):                      # Draws 5 fingers of length 30 spaced 10 degrees from each other.
    for i in range(5):
        t.left(10)
        t.forward(30)
        t.backward(30)

def arms(t):                     # Draws the arms and the fingers.
    t.penup()
    t.goto(0,-50)
    t.right(90)
    t.pendown()
    t.forward(100)
    fingers(t)
    t.penup()
    t.goto(0,-50)
    t.left(130)
    t.pendown()
    t.forward(100)
    fingers(t)
    
    
def star(t, length, n):    # Draws n number of points of a star (5 or greater makes one star) with each side measuring the length chosen.
    for i in range(n):
        t.right(72)
        t.forward(length)
        t.left(144)
        t.forward(length)

def star_placement(t):
    t.penup()
    t.goto(-200,0)
    t.pendown()
    star(t, 40, 5)           # Draws one star on the left side of the screen.
    t.penup()
    t.goto(200, 0)
    t.pendown()
    for i in range(10):      # Draws 10 stars one at a time rotating 10 degrees to the right after each is drawn.
        star(t, 45, 5)
        t.right(10)
    t.hideturtle()
    
        
def face(t):                  # Draws a circle of radius 90 and colors it yellow.
    t.fillcolor("yellow")
    t.begin_fill()
    circle(t, 90)
    t.end_fill()
    
def letter_S(t, length):     # Draws the letter S by first drawing a semi-circle, then a diagonal, then an inverted semi-circle.
    t.penup()
    t.goto(260, 200)
    t.pendown()
    t.circle(length, 190)
    t.left(30)
    t.forward(3*length)
    t.right(180)
    t.penup()
    t.circle(length, 180)
    t.pendown()
    t.circle(length, 180)
        

def my_artwork():             # Draws my artwork 
    t = turtle.Turtle()
    turtle.speed("fastest")
    t.pensize(2)
    face(t)
    eyes(t)
    hat(t)
    body(t)
    arms(t)
    star_placement(t)
    letter_S(t, 20)



    
