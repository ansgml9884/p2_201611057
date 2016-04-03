import turtle
wn=turtle.Screen()

userA=raw_input('userA input rock, scissors, paper : ')
userB=raw_input('userB input rock, scissors, paper : ')

def RSPgame():
   if userA!=userB:
      if userA=='rock' and userB=='scissors':
         print 'A is winner'
      elif userA=='scissors' and userB=='rock':
         print 'A is winner'
      elif userA=='paper' and userB=='rock':
         print 'A is winner'
      else:
         print 'B is winner'
   elif userA==userB:
      print "Draw"
RSPgame()
wn.exitonclick()