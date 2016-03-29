import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def makeSwirlsSquare(size,bigger,sides,angle):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
        else:
            size=size
            t1.fd(size)
            t1.right(angle)
makeSwirlsSquare(10,10,30,90)
wn.exitonclick()