import turtle

# Create The Background
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.tracer(0)

# Create Duck Turtle
duck = turtle.Turtle()
duck.speed(0)
duck.hideturtle()

# Define body parts: (x, y, radius, color)
body_parts = [
    (0, -100, 70, "yellow"),  # Body of duck
    (40, 0, 55, "yellow"),    # Head of duck
    (65, 55, 15, "white"),    # Eye of duck
    (65, 65, 5, "black")      # Pupil of duck
]

# Draw Duck Body Parts
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
duck.color("orange")
duck.begin_fill()
for step in range(3):
    duck.forward(30)
    duck.left(120)
duck.end_fill()

# Draw Legs
leg_positions = [-20, 20]
for x_pos in leg_positions:
    duck.penup()
    duck.goto(x_pos, -80)
    duck.pendown()
    duck.color("orange")
    duck.pensize(5)
    duck.setheading(-90)
    duck.forward(50)

# Create Cloud Turtle
cloud = turtle.Turtle()
cloud.speed(1)
cloud.hideturtle()

def draw_cloud(t, x, y):
    t.clear()
    t.color("white")
    offsets = [(0, 0, 25), (20, 15, 30), (50, 15, 30), (70, 0, 25), (35, -5, 25)]
    for ox, oy, r in offsets:
        t.penup()
        t.goto(x + ox, y + oy)
        t.pendown()
        t.begin_fill()
        t.circle(r)
        t.end_fill()

# Draw clouds in the sky
draw_cloud(cloud, -150, 120)
draw_cloud(cloud, 80, 150)

# Update screen to display drawings with tracer(0) enabled
screen.update()
turtle.done()