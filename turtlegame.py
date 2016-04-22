import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def TurtleGame():
    import random
    dot1=random.randint(-500,-350)
    dot2=random.randint(-250,-100)
    dot3=random.randint(0,100)
    dot4=random.randint(200,300)
    dot5=random.randint(400,500)
    def GameReady():
        def square(size):
            for i in range(0,4):
                t1.fd(size)
                t1.right(90)
        tracks=((dot1,dot1+500),(dot2,dot2+100),(dot3,dot3),(dot4,dot4-50),(dot5,dot5/4))
        for i in range(0,5):
            t1.penup()
            t1.setpos(tracks[i])
            t1.pendown()
            square(100)     
    def GameStart():
        def k1():
            t1.forward(45)
        def k2():
            t1.left(45)
        def k3():
            t1.right(45)
        def k4():
            t1.back(45)
        wn.onkey(k1, "Up") 
        wn.onkey(k2, "Left")
        wn.onkey(k3, "Right")
        wn.onkey(k4, "Down")
        t1.penup()
        t1.setpos(-520,0)
        t1.shape("turtle")
        t1.pencolor("Red")
        t1.pendown()
        wn.listen()
        
    GameReady()
    GameStart()
    t1.write("          Let's go! ")
    
TurtleGame()

wn.exitonclick()
