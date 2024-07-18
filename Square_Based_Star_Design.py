import turtle
import colorsys

turtle.setup(800 , 800)
turtle.speed(0)
turtle.tracer(10)
turtle.width(2)
turtle.bgcolor("black")

def square(x):
    for i in range(3):
        turtle.forward(x)
        turtle.left(90)
    turtle.forward(x)

for i in range(20):
    for j in range(10):
        turtle.color( colorsys.hsv_to_rgb( i/10 , j/20 , 1 ) )
        turtle.right(135)
        square(200-j*4)
        turtle.right(135)
        turtle.circle(50 , 36)

turtle.hideturtle()
turtle.done()