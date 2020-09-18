from pico2d import *

open_canvas()
img = load_image("../res/run_animation.png")
gra = load_image("../res/grass.png")
frame = 0
gra.draw_now(400, 30)
for x in range(0, 800, 2):
    clear_canvas()
    gra.draw(400, 30)
    img.clip_draw(frame * 100, 0, 100, 100, x, 80)
    frame = (frame+1) % 8
    update_canvas()
    get_events()
    delay(0.01)

delay(5)
close_canvas()
