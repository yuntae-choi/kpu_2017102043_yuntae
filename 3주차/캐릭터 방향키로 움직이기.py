from pico2d import *
def handle_events():
    global running, dx
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1


open_canvas()
img = load_image("../res/run_animation.png")
gra = load_image("../res/grass.png")
frame = 0
dx = 0
gra.draw_now(400, 30)
x = get_canvas_width() // 2
running = True
while running and x< 800 :
    clear_canvas()
    gra.draw(400, 30)
    img.clip_draw(frame * 100, 0, 100, 100, x, 80)
    frame = (frame+1) % 8
    # x += 2
    x += dx * 5
    update_canvas()
    handle_events()

    delay(0.01)

close_canvas()
