x=[[1,2,3],
[4,5,6],
[7,8,9]]

r=[[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]
for result in r:
    print(result)