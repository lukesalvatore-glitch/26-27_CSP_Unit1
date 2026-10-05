# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter= trtl.Turtle()
# Create a spider body
painter.pensize(40)
painter.circle(20)

# Configure spider legs
legs = 8
Leg_Length = 70
Leg_Space = 360 / legs
painter.pensize(5)

# Draw Legs
n = 0
while (n < legs):
  painter.goto(0, 15)
  painter.setheading(Leg_Space * n)
  painter.forward(Leg_Length)
  n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()