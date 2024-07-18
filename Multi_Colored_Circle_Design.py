from turtle import *
import colorsys

bgcolor("black")
tracer(500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb( h , 1 , 1 )
        h += 0.5
        up()
        goto(10,-10)
        down()
        color('black')
        fillcolor(c)
        begin_fill()
        rt(90)
        circle(i , 12)
        fd(200)
        fd(i)
        lt(24)
        for j in range(129):
            fd(j)
            circle(j , 599 , steps=2)
        end_fill()

draw()
done()