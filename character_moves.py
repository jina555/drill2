from pico2d import *

open_canvas()

grass= load_image('grass.png')
character=load_image('character.png')

while True:
    x = 400
    while (x <= 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y = 90
    while (y <= 580):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, y)
        y = y + 2
        delay(0.01)

    x = 780
    while (x <= 780 and x > 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 580)
        x = x - 2
        delay(0.01)

    y = 580
    while (y <= 580 and y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        y = y - 2
        delay(0.01)

    x = 10
    while (x <= 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)


    x=400
    while(x<=700):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    y=90
    x=700
    while(y<=400 and x>=400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        x=x-2
        y=y+2
        delay(0.01)


    y=400
    x=400
    while(y>=90 and x>=100):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        y=y-2
        delay(0.01)

    y=90
    x=100
    while(x<=400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+2
        delay(0.01)



    import math

    theta = -3 / 2 * math.pi
    r = 210
    while (theta < 1 / 2 * math.pi):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 + r * math.cos(theta), 300 - r * math.sin(theta))
        theta = theta + 0.01
        delay(0.01)