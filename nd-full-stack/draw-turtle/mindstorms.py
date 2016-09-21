import turtle

def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("green")
    brad.speed(20)
    
    for i in range(0, 36):
        draw_square(brad)
        brad.left(10)
        
    draw_circle()
    draw_triangle()
    
    window.exitonclick

def draw_square(some_turtle):    
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)  


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(5)
    
    angie.circle(100)

def draw_triangle():
    stefan = turtle.Turtle()
    stefan.shape("turtle")
    stefan.color("yellow")
    stefan.speed(10)

    for i in range(0, 3):
        stefan.forward(100)
        stefan.left(120)

draw_turtles()
