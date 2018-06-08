   #Compete both cpus:
   #def pickNextMove0():
      #find all possible moves
      #pick any 1 
   #def pickNextMove1():
      #find all possible moves 
      #pick the one that will cause the most flips
#pick 50 games 
#Strategy 1: take the corner
#near the nd of game, try all
#dictionary for generating moves positions
#movesDct["..ox.ox.."]=23  
import time
import sys
import random
aGroup=[]
neighborsFromCell={}
def main():
   global neighborsFromCell
   string="...........................OX......XO..........................."
   rr(string)
   #if(len(sys.argv)>1): stringinput=sys.argv[1]
   #if(len(sys.argv)>2): character=sys.argv[2]
   display(string)
   createNeighbors()
   print ("Player X & Player O.")
   current="X"
   
   listA=["0","1","2","3","4","5","6","7","8","9"]
   setA=set(listA)
   listB=["rr","rl","r2","i","fo","fd","fx","fy"]
   setB=set(listB)   
   
   while checkBoard(string)==False:
      while current=="X":
         possibilities=possibleMoves(string,current)
         print ("Possible letters forward: ",possibilities)
         if len(possibilities)==0:
            print ("No possibilities for Player "+current)
            current=switch(current)
            display(string)
         print ("Commands for rotations: ",listB)
         nxtchar=str(input("Turn for player "+current+": "))
         if nxtchar[0] in setA and nxtchar[-1] in setA:
            converted=convert(nxtchar[0],nxtchar[-1])
            if str(converted) not in possibilities: 
               print ("Position entered is not possible") 
            else:
               enemy=switch(current)   
               string=modify(current,enemy,string,converted)
               display(string) 
               current=enemy
         elif (nxtchar.lower()) in setB:
            display(transform(string,nxtchar))
         else:
             print ("Enter a possible character/position please. (Format:RowCol)")
            
            
      while current=="O":
         possibilities=possibleMoves(string,current)
         if len(possibilities)==0:
            print ("No possibilities for Player "+current)
            current=switch(current)
            display(string)
            break
         else:
            choiced=random.choice(list(possibilities))
            
            print (possibilities)
            print (choiced)
            
            enemy=switch(current)   
            string=modify(current,enemy,string,int(choiced))
            display(string) 
            current=enemy
            
      print ("______________________")
   print(scoreReport(string))

               
def convert(number1 ,number2):
   number1=int(number1)
   number2=int(number2)
   return (number1)*8+(number2)
   
def deconvert(number):
   return [number/8,number%8]

def transform(string, d):
   d=d.lower()
   if d=="rr":
      return rr(string)
   elif d=="rl":
      return rl(string)  
   elif d=="r2":
      return r2(string)
   elif d=="fd":
      return fd(string)
   elif d=="fo":
      return fo(string)
   elif d=="fx":
      return fx(string)
   elif d=="fy":
      return fy(string)
   elif d=="i":
      return string
   return string
        
def rl(string):

   new=[]
   base=7  
   letters=[]
   while base!=-1:
      for x in range(0,8):
         new.append(base+8*x)
      base=base-1  
   for x in range(len(string)):
      letters.append(string[new[x]])
   string=''.join(letters)      
   return string
            
def rr(string):
   new=[]
   base=0
   letters=[]
   while base!=8:
      for x in range(7,-1,-1):
         new.append(base+8*x)
      base=base+1    
   for x in range(len(string)):
      letters.append(string[new[x]])
   string=''.join(letters)    
   return string

     
def r2(string):

   return rr(rr(string))
  
def fd(string):
   new=[]
   base=7  
   letters=[]
   while base!=-1:
      for x in range(7,-1,-1):
         new.append(base+8*x)
      base=base-1  
   for x in range(len(string)):
      letters.append(string[new[x]])
   string=''.join(letters)   
   return string
     
def fo(string):
   new=[]
   base=0
   letters=[]
   while base!=8:
      for x in range(0,8):
         new.append(base+8*x)
      base=base+1    
   for x in range(len(string)):
      letters.append(string[new[x]])
   string=''.join(letters)    
   return string

def fx(string):
   new=[56,57,58,59,60,61,62,63,48,49,50,51,52,53,54,55,40,41,42,43,44,45,46,47,32,33,34,35,36,37,38,39,24,25,26,27,28,29,30,31,16,17,18,19,20,21,22,23,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7]
   letters=[]
   """
   for x in range(len(string)):
      returned=deconvert(x)
      other=7-returned[0]
      new.append(convert(other,returned[1])
   """
   for x in range(len(string)):
      letters.append(string[new[x]])
   string=''.join(letters)  
   return string

def fy(string):
   new=[]
   letters=[]
   for x in range(len(string)):
      returned=deconvert(x)
      other=7-returned[1]
      new.append(convert(returned[0],other))
   for x in range(len(string)):
      letters.append(string[new[x]])
   string=''.join(letters)
   return string


def modify(player,enemy, string, pos):
   global neighborsFromCell
   around=neighborsFromCell[pos]
   result=pos
   list=[pos]
   
   if (result+8)<=63 and string[result+8]==enemy: 
      while (result+8)<=63:
         if string[result+8]==enemy:
            result = result+8
            list.append(result)
         elif string[result+8]==".":
            break
         elif string[result+8]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos            
   list=[pos]
                      
   if (result-8)>=0 and string[result-8]==enemy:    
      while (result-8)>=0:
         if string[result-8]==enemy:
            result = result-8
            list.append(result)
         elif string[result-8]==".":
            break
         elif string[result-8]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos
   list=[pos]
    
   if (result+1)<=63 and (result+1)%8!=0 and string[result+1]==enemy:           
      while (result+1)<=63 and (result+1)%8!=0:
         if string[result+1]==enemy:
            result = result+1
            list.append(result)
         elif string[result+1]==".":
            break
         elif string[result+1]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos   
   list=[pos]
        
   if (result-1)>=0 and (result-1)%8!=0 and string[result-1]==enemy:              
      while (result-1)>=0 and (result-1)%8!=0:
         if string[result-1]==enemy:
            result = result-1
            list.append(result)
         elif string[result-1]==".":
            break
         elif string[result-1]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos   
   list=[pos]
   
   if (result-1)>=0 and (result-1)%8!=0 and (result+8)<=63 and string[result+7]==enemy:        
      while (result-1)>=0 and (result-1)%8!=0 and (result+8)<=63:
         if string[result+7]==enemy:
            result = result+7
            list.append(result)
         elif string[result+7]==".":
            break
         elif string[result+7]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos   
   list=[pos]

   
   if (result+1)<=63 and (result+1)%8!=0 and (result-8)>=0 and string[result-7]==enemy:  
      while (result+1)<=63 and (result+1)%8!=0 and (result-8)>=0:
         if string[result-7]==enemy:
            result = result-7
            list.append(result)
         elif string[result-7]==".":
            break
         elif string[result-7]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos   
   list=[pos]
           
   if (result+1)<=63 and (result+1)%8!=0 and (result+8)<=63 and string[result+9]==enemy:
      while (result+1)<=63 and (result+1)%8!=0 and (result+8)<=63: 
         if string[result+9]==enemy:
            result = result+9
            list.append(result)
         elif string[result+9]==".":
            break
         elif string[result+9]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
   result=pos   
   list=[pos]
    
   if (result-1)>=0 and (result-1)%8!=0 and  (result-8)>=0 and string[result-9]==enemy:     
      while (result-1)>=0 and (result-1)%8!=0 and  (result-8)>=0:
         if string[result-9]==enemy:
            result = result-9
            list.append(result)
         elif string[result-9]==".":
            break
         elif string[result-9]==player:
            for x in list:
               string=string[:x]+player+string[x+1:]
            break
    
   return string
   
def switch(stringchar):
   if stringchar=="X":
      return "O"
   return "X"
   
def checkBoard(string):
   countx=0
   counto=0
   for x in string:
      if x=="X":
         countx+=1
      elif x=="O":
         counto+=1
      if x == "." and countx!=0 and counto!=0:
         return False        
   return True
def scoreReport(string):
   countx=0
   counto=0
   for x in string:
      if x =="X":
         countx+=1
      if x =="O":
         counto+=1
   if countx>counto:
      return ("Player X wins!! The X-score: "+str(countx)+" and the O-score: "+str(counto))
   elif counto>countx:
      return ("Player O wins!! The O-score: "+str(counto)+" and the X-score: "+str(countx))
   else:
      return ("It's a draw!! The X-score: "+str(counto)+" and the O-score: "+str(countx))
          
def display(string):
   count=0
   print ("   0 1 2 3 4 5 6 7 ")
   print (" + - - - - - - - - + ")
   for x in range(8):
      stringtemp=str(x)+"|"
      for y in range(8):
         stringtemp=stringtemp+" "+string[count]
         
         if (y+1)%8==0:
            stringtemp=stringtemp+" |"+str(x)
            
         count=count+1

      print (stringtemp)
   print (" + - - - - - - - - + ")
   print ("   0 1 2 3 4 5 6 7 ")
   
def createNeighbors(): 
   global neighborsFromCell
   for x in range(64):
      neighborsFromCell[x]=[]
      if (x+8)<=63:
         neighborsFromCell[x].append(x+8)
      if (x-8)>=0: 
         neighborsFromCell[x].append(x-8)
      if (x+1)<=63 and (x+1)%8!=0:
         neighborsFromCell[x].append(x+1)
      if (x-1)>=0 and (x)%8!=0:
         neighborsFromCell[x].append(x-1)
         
      if (x+1)<=63 and (x+1)%8!=0 and (x-8)>=0:
         neighborsFromCell[x].append(x-7)
      if (x+1)<=63 and (x+1)%8!=0 and (x+8)<=63:
         neighborsFromCell[x].append(x+9)
      if (x-1)>=0 and (x)%8!=0 and (x-8)>=0:
         neighborsFromCell[x].append(x-9)
      if (x-1)>=0 and (x)%8!=0 and (x+8)<=0:
         neighborsFromCell[x].append(x+7)
       
def checkDirection(x, y):
   x=int(x)
   y=int(y)
   if (x+8)==y:
      return "d"
   if (x-8)==y:
      return "u"   
   if (x+1)==y:
      return "r"
   if (x-1)==y:
      return "l"
      
   if (x-7)==y:
      return "ur"
   if (x+9)==y:
      return "lr"
   if (x-9)==y:
      return "ul"
   if (x+7)==y:
      return "ll"
      
def possibleMoveHelper(s,e,string, enemy):
   direction= checkDirection(s, e)
   result=int(e)
   if direction=="d":
      while (result+8)<=63:
         if string[result+8]==enemy:
            result = result+8
         elif string[result+8]==".":
            return result+8
         else:
            return e
          
   if direction=="u":
      while (result-8)>=0:
         if string[result-8]==enemy:
            result = result-8
         elif string[result-8]==".":
            return result-8
         else:
            return e
 
             
   if direction=="r":
      while (result+1)<=63 and (result+1)%8!=0:
         if string[result+1]==enemy:
            result = result+1
         elif string[result+1]==".":
            return result+1
         else:
            return e
         

   if direction=="l": 
      while (result-1)>=0 and (result)%8!=0 and string[result]:
         if string[result-1]==enemy:
            result = result-1
         elif string[result-1]==".":
            return result-1
         else:
            return e
   
         
   if direction=="ur":
      while (result+1)<=63 and (result+1)%8!=0 and (result-8)>=0:
         if string[result-7]==enemy:
            result = result-7
         elif string[result-7]==".":
            return result-7
         else:
            return e

   if direction=="lr":
      while (result+1)<=63 and (result+1)%8!=0 and (result+8)<=63: 
         if string[result+9]==enemy:
            result = result+9
         elif string[result+9]==".":
            return result+9
         else:
            return e
   if direction=="ul":
      while (result-1)>=0 and (result)%8!=0 and  (result-8)>=0:
         if string[result-9]==enemy:
            result = result-9
         elif string[result-9]==".":
            return result-9
         else:
            return e
            
   if direction=="ll":
      while (result-1)>=0 and (result)%8!=0 and (result+8)<=63:
         if string[result+7]==enemy:
            result = result+7
         elif string[result+7]==".":
            return result+7
         else:
            return e
   return e
         
      
def possibleMoves(string,player):
   global neighborsFromCell
   possibleset=set()
   targetsymbol="O"
   if player=="O":
      targetsymbol="X"
   for x in range(len(string)):
      if string[x]==player:
         posspositions=neighborsFromCell[x]
         for y in posspositions:
            if string[y]==targetsymbol: 
               result = possibleMoveHelper(x,y,string,targetsymbol)
               if result!=y: 
                  possibleset.add(str(result))
   return possibleset                          
               
               
               
            
main()      
