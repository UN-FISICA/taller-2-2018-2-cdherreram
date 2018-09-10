from turtle import *
from math import *

setup(500,500,0,0)
title("poligonos con poligonos")

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
	#penup()
	sety(ycor()+(a/2))

def dibujarPoligonoGrande(x,y,a,n,xj,m):
	r = 360/n
	goto(x,y-(a/2))
	forward(a/2)
	k=1
	dibujarPoligono(xcor(),ycor(),xj,m)
	left(r)
	while(k<n):
		forward(a)
		right(heading())
		dibujarPoligono(xcor(),ycor(),xj,m)
		left(r*(k+1))
		k=k+1
	left(r*k+1)
	forward(a/2)

xi= 100
xj = 30

l=input("Escriba el numero de lados grande: ")
k=input("Escriba el numero de lados pequeno: ")
n= int(l)
m= int(k)

penup()
dibujarPoligonoGrande(0,0,xi,n,xj,m)

exitonclick()
