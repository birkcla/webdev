#------------------------------------------
import time
from random import seed
from random import randint
import matplotlib.pyplot as plt
from time import sleep

def generatelist(length):
  listtosort = []

  for i in range(length):
    listtosort.append(randint(0, length))
    
  return listtosort
  
#-------------------------------------------





def quicksort(listtosort):
  
  if len(listtosort) < 2:
    return listtosort
  
  pivot = listtosort[len(listtosort)-1]
  lowerlist = []
  upperlist = []
  for i in range(len(listtosort)-1):
    if listtosort[i] <= pivot:
      lowerlist.append(listtosort[i])
    if listtosort[i] > pivot:
      upperlist.append(listtosort[i])
      
  low = quicksort(lowerlist)
  high = quicksort(upperlist)


  return low + [pivot] + high
  

def getaveragetime(list_size, cycles):
  times = []
  for i in range(cycles):
    currentlist = generatelist(list_size)
    start_time = time.time()
    quicksort(currentlist)
    times.append(time.time() - start_time)
  
  summ = 0
  for i in range(cycles):
    summ += times[i]
    
  return(summ / cycles)
  
  


def draw(x, y):
  plt.plot(x, y, "b.")
  plt.show()
  sleep(0.01)



for i in range(100):
    draw(i, getaveragetime(i, 10))
  












