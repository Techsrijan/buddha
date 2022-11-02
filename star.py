from turtle import *
sc=Screen()
t=Turtle()
sc.bgcolor('black')
t.color('white','white')
def mystar():
    t.begin_fill()
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()
mystar()
t.pu()
t.goto(200,200)
t.pd()
mystar()


t.pu()
t.goto(-200,200)
t.pd()
mystar()
done()