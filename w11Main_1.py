import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()

def set_t2():
        t2.penup()
        t2.setpos(-100,100)
        t2.pendown()
        t2.forward(250)
def keyup():
	t1.forward(50)
def keydown():
	t1.backward(50)
def keyleft():
	t1.left(90)
def keyright():
	t1.right(90)

def mousegoto(x,y):
	t1.setpos(x,y)
	(x,y)=t1.pos()
	if -100<x<150 and y==100:
                print "Correct!"	

def addkeys():	
	wn.onkey(keyup,"Up")
	wn.onkey(keydown,"Down")
	wn.onkey(keyleft,"Left")
	wn.onkey(keyright,"Right")
def addMouse():
	wn.onclick(mousegoto)


set_t2()
addkeys()
addMouse()

wn.listen()
turtle.mainloop()
