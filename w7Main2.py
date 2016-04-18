
In [24]: import turtle

In [25]: wn=turtle.Screen()

In [26]: t1=turtle.Turtle()

In [34]: def drawSquareAt(size, pos):
   ....:     t1.penup()
   ....:     t1.setpos(pos)
   ....:     t1.pendown()
   ....:     tracks=list()
   ....:     for i in range(0,4):
   ....:         tracks.append(t1.pos())
   ....:         t1.forward(size)
   ....:         t1.right(90)
   ....:     return tracks
   ....:

In [35]: def lab7():
   ....:     size=100
   ....:     pos=t1.pos()
   ....:     mytrack=drawSquareAt(size,pos)
   ....:     print mytrack
   ....:

In [36]: def main():
   ....:     lab7()
   ....:
 
In [36]: main()

In [36]: wn.exitonlick()
