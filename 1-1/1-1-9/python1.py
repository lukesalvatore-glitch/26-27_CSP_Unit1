import turtle

# Create The Background
screen = turtle.Screen()
screen.bgcolor("light blue")

duck = turtle.Turtle()
duck.speed(1)
duck.hideturtle()


body_parts = [
    (0, -100, 70, "yellow"),  # Body of duck
    (40, 0, 55, "yellow"),  # Head of duck
    (65, 55, 15, "white"),  # Eye of duck
    (65, 65, 5, "black")  # Pupil of duck
]


for x, y, radius, color_name in body_parts:
    duck.penup()
    duck.goto(x, y)
    duck.pendown()
    duck.color(color_name)
    duck.begin_fill()


    if color_name == "yellow":
        duck.circle(radius)
    elif color_name in ["black", "white"]:
        duck.circle(radius)

    duck.end_fill()


duck.penup()
duck.goto(80, 35)
duck.pendown()
duck.color('orange')
duck.begin_fill()

for step in range(3):
    duck.forward(30)
    duck.left(120)
duck.end_fill()


leg_positions = [-20, 20]

for x_pos in leg_positions:
    duck.penup()
    duck.goto(x_pos, -100)
    duck.pendown()
    duck.color('orange')
    duck.pensize(5)
    duck.goto(x_pos, -140)
    duck.begin_fill()
    duck.setheading(0)


    for step in range(3):
     duck.forward(25)
    duck.left(120)

    duck.end_fill()

turtle.done()