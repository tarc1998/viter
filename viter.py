import math
import numpy as np

n=5
m=5
goal=(0,0)
gamma=1

dir_r=[-1,0,1,0]
dir_c=[0,1,0,-1]
print ( "nic")
val1=np.matrix([[0]*m]*n)
val2=np.random.rand(n, m)

reward=np.array([[[-1]*4]*m]*n)
prob=np.array([[[[[0]*m]*n]*m]*n]*4)

for i in range(0,n):
  for j in range(0,m):
    for k in range(0,4):
      if 0 <= i+dir_r[k] < n && 0<=j+dir_c[k] <m:
     	prob[4][][m][n][m] = 1
      else:
	pro[k][
	
			

while(np.array_equal(val1, val2)):
  for i in range(0,n):
    for j in range(0,m):
      if((i,j)!=goal):
	print('asud')
