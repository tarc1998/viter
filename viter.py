import math
import numpy as np

n=5
m=5
iter = n+m+10
goal=(0,0)
gamma=1

dir_r=[-1,0,1,0]
dir_c=[0,1,0,-1]
v1=np.matrix([[0]*m]*n)
v2=np.random.rand(n, m)

reward=np.array([[[-1]*4]*m]*n)
prob=np.array([[[[[0]*m]*n]*m]*n]*4)


#setting dependent probabilities
for i in range(0,n):
  for j in range(0,m):
    for k in range(0,4):
      if 0 <= i+dir_r[k] < n and 0<=j+dir_c[k] <m:
     	  prob[k][i][j][i+dir_r[k]][j+dir_c[k]] = 1
      else:
          prob[k][i][j][i][j] = 1

#the upper left corner keeps
for a in range(0,4):
    for i in range(0,n):
        for j in range(0,m):
            prob[a][0][0][i][j]=0
    prob[a][0][0][0][0]=1
    reward[0][0][a]=0

for u in range(0,iter):
    for i in range(0,n):
        for j in range(0,m):
            maks=-1000000
            for a in range(0,4):
                #v=reward[i][j][a]+gamma*sum(prob[a][i][j][r][c]*v1[r][c] for c in range(0,m) for r in range(0,n))
                suma=0
                for r in range(0,n):
                    for c in range(0,m):
                        suma+=prob[a,i,j,r,c]*v1[r,c]
                v=reward[i][j][a]+gamma*suma
                if v>maks:
                    maks=v
            v2[i][j]=maks
    v1=v2
print (v1)