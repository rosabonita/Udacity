import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square(5)
    draw_circle()
    draw_triangle()
    
    window.exitonclick()
def draw_square(n):
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("white")
    brad.speed('fast')
    j = 0
    for j in range(1,37):
        i = 0
        while(i < 4):
            brad.forward(100)
            brad.right(90)
            i += 1
        brad.right(10)
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    jim = turtle.Turtle()
    jim.shape("turtle")
    jim.color("yellow")
    i = 0
    while(i < 3):
        jim.forward(100)
        jim.left(120)
        i += 1
        
draw_shapes()
