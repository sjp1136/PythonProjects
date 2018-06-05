
#Homework: only two entities
   #Input: 1 C or C 1
   #Computer vs Person
   #structure similar to bruteForce()
   #Swapping the player (0,1)
   #How is the recursion going to terminate (if its a word)(global dictionary)
   
#*moderator...N players
#*hint....next letter
#*cheat...next letters for N=2 that win
import time
import sys
import random

def getch(): 
   import sys, tty, termios 
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(fd)
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
   return ch


def help():
   print ("Mini guide:")
   print ("1) Press letter keys of the alphabet for sequencing.")
   print ("2) Press period key for to receive all possible letters.")
   print ("3) Press comma key to challenge.")
   print ("-That's it.-")  
 
def analyze(prefix, playerNum,setA):
   if prefix in setA and len(prefix)>3: 
      return(set(),set())  
   tempGood,tempBad=set(),set()
   possible=possChar(prefix, setA)
   #print possible
   if possible!="No possibilities":
      for psletter in possible:
         tempGood,tempBad=analyze(prefix+psletter,1-playerNum,setA)
         if len(tempGood)!=0: tempBad.add(psletter)
         else: tempGood.add(psletter)
      return (tempGood,tempBad)
   return (tempGood,tempBad)
   
   
def possChar(s, wordlist):
   setA=set()
   size=len(s)
   for x in wordlist:
      if x[:size]==s and len(x)>len(s):
         setA.add(x[size:size+1])
   if len(setA)==0:
      return "No possibilities"
   return list(setA)
   
def challenge(s,wordlist):  
   size=len(s)
   if size>3:
      for x in wordlist:
         if x==s:
            return (True,""+x+" exists!")
         elif x[:size]==s and x[size:size+1]!=" ":
            return (False,x)
      return (True,s)
   else:
      return (False,"Length")
         
def buildTrie(prefix, wordIterator):   
   myDct={} #Keys: letters.  Values:
   for word in wordIterator:
      if len(word)<4: continue
      if word[:len(prefix)]!=prefix: continue
      if prefix in wordIterator: 
         myDct[" "]={}
         continue
      if word[len(prefix)] not in myDct:
         myDct[word[len(prefix)]]=set()
      myDct[word[len(prefix)]].add(word)
   for letter in myDct:
      myDct[letter]=buildTrie(prefix+letter,myDct[letter])
   return myDct   
   
def main():
   playerdict=[]
   count=1
   count1=1
   """
   for x in range(1,len(sys.argv)):
      if sys.argv[x]=="C":
         playerdict.append(sys.argv[x]+str(count))
         count=count+1
      elif sys.argv[x]=="1":
         playerdict.append(str(count1))
         count1=count1+1
   if sys.argv[1]!="1" and sys.argv[1]!="C":
      for y in range(1,int(sys.argv[1])+1):
            playerdict.append(str(y))
            """
   ghostfileset= set(open("ghost.txt","r").read().splitlines())
   #ghostfileset=set()
   
   #for x in ghostfileset1:
    #  if len(x)>=4:
     #    ghostfileset.add(x) 
   playerdict.append(0)
   playerdict.append(1)      
   
   print ("Welcome to Ghost!")
   help() 
   print ("Game begun!")
   string=""
   
   
   #playerdict={}
   #for x in range(numbers):
      #playerdict[str(x+1)]=""
      
   while len(playerdict)!=1:
      #sorted= playerdict.keys()
      #sorted.sort()
      length=len(playerdict)
      index=0
      while index <length:
         x=playerdict[index]
         #if x[0:1]!="C":
         #if x[0:1]==0:
         if x==0:
            while True:
               nxtchar=getch()
               if nxtchar==".":
                  print ("Possible letters forward: ",possChar(string,ghostfileset)) #possChar(string) method
               elif nxtchar.isalpha():
                  string=string+nxtchar
                  print ("Player "+str(x),string)
                  break
               
               elif nxtchar==",":
                  result=challenge(string,ghostfileset)
                  
                  if len(playerdict)==2:
                     print ("Game over!!")
                     if result[0]==True and len(string)>3:
                        print ("Player: "+str(x)+" wins!")
                        playerdict.remove(previous)
                     elif result[0] ==False and len(string)>3:
                        print ("Player: "+previous+" wins!")
                        playerdict.remove(x)
                    
                        
                  elif len(playerdict)>2:
                     if result[0]==True:
                        print (""+previous+" is out!")
                        playerdict.remove(previous)
                     elif result[0]==False:
                        print (""+x+" is out!")
                        playerdict.remove(x)
                  break
         #else:
         elif x==1:
            result=challenge(string,ghostfileset)
            if len(playerdict)==2 and result[0]==True:
               print ("Game over!!")
               print ("Player: "+str(x)+" wins!")
               playerdict.remove(previous)                          
            elif len(playerdict)>2 and result[0]==True:
               print (""+previous+" is out!")
               playerdict.remove(previous)
               break
            elif len(playerdict)==2 and result[0]==False:
               Randomchoice=analyze(string, 1, ghostfileset)
               goodlist,badlist=Randomchoice
               print (goodlist)
               print (badlist)
               if len(badlist)!=0: 
                  decision=random.choice(list(badlist))
                  #print goodlist
                  string=string+decision
                  print ("Player "+str(x),string)
                  break
               else:
                  #print (str(x)+" is out!")
                  #playerdict.remove(x)
                  decision=random.choice(list(goodlist))
                  string=string+decision
                  print ("Player "+str(x),string)
                  break
         length=len(playerdict)                           
         previous=x
         index=index+1
            
         
               
               
      
"""  
def challenge(pre, chal,string):
   if checkWord(string)==False: #1)if it is true then, the previous player loses the round
      return False               #and the challenger starts the next round
   else if checkpword(string)==False:#2)
      return False
   return True
def 
"""
main()
