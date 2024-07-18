import turtle
import colorsys

new_Turtle = turtle.Turtle()
new_Screen = turtle.Screen().bgcolor("black")

new_Turtle.speed(0)
number = 70
height = 0
for i in range(360):
    color = colorsys.hsv_to_rgb( height , 1 , 0.8 )
    height += 1/number
    new_Turtle.color( color )
    new_Turtle.left( 1 )
    new_Turtle.fd( 1 )
    for j in range( 2 ):
        new_Turtle.left( 2 )
        new_Turtle.circle( 100 )