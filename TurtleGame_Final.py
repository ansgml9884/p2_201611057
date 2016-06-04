import turtle
import math
import time
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
wn.bgcolor('black')

'''
list

'''
squ_coord=(((-500,-50),(-400,50)),((520,-150),(570,-100)))
t2_pos=((-500,50),(-250,-200),(-80,70),(150,-100),(500,60),(250,0))
center=((-250,-130),(-80,140),(150,-30))
color=('white','red','yellow','green')

maze_w=open("Mazegamecoord.txt",'w')
maze_w.write('250,50,200,290,50,150,330,0,100,370,100,100,370,-50,100,410,-50,60,450,-100,50,490,-50,100,530,50,100,570,100,200,\n250,100,320,290,50,40,410,50,160,330,0,200,410,-50,80,290,-100,40,530,-100,40,250,-150,320')
maze_w.close()
timelog=list()
score=0

'''
Time log funtion

'''

def TimeLog():
    Time=time.strftime('%M %S\n')
    Time=Time.split()
    sec=int(Time[0])*60+int(Time[1])
    timelog.append(sec)

def Score(myName):
    score=timelog[1]-timelog[0]
    Rank_a=open('Ranking.txt','a')
    Rank_a.write(myName+" : "+str(score)+" s\n")
    Rank_a.close()
    Rank_r=open('Ranking.txt','r')
    for line in Rank_r:
        print line
    Rank_r.close()


'''
Shape function

'''

def square():
    t2.fillcolor(color[0])
    t2.begin_fill()
    t2.pendown()
    for i in range(4):
        t2.fd(100)
        t2.right(90)
    t2.end_fill()
    t2.penup()

def circle(colorList,colorNum):
    t2.fillcolor(color[colorNum])
    t2.begin_fill()
    t2.pendown()
    t2.circle(70)
    t2.end_fill()
    t2.penup()
    
def Line(pos,size):
    t2.penup()
    t2.setpos(pos)
    t2.pendown()
    t2.fd(size)

'''
Shape Acess function

'''

def isInSquare(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye

def isInCircle(center,radius,pos):
    c=center
    return 0<(math.sqrt(math.pow(c[0]-pos[0],2)+ math.pow(c[1]-pos[1],2)))<(radius)

def isOnLine(pt,pos1,pos2):
    x1=pos1[0]-8
    y1=pos1[1]-8
    x2=pos2[0]+8
    y2=pos2[1]+8
    return isInSquare(pt,[(x1,y1),(x2,y2)])


def setGame():
    t1.penup()
    t1.setpos(-600,0)
    t1.shape('turtle')
    t1.pencolor(color[0])
    t1.pendown()
    t2.speed(10)
    t2.setpos(t2_pos[0])
    square()
    t1.write("       Let's GO!")

'''
Game funtion

'''
def HighLowGame(myName):
    import random
    global score
    guessesTaken = 0
    number = random.randint(1,100)
    print ('Well,'+myName+',I am thinking of a number between 1 and 100.')
    while guessesTaken < 10:
        print('Take a guess.')
        guess = input()
        guess = int(guess)
        guessesTaken =  guessesTaken + 1
        if guess < number:
            print('Your guess is too low.') 
        elif guess > number:
            print('Your guess is too high.')
        elif guess==number:
            print("That's right.")
            guessesTaken=10
    if guess == number:
        score=score+100
        guessesTaken = str(guessesTaken)
        print('Good job,'+myName+'! You guessed my number!') 
    elif guess!=number:
        number = str(number)
        print('Nope. The number I was thinking of was '+number+'. One more try!')


def RSPgame():
    import random
    global score
    rsp=("rock","scissors","paper")
    user=raw_input('User enters rock, scissors or paper : ')
    computer=random.choice(rsp)
    if user!=computer:
        if (user=='rock' and computer=='scissors') or (user=='scissors' and computer=='paper') or (user=='paper' and computer=='rock'):
            score=score+100
            print 'User is '+user+", Computer is "+computer+'. Congraturation! You are winner!'
        elif (computer=='rock' and user=='scissors') or (computer=='scissors' and user=='paper') or (computer=='paper' and user=='rock'):
            print 'User is '+user+", Computer is "+computer+'. Computer is winner.. One more try!'
        else:
            print 'You entered wrong words. One more try!'
    elif user==computer:
        print "Draw. No Score. One more try!"


def MazeGame(coordfile):
    t2.setpos(t2_pos[5])
    t2.pencolor(color[0])
    t2.speed(5)
    t2.setheading(270)
    for line in coordfile:
        coord=line.split(',')
        for i in range(len(coord)/3):
            Line((int(coord[3*i]),int(coord[3*i+1])),int(coord[3*i+2]))
        t2.left(90)
    t1.penup()
    t1.setpos(200,75)
    t1.pencolor(color[1])
    t1.pendown()


'''
Key function

'''

def keyup():
    t1.forward(30)
    pt=t1.pos()
    global score
    if isInSquare(pt,squ_coord[0]):
        TimeLog()
        t1.setpos(-500,-50)
        a=1
        t2.setpos(t2_pos[a])
        circle(color,a)
    elif isInCircle(center[0],70,pt):
        t1.write("Play a HighLowGame!")
        print ('Welcome! What is your name?')
        global myName
        myName = raw_input()
        while score<100:
            HighLowGame(myName)
        t1.setpos(-250,-50)
        a=2
        t2.setpos(t2_pos[a])
        circle(color,a)
    elif isInCircle(center[1],70,pt):
        t1.write("Play a RSPgame!")
        while score<200:
            RSPgame()
        t1.setpos(-80,50)
        a=3
        t2.setpos(t2_pos[a])
        circle(color,a)
    elif isInCircle(center[2],70,pt):
        t1.write("Play a Mazegame")
        maze_r=open("Mazegamecoord.txt",'r')
        MazeGame(maze_r)
        maze_r.close()
    elif isInSquare(pt,squ_coord[1]):
        t1.write("Clear!")
        TimeLog()
        Score(myName)
    maze=open("Mazegamecoord.txt",'r')
    number=list()
    for line in maze:
        num=line.split(",")
        for i in num:
            number.append(i)
    for k in range(0,9):
        coordA=(int(number[3*k]),int(number[3*k+1])-int(number[3*k+2]))
        coordB=(int(number[3*k]),int(number[3*k+1]))
        if isOnLine(pt,coordA,coordB):
            t1.setpos(220,70)
            t1.clear()
    for k in range(10,16):
        coordA=(int(number[3*k+2]),int(number[3*k+3]))
        coordB=(int(number[3*k+2])+int(number[3*k+4]),int(number[3*k+3]))
        if isOnLine(pt,coordA,coordB):
            t1.setpos(220,70)
            t1.clear()
    maze.close()
    

def keyleft():
    t1.left(45)
    
def keyright():
    t1.right(45)
    
def keydown():
    t1.backward(30)
    pt=t1.pos()
    global score
    if isInSquare(pt,squ_coord[0]):
        TimeLog()
        t1.setpos(-500,-50)
        a=1
        t2.setpos(t2_pos[a])
        circle(color,a)
    elif isInCircle(center[0],70,pt):
        t1.write("Play a HighLowGame!")
        print ('Welcome! What is your name?')
        global myName
        myName = raw_input()
        while score<100:
            HighLowGame(myName)
        t1.setpos(-250,-50)
        a=2
        t2.setpos(t2_pos[a])
        circle(color,a)
    elif isInCircle(center[1],70,pt):
        t1.write("Play a RSPgame!")
        while score<200:
            RSPgame()
        t1.setpos(-80,50)
        a=3
        t2.setpos(t2_pos[a])
        circle(color,a)
    elif isInCircle(center[2],70,pt):
        t1.write("Play a Mazegame")
        maze_r=open("Mazegamecoord.txt",'r')
        MazeGame(maze_r)
        maze_r.close()
    elif isInSquare(pt,squ_coord[1]):
        t1.write("Clear!")
        TimeLog()
        Score(myName)
    maze=open("Mazegamecoord.txt",'r')
    number=list()
    for line in maze:
        num=line.split(",")
        for i in num:
            number.append(i)
    for k in range(0,9):
        coordA=(int(number[3*k]),int(number[3*k+1])-int(number[3*k+2]))
        coordB=(int(number[3*k]),int(number[3*k+1]))
        if isOnLine(pt,coordA,coordB):
            t1.setpos(220,70)
            t1.clear()
    for k in range(10,16):
        coordA=(int(number[3*k+2]),int(number[3*k+3]))
        coordB=(int(number[3*k+2])+int(number[3*k+4]),int(number[3*k+3]))
        if isOnLine(pt,coordA,coordB):
            t1.setpos(220,70)
            t1.clear()
    maze.close()
    

            
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
    wn.onkey(wn.bye, "q")

def MuniGame():
    setGame()
    addKeys()
    wn.listen()
    turtle.mainloop()

def main():
    MuniGame()

if __name__=="__main__":
    main() 

