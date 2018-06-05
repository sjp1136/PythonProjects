import time
import sys
from math import pi , acos , sin , cos
import math
import numpy as np
#import cv2
import cProfile
           
guesses=0
aGroup=[]
neighborsFromCell={}
aPossibility={}
numbers=["1","2","3","4","5","6","7","8","9"]

def main():
   global neighborsFromCell
   prevalidateSudoku()
   createNeighbors()
   index="1"
   index2="70 "
   if(len(sys.argv)>1): index=sys.argv[1]
   if(len(sys.argv)>2): index2=sys.argv[2]
   main2(index, index2)
   
def main2(index,index2):
   global aPossibility
   startTime=time.time()
   listtime=[]  
   puzzlefile=open("sudoku128.txt","r").read().splitlines()
   if index=="" and index2=="":      
      x=1
      y=128
      while x!=y: 
         startTime2=time.time()
         print("Problem #:"+str(x+1))                      
         string = puzzlefile[x]
         print("Problem:"+string)
         result = bruteForce(string)
         print("Solved: "+result)
         timer=time.time()-startTime2
         listtime.append(timer)
         print ("time",(timer))
         print()
         x+=1
      print ("Guesses:"+str(guesses))
      print ("Total time: ",time.time()-startTime)
      top3=[]
      for x in range(3):
         a=listtime.index(max(listtime))
         top3.append(a+1)
         listtime.remove(max(listtime))
      print ("Top 3 time indexes",top3)
      
   elif index2=="":
      print ("Problem #:"+str(index))
      string = puzzlefile[int(index)-1]
      showBoard(compile(string))
      print("SOLUTION:")
      result = bruteForce(string)
      showBoard(compile(result))
      print ("Guesses:"+str(guesses))
      print ("time",((time.time()-startTime)))
      
    
   else:
      x=int(index)-1
      y=int(index2)
      while x!=y:
         print("Problem #:"+str(x+1))                        
         string = puzzlefile[x]
         #print("Problem:"+string)
         print("Problem:")
         showBoard(compile(string)) 
         cool= validate(string)
         result = bruteForce(string)
         #print("Solved: "+result)
         print("Solved: ")
         showBoard(compile(result))   
         print ("time",((time.time()-startTime)))
         print ()
         x+=1  
      print ("Guesses:"+str(guesses))
      print ("Total time: ",time.time()-startTime)

def validate(puzzle):
   global aGroup
   for groupToCheck in aGroup:
      alreadySeen=set()
      for pos in groupToCheck:
         if puzzle[pos]!=".":
            if puzzle[pos] in alreadySeen: return False
            alreadySeen.add(puzzle[pos])
   return True

def createNeighbors():  
   global neighborsFromCell
   global aGroup 
   neighborsFromCell =[set() for dummy in range(81)]
   for group in aGroup:
      for pos1 in group:
         neighborsFromCell[pos1]=neighborsFromCell[pos1]|(set(group)-{pos1})


              
"""for 2nd bruteForce method
def createAndGetMin(a, puzzle):
   global neighborsFromCell
   global aPossibility
   min=9
   index=-1
   numbers1=['1','2','3','4','5','6','7','8','9']
   setA=set(numbers1)
   for x in a:
      b=neighborsFromCell[x]
      aPossibility[x]=set()
      setB=set()
      for y in b:
         if puzzle[y]!=".":
            setB.add(puzzle[y])
      aPossibility[x]=aPossibility[x]|(setA-setB)
      if min > len(aPossibility[x]):
         min=len(aPossibility[x])
         index=x
   return [index,aPossibility[index]] 
"""
def createPossible(puzzle):
   global neighborsFromCell
   aPossibility={}
   numbers1=['1','2','3','4','5','6','7','8','9']
   A=set(numbers1)
   for pos in range(len(puzzle)):
      if puzzle[pos]==".":
         B=set()
         for pos2 in neighborsFromCell[pos]:
            neighbor=puzzle[pos2]
            if neighbor in A:
               B.add(neighbor)
         part=A-B
         aPossibility[pos]=part
   return aPossibility
   

def getMin(aPossibility4):
   min=1000
   index=-1
   if len(aPossibility4)==0: return -1
   for x in aPossibility4:
      if len(aPossibility4[x])<min:
         min=len(aPossibility4[x])
         index=x
   return index


def makeDeductions(puzzle):
   global neighborsFromCell
   global aGroup
   aPossibility3=createPossible(puzzle)
   state=True
   while state==True:
      state=False
      for pos in aPossibility3:
         numbers=aPossibility3[pos]
         if len(numbers)==0:
            return ""
         elif len(numbers)==1:
            puzzle = puzzle[:pos] + numbers.pop() + puzzle[pos+1:]
            aPossibility3=createPossible(puzzle)
         else:
            posvalues=set()
            for group in aGroup:
               if pos in group:
                  for index in group:
                     if index in aPossibility3 and index!=pos:
                        for value in aPossibility3[index]:
                           posvalues.add(value)
                  for possible in numbers:
                     if possible not in posvalues:
                        puzzle = puzzle[:pos] + possible + puzzle[pos+1:]
                        state=True
      aPossibility3=createPossible(puzzle)
   aPossibility3=createPossible(puzzle)           
   return (puzzle, aPossibility3)

def bruteForce(puzzle):
   global guesses
   result=makeDeductions(puzzle)
   if result == "":
      return ""
   puzzle, aPossibility1=result
   pos = getMin(aPossibility1)   
   if pos<0:return puzzle
   for sym in aPossibility1[pos]:
      guesses+=1
      tmpPuzzle=bruteForce(puzzle[:pos]+""+sym+puzzle[pos+1:])
      if tmpPuzzle!="": return tmpPuzzle 
   return ""
"""
def bruteForce(puzzle):
   global guesses
   global numbers
   if not validate(puzzle): return ""
   h=getPossibility(puzzle)
   if len(h)==0:
      return puzzle
   returned=createAndGetMin(h,puzzle)
   pos=returned[0]
   setA=returned[1]
   if pos < 0 : return puzzle
   for c in setA: #available symbols at some pos guess sym @pos
      guesses+=1
      bf=bruteForce(puzzle[:pos]+""+c+puzzle[pos+1:])
      if bf!="": return bf
   return ""
 """ 
def prevalidateSudoku(): 
   global aGroup
   listA2=[]
   listB2=[]
   for y in range(9):
      listA=[]
      for x in range(9):
         listA.append((y*9)+(x))
      listA2.append(listA)
   aGroup.extend(listA2)
   
   for x in range(9):
      listB=[]
      for y in range(9):
         listB.append((y*9)+(x))
      listB2.append(listB)
   aGroup.extend(listB2)
             
   y=0
   x=0
   listC2=[]
   while y < 9:
      x=0
      while x < 9:
         listC=[]
         for b in range(3):
            for a in range(3):
               listC.append(((y+b)*9)+(x+a))
         listC2.append(listC)
         x=x+3
      y=y+3
   aGroup.extend(listC2)


def compile(puzzle):
   size=math.sqrt(len(puzzle))
   sample = puzzle
   puzzledict={}
   count=0
   for y in range(int(size)):
      puzzledict[y]={}
   for y in range(int(size)):
      for x in range(int(size)):
         puzzledict[x][y]=sample[count]
         count=count+1
   return puzzledict
   
def showBoard(puzzle):
   count=0 
   count1=0  
   for y in range(len(puzzle)):
      str=""
      str2=""
      if y%3==0 and y!=0:
         for x in range(len(puzzle)):
            if count1%3==0:
               str2+=" "
            str2+="-"
            count1+=1
         print (str2) 
      for x in range(len(puzzle)):
         if count%3==0 or (x==0 and y==0):
            str+="|"
         str+=puzzle[x][y]
         count+=1 
      str+="|"
      print (str)
        
main()
       
  
            
      
      
            
         
  
   

   
