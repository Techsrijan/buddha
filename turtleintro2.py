from turtle import *
t=Turtle()
sc=Screen()
sc.setup(1000,800)
def shape(x):
    n=x
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    t.forward(n)


shape(70)
t.penup()
t.forward(100)
t.pd()
shape(600)
done()
