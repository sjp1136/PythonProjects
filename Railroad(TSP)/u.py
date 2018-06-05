#h( board ) = # of pairs of attacking queens
#solution... h = 0
#index = column
#value = row
#board = range( N )
#shuffle( board )
#then... only check diagonals
#generate all nbrs... swap any pair
#calculate h( nbr )
#find min h ...repeat
#does not always succeed
#run 100 trials... success rate
#run 100 trials... average # of steps
#variations... sideways moves... limit
#variations... first choice... random nbr
import sys
import numpy as np
import math
import random
import cv2
import time
global rdict

def main():
   #default="tsp0038.txt"
   default="tsp0734.txt"
   if(len(sys.argv)>1): 
      default = sys.argv[1]

   f=open(default)
   storage=f.readlines()
   count=0.0
   dict={}
   totaltime=0.0
   list=[]
   xmax=0.0
   xmin=9999999.0
   ymax=0.0
   ymin=9999999.0
   xcen=0.0
   ycen=0.0
   xsum=0.0
   ysum=0.0
   
   for x in storage:
      if count!=0.0:
         x1=x.split(" ")
         s0=float(x1[0])
         s1=float(x1[1])
         dict[count]=(s0,s1)
         list.append(count)
         
         if xmax<s1:
            xmax=s1
         if ymax<s0:
            ymax=s0
         if xmin>s1:
            xmin=s1
         if ymin>s0:
            ymin=s0
         xsum+=s1
         ysum+=s0
      else:
         size=x[0] 
      count+=1.0
   xcen=xsum/count
   ycen=ysum/count
   
   makeDict(dict,list)
   list= [726.0, 717.0, 727.0, 732.0, 733.0, 729.0, 728.0, 730.0, 731.0, 721.0, 720.0, 719.0, 718.0, 713.0, 710.0, 708.0, 709.0, 715.0, 705.0, 704.0, 701.0, 695.0, 696.0, 688.0, 685.0, 678.0, 672.0, 666.0, 697.0, 691.0, 687.0, 658.0, 655.0, 651.0, 644.0, 645.0, 646.0, 643.0, 640.0, 631.0, 615.0, 619.0, 624.0, 616.0, 610.0, 604.0, 592.0, 599.0, 606.0, 609.0, 573.0, 552.0, 541.0, 534.0, 497.0, 486.0, 475.0, 478.0, 458.0, 436.0, 442.0, 435.0, 408.0, 418.0, 422.0, 416.0, 410.0, 392.0, 390.0, 438.0, 439.0, 448.0, 451.0, 446.0, 447.0, 411.0, 424.0, 395.0, 401.0, 372.0, 387.0, 384.0, 374.0, 375.0, 402.0, 412.0, 443.0, 426.0, 419.0, 454.0, 462.0, 470.0, 465.0, 479.0, 453.0, 459.0, 489.0, 492.0, 511.0, 503.0, 488.0, 514.0, 557.0, 560.0, 556.0, 542.0, 562.0, 581.0, 577.0, 586.0, 548.0, 564.0, 588.0, 607.0, 650.0, 659.0, 663.0, 664.0, 671.0, 665.0, 642.0, 637.0, 571.0, 578.0, 600.0, 601.0, 611.0, 579.0, 575.0, 584.0, 589.0, 617.0, 612.0, 621.0, 590.0, 580.0, 537.0, 535.0, 498.0, 499.0, 508.0, 493.0, 485.0, 480.0, 494.0, 490.0, 500.0, 523.0, 536.0, 558.0, 576.0, 585.0, 622.0, 632.0, 633.0, 623.0, 614.0, 591.0, 618.0, 613.0, 630.0, 602.0, 567.0, 572.0, 559.0, 551.0, 543.0, 539.0, 526.0, 517.0, 512.0, 504.0, 476.0, 460.0, 455.0, 449.0, 472.0, 509.0, 518.0, 527.0, 544.0, 522.0, 519.0, 513.0, 515.0, 520.0, 501.0, 481.0, 483.0, 473.0, 463.0, 421.0, 379.0, 357.0, 314.0, 271.0, 326.0, 325.0, 322.0, 348.0, 353.0, 338.0, 337.0, 313.0, 317.0, 295.0, 292.0, 331.0, 352.0, 381.0, 365.0, 343.0, 364.0, 368.0, 371.0, 400.0, 378.0, 370.0, 369.0, 360.0, 386.0, 414.0, 413.0, 423.0, 432.0, 434.0, 450.0, 506.0, 521.0, 525.0, 491.0, 484.0, 505.0, 502.0, 487.0, 477.0, 457.0, 437.0, 431.0, 433.0, 430.0, 417.0, 406.0, 405.0, 441.0, 474.0, 496.0, 471.0, 469.0, 445.0, 420.0, 404.0, 394.0, 391.0, 399.0, 427.0, 466.0, 456.0, 444.0, 425.0, 428.0, 429.0, 409.0, 389.0, 376.0, 377.0, 380.0, 383.0, 373.0, 359.0, 363.0, 347.0, 333.0, 356.0, 350.0, 354.0, 307.0, 275.0, 258.0, 283.0, 320.0, 308.0, 286.0, 290.0, 287.0, 299.0, 311.0, 288.0, 259.0, 255.0, 273.0, 260.0, 276.0, 304.0, 344.0, 355.0, 341.0, 351.0, 342.0, 334.0, 323.0, 310.0, 291.0, 298.0, 316.0, 324.0, 321.0, 300.0, 329.0, 328.0, 339.0, 345.0, 346.0, 335.0, 305.0, 330.0, 336.0, 340.0, 332.0, 301.0, 306.0, 312.0, 294.0, 266.0, 265.0, 261.0, 252.0, 236.0, 234.0, 205.0, 208.0, 245.0, 253.0, 237.0, 269.0, 296.0, 262.0, 270.0, 263.0, 289.0, 281.0, 246.0, 256.0, 247.0, 257.0, 248.0, 242.0, 240.0, 229.0, 209.0, 182.0, 213.0, 181.0, 192.0, 215.0, 212.0, 165.0, 162.0, 180.0, 190.0, 191.0, 195.0, 169.0, 187.0, 196.0, 184.0, 170.0, 171.0, 133.0, 118.0, 110.0, 109.0, 105.0, 123.0, 124.0, 121.0, 126.0, 120.0, 100.0, 95.0, 83.0, 51.0, 43.0, 39.0, 40.0, 34.0, 41.0, 66.0, 56.0, 53.0, 50.0, 44.0, 54.0, 63.0, 72.0, 73.0, 74.0, 75.0, 76.0, 67.0, 68.0, 58.0, 45.0, 47.0, 81.0, 86.0, 91.0, 115.0, 127.0, 93.0, 84.0, 85.0, 80.0, 79.0, 77.0, 46.0, 36.0, 27.0, 18.0, 16.0, 1.0, 3.0, 6.0, 11.0, 22.0, 25.0, 21.0, 7.0, 2.0, 5.0, 4.0, 8.0, 10.0, 12.0, 9.0, 14.0, 13.0, 15.0, 17.0, 19.0, 24.0, 26.0, 28.0, 23.0, 20.0, 29.0, 31.0, 38.0, 55.0, 60.0, 69.0, 92.0, 98.0, 71.0, 65.0, 42.0, 49.0, 62.0, 70.0, 57.0, 52.0, 37.0, 33.0, 30.0, 32.0, 35.0, 48.0, 59.0, 61.0, 64.0, 82.0, 88.0, 111.0, 78.0, 117.0, 97.0, 96.0, 114.0, 87.0, 99.0, 103.0, 135.0, 130.0, 139.0, 155.0, 150.0, 159.0, 156.0, 160.0, 157.0, 161.0, 163.0, 140.0, 142.0, 137.0, 131.0, 119.0, 112.0, 107.0, 89.0, 90.0, 108.0, 104.0, 113.0, 134.0, 132.0, 125.0, 143.0, 147.0, 151.0, 179.0, 168.0, 167.0, 178.0, 176.0, 200.0, 186.0, 199.0, 207.0, 224.0, 231.0, 227.0, 220.0, 267.0, 268.0, 272.0, 280.0, 277.0, 284.0, 274.0, 244.0, 239.0, 243.0, 251.0, 235.0, 233.0, 230.0, 264.0, 241.0, 226.0, 203.0, 189.0, 175.0, 166.0, 149.0, 154.0, 153.0, 146.0, 138.0, 174.0, 183.0, 194.0, 219.0, 223.0, 225.0, 232.0, 238.0, 218.0, 217.0, 211.0, 202.0, 201.0, 198.0, 177.0, 173.0, 145.0, 148.0, 152.0, 128.0, 129.0, 141.0, 122.0, 106.0, 94.0, 101.0, 102.0, 116.0, 136.0, 144.0, 164.0, 158.0, 172.0, 185.0, 188.0, 197.0, 193.0, 206.0, 216.0, 222.0, 214.0, 228.0, 250.0, 254.0, 282.0, 249.0, 204.0, 210.0, 221.0, 279.0, 278.0, 285.0, 293.0, 297.0, 302.0, 318.0, 309.0, 319.0, 327.0, 303.0, 315.0, 349.0, 358.0, 361.0, 362.0, 366.0, 367.0, 382.0, 398.0, 407.0, 397.0, 396.0, 385.0, 393.0, 388.0, 403.0, 415.0, 468.0, 467.0, 495.0, 461.0, 440.0, 452.0, 464.0, 482.0, 524.0, 516.0, 531.0, 540.0, 546.0, 545.0, 549.0, 593.0, 608.0, 594.0, 565.0, 553.0, 595.0, 667.0, 652.0, 634.0, 566.0, 532.0, 547.0, 554.0, 528.0, 568.0, 569.0, 603.0, 596.0, 692.0, 712.0, 723.0, 734.0, 724.0, 693.0, 679.0, 661.0, 668.0, 683.0, 694.0, 675.0, 676.0, 656.0, 653.0, 641.0, 582.0, 597.0, 639.0, 635.0, 636.0, 583.0, 587.0, 598.0, 626.0, 574.0, 563.0, 561.0, 550.0, 529.0, 510.0, 507.0, 533.0, 530.0, 538.0, 555.0, 570.0, 605.0, 629.0, 628.0, 627.0, 625.0, 654.0, 660.0, 638.0, 620.0, 647.0, 662.0, 649.0, 648.0, 670.0, 684.0, 680.0, 689.0, 673.0, 677.0, 657.0, 669.0, 681.0, 674.0, 682.0, 686.0, 690.0, 699.0, 698.0, 700.0, 703.0, 702.0, 714.0, 707.0, 706.0, 711.0, 716.0, 722.0, 725.0]

   #skip2 = how can u stop me from doing this 
   
   copied=list[:]
   tdis= gettDistance(list)#,dict)
   height = 500
   width = 500
   image = np.zeros((height,width,3), np.uint8)
   image[:,:] = (255,255,255)
   
   #how do u the dabbing
   #hate me for that
   #dab on dat can u pls tell me 
   #it will not work 
   #quit hating
   #i loveu too
   #what is wrong with u lolz
   #stop dabbding
   # or i will slap u lolz
   # 2nd part: how to do list 
   # 3rd part: ghost-rider how to do this man 
   # completion grade is so done 
   #how to complete this project in one second flat 
   # try to complete this 
   # how u gonnna do dat
   # 
     
   print(list)
   print(tdis)
   diff=0
   diff2=0
   listpos2=[]
   g=0
      
   tdis2= gettDistance(copied)
   while True:
      for i in range(len(copied)-1):
         for j in range(i+1, len(copied)):
            try:
               rtemp=reverse(copied,i,j)
               tdis3=gettDistance(rtemp)
               if tdis2>tdis3:
                  copied=rtemp[:]
                  tdis2=tdis3
                  print("Improvement:",gettDistance(copied))
            except KeyboardInterrupt:
               print(copied)
               print(tdis2)
               
               
               
               for i in range(len(copied)):
                  y1=int(height*(dict[copied[i]][0] - ymin)/(ymax-ymin))
                  x1=int(width*(dict[copied[i]][1] - xmin)/(xmax-xmin)) 
                  cv2.circle(image,(y1,x1),4,(0,0,255),-1)
         
               for i in range(-1,len(copied)-1):  
                  y1=int(height*(dict[copied[i]][0] - ymin)/(ymax-ymin))
                  x1=int(width*(dict[copied[i]][1] - xmin)/(xmax-xmin))
                  y2=int(height*(dict[copied[i+1]][0] - ymin)/(ymax-ymin))
                  x2=int(width*(dict[copied[i+1]][1] - xmin)/(xmax-xmin))
                  cv2.line(image,(y1,x1),(y2,x2),(255,0,0),2)     
               cv2.imshow('Image', image)
               cv2.waitKey(1000000000)
               #sys.exit(0)
            except :  
               sys.exit(0)
                 
          

            
      #listpos2.append(copied)
      #g+=1
      
      #t=time.time() - start_time
      #totaltime+=t
      #print(g,"--- %s seconds ---" % (t),) 
      #print(gettDistance(copied))
#____________________________________________________________
   
            

def reverse(list2, i,i2):
   copied=list2[:]
   copied[i:i2+1] = reversed(copied[i:i2+1])  
   return copied
      
   
def swap(list2,first,second):
   copied=list2[:]
   temp = copied[first]
   copied[first]=copied[second]
   copied[second]=temp
   return copied
   
def getDistance(x1,y1,x2,y2):
   return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
   
def makeDict(dicted, listed):
   global rdict
   rdict={}
   for i in range(len(listed)-1): 
      for j in range(i+1, len(listed)):
      
         x1=dicted[listed[i]][1]
         y1=dicted[listed[i]][0]
         x2=dicted[listed[j]][1]
         y2=dicted[listed[j]][0]
         dist= getDistance(x1,y1,x2,y2)
         rdict[(listed[i],listed[j])]=dist
         rdict[(listed[j],listed[i])]=dist
         
   x1=dicted[listed[0]][1]
   y1=dicted[listed[0]][0]
   x2=dicted[listed[len(listed)-1]][1]
   y2=dicted[listed[len(listed)-1]][0] 
   dist= getDistance(x1,y1,x2,y2)
   rdict[(listed[i],listed[j])]=dist
   rdict[(listed[j],listed[i])]=dist

def gettDistance(listed):
   sum=0.0 
   for i in range(0,len(listed)-1):
      bob=listed[i]
      cool=listed[i+1]
      sum+=rdict[(bob,cool)]
      
   bob=listed[0]
   cool=listed[len(listed)-1]
   sum+=rdict[(bob,cool)]  
      
   return sum
"""   
def gettDistance(listed,dicted):
   sum=0.0 
   for i in range(0,len(listed)-1):
      x1=dicted[listed[i]][1]
      y1=dicted[listed[i]][0]
      x2=dicted[listed[i+1]][1]
      y2=dicted[listed[i+1]][0]
      sum+=getDistance(x1,y1,x2,y2)
   x1=dicted[listed[0]][1]
   y1=dicted[listed[0]][0]
   x2=dicted[listed[len(listed)-1]][1]
   y2=dicted[listed[len(listed)-1]][0] 
   sum+=getDistance(x1,y1,x2,y2)
   return sum
   """
"""
def findAllTerms(list):
   #find all numbers from - to (n-1)
   if len(list)==0: return [[]]
   if len(list)==1: return [[list]]
   #if len(list)==2: return [[list
   list=[]
   for i in range(len(list)):
      subA= =findAllTerms(
      subA=
"""
#start_time = time.time()
main() 
#print("--- %s seconds ---" % (time.time() - start_time))      
#Next lab:
#score = 100-sqrt(ourbestdistance - bestdistance)   
#best distance = 70,000
   
""" 
def findSwapPos(n):
   #find the sequence of adjacent swap positions 
   #that generate all permuatations of [0...1]
   if n==1: return []
   if n==2: return [0,0]
   fs = findSwapPos(n=1)   
   pfx=[[i for i in range(n-1)],[i for i in range(n-1)][[::-1]] #(reverse) list of two different lists
   fsr=[pfx[i%2]+[fs[i]+(i%2)] for i in range(len(fs))]
   return [elem for fsrsub  in fsr for elem in fsrsub]
   #inidivual swap positions 
   """
