import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def getCoordsFromFile():
    frec=open('reccoords.txt')
    mycoords=[]
    for line in frec:
        line1=line.split(',')
        mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
        for coord in mycoords:
            x1=int(coord[0][0])
            x2=int(coord[1][0])
            y1=int(coord[0][1])
            y2=int(coord[1][1])
        coord_li=((x1,y1),(x2,y1),(x2,y2),(x1,y2),(x1,y1))
        t1.penup()
        t1.setpos(coord_li[0])
        t1.pendown()
        for c in coord_li:
            t1.goto(c)   
    frec.close()
def lab13_2():
    getCoordsFromFile()
    wn.exitonclick()
    
def main():
    lab13_2()

if __name__=="__main__": 
    main()  

    
