import turtle 

wn=turtle.Screen() 

t1=turtle.Turtle() 

def drawSquareAt(size, pos): 
    t1.penup() 
    t1.setpos(pos) 
    t1.pendown() 
    tracks=list() 
    for i in range(0,4): 
        tracks.append(t1.pos()) 
        t1.forward(size) 
        t1.right(90) 
    return tracks 

def lab7b(): 
    size=100 
    pos=t1.pos() 
    mytrack=drawSquareAt(size,pos) 
    print mytrack 

def lab7c():
    tracks=((0,0),(180,0),(180,-250),(0,-250),(0,0))
    for i in range(0,5):
        t1.goto(tracks[i])
    
def main():
    lab7b()
    t1.home()
    t1.clear()
    lab7c()

if __name__=="__main__": 
     main() 
