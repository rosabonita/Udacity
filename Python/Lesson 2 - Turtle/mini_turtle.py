import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("green")
    draw_triangle()
    draw_triforce()

    window.exitonclick()

def draw_triangle():
    link = turtle.Turtle()
    link.shape("turtle")
    link.speed("fastest")
    link.color("gold")

    i = 0
    while(i < 3):
        link.forward(100)
        link.left(120)
        i += 1

def draw_triforce():
    zelda = turtle.Turtle()
    zelda.shape("turtle")
    zelda.speed("fastest")
    zelda.color("gold")

    draw_triangle()
