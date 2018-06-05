import sys
import numpy as np
import math
#import urllib.request as ur
import cv2
#import Image

def makegray(image):
   for x in range(image.shape[0]):
      for y in range(image.shape[1]):
         pixel=image[x,y]
         graycolor= 0.3*pixel[0]+0.59*pixel[1]+0.11*pixel[2]
         image[x,y]=[graycolor,graycolor,graycolor]
   return image
   
  
def makeblur(image):
   copied=image.copy()
   temp=image.copy() 
   h=image.shape[0]
   w=image.shape[1]
   for x in range(1,h-2):
      for y in range(1,w-2):
         r=(1.0/16) *(4*image[x,y][0] +2*image[x,y-1][0] +2*image[x,y+1][0] +2*image[x+1,y][0] +2*image[x-1,y][0]+image[x-1,y-1][0]+image[x+1,y-1][0]+image[x-1,y+1][0]+image[x+1,y+1][0])
         g=(1.0/16) *(4*image[x,y][1] +2*image[x,y-1][1]+2*image[x,y+1][1]+2*image[x+1,y][1]+2*image[x-1,y][1]+image[x-1,y-1][1]+image[x+1,y-1][1]+image[x-1,y+1][1]+image[x+1,y+1][1])
         b=(1.0/16) *(4*image[x,y][2] +2*image[x,y-1][2]+2*image[x,y+1][2]+2*image[x+1,y][2]+2*image[x-1,y][2]+image[x-1,y-1][2]+image[x+1,y-1][2]+image[x-1,y+1][2]+image[x+1,y+1][2])
         copied[x,y]=[r,g,b]
   return copied  

def makeedge(image,threshold):
   copied=image.copy()
   h=image.shape[0]
   w=image.shape[1]
   for x in range(1,h-2):
      for y in range(1,w-2):
         gx=(-2*image[x,y-1][0] +2*image[x,y+1][0] +(-1)*image[x-1,y-1][0]+(-1)*image[x+1,y-1][0]+image[x-1,y+1][0]+image[x+1,y+1][0])
         gy=(2*image[x+1,y][1]+(-2)*image[x-1,y][1]+(-1)*image[x-1,y-1][1]+image[x+1,y-1][1]+(-1)*image[x-1,y+1][1]+image[x+1,y+1][1])
         gxt=gx*gx
         gyt=gy*gy
         g=math.sqrt(gxt+gyt)
         if g>threshold: 
            copied[x,y] = [0,0,0]
         else:
            copied[x,y] = [255,255,255]
   return copied  
    
def makecanny(image,threshold):
   copied=image.copy()
   h=image.shape[0]
   w=image.shape[1]
   x=1
   y=1
   while x!=h-2:
      y=1
      while y!=w-2:  
         gx=(-2*image[x,y-1][0] +2*image[x,y+1][0] +(-1)*image[x-1,y-1][0]+(-1)*image[x+1,y-1][0]+image[x-1,y+1][0]+image[x+1,y+1][0])
         gy=(2*image[x+1,y][1]+(-2)*image[x-1,y][1]+(-1)*image[x-1,y-1][1]+image[x+1,y-1][1]+(-1)*image[x-1,y+1][1]+image[x+1,y+1][1])
         gxt=gx*gx
         gyt=gy*gy
         g=math.sqrt(gxt+gyt)
         angle=math.atan2(gy, gx)*180/math.pi
         if -180<=angle and angle<=-157.5 or -22.5<angle and angle<=22.5 or 157.5<angle and angle<=180:
            y1=y-1
            y2=y+1    
            gy1=(2*image[x+1,y1][1]+(-2)*image[x-1,y1][1]+(-1)*image[x-1,y1-1][1]+image[x+1,y1-1][1]+(-1)*image[x-1,y1+1][1]+image[x+1,y1+1][1])
            gy2=(2*image[x+1,y2][1]+(-2)*image[x-1,y2][1]+(-1)*image[x-1,y2-1][1]+image[x+1,y2-1][1]+(-1)*image[x-1,y2+1][1]+image[x+1,y2+1][1])
            g1=math.sqrt(gxt+(gy1*gy1))
            g2=math.sqrt(gxt+(gy2*gy2))
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
            else:  
               copied[x,y] = [255,255,255]
         elif -157.5<angle and angle<=-112.5 or 22.5<angle and angle<=67.5:
         
            x1=x+1
            y1=y-1
            x2=x-1
            y2=y+1
            gx1=(-2*image[x1,y1-1][0] +2*image[x1,y1+1][0] +(-1)*image[x1-1,y1-1][0]+(-1)*image[x1+1,y1-1][0]+image[x1-1,y1+1][0]+image[x1+1,y1+1][0])
            gx2=(-2*image[x2,y2-1][0] +2*image[x2,y2+1][0] +(-1)*image[x2-1,y2-1][0]+(-1)*image[x2+1,y2-1][0]+image[x2-1,y2+1][0]+image[x2+1,y2+1][0])
            gy1=(2*image[x1+1,y1][1]+(-2)*image[x1-1,y1][1]+(-1)*image[x1-1,y1-1][1]+image[x1+1,y1-1][1]+(-1)*image[x1-1,y1+1][1]+image[x1+1,y1+1][1])
            gy2=(2*image[x2+1,y2][1]+(-2)*image[x2-1,y2][1]+(-1)*image[x2-1,y2-1][1]+image[x2+1,y2-1][1]+(-1)*image[x2-1,y2+1][1]+image[x2+1,y2+1][1])
            g1=math.sqrt(gx1*gx1+gy1*gy1)
            g2=math.sqrt(gx2*gx2+gy2*gy2)
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
            else: 
               copied[x,y] = [255,255,255]
         
         elif -112.5<angle and angle<=-67.5 or 67.5<=angle and angle<112.5:
            x1=x+1
            x2=x-1
            gx1=(-2*image[x1,y-1][0] +2*image[x1,y+1][0] +(-1)*image[x1-1,y-1][0]+(-1)*image[x1+1,y-1][0]+image[x1-1,y+1][0]+image[x1+1,y+1][0])
            gx2=(-2*image[x2,y-1][0] +2*image[x2,y+1][0] +(-1)*image[x2-1,y-1][0]+(-1)*image[x2+1,y-1][0]+image[x2-1,y+1][0]+image[x2+1,y+1][0])
            g1=math.sqrt(gx1*gx1+gyt)
            g2=math.sqrt(gx2*gx2+gyt)
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
            else:  
               copied[x,y] = [255,255,255]
         
         elif -67.5<angle and angle<=-22.5 or 115.5<angle and angle<=157.5:
            x1=x+1
            y1=y+1
            x2=x-1
            y2=y-1
            gx1=(-2*image[x1,y1-1][0] +2*image[x1,y1+1][0] +(-1)*image[x1-1,y1-1][0]+(-1)*image[x1+1,y1-1][0]+image[x1-1,y1+1][0]+image[x1+1,y1+1][0])
            gx2=(-2*image[x2,y2-1][0] +2*image[x2,y2+1][0] +(-1)*image[x2-1,y2-1][0]+(-1)*image[x2+1,y2-1][0]+image[x2-1,y2+1][0]+image[x2+1,y2+1][0])
            gy1=(2*image[x1+1,y1][1]+(-2)*image[x1-1,y1][1]+(-1)*image[x1-1,y1-1][1]+image[x1+1,y1-1][1]+(-1)*image[x1-1,y1+1][1]+image[x1+1,y1+1][1])
            gy2=(2*image[x2+1,y2][1]+(-2)*image[x2-1,y2][1]+(-1)*image[x2-1,y2-1][1]+image[x2+1,y2-1][1]+(-1)*image[x2-1,y2+1][1]+image[x2+1,y2+1][1])
            g1=math.sqrt(gx1*gx1+gy1*gy1)
            g2=math.sqrt(gx2*gx2+gy2*gy2)
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
            else:  
               copied[x,y] = [255,255,255]
      
         y=y+1
      x=x+1
   return copied  
   """ 
def makeLine(image, slope,y,x,targetx):
   copied=image.copy()
   equation=slope*(targetx-x)-y
   """
def detectCircle(image, threshold, threshold2):
   copied=image.copy()
   h=image.shape[0]
   w=image.shape[1]
   x=1
   y=1
   dict={}
   for i in range(h):
      for k in range(w):
         dict[(i,k)]=0
         
   while x!=h-2:
      y=1
      while y!=w-2:  
         gx=(-2*image[x,y-1][0] +2*image[x,y+1][0] +(-1)*image[x-1,y-1][0]+(-1)*image[x+1,y-1][0]+image[x-1,y+1][0]+image[x+1,y+1][0])
         gy=(2*image[x+1,y][0]+(-2)*image[x-1,y][0]+(-1)*image[x-1,y-1][0]+image[x+1,y-1][0]+(-1)*image[x-1,y+1][1]+image[x+1,y+1][1])
         gxt=gx*gx
         gyt=gy*gy
         g=math.sqrt(gxt+gyt)
         #angle=math.atan2(gy, gx)*180/math.pi
         #print ("X"+str(gx))
         #print ("Y"+str(gy))
         # d=qcos(0) -Psind(0)
         if gy!=0 and gx!=0 and round(-gx/gy)!=0:
            #slope=gy/gx
            
            pslope=round(-(gx/gy))
            print (pslope)
            
            #print ("S"+str(slope))
            if pslope<0:
               x1=x+abs(pslope)
               y1=y+1
               x2=x-abs(pslope)
               y2=y-1
               if x1>1 and x1<h-2 and x2>1 and x2<h-2 and y1>1 and y2>1 and y1<w-2 and y2<w-2:
                  gx1=(-2*image[x1,y1-1][0] +2*image[x1,y1+1][0] +(-1)*image[x1-1,y1-1][0]+(-1)*image[x1+1,y1-1][0]+image[x1-1,y1+1][0]+image[x1+1,y1+1][0])
                  gx2=(-2*image[x2,y2-1][0] +2*image[x2,y2+1][0] +(-1)*image[x2-1,y2-1][0]+(-1)*image[x2+1,y2-1][0]+image[x2-1,y2+1][0]+image[x2+1,y2+1][0])
                  gy1=(2*image[x1+1,y1][0]+(-2)*image[x1-1,y1][1]+(-1)*image[x1-1,y1-1][1]+image[x1+1,y1-1][1]+(-1)*image[x1-1,y1+1][1]+image[x1+1,y1+1][1])
                  gy2=(2*image[x2+1,y2][0]+(-2)*image[x2-1,y2][1]+(-1)*image[x2-1,y2-1][1]+image[x2+1,y2-1][1]+(-1)*image[x2-1,y2+1][1]+image[x2+1,y2+1][1])
                  g1=math.sqrt(gx1*gx1+gy1*gy1)
                  g2=math.sqrt(gx2*gx2+gy2*gy2)
                  if g>threshold and g>g1 and g>g2:
                     copied[x,y]=[0,0,0]
                     sub=x
                     sub2=y
                     while sub>1 and sub2>1 and sub<h-2 and sub2<w-3: 
                        for count in range(abs(int(pslope))):
                           if sub>1 and sub<h-2: 
                              sub+=1
                              copied[sub, sub2]=[0,0,0]
                              dict[(sub,sub2)]+=1
                        if sub2>1 and sub2<w-3:
                           sub2+=1  
                           copied[sub,sub2]=[0,0,0]
                           dict[(sub,sub2)]+=1 
                     sub=x
                     sub2=y
                     while sub>1 and sub2>1 and sub<h-2 and sub2<w-3: 
                        for count in range(abs(int(pslope))):
                           
                           if sub>1 and sub<h-2:
                              sub=sub-1  
                              copied[sub, sub2]=[0,0,0]
                              dict[(sub,sub2)]+=1           
                        if sub2>1 and sub2<w-3:  
                           sub2=sub2-1
                           copied[sub,sub2]=[0,0,0]
                           dict[(sub,sub2)]+=1
            
            elif pslope>0:
               x1=x-abs(pslope)
               y1=y+1
               x2=x+abs(pslope)
               y2=y-1
               if x1>1 and x1<h-2 and x2>1 and x2<h-2 and y1>1 and y2>1 and y1<w-2 and y2<w-2:
                  gx1=(-2*image[x1,y1-1][0] +2*image[x1,y1+1][0] +(-1)*image[x1-1,y1-1][0]+(-1)*image[x1+1,y1-1][0]+image[x1-1,y1+1][0]+image[x1+1,y1+1][0])
                  gx2=(-2*image[x2,y2-1][0] +2*image[x2,y2+1][0] +(-1)*image[x2-1,y2-1][0]+(-1)*image[x2+1,y2-1][0]+image[x2-1,y2+1][0]+image[x2+1,y2+1][0])
                  gy1=(2*image[x1+1,y1][1]+(-2)*image[x1-1,y1][1]+(-1)*image[x1-1,y1-1][1]+image[x1+1,y1-1][1]+(-1)*image[x1-1,y1+1][1]+image[x1+1,y1+1][1])
                  gy2=(2*image[x2+1,y2][1]+(-2)*image[x2-1,y2][1]+(-1)*image[x2-1,y2-1][1]+image[x2+1,y2-1][1]+(-1)*image[x2-1,y2+1][1]+image[x2+1,y2+1][1])
                  g1=math.sqrt(gx1*gx1+gy1*gy1)
                  g2=math.sqrt(gx2*gx2+gy2*gy2)
                  if g>threshold and g>g1 and g>g2:
                     copied[x,y]=[0,0,0]
                     sub=x
                     sub2=y
                     while sub>1 and sub2>1 and sub<h-2 and sub2<w-3: 
                        for count in range(abs(int(pslope))):
                           
                           if sub>1 and sub<h-2: 
                              sub=sub-1 
                              copied[sub, sub2]=[0,0,0]
                              dict[(sub,sub2)]+=1
                        if sub2>1 and sub2<w-3:  
                           sub2+=1
                           copied[sub,sub2]=[0,0,0]
                           dict[(sub,sub2)]+=1
                  
                     sub=x
                     sub2=y
                     while sub>1 and sub2>1 and sub<h-2 and sub2<w-3: 
                        for count in range(abs(int(pslope))):
                           
                           if sub>1 and sub<h-2: 
                              sub+=1 
                              copied[sub,sub2]=[0,0,0]
                              dict[(sub,sub2)]+=1
                        if sub2>1 and sub2<w-3:
                           sub2=sub2-1  
                           copied[sub,sub2]=[0,0,0]
                           dict[(sub,sub2)]+=1
            
         #elif gx==0:
            #for count in range(h):
               #copied[count,y]=[0,0,0]
               #dict[(count,y)]+=1      
         y=y+1                           
      x=x+1
   #for i in range(h):
      #for j in range(w):
         #if dict[(i,j)]<threshold2:
            #copied[i,j]=[144,110,150]
   return copied
     
def calcG(image, x,y):
   gx=(-2*image[x,y-1][0] +2*image[x,y+1][0] +(-1)*image[x-1,y-1][0]+(-1)*image[x+1,y-1][0]+image[x-1,y+1][0]+image[x+1,y+1][0])
   gy=(2*image[x+1,y][1]+(-2)*image[x-1,y][1]+(-1)*image[x-1,y-1][1]+image[x+1,y-1][1]+(-1)*image[x-1,y+1][1]+image[x+1,y+1][1])
   gxt=gx*gx
   gyt=gy*gy
   g=math.sqrt(gxt+gyt)
   return g
   
def adj(image,returned,x,y,t,t2):
   if t<calcG(image,x+1,y)<t2:
      returned[x+1,y]=[0,0,0]
   if t<calcG(image,x-1,y)<t2:
      returned[x-1,y]=[0,0,0]
   if t< calcG(image,x,y+1)<t2:
      returned[x,y+1]=[0,0,0]
   if t<calcG(image,x,y-1)<t2:
      returned[x,y-1]=[0,0,0]
   if t<calcG(image,x+1,y+1)<t2:
      returned[x+1,y+1]=[0,0,0]
   if t<calcG(image,x+1,y-1)<t2:
      returned[x+1,y-1]=[0,0,0]
   if t<calcG(image,x-1,y-1)<t2:
      returned[x-1,y-1]=[0,0,0]
   if t<calcG(image,x-1,y+1)<t2:
      returned[x-1,y+1]=[0,0,0]
   return returned
   
   


def makecanny2(image, threshold, threshold2):
   copied=image.copy()
   h=image.shape[0]
   w=image.shape[1]
   x=1
   y=1
   listedd=[]
   while x!=h-2:
      y=1
      while y!=w-2:  
         gx=(-1*image[x-1,y-1][0] + (-2)*image[x,y-1][0] +(-1)*image[x+1,y-1][0]+(1)*image[x-1,y+1][0]+(2)*image[x,y+1][0]+image[x+1,y+1][0])
         gy=((-1)*image[x-1,y-1][1]+(-2)*image[x-1,y][1]+(-1)*image[x-1,y+1][1]+image[x+1,y-1][1]+(2)*image[x+1,y][1]+image[x+1,y+1][1])
         gxt=gx*gx
         gyt=gy*gy
         g=math.sqrt(gxt+gyt)
         angle=math.atan2(gy, gx)*180/math.pi
         if -180<=angle and angle<-157.5 or -22.5<=angle and angle<22.5 or 157.5<=angle and angle<180:
            y1=y-1
            y2=y+1    
            gy1=((-1)*image[x-1,y1-1][1]+(-2)*image[x-1,y1][1]+(-1)*image[x-1,y1+1][1]+image[x+1,y1-1][1]+(2)*image[x+1,y1][1]+image[x+1,y1+1][1])
            gy2=((-1)*image[x-1,y2-1][1]+(-2)*image[x-1,y2][1]+(-1)*image[x-1,y2+1][1]+image[x+1,y2-1][1]+(2)*image[x+1,y2][1]+image[x+1,y2+1][1])
            g1=math.sqrt(gxt+(gy1*gy1))
            g2=math.sqrt(gxt+(gy2*gy2))
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
               copied=adj(image,copied,x,y,threshold, threshold2)
               listedd.append((x,y))
            #else:  
             #  copied[x,y] = [255,255,255]
               #listedd.append((x,y))
         
         elif -157.5<=angle and angle<112.5 or 22.5<=angle and angle<67.5:
         
            x1=x+1
            y1=y-1
            x2=x-1
            y2=y+1
            gx1=(-1*image[x1-1,y1-1][0] + (-2)*image[x1,y1-1][0] +(-1)*image[x1+1,y1-1][0]+(1)*image[x1-1,y1+1][0]+(2)*image[x1,y1+1][0]+image[x1+1,y1+1][0])
            gx2=(-1*image[x2-1,y2-1][0] + (-2)*image[x2,y2-1][0] +(-1)*image[x2+1,y2-1][0]+(1)*image[x2-1,y2+1][0]+(2)*image[x2,y2+1][0]+image[x2+1,y2+1][0])
            
            gy1=((-1)*image[x1-1,y1-1][1]+(-2)*image[x1-1,y1][1]+(-1)*image[x1-1,y1+1][1]+image[x1+1,y1-1][1]+(2)*image[x1+1,y1][1]+image[x1+1,y1+1][1])
            gy2=((-1)*image[x2-1,y2-1][1]+(-2)*image[x2-1,y2][1]+(-1)*image[x2-1,y2+1][1]+image[x2+1,y2-1][1]+(2)*image[x2+1,y2][1]+image[x2+1,y2+1][1])
            g1=math.sqrt(gx1*gx1+gy1*gy1)
            g2=math.sqrt(gx2*gx2+gy2*gy2)
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
               listedd.append((x,y))
            
               copied=adj(image,copied,x,y,threshold, threshold2)
            
            #else: 
               #copied[x,y] = [255,255,255]
               #listedd.append((x,y))
         
         
         elif -112.5<=angle and angle<-67.5 or 67.5<=angle and angle<112.5:
            x1=x+1
            x2=x-1
            gx1=(-1*image[x1-1,y1-1][0] + (-2)*image[x1,y1-1][0] +(-1)*image[x1+1,y1-1][0]+(1)*image[x1-1,y1+1][0]+(2)*image[x1,y1+1][0]+image[x1+1,y1+1][0])
            gx2=(-1*image[x2-1,y2-1][0] + (-2)*image[x2,y2-1][0] +(-1)*image[x2+1,y2-1][0]+(1)*image[x2-1,y2+1][0]+(2)*image[x2,y2+1][0]+image[x2+1,y2+1][0])
            g1=math.sqrt(gx1*gx1+gyt)
            g2=math.sqrt(gx2*gx2+gyt)
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
               copied=adj(image,copied,x,y,threshold, threshold2)
               listedd.append((x,y))
            
            #else:  
             #  copied[x,y] = [255,255,255]
               #listedd.append((x,y))
         
         elif -67.5<=angle and angle<-22.5 or 115.5<=angle and angle<157.5:
            x1=x+1
            y1=y+1
            x2=x-1
            y2=y-1
            gx1=(-1*image[x1-1,y1-1][0] + (-2)*image[x1,y1-1][0] +(-1)*image[x1+1,y1-1][0]+(1)*image[x1-1,y1+1][0]+(2)*image[x1,y1+1][0]+image[x1+1,y1+1][0])
            gx2=(-1*image[x2-1,y2-1][0] + (-2)*image[x2,y2-1][0] +(-1)*image[x2+1,y2-1][0]+(1)*image[x2-1,y2+1][0]+(2)*image[x2,y2+1][0]+image[x2+1,y2+1][0])
            
            gy1=((-1)*image[x1-1,y1-1][1]+(-2)*image[x1-1,y1][1]+(-1)*image[x1-1,y1+1][1]+image[x1+1,y1-1][1]+(2)*image[x1+1,y1][1]+image[x1+1,y1+1][1])
            gy2=((-1)*image[x2-1,y2-1][1]+(-2)*image[x2-1,y2][1]+(-1)*image[x2-1,y2+1][1]+image[x2+1,y2-1][1]+(2)*image[x2+1,y2][1]+image[x2+1,y2+1][1])
            g1=math.sqrt(gx1*gx1+gy1*gy1)
            g2=math.sqrt(gx2*gx2+gy2*gy2)
            if g>threshold and g>g1 and g>g2:
               copied[x,y] = [0,0,0]
               copied=adj(image,copied,x,y,threshold, threshold2)
               listedd.append((x,y))
            #else:  
             #  copied[x,y] = [255,255,255]
               #listedd.append((x,y))
      
         y=y+1
      x=x+1
   return (copied, listedd)
   
def makeCircle(image, list):
   copied=image.copy()
   i=255
   setA=set(list)
   dict={}
   for x in range(image.shape[0]):
      for y in range(image.shape[1]):
         copied[x,y]=[255,255,255]
   s = 100/len(setA)
   iter=0
   for (x,y) in setA: #p=vertical q=horizontal
      gx=(-2*image[x,y-1][0] +2*image[x,y+1][0] +(-1)*image[x-1,y-1][0]+(-1)*image[x+1,y-1][0]+image[x-1,y+1][0]+image[x+1,y+1][0])
      gy=(2*image[x+1,y][1]+(-2)*image[x-1,y][1]+(-1)*image[x-1,y-1][1]+image[x+1,y-1][1]+(-1)*image[x-1,y+1][1]+image[x+1,y+1][1])
      if gy==0 or gx==0: continue
      for d in range(image.shape[1]):
         yvalue=(d-y)*(gy/gx)+x
         yvalue=int(yvalue)
      
         if yvalue>=0 and yvalue<image.shape[0]:
         
            i=copied.item(yvalue,d,0)-1.5
            copied[yvalue,d]=[i,i,i]
      # sys.stdout.write("{}%             \r".format(iter*s))
      # sys.stdout.flush()
      iter+=1
      #if iter>1000:
         #break   
   value=255
   tuples=[] #getting points of possible centers 
   datadict={}
   resultdict={}
   for i in range(image.shape[0]):
      for j in range(image.shape[1]):
         if value > copied[i,j][0]:
            value=copied[i,j][0]
   #got the color value
            
   for i in range(image.shape[0]):
      for j in range(image.shape[1]):   
         if copied[i,j][0]==value:   # or (copied[i,j][0])<value<(copied[i,j][0]):
            tuples.append((i,j))
            datadict[(i,j)]=[]
            resultdict[(i,j)]=[]
            
   for points in tuples:
      for (y,x) in setA: 
         distance= ((points[0]-y)**2 + (points[1]-x)**2)**(0.5) 
         distance=int(distance)
         dict[distance]=0
   
      for (y,x) in setA: #setA is set of edge points
         distance= ((points[0]-y)**2 + (points[1]-x)**2)**(0.5)
         distance=int(distance)
         dict[distance]+=1#distance and votes
   
      votes=0
      radius=0
      sum=0
      count=0
      count1=1
      
      for thing in dict:
         if dict[thing]>5:#votes
            radius=thing
            votes=dict[thing]
            datadict[(points[0],points[1])].append(radius) #point with good radius
   for keys in datadict:
      ref=datadict[(keys[0],keys[1])][0]
      for objs in datadict[(keys[0],keys[1])]:
         
         if (ref-9)<objs<(ref+9):
            sum+=objs
            count+=1
         else:
            resultdict[(keys[0],keys[1])].append(int(sum/(count)))
            sum=objs
            count=1           
         ref=objs
   return (copied, resultdict)
  
def makeline(image,edgelist):
   sinegraph = np.zeros((360,image.shape[1],3), np.uint8)
   # Image.new( 'RGB', (360,image.shape[1]), "white")
   copied=image.copy()
   inc=0
   dicttemp={}
   dict={}
   h=image.shape[0]
   w=image.shape[1]
   dmax=0
   
   for y in range(sinegraph.shape[0]):
      for x in range(sinegraph.shape[1]):
         sinegraph[y,x]=[255,255,255]
         
   print ("process 1")
   for tup in edgelist:
      inc=0
      while inc<(2*math.pi):
         d= -(tup[1])*math.sin(inc) + (tup[0])*math.cos(inc)
         dicttemp[(d,inc)]=0
         if d>dmax:
            dmax=d+1
         inc+=math.pi/h
   print ("process 2")
   
   for tup in dicttemp:
      ds=tup[0]*image.shape[1]/dmax #y
      incs=tup[1]*360/(2*math.pi) #x   
      #print (incs,ds)
   
      i=sinegraph.item(incs,ds,0)-0.001
      sinegraph[incs,ds]=[i,i,i]
      if i<90: 
         dict[(ds, tup[1])]=0
         
   print ("process 3")
   #return sinegraph
   
   print (dict)
              
   for tuple in dict:
      for x in range(image.shape[1]):
         y = (tuple[0]+x*math.sin(tuple[1])) / math.cos(tuple[1])
         if 0<=y<=(image.shape[0]-1):
            copied[image.shape[1]-y,x]=[0,0,255]
   print ("process 4")

   return sinegraph,copied

def main():
   file1 = "fractals.png"
   sub=cv2.imread(file1)
   listed=["1","2","3","4","5","6","7","8","9","0"]
   numbers=set(listed)
   t=150
   t2=200
   if(len(sys.argv)>1): 
      value = sys.argv[1]
      if value[0] in numbers:
         t= int(value)
      elif value[0,5]=="www.":       
         urlstring=""
         resp=urllib.request.urlopen(urlstring)
         sub=np.asarray(bytearray(resp.read()),dtype="uint8")
         sub=cv2.imdecode(sub,CV2.IMREAD_COLOR)
      else:
         file1=value
         sub=cv2.imread(file1)
   
   image= cv2.resize(sub, (0,0), fx=0.4, fy=0.4 ) 
   print (image.shape[0])
   cv2.imshow('Image',image)
   k=0
   print ("Note: r= original, g= grayscale, b= blur, e= edge, o= canny, k=canny2, c=circle, l=line, esc= exit")
   imagetemp=image.copy()
   while k != 27:  
      k=cv2.waitKey(0)
      if k==27:      
         cv2.destroyAllWindows()
      elif k == ord('r'):
         cv2.imshow('Image',imagetemp)
         image=imagetemp.copy()
      elif k== ord('g'):
         image = makegray(image)
         cv2.imshow('Image',image)
      elif k== ord('b'):
         image=makegray(image)
         image=makeblur(image)
         cv2.imshow('Image',image)
      elif k==ord('e'):
         image=makegray(image)
         image=makeblur(image)
         image=makeedge(image, t)
         cv2.imshow('Image',image)
      elif k==ord('o'):
         image=makegray(image)
         image=makeblur(image)
         image=makecanny(image,t2)
         cv2.imshow('Image',image)
      elif k==ord('k'):
         image=makegray(image)
         image=makeblur(image)
         image,blah=makecanny2(image,t,t2)
         #image=cv2.Canny(image,t,t2)
         cv2.imshow('Image',image)
         print (image)
      elif k==ord("c"):
         image=makegray(image)
         image=makeblur(image)
         temp,listA =makecanny2(image,t,t2)
         image, datadict=makeCircle(image, listA)     
         list=[135,164,50,76,106]
         for points in datadict:
            for objs in datadict[points[0],points[1]]:
               cv2.circle(image,(points[1],points[0]),objs,(0,0,0))
         cv2.imshow('Image',image)
      elif k==ord("l"):
         
         image=makegray(image)
         image=makeblur(image)
         image,listA =makecanny2(image,t,t2)
         edges=255-cv2.Canny(image,t,t2)
         sign,image1=makeline(image,listA)
         image=imagetemp.copy()
         
         grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
         cannyimage = cv2.Canny(grayimage, 100, 150)

         lines = cv2.HoughLines(cannyimage, 1, math.pi/180.0, 106, np.array([]), 0, 0)
         a,b,c = lines.shape
         for i in range(a):
            val = lines[i][0][0]
            angle = lines[i][0][1]
            a = math.cos(angle)
            b = math.sin(angle)
            x0, y0 = a*val, b*val
            pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
            pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
            cv2.line(grayimage, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)
         cv2.imshow('Image',grayimage)
         print("Done")
main()
