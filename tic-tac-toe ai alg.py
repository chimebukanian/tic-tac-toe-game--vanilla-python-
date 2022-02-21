#tic tac toe
import time
from random import randrange, choice, sample
def displayboard(board):
    print("+-------"*3,"+",sep="")
    for row in range(3):
        print("|       "*3,"|",sep="")
        for col in range(3):
            print("|    "+ str(board[row][col]) + "  ",end="")
        print("|")
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="")
    
def entermove(board):
    ok=False
    while not ok:
        move=input("move-")
        ok=len(move)==1 and move>='1' and move<='9'
        if not ok:
            print("wrong move!,try again")
            continue
        move=int(move)-1#cell's number from 0 to 8
        row=move//3#cell's row 
        col=move%3#cell's col                                     
        sign=board[row][col] #check the square out
        ok=sign not in ['O','X']
        if not ok:#it's occupied-input again
            print("field filled retry")
            continue
    board[row][col]='O'#put in selected square
    #freefields
def freefields(board):
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                free.append((row,col))
    return free
def victor(board,sgn):
    if sgn=='X':#are we looking for x?
        who='me'#computer
    elif sgn=='O':#or o
        who='you'#me
    else:
        who=None
    cross1=cross2=True#diagonals
    for rc in range(3):
        if board[rc][0]==sgn and board[rc][1]==sgn and board[rc][2]==sgn:#for rows
            return who
        if board[0][rc]==sgn and board[1][rc]==sgn and board[2][rc]==sgn:#for col
            return who
        if board[rc][rc]!=sgn:#diagonal_from-0,0

            cross1=False
        if board[abs(0-rc)][2-rc]!=sgn:
            cross2=False
    if cross1 or cross2:
        return who
    return None
def drawmove(board):
    if board[0][0]=='X' and board[0][1]=='X':#1strowright
        if board[0][2] not in ['X','O']:
            board[0][2]='X' ;
            print('f')
            return board[0][2]
    
    if board[0][0]=='X' and board[1][0]=='X':#1stColdown
        if board[2][0] not in ['X','O']:
            board[2][0]='X'
            print('f')
            return board[2][0]
        
            
    if board[1][0]=='X' and board[1][1]=='X':#2ndrowright
        if board[1][2] not in ['X','O']:
            board[1][2]='X'
            print('f')
            return board[1][2]
        
    
                
    if board[0][0]=='X' and board[2][0]=='X':#1stcolcentre
        if board[1][0] not in ['X','O']:
            board[1][0]='X'
            print('f')
            return board[1][0]
        
    if board[2][0]=='X' and board[2][1]=='X':#3rdrowright
        if board[2][2] not in ['X','O']:
            board[2][2]='X'
            print('f')
            return board[2][2]

    if board[2][0]=='X' and board[1][0]=='X':#1stcoltop
        if board[0][0] not in ['X','O']:
            board[0][0]='X'
            print('f')
            return board[0][0]
        
    if board[0][2]=='X' and board[0][1]=='X':#1strowleft
        if board[0][0] not in ['X','O']:
            board[0][0]='X'
            print('f')
            return board[0][0]
                                 
    if board[0][2]=='X' and board[1][2]=='X':#3rdcoldown
        if board[2][2] not in ['X','O']:
            board[2][2]='X'
            print('f')
            return board[2][2]
                                                     
    if board[1][2]=='X' and board[1][1]=='X':#2ndrowleft
      if board[1][0] not in ['X','O']:
          board[1][0]='X'
          print('f')
          return board[1][0]
                                                                      
    if board[0][2]=='X' and board[2][2]=='X':#1stcolcentre
        if board[1][2] not in ['X','O']:
            board[1][2]='X'
            print('f')
            return board[1][2]
                                                                             
    if board[2][2]=='X' and board[2][1]=='X':#3rdrowleft
       if board[2][0] not in ['X','O']:
           board[2][0]='X'
           print('f')
           return board[2][0]
                                                                                                                               
    if board[2][2]=='X' and board[1][2]=='X':#3rdcoltop
        if board[0][2] not in ['X','O']:
            board[0][2]='X'
            print('f')
            return board[0][2]
                                                      
    if board[0][0]=='X' and board[0][2]=='X':#1strowcentre
       if board[0][1] not in ['X','O']:
           board[0][1]='X'
           print('f')
           return board[0][1]
                                                           
    if board[1][0]=='X' and board[1][2]=='X':#2ndrowcentre
        if board[1][1] not in ['X','O']:
            board[1][1]='X'
            print('f')
            return board[1][1]
        
    if board[2][0]=='X' and board[2][2]=='X':#3rdrowcentre
       if board[2][1] not in ['X','O']:
           board[2][1]='X'
           print('f')
           return board[2][1]
                          
    if board[0][0]=='X' and board[1][1]=='X':#righttdiagdown
       if board[2][2] not in ['X','O']:
           board[2][2]='X'
           print('f')
           return board[2][2]
        
    if board[0][0]=='X' and board[2][2]=='X':#rightdiagcentre
         if board[1][1] not in ['X','O']:
             board[1][1]='X'
             print('f')
             return board[1][1]
        
    if board[2][2]=='X' and board[1][1]=='X':#rightdiagtop
             if board[0][0] not in ['X','O']:
                 board[0][0]='X'
                 print('f')
                 return board[0][0]
        
    if board[0][2]=='X' and board[1][1]=='X':#leftdiagdown
              if board[2][0] not in ['X','O']:
                  board[2][0]='X'
                  print('f')
                  return board[2][0]
                                                                                                                        
    if board[0][2]=='X' and board[2][0]=='X':#leftdiagcentre
              if board[1][1] not in ['X','O']:
                  board[1][1]='X'
                  print('f')
                  return board[1][1]
        
    if board[2][0]=='X' and board[1][1]=='X':#leftdiagtop
              if board[0][2] not in ['X','O']:
                  board[0][2]='X'
                  print('f')
                  return board[0][2]
                                                                                    
    if board[0][1]=='X' and board[1][1]=='X':#centredown
              if board[2][1] not in ['X','O']:
                  board[2][1]='X'
                  print('f')
                  return board[2][1]
        
    if board[0][1]=='X' and board[2][1]=='X':#centrecentre
              if board[1][1] not in ['X','O']:
                   board[1][1]='X'
                   print('f')
                   return board[1][1]
                                                                                                
    if board[2][1]=='X' and board[1][1]=='X' :#centretop 
              if board[0][1] not in ['X','O']:
                  board[0][1]='X';
                  print('f') 
                  return board[0][1]
        
#'Os'
    if board[0][0]=='O' and board[0][1]=='O':#1strowright
        if board[0][2] not in ['X','O']:
            board[0][2]='X' ;
            print('f')
            return board[0][2]
    
    if board[0][0]=='O' and board[1][0]=='O':#1stColdown
        if board[2][0] not in ['X','O']:
            board[2][0]='X'
            print('f')
            return board[2][0]
        
            
    if board[1][0]=='O' and board[1][1]=='O':#2ndrowright
        if board[1][2] not in ['X','O']:
            board[1][2]='X'
            print('f')
            return board[1][2]
        
    
                
    if board[0][0]=='O' and board[2][0]=='O':#1stcolcentre
        if board[1][0] not in ['X','O']:
            board[1][0]='X'
            print('f')
            return board[1][0]
        
    if board[2][0]=='O' and board[2][1]=='O':#3rdrowright
        if board[2][2] not in ['X','O']:
            board[2][2]='X'
            print('f')
            return board[2][2]

    if board[2][0]=='O' and board[1][0]=='O':#1stcoltop
        if board[0][0] not in ['X','O']:
            board[0][0]='X'
            print('f')
            return board[0][0]
        
    if board[0][2]=='O' and board[0][1]=='O':#1strowleft
        if board[0][0] not in ['X','O']:
            board[0][0]='X'
            print('f')
            return board[0][0]
                                 
    if board[0][2]=='O' and board[1][2]=='O':#3rdcoldown
        if board[2][2] not in ['X','O']:
            board[2][2]='X'
            print('f')
            return board[2][2]
                                                     
    if board[1][2]=='O' and board[1][1]=='O':#2ndrowleft
      if board[1][0] not in ['X','O']:
          board[1][0]='X'
          print('f')
          return board[1][0]
                                                                      
    if board[0][2]=='O' and board[2][2]=='O':#1stcolcentre
        if board[1][2] not in ['X','O']:
            board[1][2]='X'
            print('f')
            return board[1][2]
                                                                             
    if board[2][2]=='O' and board[2][1]=='O':#3rdrowleft
       if board[2][0] not in ['X','O']:
           board[2][0]='X'
           print('f')
           return board[2][0]
                                                                                                                               
    if board[2][2]=='X' and board[1][2]=='X' or board[2][2]=='O' and board[1][2]=='O':#3rdcoltop
        if board[0][2] not in ['X','O']:
            board[0][2]='X'
            print('f')
            return board[0][2]
                                                      
    if board[0][0]=='O' and board[0][2]=='O':#1strowcentre
       if board[0][1] not in ['X','O']:
           board[0][1]='X'
           print('f')
           return board[0][1]
                                                           
    if board[1][0]=='O' and board[1][2]=='O':#2ndrowcentre
        if board[1][1] not in ['X','O']:
            board[1][1]='X'
            print('f')
            return board[1][1]
        
    if board[2][0]=='O' and board[2][2]=='O':#3rdrowcentre
       if board[2][1] not in ['X','O']:
           board[2][1]='X'
           print('f')
           return board[2][1]
                          
    if board[0][0]=='X' and board[1][1]=='X' or board[0][0]=='O' and board[1][1]=='O':#righttdiagdown
       if board[2][2] not in ['X','O']:
           board[2][2]='X'
           print('f')
           return board[2][2]
        
    if board[0][0]=='O' and board[2][2]=='O':#rightdiagcentre
         if board[1][1] not in ['X','O']:
             board[1][1]='X'
             print('f')
             return board[1][1]
        
    if board[2][2]=='O' and board[1][1]=='O':#rightdiagtop
             if board[0][0] not in ['X','O']:
                 board[0][0]='X'
                 print('f')
                 return board[0][0]
        
    if board[0][2]=='O' and board[1][1]=='O':#leftdiagdown
              if board[2][0] not in ['X','O']:
                  board[2][0]='X'
                  print('f')
                  return board[2][0]
                                                                                                                        
    if board[0][2]=='X' and board[2][0]=='X' or board[0][2]=='O' and board[2][0]=='O':#leftdiagcentre
              if board[1][1] not in ['X','O']:
                  board[1][1]='X'
                  print('f')
                  return board[1][1]
        
    if board[2][0]=='X' and board[1][1]=='X' or board[2][0]=='O' and board[1][1]=='O':#leftdiagtop
              if board[0][2] not in ['X','O']:
                  board[0][2]='X'
                  print('f')
                  return board[0][2]
                                                                                    
    if board[0][1]=='O' and board[1][1]=='O':#centredown
              if board[2][1] not in ['X','O']:
                  board[2][1]='X'
                  print('f')
                  return board[2][1]
        
    if board[0][1]=='O' and board[2][1]=='O':#centrecentre
              if board[1][1] not in ['X','O']:
                   board[1][1]='X'
                   print('f')
                   return board[1][1]
                                                                                                
    if board[2][1]=='O' and board[1][1]=='O':#centretop 
              if board[0][1] not in ['X','O']:
                  board[0][1]='X';
                  print('f') 
                  return board[0][1]
        
    else:     
             free=freefields(board)
             freelen=len(free)
             if freelen>0:#if not-empty,choose a place for "x"
                 place=randrange(freelen)
                 row,col=free[place]
                 board[row][col]='X'

board=[[3*j+i+1 for i in range(3)] for j in range(3)]
trashtalk=["ok in your mind you think you're smart, you're a mumu man!","learner","wow,that was dum","mtchew, i thought you know how to play this game","let me remind you, i'm the master here"]
trashatt=["let's see how you'd block that", "i'm the smarter one bro!, hahaha,","come let me teach you this game! ", "lol, too smart"]

first=input('you wanna go first? y/n')
if first=='y'or first=='yes':
    print("guess you're scared of me")
else:
    print('''hmm let me think..
ok! i've got it''')
    from time import sleep
    sleep(2)
    free=freefields(board)
    freelen=len(free)
    if freelen>0:#if not-empty,choose a place for "x"
        place=randrange(freelen)
        row,col=free[place]
        board[row][col]='X'
        displayboard(board)
        print(choice(trashatt))
        
free=freefields(board)
manturn=True#whose turn
check=''
while len(free):
    displayboard(board)
    if check:
        print(choice(trashtalk))
    else:
        if check==False:
            print(choice(trashatt))
    if manturn:
        entermove(board)
        check=True
        victory=victor(board,'O')
    else:        
        drawmove(board)
        check=False
        victory=victor(board,'X')
    sample(trashtalk,len(trashtalk))
    sample(trashatt,len(trashatt))
    if victory!=None:
        break
    manturn=not manturn
    free=freefields(board)
displayboard(board)
if victory=='you':
    print('you won')
    print("if you get mind make we play again")
elif victory=='me':
    print('i won!!, hahaha, in your face sucker!')
    print("na computer of 26000k dey win you for ordinary tic tac toe,")
    print("you no dey shame")
else:
    print('tie')
    time.sleep(2)
    print("see this one na computer you follow draw you come dey happy, you're a mumu man") 
    print("if you get mind, make we play again, ")
