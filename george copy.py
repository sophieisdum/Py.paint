import turtle
import random
import time
turtle.tracer(False)
turtle.hideturtle()
turtle.bgcolor('#000000')
turtle.color('#00ff00')
style = ('pristina', 30, 'bold')
turtle.write('Paint.net but bad', font=style, align='center')
turtle.write('Left click=draw \n Right click=colour \n Middle click=rubber \n', font=style, align='center')
turtle.hideturtle()
time.sleep(5)
turtle.clear()
turtle.home()

def clickLeft(x, y):  # Make sure to have parameters x, y
    
    colors = ["red", "blue", "green", "#F09521", "white", "#E443F4", "#82D2E1"]
    t.pencolor(random.choice(colors))
    print("click")
    t.pensize(1)

def clickRmiddlet(x, y):  # Make sure to have parameters x, y
        t.pencolor('#000000')
        t.pensize(10)
        
"""
Paint Application using Python Turtle
by t-wy
"""

def save():
    turtle.getscreen().getcanvas().postscript(colormode='color', file="drawing.eps")
    
def draw(x, y):
    t.ondrag(None)
    t.down()
    t.goto(x, y)
    t.up()
    turtle.update()
    t.ondrag(draw)

def move(x, y):
    turtle.onscreenclick(None)
    t.goto(x, y)
    turtle.onscreenclick(move)
    turtle.update()

t = turtle.Turtle()
t.shape("square")
t.fillcolor("")
t.up()

# dirty hack to hide the border completely
drawturtle_backup = t._drawturtle
def _drawturtle(*args, **kwargs):
    bkup = t._pencolor
    drawturtle_backup(*args, **kwargs)
    t._pencolor = bkup
t._drawturtle = _drawturtle

t.turtlesize(1000000, 1000000)
ts = turtle.getscreen()
t.ondrag(draw)
turtle.onscreenclick(move)
turtle.update()
turtle.onkeypress(save, "space") # Press Space to Save

turtle.onscreenclick(clickLeft, 3)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRmiddlet, 2)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.listen()

turtle.done()
