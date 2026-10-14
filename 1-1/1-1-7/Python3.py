import turtle as trtl
import math  # Needed for sin and cos

# List of turtle shapes and colors
turtle_shapes = ["turtle"] * 6
turtle_colors = ["Dark Green", "Yellow Green", "Green", "Forest Green", "Olive", "Lime"]

# Create turtles and place them in different spots
my_turtles = []
startx = 0
starty = 0
direction = 0
radius = 100  # Distance from center

for i in range(len(turtle_shapes)):
    t = trtl.Turtle(shape=turtle_shapes[i])
    t.color(turtle_colors[i])
    t.penup()  # Prevent drawing lines

    # Calculate position using math functions
    angle_rad = math.radians(direction)
    x = startx + radius * math.cos(angle_rad)
    y = starty + radius * math.sin(angle_rad)

    t.goto(x, y)  # Move turtle to position
    t.setheading(direction)  # Face outward
    my_turtles.append(t)

    direction += 60  # Spread evenly (360° / 6 turtles)

# Keep window open
wn = trtl.Screen()
wn.mainloop()


