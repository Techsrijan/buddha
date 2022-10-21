from turtle import *
t=Turtle()
#t.circle(50)
#t.circle(-50)
#t.circle(100)

t.pu()
t.forward(200)
t.pd()

l=['red','green','blue','orange','yellow']
for i in range(5):
    t.pencolor(l[i])
    t.circle(50)
    t.bk(100)

done()