# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter= trtl.Turtle()
painter.pensize(40)
painter.circle(20)
legs = 8
Leg_Length = 125
Leg_Space = 360 / legs
painter.pensize(10)
n = 0
while (n < legs):
  painter.goto(0, 0)
  painter.setheading(Leg_Space * n)
  painter.forward(Leg_Length)
  n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()