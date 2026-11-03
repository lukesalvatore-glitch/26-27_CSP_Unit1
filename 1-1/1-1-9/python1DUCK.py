import turtle

# Create The Background
screen = turtle.Screen()
screen.bgcolor("light blue")



duck = turtle.Turtle()
duck.speed(1)
duck.hideturtle()

# Draw the body of the duck
duck.penup()
duck.goto(0, -100)
duck.pendown()
duck.color('yellow')
duck.begin_fill()
duck.circle(70)
duck.end_fill()

# Draw the head of the duck
duck.penup()
duck.goto(40, 0)
duck.pendown()
duck.color('yellow')
duck.begin_fill()
duck.circle(55)
duck.end_fill()

# Draw The Eye
duck.penup()
duck.goto(65,55)
duck.pendown()
duck.color('black')
duck.begin_fill()
duck.circle(15)
duck.end_fill()

# Draw The Pupil
duck.penup()
duck.goto(65,65)
duck.pendown()
duck.color('white')
duck.begin_fill()
duck.circle(5)
duck.end_fill()

# Draw The Beak
duck.penup()
duck.goto(80, 35)
duck.pendown()
duck.color('orange')
duck.begin_fill()
for step in range(3):
  duck.forward(30)
  duck.left(120)
duck.end_fill()

# Draw Left Leg
duck.penup()
duck.goto(-20, -100)
duck.pendown()
duck.color('orange')
duck.pensize(5)
duck.goto(-20, -140)
duck.begin_fill()
duck.setheading(0)
duck.forward(25)
duck.left(120)
duck.forward(25)
duck.left(120)
duck.forward(25)
duck.end_fill()

# Draw Right Leg
duck.penup()
duck.goto(20, -100)
duck.pendown()
duck.color('orange')
duck.pensize(5)
duck.goto(20, -140)
duck.begin_fill()
duck.setheading(0)
duck.forward(25)
duck.left(120)
duck.forward(25)
duck.left(120)
duck.forward(25)
duck.end_fill()


# Make sure to keep the window open until the user x's out
screen.mainloop()