from ast import Lt
from operator import lt
from time import sleep
import turtle as turtle

_x=600
_y=100

def Jfunc() :
    turtle.Turtle()
    turtle.bgcolor("cyan")
    turtle.color("red")
    turtle.shape("turtle")
    turtle.speed(1)
    turtle.pensize(10)

    turtle.penup()
    turtle.setpos((-_x,_y))
    turtle.pendown()

    turtle.fd(200)
    turtle.penup()
    turtle.backward(100)
    turtle.rt(90)
    turtle.pendown()
    turtle.fd(200)
    turtle.right(180)
    turtle.circle(60,-180)

def Afunc() :
    turtle.penup()
    turtle.setpos(((220-_x),_y))
    turtle.pendown()

    turtle.right(20)
    turtle.fd(290)

    turtle.right(-20-90)
    turtle.penup()
    turtle.fd(200)

    turtle.pendown()
    turtle.right(70)   
    turtle.backward(290)

    turtle.fd(150)
    turtle.right(110)
    turtle.fd(100)   

def Rfunc():
    turtle.penup()
    turtle.setpos(((120+220-_x),_y))
    turtle.pendown() 

    turtle.rt(-90)
    turtle.fd(270)
    turtle.penup()
    turtle.backward(140)
    turtle.pendown()
    turtle.lt(90)
    turtle.circle(100,180)
    turtle.penup()
    turtle.setpos(((120+220-_x),_y))
    turtle.pendown()
    
    


    



Jfunc()
Afunc()
Rfunc()