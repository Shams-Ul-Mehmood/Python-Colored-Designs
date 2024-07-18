import turtle

turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(20)

# squary.pencolor("red")

for i in range(100):
    for color in ["red" , "blue" , "yellow"]:
        squary.pencolor( color )
        squary.forward(i)
        squary.left(90)
        squary.right(12)
