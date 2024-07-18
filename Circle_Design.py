from turtle import *
import colorsys

speed(0)
tracer(5)
width(2)
bgcolor("black")
hideturtle()
height = 0.001

for i in range(90):
    color( colorsys.hsv_to_rgb( height , 1 , 1 ) )
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)
    height += 0.02
    color( colorsys.hsv_to_rgb( height , 1 , 1 ) )
    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    height += 0.02
done()
