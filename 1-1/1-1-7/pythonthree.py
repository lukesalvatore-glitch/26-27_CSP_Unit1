import turtle as trtl
import math
import time

turtle_shapes = ['turtle', 'turtle', 'turtle', 'turtle', 'turtle', 'turtle']
turtle_colors = ['darkgreen', 'yellowgreen', 'green', 'forestgreen', 'olive', 'lime']

my_turtles = []
startx = 0
starty = 0
radius = 100

for i in range(len(turtle_shapes)):
    t = trtl.Turtle(shape=turtle_shapes[i])
    t.color(turtle_colors[i])
    t.penup()
    t.speed(0)
    my_turtles.append(t)

wn = trtl.Screen()
wn.tracer(0)

current_angle = 0

while True:
    for i, t in enumerate(my_turtles):
        angle_deg = (i * 60) + current_angle
        angle_rad = math.radians(angle_deg)


        x = startx + radius * math.cos(angle_rad)
        y = starty + radius * math.sin(angle_rad)

        t.goto(x, y)
        t.setheading(angle_deg + 60)

    wn.update()


    time.sleep(0.01)

    current_angle += 1

# wn.mainloop()

