import turtle

def draw_circle(x,y,radius,fill_color):
    turtle.up()
    turtle.goto(x,y - radius)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.fillcolor(fill_color)
    turtle.end_fill()
    turtle.up()

def draw_nose(x,y,radius,fill_color):
    turtle.up()
    turtle.goto(x,y - radius)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.fillcolor(fill_color)
    turtle.end_fill()
    turtle.up()

def draw_eye(x,y,radius,iris_color):
    draw_circle(x,y,radius,"white")
    iris_radius= radius/ 2
    draw_circle(x,y,iris_radius,iris_color)
    pupil_radius= radius/ 4
    draw_circle(x,y,pupil_radius,"black")

def main():
    draw_circle(0,0,200,"yellow")
    draw_nose(0,0,20,"pink")
    draw_eye(70,70,50,"blue")
    draw_eye(-70,70,50,"blue")
    turtle.done()
main()    