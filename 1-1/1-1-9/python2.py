import turtle

# Create The Background
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title('Beginner Turtle Duck Artwork')


duck = turtle.Turtle()
duck.speed(3)
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
duck.goto(65,55)
duck.pendown()
duck.color('white')
duck.begin_fill()