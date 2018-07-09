import math
import numpy as np

n=5
m=5
iter = n+m+10
goal=(0,0)
gamma=1

dir_r=[-1,0,1,0]
dir_c=[0,1,0,-1]
print ( "nic")
v1=np.matrix([[0]*m]*n)
v2=np.random.rand(n, m)

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
			

for u in range (0,iter):
  for i in range(0,n):
    for j in range(0,m):
        maks = -1000
        for k1 in range (0,n):
            for k2 in range (0,m):
                for k_dir in range(0, 4):
                if( reward[k_dir][k1][k2] + gamma * prob[k_dir][i][j][k1][k2] * v1[k1][k2] > maks )
                    maks =  reward[k_dir][k1][k2] + gamma * prob[k_dir][i][j][k1][k2] * v1[k1][k2]
        v2[i][j] = maks
   for i in range (0,n):
       for j in range(0, m):
           v1[i][j] = v2[i][j]

