
'''
Group 5 members: Lana Kendakji (lk3501), Raza Ali (raa4793), Noor Aldin Mohsi (nm6914)
Brief description: We have used the skills we learnt in class such as turtle and turta object to creat several functions and called them all in main.
The set position function was used to start drawing in the correct position
background function was used to set the background colors
other functions were created in accordance to the instructions.
Contributions:
Noor Aldin = import turtle, and input functions
Raza Ali = Pattern function, sqaure and circle function and main function.
Lana Kendakji = background function, setposition function, hexagon function and coordinates setting for setpos.

'''
from turtle import Turtle, Screen #write before code

#begin by asking for input as a global variable
hexa_color = input("Enter the color of hexagon: ")
circle_color = input("Enter the color of circle: ")
square_color = input("Enter the color of sqaure: ")
border_color = input("Enter the color of shape borders: ")

#setting backgorund color
def backgroundcolor(wind):
    '''
    wind = Screen() as defined in the main() function
    '''
    wind.bgcolor("SkyBlue") 


def SetPos(turta,x,y): 
    '''
    defining a set position function that will move the pen with out drawing
    turta = object
    x = x-axis coordinate
    y = y-axis coordinate
    '''
    turta.penup()
    turta.goto(x,y)
    turta.pendown()

#defining function that draws a hexagon
def hexagon(turta, hexa_color, border_color): #using arguments
    turta.pencolor(border_color) #border_color will be taken from input
    turta.fillcolor(hexa_color) #hexa_color will be taken from input
    turta.begin_fill()
    turta.forward(50) #forward 50 as specified by instructions
    turta.right(60) # right 60 because 360/6 = 60 degrees
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.end_fill()

#defining function that draws a circle
def circle(turta, circle_color, border_color): #using arguments
    turta.pencolor(border_color) #border_color will be taken from input
    turta.fillcolor(circle_color) #cricle_color will be taken from input
    turta.begin_fill()
    turta.circle(50) #use value 50 because it is close in size to hexagon and square
    turta.end_fill()

#defining function that draws a sqaure
def square(turta, square_color, border_color): #using arguments
    turta.pencolor(border_color) #border_color will be taken from input
    turta.fillcolor(square_color) #sqaure_color will be taken from input
    turta.begin_fill()
    turta.forward(90) #forward 90 as specified by instructions
    turta.right(90) #right 90 because 360/4 = 90 degrees
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.end_fill()

def pattern(turta,hexa_color,circle_color,square_color,border_color):
    SetPos(turta,-250,200) #position of hexagon 1
    hexagon(turta, hexa_color, border_color)
    SetPos(turta,-100,110) #position of circle 1
    circle(turta, circle_color, border_color)
    SetPos(turta, -25, 200) #position of square 1
    square(turta, square_color, border_color)

    SetPos(turta,-150,75) #position of hexagon 2
    hexagon(turta, hexa_color, border_color)
    SetPos(turta,0, -10) #position of circle 2
    circle(turta, circle_color, border_color)
    SetPos(turta,75,75) #position of square 2
    square(turta, square_color, border_color)

    SetPos(turta,-50,-50) #position of hexagon 3
    hexagon(turta, hexa_color, border_color)
    SetPos(turta,100,-140) #position of circle 3
    circle(turta, circle_color, border_color)
    SetPos(turta,175,-50) #position of square 3
    square(turta, square_color, border_color)

def main():
    wind = Screen()
    t = Turtle()
    backgroundcolor(wind)
    pattern(t,hexa_color,circle_color,square_color,border_color)
    wind.exitonclick() #this will allow the window drawing to remain until we exit

main()