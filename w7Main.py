import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 

def saveTracks():
    mytracks=list()
    mytracks.append(t1.pos())
    t1.speed(1) 
    t1.penup()
    mytracks=list()
    t1.goto(-400,300)
    mytracks.append(t1.pos())
    t1.pendown() 
    t1.pencolor("Red") 
    t1.right(90) 
    t1.fd(400)
    mytracks.append(t1.pos())
    t1.backward(150) 
    mytracks.append(t1.pos())
    t1.left(90) 
    t1.fd(300) 
    mytracks.append(t1.pos())
    t1.left(90) 
    t1.fd(300)
    mytracks.append(t1.pos())
    t1.back(150) 
    mytracks.append(t1.pos())
    t1.right(90) 
    t1.fd(300) 
    mytracks.append(t1.pos())
    t1.left(90) 
    t1.right(90) 
    t1.right(90) 
    t1.fd(200) 
    mytracks.append(t1.pos())
    t1.fd(300) 
    mytracks.append(t1.pos())
    t1.back(100) 
    mytracks.append(t1.pos())
    t1.left(90) 
    t1.fd(200) 
    mytracks.append(t1.pos())
    return mytracks


def replayTracks(mytracks):
    for t in mytracks:
        print t

def lab7():
    mytracks=saveTracks()
    replayTracks(mytracks)
    
def main():
    lab7()

main()

wn.exitonclick()