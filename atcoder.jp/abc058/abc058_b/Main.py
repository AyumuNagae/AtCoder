O = input()
E = input()
ans = ''
for i,j in zip(O,E):
  ans = ans + i + j 
if len(O)>len(E):
  print(ans,O[-1],sep="",end="")
else:
  print(ans,sep="",end="")