# import turtle module
import turtle as trtl


# create turtle object
painter = trtl.Turtle()
painter.pensize(15)


# move turtle without marking a line
painter.penup()
painter.color("Yellow")
painter.fillcolor("yellow")
painter.goto(5, -45)
painter.pendown()


# draw a semi-circle
painter.circle(180, 365)
painter.color("Yellow")

# move turtle without marking a line
painter.penup()
painter.goto(0, 20)
painter.pendown()
painter.color("black")
painter.fillcolor("red")
painter.circle(55, 365)
painter.color("black")
painter.penup()
painter.goto(5, -45)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()