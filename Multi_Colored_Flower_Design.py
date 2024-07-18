from turtle import *
import colorsys

speed(0)
bgcolor("black")
height = 0
for row in range(18):
    for column in range(18):
        colors = colorsys.hsv_to_rgb( height , 1 , 1 )
        color(colors)
        height += 0.005
        rt(90)
        circle( 150 - column * 6 , 90 )
        lt(90)
        circle( 150 - column * 6 , 90 )
        rt(180)
    circle(40, 24)
done()