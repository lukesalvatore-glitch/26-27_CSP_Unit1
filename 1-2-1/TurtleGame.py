# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = ["arrow","turtle","circle", "square", "triangle", "classic"]
#-----initialize turtle-----
t = trtl.Turtle()

#-----game functions--------
def spot_clicked(x,y):
    print("Spot was clicked!")


#-----events----------------




wn = trtl.Screen()
wn.onclick(spot_clicked)
wn.mainloop()