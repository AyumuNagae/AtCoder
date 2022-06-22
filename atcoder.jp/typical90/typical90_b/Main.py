n = int(input())
k = n/2
if n%2 == 1: exit(print(''))
  
def dfs(s,l,r):
  if r==0: print(s); return
  if l>0: dfs(s+'(',l-1,r)
  if l<r: dfs(s+')',l,r-1)

dfs('(',k-1,k)