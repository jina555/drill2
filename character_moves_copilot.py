
import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_scene(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

def move_rectangle():
    points = [(400, 90), (700, 90), (700, 500), (100, 500), (100, 90), (400, 90)]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            draw_scene(x, y)
            delay(0.03)

def move_triangle():
    points = [(400, 500), (700, 90), (100, 90), (400, 500)]
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        for t in range(0, 100, 2):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            draw_scene(x, y)
            delay(0.03)

def move_circle():
    cx, cy, r = 400, 300, 210
    for degree in range(0, 360, 2):
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        draw_scene(x, y)
        delay(0.03)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()


