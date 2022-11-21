import turtle, random
import io
from PIL import Image, ImageChops
from time import sleep
import math
import mouse
import time

variation = 13
STEMS = 20
STEM_LENGTH = 20
STEM_SEGMENT_LEN = 10
spawn_var = STEMS * 3.5
save = False
fps = 0.0005
d = 0.6

seed = random.randint(111,9999999999999999999999999999)

random.seed(seed)
t = turtle.Turtle()
t.left(90)
t.pencolor("Green")
t.pensize(7)
t.hideturtle()
t.speed(10)
ti = time.process_time()
i = 0
turtle.screensize(spawn_var * 2, STEM_LENGTH * STEMS * 2, bg=None)
seed = random.randint(111111,999999)

turtle.tracer(0,0)

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

while True:
    # seed = random.randint(111111,999999)
    random.seed(seed)
    d = math.sin(((i/8) % 360))/4 + 0.2
    d += mouse.get_position()[0] / 1600
    if mouse.is_pressed():
            seed = random.randint(111111,999999)
            sleep(0.1)
    for x in range(STEMS):
        for j in range(STEM_LENGTH):
            t.pensize((int(STEM_LENGTH/ 20) * STEM_LENGTH - j) / 1.4)
            t.pencolor(j/STEM_LENGTH/1.8, (j/STEM_LENGTH/1.8) + .36 , j/STEM_LENGTH/1.8)
            t.right(random.randint(-variation,variation))
            t.fd(int(random.randint(((STEM_SEGMENT_LEN / 5) * 3), STEM_LENGTH)))
            t.right(d)
            # t.goto(t.pos() + (d * j, 0))
        t.penup()
        t.goto((random.randint(-spawn_var, spawn_var),0))
        t.setheading(90)
        t.pendown()
    if save:
        ps = turtle.getscreen().getcanvas().postscript(colormode="color")
        im = Image.open(io.BytesIO(ps.encode("utf-8")))
        im = trim(im)
        im = im.convert('RGBA')


        # Transparency
        newImage = []
        for item in im.getdata():
            if item[:3] == (255, 255, 255):
                newImage.append((255, 255, 255, 0))
            else:
                newImage.append(item)

        im.putdata(newImage)
        im.save(f"images/image{i}.png", format="PNG")
    t.pu()
    t.goto((-200, -200))
    t.pencolor(0,0,0)
    t.write("FPS: " + str(int(i/(time.process_time() - ti + 0.0001))) + "\nFRAMES: " + str(i), font=("Verdana", 25, "normal"))
    turtle.update()
    sleep(fps)
    t.reset()
    t.left(90)
    t.pencolor("Green")
    t.pensize(7)
    t.hideturtle()
    t.speed(10)
    i += 1