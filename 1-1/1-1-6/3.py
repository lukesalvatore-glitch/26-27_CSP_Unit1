#   a116_ladybug.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used

painter= trtl.Turtle()
# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 3
xpos = -22
ypos = -55
ladybug.pensize(10)
# draw 2 sets of dots
while num_dots <= 4:
    ladybug.penup()
    ladybug.goto(xpos, ypos)
    ladybug.pendown()
    ladybug.circle(2)
    ladybug.penup()
    ladybug.goto(xpos + 30, ypos + 20)
    ladybug.pendown()
    ladybug.circle(2)

    # position next dots
    ypos = ypos + 25
    num_dots = num_dots + 1

# Configure ladybug legs
legs = 3             # 3 legs on each side
leg_length = 50
leg_angle = 30       # Angle spacing between legs

# Draw Left Legs
n = 0
while (n < legs):
    ladybug.penup()
    ladybug.goto(0, -35)
    ladybug.setheading(135 + (n * leg_angle))
    ladybug.pendown()
    ladybug.forward(leg_length)
    n = n + 1

# Draw Right Legs
n = 0
while (n < legs):
    ladybug.penup()
    ladybug.goto(0, -35)
    ladybug.setheading(45 - (n * leg_angle))
    ladybug.pendown()
    ladybug.forward(leg_length)
    n = n + 1

ladybug.hideturtle()
wn = trtl.Screen()
wn.mainloop()