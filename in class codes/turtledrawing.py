import turtle

"""turtle.up()#make the pen go up,no drwaing plz

turtle.goto(45,35) #go to the coordinates 

turtle.down() # lower the pen to start drawing

turtle.forward(100)

turtle.done()"""# to show that the drawing is done
def turtle_state():
    
    turtle.isdown()
    turtle.heading()
    print(turtle.xcor())
    print(turtle.ycor())


def TestDrive():
    
    
    turtle.speed(5)
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)
    turtle.done()

def main():
    
    turtle_state()
    TestDrive()
    turtle_state()

main()    