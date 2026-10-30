# a118_turtles_in_traffic.py
# Move turtles horizontally and vertically across screen.
# Stopping turtles when they collide.
import turtle as trtl

# Create empty lists for turtles and their speeds
horiz_turtles = []
vert_turtles = []
horiz_speeds = []
vert_speeds = []

# Use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 65
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    horiz_speeds.append(5)  # Initialize starting speed
    ht.penup()
    ht.fillcolor(horiz_colors.pop())
    ht.goto(-350, tloc)
    ht.setheading(0)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vert_speeds.append(5)  # Initialize starting speed
    vt.penup()
    vt.fillcolor(vert_colors.pop())
    vt.goto(-tloc, 350)
    vt.setheading(270)

    tloc += 50

# Move turtles across and down screen, stopping for collisions
for step in range(150):
    # 1. Update speeds and move active horizontal turtles
    for i in range(len(horiz_turtles)):
        horiz_speeds[i] += 1
        if horiz_speeds[i] > 25:
            horiz_speeds[i] = 5
        horiz_turtles[i].forward(horiz_speeds[i])

    # 2. Update speeds and move active vertical turtles
    for i in range(len(vert_turtles)):
        vert_speeds[i] += 1
        if vert_speeds[i] > 25:
            vert_speeds[i] = 5
        vert_turtles[i].forward(vert_speeds[i])

    # 3. Check for collisions between remaining active turtles
    for ht in horiz_turtles[:]:
        for vt in vert_turtles[:]:
            if (abs(ht.xcor() - vt.xcor()) < 20) and (abs(ht.ycor() - vt.ycor()) < 20):
                # Turn them gray to indicate a collision
                ht.fillcolor("red")
                vt.fillcolor("blue")
                turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
                last_turtle = turtle_shapes.pop()

                # Remove collided turtles from movement lists
                if ht in horiz_turtles:
                    h_index = horiz_turtles.index(ht)
                    horiz_turtles.remove(ht)
                    horiz_speeds.pop(h_index)

                if vt in vert_turtles:
                    v_index = vert_turtles.index(vt)
                    vert_turtles.remove(vt)
                    vert_speeds.pop(v_index)

wn = trtl.Screen()
wn.mainloop()