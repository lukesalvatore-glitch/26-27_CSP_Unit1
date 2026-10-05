import turtle as trtl

painter = trtl.Turtle()

# Create a spider body
painter.pensize(40)
painter.circle(20)

# Configure spider legs
legs = 8
Leg_Length = 70
Leg_Space = 360 / legs - 20
painter.pensize(5)

# Draw Legs
n = 0
while (n < legs):
  painter.goto(0, 20)
  if n<= 3:
    painter.setheading(Leg_Space * n - 45)
  if n > 3:
    painter.setheading(Leg_Space * n + 45)
  painter.forward(Leg_Length)
  n = n + 1

# Draw Spider eyes
painter.pensize(6)
painter.penup()
painter.color("red")
# Left Eye
painter.goto(-15, 45)
painter.pendown()
painter.circle(3)
painter.penup()
# Right Eye
painter.goto(15, 45)
painter.pendown()
painter.circle(3)

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()