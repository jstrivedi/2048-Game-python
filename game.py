from collections import defaultdict
import numpy as np
import random

def shiftL(arr):
    for i in range(len(arr)):
        row = [j for j in arr[i] if j !=None]
        
        if len(row)==2:
            if row[0]==row[1]:
                row = [row[0]*2]
        elif len(row)==3:
            if row[0]==row[1]:
                row= [row[0]*2, row[-1]]
            elif row[1]==row[2]:
                row = [row[0], row[1]*2]
        elif len(row)==4:
            if row[0]==row[1] and row[2]==row[3]:
                row = [row[0]*2, row[2]*2]
            elif row[0]==row[1]:
                row = [row[0]*2, row[2], row[3]]
            elif row[1]==row[2]:
                row = [row[0], row[1]*2, row[3]]
            elif row[2]==row[3]:
                row = [row[0], row[1], row[2]*2]
        row+= [None]*(4-len(row))
        arr[i]= row
    return arr

def printarr(arr):
  for i in arr:
    print([hm.get(j,str(j)) for j in i])

def shiftR(arr):
  for i in range(len(arr)):
    arr[i]=arr[i][::-1]
  arr = shiftL(arr)
  for i in range(len(arr)):
    arr[i]=arr[i][::-1]
  return arr

def shiftU(arr):
  arr = np.transpose(arr)
  arr = shiftL(arr)
  arr = [list(j) for j in np.transpose(arr)]
  return arr

def shiftD(arr):
  arr = np.transpose(arr)
  arr = shiftR(arr)
  arr = [list(j) for j in np.transpose(arr)]
  return arr

def addtwo(arr,flag):
  candidate = []
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] ==None:
        candidate.append((i,j))
  if len(candidate) == 0:
    print('Game END')
    flag = False
  else:
    candidate = random.choice(candidate)
    arr[candidate[0]][candidate[1]] = 2
    return arr



arr =  [[None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]]

# add 2 two at the beginning
arr[0][0] = 2
arr[3][3] = 2

hm = {None:'*'}

flag = True

actionhm = {'a':'Left',
            'd':'Right',
            'w':'Up',
            's':'Down'}
            

printarr(arr)
print('Choose Action : ', actionhm)
while flag:

  action = input("Enter action:")
  if action=='a':
    arr = shiftL(arr)
    arr = addtwo(arr,flag)
    print('Left')
    printarr(arr)
  elif action=='d':
    arr = shiftR(arr)
    arr = addtwo(arr,flag)
    print('Right')
    printarr(arr)
  elif action=='w':
    arr = shiftU(arr)
    arr = addtwo(arr,flag)
    print('UP')
    printarr(arr)
  elif action=='s':
    arr = shiftD(arr)
    arr = addtwo(arr,flag)
    print('Down')
    printarr(arr)
  else:
    flag = False
    print('Incorrect input')