from turtle import *
from math import *

setup(500,500,0,0)
title("cuadrados")	
	
#x, y posicion
#a tamano del cuadrado
	
def dibujarCuadrado(x,y,a):
	penup()
	goto(x,y-(a/2))
	pendown()
	setx(x+(a/2))
	sety(y+(a/2))
	setx(x-(a/2))
	sety(y-(a/2))
	setx(x)
	penup()
		
xi= -100
xj = 30
penup()
goto(xi,xi)
dibujarCuadrado(xcor(),ycor(),xj)
goto(xi,xi)

penup()
xi=-xi
setx(xi)
dibujarCuadrado(xcor(),ycor(),xj)
goto(xi,-xi)

penup()
sety(xi)
dibujarCuadrado(xcor(),ycor(),xj)
goto(xi,xi)

penup()
xi=-xi
setx(xi)
dibujarCuadrado(xcor(),ycor(),xj)
goto(xi,-xi)

exitonclick()
