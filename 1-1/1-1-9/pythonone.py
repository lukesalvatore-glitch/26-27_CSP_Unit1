import turtle

# Create The Background
screen = turtle.Screen()
screen.bgcolor("light blue")

duck = turtle.Turtle()
pen = turtle.Turtle()
t = turtle.Turtle()  # Turtle instance for drawing the sun

duck.speed(100)
duck.hideturtle()
t.speed(100)
t.hideturtle()

# Define body parts: (x, y, radius, color)
body_parts = [
    (0, -100, 70, "yellow"),  # Body of duck
    (40, 0, 55, "yellow"),  # Head of duck
    (65, 55, 15, "white"),  # Eye of duck
    (65, 65, 5, "black")  # Pupil of duck
]

# Draw Duck Body, Head, and Eye
for x, y, radius, color_name in body_parts:
    duck.penup()
    duck.goto(x, y)
    duck.pendown()
    duck.color(color_name)
    duck.begin_fill()
    duck.circle(radius)
    duck.end_fill()

# Draw Beak
duck.penup()
duck.goto(80, 35)
duck.pendown()
duck.color('light pink')
duck.begin_fill()
for step in range(3):
    duck.forward(30)
    duck.left(120)
duck.end_fill()

# Draw Legs and Feet
leg_positions = [-20, 20]
for x_pos in leg_positions:
    duck.penup()
    duck.goto(x_pos, -80)
    duck.pendown()
    duck.color('orange')
    duck.pensize(5)
    duck.goto(x_pos, -140)

    # Draw Foot
    duck.begin_fill()
    duck.setheading(0)
    for step in range(3):
        duck.forward(15)
        duck.left(120)
    duck.end_fill()



def draw_sun(radius, color):
    t.penup()
    t.goto(-350, 200)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
draw_sun(65, "gold")
screen.bgcolor("black")
def draw_moon(radius, color):
    t.goto(-350,200)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
draw_moon(65,"gray")



turtle.done()