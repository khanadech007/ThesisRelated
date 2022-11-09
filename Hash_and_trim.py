#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import hashlib as hash
import random as rand
import os
from os.path import abspath
#Declare Array for using
ck = True

y = []
r = []
strip = [] #This is the result of stripping the string
if not os.path.exists("output"):
    os.makedirs("output")
x = list(input("Enter multiple value: ").split(" "))
while ck:
    try:
        z = int(input("How many digit would you like?: "))
        ck = False
    except:
        print("The input is not integer")
naming = str(input("What file name would you like: ")) #This use for setting file name



#Declare Function

def showData():
    print (x)
    print (y)
    print (r)
    print (strip)

def hashData():
    for i in x:
        enc = i.encode("utf-8")
        digest = hash.sha256(enc).hexdigest()
        y.append(str(digest))
 

def trimming(num):
    for val in y:
        val1 = " "
        val1 = val[:num]
        strip.append(val1)
        
def rando(): #Random hash value for more security on cloud
    for ran in y:
        rs = ''.join(rand.sample(ran, len(ran)))
        r.append(rs)

def creatTxt(name):
    name = name +".txt"
    f = open("output/"+ name,"w") 
    for i in range (0, len(strip),1):
        lx = x[i]
        ls = strip[i]
        ly = y[i]
        tw = "%s : %s : %s \n"%( lx, ly, ls )
        try:
            f.write(tw)
        except:
            print("Something went wrong when writing to the file")
            
    print(f"Writting Successful  saved at {abspath(f.name)}")    
    f.close()


#Main Loop
hashData()
trimming(z)
rando()
# showData()
creatTxt(naming)
input("Press Enter To Close the Application")


