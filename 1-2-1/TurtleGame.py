# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
score = 0

#-----initialize spot-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.color(spot_color)
#-----game functions--------

def update_score():
    global score
    score += 1
    print(score)

def spot_clicked(x, y):
    change_positon()
    update_score()

def change_positon():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()
    spot.showturtle()



#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()