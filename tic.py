#For user1 and user2 game playing
def user1VsUser2(b):
    i=0
    print 'user1=x user2=o'
    while(i<9):
       if isAnyWin(b)==0:
          print "User1 Turn to play move from 0 to 8"
          play=int(input())
          b[play]=-1
          print_grid(b)
          print "User2 Turn to play move from 0 to 8"
          play=int(input())
          b[play]=1
          print_grid(b)
    print b

#User Move In AI
def userMove(b):
    f=True
    while f:
       print "Input move 0 to 8"
       user_turn=int(input())
       if user_turn>8:
          print "Play Valid Move From 0 to 8"
       elif b[user_turn]==-1 or b[user_turn]==1:
            print "You played already played move"
       else:
          b[user_turn]=-1
          f=False


#Checks If Win Otherwise Select Best Move      
def tree_algorithm(b,p):
    winner=isAnyWin(b)
    if winner!=0:
        return 1
    mo=-1
    sc=-2
    for i in range(9):
        if b[i]==0:
           b[i]=p
           t=tree_algorithm(b,p*-1)
           if (t)>sc:
              sc=t
              mo=i
           b[i]=0
    if mo==-1:
         return 0
    return -(sc)

#Checks Winning Move Or Defend Move
def isAnyWin(b):
    winMoves=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if b[winMoves[i][0]]!=0 and b[winMoves[i][0]]==b[winMoves[i][1]] and b[winMoves[i][0]]==b[winMoves[i][2]]:
               return b[winMoves[i][2]]
    return 0 


#Sends Not Played Move To Tree Algorithm To make tree
def opponentMove(b):
    mo=-1
    sc=-2
    for i in range(9):
        if b[i]==0:
           b[i]=1
           ts=(tree_algorithm(b,-1))
           b[i]=0
           if ts>sc:
                sc=ts
                mo=i
    b[mo]=1
    
#Print grid 
def print_grid(b):
    i=0
    for i in range(9):
        if b[i]==-1:
           print ' X |',
        if b[i]==0:
           print ' * |',
        if b[i]==1:
           print ' O |',
        if i==2 or i==5:
           print '\n--------------'
    print ''

#Empty 				1
grid=[0]*9
f=0
def main():
    print "TIC-TAC-TOE\nComputer: 0 User=x\nplay 1st or 2nd"
    #Get The User Input
    user_input=(input())
    for i in range(0,9):
       if (i+user_input)%2==0:
            opponentMove(grid)
       else:
           print_grid(grid)
           userMove(grid)
       if isAnyWin(grid)==-1:
          return 2       
       if isAnyWin(grid)==1:
          return 1
    return 0

##Program Starts here Call Main
f=main()
#Print Final Grid 
print_grid(grid)
#Check Final result
if f==0:
   print "Tie"
if f==2:
   print "User Wins"
if f==1:
   print "System Wins"
#user1VsUser2(grid)
