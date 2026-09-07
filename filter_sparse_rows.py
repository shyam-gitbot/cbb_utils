import numpy as np 
import sys

file = sys.stdin
argument = int(sys.argv[1])
row,count=0,0
for line in file:
  row+=1
  arr = (line.split("\t"))
  nparr= np.array(arr,dtype=float)
  zeros=np.sum(nparr==0,axis=0)
  if zeros<=argument:
    #if the number of zeros in the row , then we dont take want it
    print(nparr)
    count+=1
print(f"Total number of rows containing less of equal to 500 0's :{count}")
