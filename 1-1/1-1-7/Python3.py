# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle","turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle", "turtle" , "turtle", "turtle", "turtle", "turtle" , "turtle", "turtle", "turtle", "turtle", "turtle" , "turtle", "turtle", "turtle", "turtle"]
turtle_colors = ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue","red","blue","blue", "red", "blue", "red", "blue","red","blue","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","red","blue","red","blue","red"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors.pop())
  my_turtles.append(t)

# Starting values for x and y
startx = -25
starty = 0
# Direction Of Turtle
direction = 90
spiral = 50
# Loop through the turtles and draw.
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction)
  t.right(45)
  t.forward(spiral)
  spiral += 10


  # Change direction to the heading of the last turtle
  direction = t.heading()

  # Adjusting the starting values for the next turtle
  startx = t.xcor()
  starty = t.ycor()


wn = trtl.Screen()
wn.mainloop()