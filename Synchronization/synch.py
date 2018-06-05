import sys
import numpy as np
import math
import random
import time
import cv2
import time 
bump=1.01
deltax=0.1
threshold=0.90

def generateDots():
   y=np.random.rand(100)
   x=np.random.rand(100)
   i=np.random.rand(255)
   return y,x,i
   
def function(dots,xval, yval, gimg):
   for x in range(len(dots)):
      new = dots[x]+(1-dots[x])*deltax
      dots[x]=new
      if dots[x]>threshold:
         dots[x] =0
         for y in range(x):
            dots[y]=dots[y]*bump
         for z in range(100-x):
            dots[z+x]= dots[z+x]*bump
   #cv2.waitKey(100)
   drawDots(dots,xval,yval,gimg)
   
def drawDots(dots,xval,yval, gimg):
   #cv2.waitKey(300)   
   for x in range(len(dots)):
      cv2.circle(gimg,(int(xval[x]*500),int(yval[x]*500)),4,dots[x]*255,-1)
   cv2.imshow("Original",gimg)
   cv2.waitKey(10)

dots,xval,yval=generateDots()
gimg=cv2.imread("white.png",0)
cv2.resize(gimg,(300,300))

while(True):
   function(dots,xval,yval, gimg)
"""

def main():
   global dict
   dict={}
   check =True
   image=cv2.imread("white.png",0)
   cv2.resize(image,(200,200))
   
   
   for x in range(99):
      y=np.random.rand(100)
      x=np.random.rand(100)
      dict[(y,x)] = np.random.rand(255)
      
   count=1   
   while check==True:
      for tup in dict:
         fx=f(count)
         dict[tup]= function(dict[tup],fx, count)
         if dict[tup]>=255:
            bump(tup)
      draw(image)
      count+=1
         
         
   
def f(x):
   value = 1-2.78**(-x)
   return value
def function(prev, fx,x):
   deltax=0.1
   print(prev,fx,deltax)
   value2 = prev+(1+fx)(deltax)
   return value2
   
def draw(image):
    global dict
    for tup in dict:
      y=tup[0]
      x=tup[1]
      cv2.circle(image, y, x, int(intensity), -1)
      cv2.imshow("Synch", image)
      #cv2.waitKey(1)
def bump(id):
   global dict
   for tup in dict:
      if id!=tup:
         dict[tup]+=5
   
main()
"""      
      
