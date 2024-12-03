import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("RAKIB using Turtle")
screen.bgcolor("white")

# Create and set up the turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(5)
t.color("blue")

# Function to move turtle without drawing
def move_without_drawing(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Draw letter R
move_without_drawing(-200, 100)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)
t.left(135)
t.forward(70)

# Draw letter A
move_without_drawing(-100, 100)
t.left(135)
t.forward(100)
t.right(150)
t.forward(100)
move_without_drawing(-80, 150)
t.right(120)
t.forward(40)

# Draw letter K
move_without_drawing(0, 100)
t.left(90)
t.forward(100)
move_without_drawing(0, 150)
t.right(45)
t.forward(70)
move_without_drawing(0, 150)
t.right(90)
t.forward(70)

# Draw letter I
move_without_drawing(80, 100)
t.right(45)
t.forward(100)

# Draw letter B
move_without_drawing(150, 100)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)
t.right(180)
t.circle(-25, 180)

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop() 