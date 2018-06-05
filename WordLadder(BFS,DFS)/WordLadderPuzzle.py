import sys
import time
from collections import deque
#DFS
#Dijkstra
       
def dijkstra(graf, w,list1):
   dist={}
   previous={}
   small=99999
   queue1=list1
   for v in graf:
      dist[v]=9999
      previous[v]=None 
   dist[w]=0
   index=0
   while len(queue1)>0:
      small=99999 
      for x in queue1:
         if dist[x]<small:
            small= dist[x]
            index=queue1.index(x)                        
      u=queue1[index]
      queue1.remove(u) #queue1.remove(u)
      for v in graf[u].keys():  
         alt =dist[u]+graf[u][v]
         if alt<dist[v]:
            dist[v]=alt
            previous[v]=u
   return previous
      
def DFS(start, dict):
   visited = set()
   stack=[start]
   far=""
   parent = {start:None}
   index = 0
   while stack:
      vertex = stack.pop()
      if vertex not in visited:
         visited.add(vertex) 
         
         for x in dict[vertex]:
            if x not in visited:#checks if child is direct descentdant instead of interdirections
               stack.append(x)
               parent[x]=vertex
   return [parent,far]
   
#Assignment 4: Making BFS
def BFS(w,adj):
   components=[w]         
   level ={w:0}   
   parent={w:None}
   i=1          
   frontier=[w]
   highsub = w
   max =0
   while frontier:
      next =[]
      for x in frontier:
         for y in adj[x]:
            if y not in level:
               highsub=y
               level[y]=i
               parent[y]=x
               next.append(y) 
               components.append(y)
      frontier=next
      i+=1
   return [components,highsub,level[highsub],parent, level]


 
   
startTime=time.time()
#fileLoc=sys.argv[0] + "\\..\\words.txt"

#default word
word = "battle"
word2 = "castle"
#opening and reading the link
listA = open("words.txt", "r").read().splitlines()
if(len(sys.argv)>1): word=sys.argv[1] 
if(len(sys.argv)>2): word2=sys.argv[2]


#setting variables
dictionary={}
dictionary2={}
wordcount=0
lettercount=0
edgecount=0
templist=[]
listappend=[]
alphabet="abcdefghijklmnopqrstuvwxyz"
# part 2 variables
dictfreq={}
highnumber=0
number=0

#making dictionray values list
for bob in listA:
   dictionary[bob]=[]
   dictionary2[bob]=[]
   wordcount=wordcount+1

setA = set(listA)

# Assignment 3: Speed up making dictionary
for i in range(wordcount):
   string=listA[i]
   for x in range(6):
   
      for y in alphabet:
         if string[x]!=y:
            list2=list(string) # get the list form of string
            list2[x]=y   #changing one letter
            list2=''.join(list2)#make back into stringing
            if list2 in setA:
               dictionary[string].append(list2)
#Assignment 5: Making Djikstra dictionary
for i in range(wordcount):
   string=listA[i]
   for x in range(5):
      list2=list(string)
      temp=string[x]
      temp2=string[x+1]
      list2[x]=temp2
      list2[x+1]=temp
      list2=''.join(list2) 
      if list2 in setA and temp!=temp2:
         dictionary2[string].append(list2)
         
        
        
      #Assignment 2:finding frequency    
#for wordz in listA:
   #dictfreq[wordz]=len(dictionary[wordz])
   #if highnumber < len(dictionary[wordz]):
      #highnumber=len(dictionary[wordz]) 
#listfreq=[]
#for wordz in listA:
   #if dictfreq[wordz]==highnumber:
      #listfreq.append(wordz)


#4: getting the number of components, farthest word, distance, and path    
temp=listA[:]
component=[]
data={}       
for cool in temp:
   returned=BFS(cool, dictionary)
   component=returned[0]
   if len(component)>0:
      data[len(component)]=0
      for x in component:
         if x in temp: temp.remove(x)

temp=listA[:]
for cool in temp:
   returned=BFS(cool, dictionary)
   component=returned[0]
   if len(component)>0:
      data[len(component)]+=1
      for x in component: 
         if x in temp: temp.remove(x)
maxqueue=0
for key in data:
   if maxqueue<key:
      maxqueue=key
#Largest diameter
"""
diameter=0
for x in listA:
   returned = BFS(x, dictionary)
   distanceofword= returned[2]
   if(diameter < distanceofword):
      diameter=distanceofword


return [components,highsub,level[highsub],parent, level]
   

#1 variable:finding the BFS path
returned = BFS(word, dictionary)
parents = returned[3]
farword = returned[1]
limit = returned[2]
backpath=[farword]
path=[]
for x in range(limit):
   farword = parents[farword]
   backpath.append(farword)
for x in reversed(range(len(backpath))):
   path.append(backpath[x])
"""
#2 variables: finding the BFS path
"""
returned = BFS(word,dictionary)
parents=returned[3]
path=[]
read=word2
print (word)
print (word2)   
while read!=word:
   path.append(read)
   read=parents[read]
path.append(word)

path.reverse()
"""
#DFS
"""  
#2 variable DFS    
returned = DFS(word,dictionary)
parents=returned[0]
path=[]
read=word2
print (word)
print (word2)
if word2 not in parents:
print ("Path does not exist")
else:    
while read!=word:
path.append(read)
read=parents[read]
path.append(word)

path.reverse()
"""  

# Making Graph for Dijkstra
graph={}
for i in range(wordcount):
   string=listA[i]
   graph[string]={}
   for x in dictionary[string]:
      graph[string][x]=1
   for y in dictionary2[string]:
      if y is not None:
         graph[string][y]=5
   
#Dijkstra      
parents = dijkstra(graph,word,listA)
#print parents
path=[]
read=word2
graphno=0
print (word)
print (word2)
if word2 not in parents or parents[word2] is None:
   print ("Path does not exist")
else:    
   while read!=word:
      path.append(read) 
      read=parents[read]                   
   path.append(word)
   path.reverse()

for x in range(len(path)-1):
   graphno+=graph[path[x]][path[x+1]]



 
      
#academics.tjhsst.edu/compsci/ai   
#PRINTING RESULTS
#print(edgecount/2)
#print (word)
#print (word2)
#print (dictionary[word])
#print (wordcount)
#print ("The SPECIAL word(s):")
#for word1 in listfreq:
   #print (word1 +"'s neighbors:")
   #print (dictionary[word1])
#print (data)
#print("The longest length ever:")
#print (diameter)
print ("Path:")
print (path,"Length:",graphno, "Vertices visited:",len(path), "Max Queue:",maxqueue)
print ((time.time()-startTime))



#Djistra: difference is weights
#Bidirectional BFS
#DFS with interactive deepening: checking by list each level
#Given two words find
#1. shortest path between them
#2.#of words visited
#3.Largest size of your queue
#4.running time  


   
   
      
      
      
      
      
      
      
      
      
      
      
      
