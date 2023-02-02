x=[[1,2,3],
   [4,5,6],
  [3,6,7,]]
y=[[2,3,4],
   [2,6,7],
   [4,6,7]]
r=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[i][j]=x[i][j]+y[i][j]
for result in r:
    print(result)
