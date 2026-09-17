# import turtle module
import turtle
import turtle as trtl
color = input("What color do you want your background?")

# create turtle object
painter = trtl.Turtle()
painter2 = trtl.Turtle()
painter3 = trtl.Turtle()
painter.begin_fill()
painter.pensize(15)
painter2.pensize(15)
painter3.pensize(15)

# move turtle without marking a line
painter.penup()
painter.begin_fill()
painter.goto(5,-45)
painter.pendown()

# draw a semi-circle


painter.circle(180,365)
# move turtle without marking a line
painter.penup()
painter.goto(0, 20)
painter.pendown()
painter.color("black")
painter.circle(55,365)
painter.color("black")
painter.penup()
painter.goto(5, -45)


painter2.penup()
painter2.goto(-65,200)
painter2.pendown()
painter2.color("black")
painter2.circle(25,365)
painter2.color("black")
painter2.penup()

painter3.penup()
painter3.goto(65,200)
painter3.pendown()
painter3.color("black")
painter3.circle(25,365)
painter3.color("black")
painter3.penup()
# put the color that the user puts down
if color == "green":
    turtle.bgcolor("green")
if color == "red":
    turtle.bgcolor("red")
if color == "yellow":
    turtle.bgcolor("yellow")
if color == "blue":
    turtle.bgcolor("blue")

turtle.done()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()