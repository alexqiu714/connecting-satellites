import pgzrun
import random
from time import time

WIDTH = 750
HEIGHT = 500

sat = []
lines = []
next = 0
start = time()

for i in range(10):
    satellite = Actor("satellite")
    satellite.x = random.randint(0,730)
    satellite.y = random.randint(0,480)
    sat.append(satellite)

def draw():
    global total
    number = 1
    screen.blit("background", (0,0))
    for i in sat:
        i.draw()
        screen.draw.text(str (number), (i.x, i.y + 20))
        number += 1
    for l in lines:
        screen.draw.line(l[0], l[1], "yellow")
    if next<10:
        total = time() - start
        screen.draw.text(str (total), (320,60))
    
    else:
        screen.draw.text(str (total), (320,60))

def on_mouse_down(pos):
    global next, lines
    if sat[next].collidepoint(pos):
        if next>0:
            lines.append((sat[next-1].pos,sat[next].pos))
        next += 1
        
    else:
        lines = []
        next = 0

def update():
    pass


pgzrun.go()