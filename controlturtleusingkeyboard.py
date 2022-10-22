from turtle import *
sc=Screen()
t=Turtle()
t.shape('turtle')
def aage():
    #t.forward(100)
    t.setpos(30, 30)
    k=50
    for i in range(5):
        t.pu()
        t.forward(k)
        t.pd()
        t.stamp()
        k=k+20
def peeche():
    t.bk(100)
def rightmud():
    t.right(90)
def leftmud():
    t.left(90)


sc.onkey(aage,'Up')
sc.onkey(peeche,'Down')
sc.onkey(rightmud,'Right')
#sc.onkey(leftmud,'Left')
sc.onkey(leftmud,'j')
sc.listen()
done()