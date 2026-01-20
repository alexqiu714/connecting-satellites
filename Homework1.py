import pgzrun
import random
from time import time

WIDTH = 750
HEIGHT = 500

s = []
lines = []
next = 0
start = time()
gameover = False

for i in range(10):
    star = Actor("star")
    star.x = random.randint(0,730)
    star.y = random.randint(0,480)
    s.append(star)

def draw():
    global total
    number = 1
    screen.blit("background", (0,0))
    for i in s:
        i.draw()
        screen.draw.text(str (number), (i.x, i.y + 20))
        number += 1
    for l in lines:
        screen.draw.line(l[0], l[1], "yellow")
    if next<10:
        total = time() - start
        screen.draw.text(str (total), (320,60))

    if gameover == True:
        end = 10.0 - total
        screen.draw.text("You lost!, you went up to " + (str (end)), (320,60))

def on_mouse_down(pos):
    global next, lines
    if s[next].collidepoint(pos):
        if next>0:
            lines.append((s[next-1].pos,s[next].pos))
        next += 1
        
    else:
        lines = []
        next = 0

def update():
    pass

def time_up():
    global gameover
    gameover = True

clock.schedule(time_up, 10.0)

pgzrun.go()