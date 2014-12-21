import turtle
from turtle import*

ht()
tracer(0,1)
x,y = position()

size=20
color="red"

def square (x,y):
    global size,color
    pensize(size)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    fillcolor(color)
    forward(50)
    lt(100)
    forward(50)	
    lt(100)
    forward(50)
    lt(100)
    penup()
    end_fill()

def circle (x,y):
    global size,color
    turtle.color(color)
    pencolor()
    penup()
    goto(x,y)
    pendown()
    dot(size)

def triangle (x,y):
    global size,color
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)

def change_circle():
    onscreenclick(circle,btn=1,add=False)
    listen()
    
def change_square():
    onscreenclick(square,btn=1,add=False)
    listen()

def change_color_blue():
    turtle.pencolor("blue")
    turtle.color("blue")
def change_color_pink():
    turtle.pencolor("pink")
    turtle.color("pink","pink")
    
onscreenclick(square,btn=1,add=True)
getscreen().onkeypress(change_circle,key="a")
getscreen().onkeypress(change_square,key="b")
onscreenclick(triangle,btn=3,add=True)
getscreen().onkeypress(change_color_blue,key="c")
getscreen().onkeypress(change_color_pink,key="k")

listen()
turtle.mainloop()


