# CODE TO COPY
# a118_turtles_in_traffic.py
# Move turtles horizontally and vertically across screen.
# Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, 350)
    vt.setheading(270)
    tloc += 50

# Move turtles across and down screen, stopping for collisions
for step in range(50):
    # 1. Move all currently active turtles forward by 5 pixels per frame
    for ht in horiz_turtles:
        ht.forward(10)
    for vt in vert_turtles:
        vt.forward(10)

    # 2. Check for collisions between remaining active turtles
    for ht in horiz_turtles[:]:
        for vt in vert_turtles[:]:
            # Check for collisions in the x and y coordinates
            if (abs(ht.xcor() - vt.xcor()) < 40) and (abs(ht.ycor() - vt.ycor()) < 40):
                # Turn them gray to indicate a collision
                ht.fillcolor("gray")
                vt.fillcolor("gray")

                # Remove the turtles from the list
                horiz_turtles.remove(ht)
                vert_turtles.remove(vt)

wn = trtl.Screen()
wn.mainloop()
