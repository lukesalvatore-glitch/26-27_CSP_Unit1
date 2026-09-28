import turtle as trtl

# define the color variables
color1 = "pink"
color2 = "purple"

# Define the screen
wn = trtl.Screen()
width = 1000
height = 300

# Define the turtle
painter = trtl.Turtle()

# Start assuming we will draw
answer = "y"

# Loop until the user is bored
while (answer == "y"):
    # Clear only the drawings, keeping the turtle object intact
    painter.clear()

    # Reset turtle state for the new drawing
    painter.speed(0)
    painter.color(color1)
    painter.penup()
    painter.goto(0, 0)
    painter.setheading(0)
    painter.pendown()

    # Reset the space counter for the new drawing
    space = 1

    # get angle from the user
    angle = 65
    seg = int(360 / angle)

    # Draw the pattern until the turtle goes past the height limit
    while (painter.ycor() < height):
        if (space % 100 == 0):
            painter.fillcolor(color2)
            painter.color(color2)
        if (space % 200 == 0):
            painter.fillcolor(color1)
            painter.color(color1)

        painter.right(angle)
        painter.forward(2 * space + 10)

        painter.begin_fill()
        painter.circle(3)
        painter.end_fill()

        space += 1

    # Ask the user if they want to draw again to make the outer loop useful
    answer = wn.textinput("Continue?", "Do you want to draw again? (y/n): ")

wn.mainloop()
