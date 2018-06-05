from math import pi , acos , sin , cos
import sys
import time
def dijkstra(graf, w,list1,cityb):
   count=0
   dist={}
   previous={}
   small=99999
   queue1=list1
   setA=set()
   for v in queue1:
      dist[v]=9999
      previous[v]=None 
   dist[w]=0
   index=0
   while len(queue1)>0:
      index=0
      small=99999 
      for x in queue1:
         if dist[x]<small:
            small= dist[x]
            index=queue1.index(x)                             
      u=queue1[index]
      setA.add(u)
      queue1.remove(u) #queue1.remove(u)
      count=count+1
      for v in graf[u].keys():  
         alt =dist[u]+graf[u][v]
         if alt<dist[v]:
            dist[v]=alt
            previous[v]=u
   return [previous,dist[cityb],len(setA)]
   
def AStar(cityA,cityB,pathdict,coordinate,disdict):
   frontier={cityA:0}
   camefrom={cityA:None}
   costsofar={cityA:0} 
   countofdel=0 
   closed=[]
   c=set(closed) 
   while frontier is not None:
      least=99999999999
      for x in frontier:
         if frontier[x]<least:
            least=frontier[x]
            current=x
      c.add(current)
      del frontier[current]
      if current is cityB:
         return [camefrom,costsofar[cityB],len(c)]
      for next in pathdict[current]:
         newcost=costsofar[current] + disdict[current][next]
         if next not in costsofar or newcost<costsofar[next]:
            costsofar[next]=newcost
            priority=newcost + calcd(coordinate[next][0],coordinate[next][1],coordinate[cityB][0],coordinate[cityB][1])
            frontier[next]=priority
            camefrom[next]=current
        
#SUB METHODSS   
def makedict(namelist):
   dictionary={}
   for x in range(len(namelist)):
      firstletter=namelist[x][0]
      dictionary[firstletter]=namelist[x]
   return dictionary

def makepath(path):
   dictionary={}
   for x in range(len(path)):
      temp=path[x][0]
      temp2=path[x][2]
      dictionary[temp]=[]
      dictionary[temp2]=[]
   for x in range(len(path)):
      temp=path[x][0]
      temp2=path[x][2]
      dictionary[temp].append(temp2)
      dictionary[temp2].append(temp)
   return dictionary
   
def fulldict(geolist, path): #geolist: list of word and coordinates #path: A:B; A:C
   dictionary={}
   finaldict={}
   x = 0
   while x < len(geolist):
      dictionary[geolist[x]]=[geolist[x+2],geolist[x+1]]#dictionary [A:[x,y]]
      x=x+3
      
   for x in path.keys():
      finaldict[x]={}
      
   for x in path.keys():
      listlenA=dictionary[x]#brings out x  coordinates
      neighbors=path[x] #neighbors of x
      for y in neighbors: 
         listlenB=dictionary[y] #brings out neighbors coordinates
         finaldict[x][y]=calcd(listlenA[0], listlenA[1], listlenB[0], listlenB[1])
   return [finaldict,dictionary]   

def calcd(x1,y1, x2,y2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = 3958.76 # miles
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   if(x2 - x1 == 0): return 0
   return acos( (sin(y1)*sin(y2)) + (cos(y1)*cos(y2))*abs(cos(x2-x1)) ) * R

def main():
   startTime=time.time()
   namefile = open("romNames.txt", "r").read().splitlines()
   pathfile = open("romEdges.txt","r").read().splitlines()
   disfile = open("romNodes.txt", "r").read().split("\n")
   disfile2=[]
   for x in disfile:
      listA=x.split()
      for y in listA:
         disfile2.append(y)
   #MAKING ALL DATA 
   namedict=makedict(namefile)
   pathdict1=makepath(pathfile) #A:[B,C,D]
   returned=fulldict(disfile2,pathdict1)
   disdict1=returned[0]#dict:dict
   coordinate1=returned[1]#A:[1,2]
   citya="A"
   cityb="B"
                  
   if(len(sys.argv)>1): citya=sys.argv[1]
   if(len(sys.argv)>2): cityb=sys.argv[2]
   citya=citya[0]
   cityb=cityb[0]
  
   
   returned1=AStar(citya[0],cityb[0],pathdict1,coordinate1,disdict1)
   #returned1=dijkstra(disdict1,citya[0],disdict1.keys(),cityb[0])
   parents=returned1[0]
   costlist=returned1[1]
   #http://www.redblobgames.com/pathfinding/a-star/introduction.html
   #AStar Logic
   #Generating the Path
   if citya not in namedict or cityb not in namedict or parents[cityb] is None:
      print ("Path does not exist")
   else:    
      
      path=[]
      read=cityb
      while read!=citya:
         path.append(read) 
         read=parents[read]                   
      path.append(citya)
      path.reverse()  
   #Printing out everything  
   print (namedict[citya],"to",namedict[cityb])
   print ("Path:",path)   
   print ("Cost/Length:",costlist)
   print ("Numberofdeletions",returned1[2])
   print ("time",(time.time()-startTime))
         
   
main()



