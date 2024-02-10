import turtle
from turtle import Turtle, Screen

def draw_circle(turta,x,y,radius,fill_color):
    turta.begin_fill()
    turta.fillcolor(fill_color)
    turta.up()
    turta.goto(x,y - radius)
    turta.down()
    turta.circle(radius)
    turta.penup()
    turta.end_fill()
def draw_nose(turta,x,y,radius,fill_color):

    turta.goto(x,y - radius)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(fill_color)
    turta.circle(radius)
    turta.end_fill()
    turta.up()
def draw_eyes(turta,x,y,radius,iris_color):
    turta.down()
    draw_circle(turta,x,y,radius,"white")
    iris_radius= radius/2
    draw_circle(turta,x,y,iris_radius,iris_color)
    pupil_radius=radius/4
    draw_circle(turta,x,y,pupil_radius,"black")
    turta.up()

def draw_mouth(turta,x,y,radius,fill_color):
    turta.up()
    turta.begin_fill()
    turta.fillcolor(fill_color)
    turta.goto(-90,-50)
    turta.down()
    turta.right(90)
    turta.circle(90,180)
    turta.goto(-90,-50)
    turta.end_fill()
def main():
   
    wind =Screen()

    t=Turtle()
    print(t.xcor())
    print(t.ycor())
    t.speed(20)
    
    draw_circle(t,0,0,200,"yellow")
    draw_nose(t,0,0,20,"pink")
    draw_eyes(t,70,70,50,"blue")
    draw_eyes(t,-70,70,50,"blue")
    draw_mouth(t,-90,-50,90,"red")
    turtle.done()
main()