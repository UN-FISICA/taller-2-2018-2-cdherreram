from turtle import *
from math import *

setup(500,500,0,0)
title("poligonos")	

#n numerolados
#a longitud lado

def dibujarPoligono(x,y,a,n):
	r = 360/n
	penup()
	goto(x,y-(a/2))
	pendown()
	forward(a/2)
	k=1
	while(k<n):
		left(r)
		forward(a)
		k=k+1
	left(r)
	forward(a/2)
	
xi= -100
xj = 30

l=input("Escriba el numero de lados: ")
n= int(l)

penup()
goto(xi,xi)
dibujarPoligono(xcor(),ycor(),xj,n)
penup()
goto(xi,xi)

penup()
xi=-xi
setx(xi)
dibujarPoligono(xcor(),ycor(),xj,n)
penup()
goto(xi,-xi)

penup()
sety(xi)
dibujarPoligono(xcor(),ycor(),xj,n)
penup()
goto(xi,xi)

penup()
xi=-xi
setx(xi)
dibujarPoligono(xcor(),ycor(),xj,n)
penup()
goto(xi,-xi)

exitonclick()
