import turtle
def square():
    
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.pencolor("red")
    turtle.pensize(10)
    turtle.bgcolor("pink")
    turtle.end_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    
    turtle.end_fill()
    
    
def main():
    square()
    turtle.done()
    
main()    