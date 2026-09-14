# import turtle module
import turtle
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter2 = trtl.Turtle()
painter3 = trtl.Turtle()
painter.fillcolor("yellow")
painter.begin_fill()
painter.pensize(15)
painter2.pensize(15)
painter3.pensize(15)

# move turtle without marking a line
painter.penup()
painter.begin_fill()
painter.goto(5, -45)
painter.pendown()

# draw a semi-circle


painter.circle(180, 365)
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


# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()