import numpy as np
import pandas as pd
import os
import json



#STEP 1: IMPORT DATA
os.chdir("../")
#just for showing data to try and understand shit
#with open("data/dataDesc.txt") as f:
 #m = json.load(f)
 #print(m)


#list of nodes, each node points to other node and has all the data in it : )
class Node:

 def __init__(self,y:list,depth,nodetype,attribute):
  self.y = y
  self.attribute = attribute
  self.val = 0
  self.depth = depth if depth else 0
  self.nodetype = nodetype if nodetype else 'root'
  self.left = None
  self.middle = None
  self.right = None


def growtree(self):
 pass

def entropyfxn(x):
 pass

#Import Data from text file into numpy array
with open("data/train.txt") as f:
 m = np.loadtxt(f)
 print(m[0][:])

#seeing how all attributes relate to first row of array.

#STEP 2: CALCULATE ENTROPY FOR EACH ROW
def compare(x,y):
 if (x > y):
  return x
 if (x < y):
  return y
 #else: return 0
#inefficient and stupid but I don't care at this point
'''
x1 = entropyfxn(m[1][:])
x2 = entropyfxn(m[2][:])
x3 = entropyfxn(m[3][:])
x4 = entropyfxn(m[4][:])
x5 = entropyfxn(m[5][:])
l = compare(x1,x2)
l = compare(l,x3)
l = compare(l, x4)
l = compare(l, x5)
'''

x=[entropyfxn(m[1][:]),entropyfxn(m[2][:]),entropyfxn(m[3][:]),entropyfxn(m[4][:]),entropyfxn(m[5][:])]
for i in range (len(x)-1):
 l = compare(i,i+1)

for i in range (len(x)):
 if l == i:
  atr_adr = i



#STEP 3: COMPARE GAIN WITH ALL ATTRIBUTES, LARGEST GAIN IS ROOT ATTRIBUTE (TESTING ATTRIBUTE)
#for this part, basically just call the gain function like 5 times and compare whats larger
#STEP 4: WHICHEVER HAS LARGEST GAIN, SET IT AS THE "ATTRIBUTE" OF THE ROOT NODE

dectree = []
#if atr_adr == 0:


#makes the root of the dectree equal to whatever attribute is represented by atr_adr
dectree.append(Node(dectree,0,'root',atr_adr))
#values are either 1, 2, or 3, so we can't just do binary left/right child
#if all '1', '2', or '3' of the attribute have the same risk value, then make a leaf node under that area.
m[atr_adr+1][:]
#else, redo entropy calc w/o the attribute that's been selected on elements that fit under this node (ex. on all where age < 30)


#STEP 5:CALL FXN TO DETERMINE IF WE CAN FIND OUT HI/LOW FROM THE ATTRIBUTE SELECTED.
#STEP 6. REPEAT STEP 3/4, EXCEPT SET IT AS ATTRIBUTE OF CHILD OF NEXT NODE
#(EX. IF YES, THEN TEST FOR X. IF NO, THEN TEST FOR Y.)
#WHEN WE GET A RISK HIGH/LOW, GO TO NEXT SUBTREE
#SOMEWHERE ALONG THE WAY, EITHER STORE STUFF TO A NODE OR INTO A LIST





