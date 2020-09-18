from pico2d import *

open_canvas()
img =load_image("../res/cat.jpg")
img.draw_now(200,300)

delay(2)
close_canvas()
