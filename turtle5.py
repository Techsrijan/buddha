from turtle import *
t=Turtle()
t.pu()
t.goto(100,200)
t.pd()
t.circle(50)

t.pu()
t.goto(100,225)
t.pd()
t.circle(25)
t.undo()
#t.reset()
t.write("Abc",font=("comic Sans Ms",25,"bold"))
l=['red','green','blue','orange','yellow']
for i in range(5):
    t.pencolor(l[i])
    t.circle(50)
    t.bk(100)
done()