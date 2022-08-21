h,w  = map(int, input().split())
g = [input() for i in range(h)]
s = [[False]*w for i in range(h)]
s[0][0]=True
i,j = 0,0
while True:
  #上
  if g[i][j] == "U" and i != 0:
    i-=1
    if s[i][j] == True:exit(print(-1))
    else:s[i][j]= True
  #下
  elif g[i][j] == "D" and i != h-1:
    i+=1
    if s[i][j] == True:exit(print(-1))
    else:s[i][j]= True
  #左
  elif g[i][j] == "L" and j != 0:
    j-=1
    if s[i][j] == True:exit(print(-1))
    else:s[i][j]= True
  #右
  elif g[i][j] == "R" and j != w-1:
    j+=1
    if s[i][j] == True:exit(print(-1))
    else:s[i][j]= True
  else:exit(print(i+1,j+1))