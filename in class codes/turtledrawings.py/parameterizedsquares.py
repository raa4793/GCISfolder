import turtle

def turtle_square1(side,dist):
    turtle.begin_fill()
    turtle.pen()
    turtle.color("purple")
    ang=90
    turtle.forward(dist)
    turtle.left(ang)
    turtle.forward(dist) 
    turtle.left(ang)

    turtle.forward(dist)
    turtle.left(ang)
    turtle.forward(dist) 
    turtle.left(ang)  
    turtle.end_fill()

def turtle_square2(sides,dists):
    angle=90
    turtle.begin_fill()
    turtle.pen()
    turtle.color("blue")
    turtle.forward(dists)
    turtle.left(angle)
    turtle.forward(dists) 
    turtle.left(angle)
    
    turtle.forward(dists)
    turtle.left(angle)
    turtle.forward(dists) 
    turtle.left(angle)
    turtle.end_fill() 

def turtle_square3(side0,dist0):
    angle0=90
    turtle.begin_fill()
    turtle.pen()
    turtle.color("pink")
    turtle.forward(dist0)
    turtle.left(angle0)
    turtle.forward(dist0) 
    turtle.left(angle0)
    
    turtle.forward(dist0)
    turtle.left(angle0)
    turtle.forward(dist0) 
    turtle.left(angle0) 
    turtle.end_fill()



def main():
    turtle_square1(4,120)
    turtle_square2(4,90)
    turtle_square3(4,60)
    turtle.done()
main()    
