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


//setting dependent probabilities
for i in range(0,n):
  for j in range(0,m):
    for k in range(0,4):
      if 0 <= i+dir_r[k] < n && 0<=j+dir_c[k] <m:
     	  prob[4][i][j][i+dir_r[k]][j+dir_c[k]] = 1
      else:
          prob[4][i][j][i + dir_r[k]][j + dir_c[k]] = 0

//the upper left corner keeps
for i in range(0,4):
    prob[i][0][0][0][0] = 0
			

while(np.array_equal(val1, val2)):
  for i in range(0,n):
    for j in range(0,m):
        
