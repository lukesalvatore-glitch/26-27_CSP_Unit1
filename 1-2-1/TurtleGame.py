# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
spot_color = "red"
spot_shape = "circle"
spot_size = 2
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000 #1000 is 1 second
timer_up = False
sizes = [0.5, 1, 1.5, 2, 2.5,3, 3.5, 4, 4.5, 5, 5.5, 6 ]





#-----initialize spot-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.color(spot_color)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(265,265)
score_writer.hideturtle()

counter = trtl.Turtle()
counter.penup()
counter.goto(300,300)



#-----game functions--------

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

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

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def change_size():
    new_size = rand.choice(sizes)
    spot.turtlesize(new_size)

def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_positon()
        change_size()
        update_score()
    else:
        spot.hideturtle()

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.bgcolor("light blue")
wn.mainloop()