import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("C:\Users\ss\Desktop/pricture.gif")

def keyup():
    t1.forward(30)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    t1.back(30)

def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")

def mousegoto(x,y):
    t1.setpos(x,y)

def addMouse():
    wn.onclick(mousegoto)  

def TurtleGame():
    t1.penup()
    t1.setpos(-250,170)
    t1.pendown()
    t1.shape("turtle")
    t1.pencolor("red")
    
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()

def lab11_3():
    TurtleGame()
            
def main():
    lab11_3()

if __name__=="__main__":
    main()
