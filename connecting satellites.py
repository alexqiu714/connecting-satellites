import pgzrun
import random

WIDTH = 750
HEIGHT = 500

sat = []
number = 1

for i in range(10):
    satellite = Actor("satellite")
    satellite.x = random.randint(0,750)
    satellite.y = random.randint(0,500)
    sat.append(satellite)

def draw():
    global number
    screen.blit("background", (0,0))
    for i in sat:
        i.draw()
        screen.draw.text(str (number), (i.x, i.y + 20))
        number += 1


pgzrun.go()